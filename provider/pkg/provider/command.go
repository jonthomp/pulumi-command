// Copyright 2016-2020, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package provider

import (
	"bufio"
	"bytes"
	"context"
	"fmt"
	"io"
	"os"
	"os/exec"
	"runtime"

	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"

	"github.com/pulumi/pulumi/sdk/v3/go/common/diag"

	"github.com/pulumi/pulumi/pkg/v3/resource/provider"
)

type command struct {
	// Input
	Interpreter *[]string          `pulumi:"interpreter,optional"`
	Dir         *string            `pulumi:"dir,optional"`
	Environment *map[string]string `pulumi:"environment,optional"`
	Create      string             `pulumi:"create"`
	Delete      *string            `pulumi:"delete,optional"`

	// Output

	Stdout string `pulumi:"stdout"`
	Stderr string `pulumi:"stderr"`
}

// RunCreate executes the create command, sets Stdout and Stderr, and returns a unique
// ID for the command execution
func (c *command) RunCreate(ctx context.Context, host *provider.HostClient, urn resource.URN) (string, error) {
	stdout, stderr, id, err := c.run(ctx, c.Create, host, urn)
	c.Stdout = stdout
	c.Stderr = stderr
	return id, err
}

// RunDelete executes the create command, sets Stdout and Stderr, and returns a unique
// ID for the command execution
func (c *command) RunDelete(ctx context.Context, host *provider.HostClient, urn resource.URN) error {
	if c.Delete == nil {
		return nil
	}
	_, _, _, err := c.run(ctx, *c.Delete, host, urn)
	return err
}

// run executes the create command, sets Stdout and Stderr, and returns a unique
// ID for the command execution
func (c *command) run(ctx context.Context, command string, host *provider.HostClient, urn resource.URN) (string, string, string, error) {
	var args []string
	if c.Interpreter != nil && len(*c.Interpreter) > 0 {
		args = append(args, *c.Interpreter...)
	} else {
		if runtime.GOOS == "windows" {
			args = []string{"cmd", "/C"}
		} else {
			args = []string{"/bin/sh", "-c"}
		}
	}
	args = append(args, command)

	stdoutr, stdoutw, err := os.Pipe()
	if err != nil {
		return "", "", "", err
	}
	stderrr, stderrw, err := os.Pipe()
	if err != nil {
		return "", "", "", err
	}

	cmd := exec.CommandContext(ctx, args[0], args[1:]...)
	cmd.Stdout = stdoutw
	cmd.Stderr = stderrw
	if c.Dir != nil {
		cmd.Dir = *c.Dir
	}
	cmd.Env = os.Environ()
	if c.Environment != nil {
		for k, v := range *c.Environment {
			cmd.Env = append(cmd.Env, fmt.Sprintf("%s=%s", k, v))
		}
	}

	var stdoutbuf bytes.Buffer
	var stderrbuf bytes.Buffer

	stdouttee := io.TeeReader(stdoutr, &stdoutbuf)
	stderrtee := io.TeeReader(stderrr, &stderrbuf)

	stdoutch := make(chan struct{})
	stderrch := make(chan struct{})
	go copyOutput(ctx, host, urn, stdouttee, stdoutch)
	go copyOutput(ctx, host, urn, stderrtee, stderrch)

	err = cmd.Start()
	pid := cmd.Process.Pid
	if err == nil {
		err = cmd.Wait()
	}

	fmt.Printf("closing...\n")

	stdoutw.Close()
	stderrw.Close()

	fmt.Printf("reading from output done channels...\n")
	<-stdoutch
	<-stderrch

	fmt.Printf("preparing to return...\n")
	if err != nil {
		return "", "", "", err
	}

	id, err := resource.NewUniqueHex(fmt.Sprintf("%d", pid), 8, 0)
	if err != nil {
		return "", "", "", err
	}

	return stdoutbuf.String(), stderrbuf.String(), id, nil
}

func copyOutput(ctx context.Context, host *provider.HostClient, urn resource.URN, r io.Reader, doneCh chan<- struct{}) {
	defer close(doneCh)
	scanner := bufio.NewScanner(r)
	for scanner.Scan() {
		err := host.Log(ctx, diag.Info, urn, scanner.Text())
		if err != nil {
			return
		}
	}
}
