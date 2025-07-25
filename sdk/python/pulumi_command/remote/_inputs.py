# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins as _builtins
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities
from ._enums import *

__all__ = [
    'ConnectionArgs',
    'ConnectionArgsDict',
    'ProxyConnectionArgs',
    'ProxyConnectionArgsDict',
]

MYPY = False

if not MYPY:
    class ConnectionArgsDict(TypedDict):
        """
        Instructions for how to connect to a remote endpoint.
        """
        host: pulumi.Input[_builtins.str]
        """
        The address of the resource to connect to.
        """
        agent_socket_path: NotRequired[pulumi.Input[_builtins.str]]
        """
        SSH Agent socket path. Default to environment variable SSH_AUTH_SOCK if present.
        """
        dial_error_limit: NotRequired[pulumi.Input[_builtins.int]]
        """
        Max allowed errors on trying to dial the remote host. -1 set count to unlimited. Default value is 10.
        """
        host_key: NotRequired[pulumi.Input[_builtins.str]]
        """
        The expected host key to verify the server's identity. If not provided, the host key will be ignored.
        """
        password: NotRequired[pulumi.Input[_builtins.str]]
        """
        The password we should use for the connection.
        """
        per_dial_timeout: NotRequired[pulumi.Input[_builtins.int]]
        """
        Max number of seconds for each dial attempt. 0 implies no maximum. Default value is 15 seconds.
        """
        port: NotRequired[pulumi.Input[_builtins.float]]
        """
        The port to connect to. Defaults to 22.
        """
        private_key: NotRequired[pulumi.Input[_builtins.str]]
        """
        The contents of an SSH key to use for the connection. This takes preference over the password if provided.
        """
        private_key_password: NotRequired[pulumi.Input[_builtins.str]]
        """
        The password to use in case the private key is encrypted.
        """
        proxy: NotRequired[pulumi.Input['ProxyConnectionArgsDict']]
        """
        The connection settings for the bastion/proxy host.
        """
        user: NotRequired[pulumi.Input[_builtins.str]]
        """
        The user that we should use for the connection.
        """
elif False:
    ConnectionArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ConnectionArgs:
    def __init__(__self__, *,
                 host: pulumi.Input[_builtins.str],
                 agent_socket_path: Optional[pulumi.Input[_builtins.str]] = None,
                 dial_error_limit: Optional[pulumi.Input[_builtins.int]] = None,
                 host_key: Optional[pulumi.Input[_builtins.str]] = None,
                 password: Optional[pulumi.Input[_builtins.str]] = None,
                 per_dial_timeout: Optional[pulumi.Input[_builtins.int]] = None,
                 port: Optional[pulumi.Input[_builtins.float]] = None,
                 private_key: Optional[pulumi.Input[_builtins.str]] = None,
                 private_key_password: Optional[pulumi.Input[_builtins.str]] = None,
                 proxy: Optional[pulumi.Input['ProxyConnectionArgs']] = None,
                 user: Optional[pulumi.Input[_builtins.str]] = None):
        """
        Instructions for how to connect to a remote endpoint.
        :param pulumi.Input[_builtins.str] host: The address of the resource to connect to.
        :param pulumi.Input[_builtins.str] agent_socket_path: SSH Agent socket path. Default to environment variable SSH_AUTH_SOCK if present.
        :param pulumi.Input[_builtins.int] dial_error_limit: Max allowed errors on trying to dial the remote host. -1 set count to unlimited. Default value is 10.
        :param pulumi.Input[_builtins.str] host_key: The expected host key to verify the server's identity. If not provided, the host key will be ignored.
        :param pulumi.Input[_builtins.str] password: The password we should use for the connection.
        :param pulumi.Input[_builtins.int] per_dial_timeout: Max number of seconds for each dial attempt. 0 implies no maximum. Default value is 15 seconds.
        :param pulumi.Input[_builtins.float] port: The port to connect to. Defaults to 22.
        :param pulumi.Input[_builtins.str] private_key: The contents of an SSH key to use for the connection. This takes preference over the password if provided.
        :param pulumi.Input[_builtins.str] private_key_password: The password to use in case the private key is encrypted.
        :param pulumi.Input['ProxyConnectionArgs'] proxy: The connection settings for the bastion/proxy host.
        :param pulumi.Input[_builtins.str] user: The user that we should use for the connection.
        """
        pulumi.set(__self__, "host", host)
        if agent_socket_path is not None:
            pulumi.set(__self__, "agent_socket_path", agent_socket_path)
        if dial_error_limit is None:
            dial_error_limit = 10
        if dial_error_limit is not None:
            pulumi.set(__self__, "dial_error_limit", dial_error_limit)
        if host_key is not None:
            pulumi.set(__self__, "host_key", host_key)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if per_dial_timeout is None:
            per_dial_timeout = 15
        if per_dial_timeout is not None:
            pulumi.set(__self__, "per_dial_timeout", per_dial_timeout)
        if port is None:
            port = 22
        if port is not None:
            pulumi.set(__self__, "port", port)
        if private_key is not None:
            pulumi.set(__self__, "private_key", private_key)
        if private_key_password is not None:
            pulumi.set(__self__, "private_key_password", private_key_password)
        if proxy is not None:
            pulumi.set(__self__, "proxy", proxy)
        if user is None:
            user = 'root'
        if user is not None:
            pulumi.set(__self__, "user", user)

    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]:
        """
        The address of the resource to connect to.
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]):
        pulumi.set(self, "host", value)

    @_builtins.property
    @pulumi.getter(name="agentSocketPath")
    def agent_socket_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        SSH Agent socket path. Default to environment variable SSH_AUTH_SOCK if present.
        """
        return pulumi.get(self, "agent_socket_path")

    @agent_socket_path.setter
    def agent_socket_path(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "agent_socket_path", value)

    @_builtins.property
    @pulumi.getter(name="dialErrorLimit")
    def dial_error_limit(self) -> Optional[pulumi.Input[_builtins.int]]:
        """
        Max allowed errors on trying to dial the remote host. -1 set count to unlimited. Default value is 10.
        """
        return pulumi.get(self, "dial_error_limit")

    @dial_error_limit.setter
    def dial_error_limit(self, value: Optional[pulumi.Input[_builtins.int]]):
        pulumi.set(self, "dial_error_limit", value)

    @_builtins.property
    @pulumi.getter(name="hostKey")
    def host_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The expected host key to verify the server's identity. If not provided, the host key will be ignored.
        """
        return pulumi.get(self, "host_key")

    @host_key.setter
    def host_key(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "host_key", value)

    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The password we should use for the connection.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "password", value)

    @_builtins.property
    @pulumi.getter(name="perDialTimeout")
    def per_dial_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        """
        Max number of seconds for each dial attempt. 0 implies no maximum. Default value is 15 seconds.
        """
        return pulumi.get(self, "per_dial_timeout")

    @per_dial_timeout.setter
    def per_dial_timeout(self, value: Optional[pulumi.Input[_builtins.int]]):
        pulumi.set(self, "per_dial_timeout", value)

    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.float]]:
        """
        The port to connect to. Defaults to 22.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.float]]):
        pulumi.set(self, "port", value)

    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The contents of an SSH key to use for the connection. This takes preference over the password if provided.
        """
        return pulumi.get(self, "private_key")

    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "private_key", value)

    @_builtins.property
    @pulumi.getter(name="privateKeyPassword")
    def private_key_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The password to use in case the private key is encrypted.
        """
        return pulumi.get(self, "private_key_password")

    @private_key_password.setter
    def private_key_password(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "private_key_password", value)

    @_builtins.property
    @pulumi.getter
    def proxy(self) -> Optional[pulumi.Input['ProxyConnectionArgs']]:
        """
        The connection settings for the bastion/proxy host.
        """
        return pulumi.get(self, "proxy")

    @proxy.setter
    def proxy(self, value: Optional[pulumi.Input['ProxyConnectionArgs']]):
        pulumi.set(self, "proxy", value)

    @_builtins.property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The user that we should use for the connection.
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "user", value)


if not MYPY:
    class ProxyConnectionArgsDict(TypedDict):
        """
        Instructions for how to connect to a remote endpoint via a bastion host.
        """
        host: pulumi.Input[_builtins.str]
        """
        The address of the bastion host to connect to.
        """
        agent_socket_path: NotRequired[pulumi.Input[_builtins.str]]
        """
        SSH Agent socket path. Default to environment variable SSH_AUTH_SOCK if present.
        """
        dial_error_limit: NotRequired[pulumi.Input[_builtins.int]]
        """
        Max allowed errors on trying to dial the remote host. -1 set count to unlimited. Default value is 10.
        """
        host_key: NotRequired[pulumi.Input[_builtins.str]]
        """
        The expected host key to verify the server's identity. If not provided, the host key will be ignored.
        """
        password: NotRequired[pulumi.Input[_builtins.str]]
        """
        The password we should use for the connection to the bastion host.
        """
        per_dial_timeout: NotRequired[pulumi.Input[_builtins.int]]
        """
        Max number of seconds for each dial attempt. 0 implies no maximum. Default value is 15 seconds.
        """
        port: NotRequired[pulumi.Input[_builtins.float]]
        """
        The port of the bastion host to connect to.
        """
        private_key: NotRequired[pulumi.Input[_builtins.str]]
        """
        The contents of an SSH key to use for the connection. This takes preference over the password if provided.
        """
        private_key_password: NotRequired[pulumi.Input[_builtins.str]]
        """
        The password to use in case the private key is encrypted.
        """
        user: NotRequired[pulumi.Input[_builtins.str]]
        """
        The user that we should use for the connection to the bastion host.
        """
elif False:
    ProxyConnectionArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ProxyConnectionArgs:
    def __init__(__self__, *,
                 host: pulumi.Input[_builtins.str],
                 agent_socket_path: Optional[pulumi.Input[_builtins.str]] = None,
                 dial_error_limit: Optional[pulumi.Input[_builtins.int]] = None,
                 host_key: Optional[pulumi.Input[_builtins.str]] = None,
                 password: Optional[pulumi.Input[_builtins.str]] = None,
                 per_dial_timeout: Optional[pulumi.Input[_builtins.int]] = None,
                 port: Optional[pulumi.Input[_builtins.float]] = None,
                 private_key: Optional[pulumi.Input[_builtins.str]] = None,
                 private_key_password: Optional[pulumi.Input[_builtins.str]] = None,
                 user: Optional[pulumi.Input[_builtins.str]] = None):
        """
        Instructions for how to connect to a remote endpoint via a bastion host.
        :param pulumi.Input[_builtins.str] host: The address of the bastion host to connect to.
        :param pulumi.Input[_builtins.str] agent_socket_path: SSH Agent socket path. Default to environment variable SSH_AUTH_SOCK if present.
        :param pulumi.Input[_builtins.int] dial_error_limit: Max allowed errors on trying to dial the remote host. -1 set count to unlimited. Default value is 10.
        :param pulumi.Input[_builtins.str] host_key: The expected host key to verify the server's identity. If not provided, the host key will be ignored.
        :param pulumi.Input[_builtins.str] password: The password we should use for the connection to the bastion host.
        :param pulumi.Input[_builtins.int] per_dial_timeout: Max number of seconds for each dial attempt. 0 implies no maximum. Default value is 15 seconds.
        :param pulumi.Input[_builtins.float] port: The port of the bastion host to connect to.
        :param pulumi.Input[_builtins.str] private_key: The contents of an SSH key to use for the connection. This takes preference over the password if provided.
        :param pulumi.Input[_builtins.str] private_key_password: The password to use in case the private key is encrypted.
        :param pulumi.Input[_builtins.str] user: The user that we should use for the connection to the bastion host.
        """
        pulumi.set(__self__, "host", host)
        if agent_socket_path is not None:
            pulumi.set(__self__, "agent_socket_path", agent_socket_path)
        if dial_error_limit is None:
            dial_error_limit = 10
        if dial_error_limit is not None:
            pulumi.set(__self__, "dial_error_limit", dial_error_limit)
        if host_key is not None:
            pulumi.set(__self__, "host_key", host_key)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if per_dial_timeout is None:
            per_dial_timeout = 15
        if per_dial_timeout is not None:
            pulumi.set(__self__, "per_dial_timeout", per_dial_timeout)
        if port is None:
            port = 22
        if port is not None:
            pulumi.set(__self__, "port", port)
        if private_key is not None:
            pulumi.set(__self__, "private_key", private_key)
        if private_key_password is not None:
            pulumi.set(__self__, "private_key_password", private_key_password)
        if user is None:
            user = 'root'
        if user is not None:
            pulumi.set(__self__, "user", user)

    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]:
        """
        The address of the bastion host to connect to.
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]):
        pulumi.set(self, "host", value)

    @_builtins.property
    @pulumi.getter(name="agentSocketPath")
    def agent_socket_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        SSH Agent socket path. Default to environment variable SSH_AUTH_SOCK if present.
        """
        return pulumi.get(self, "agent_socket_path")

    @agent_socket_path.setter
    def agent_socket_path(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "agent_socket_path", value)

    @_builtins.property
    @pulumi.getter(name="dialErrorLimit")
    def dial_error_limit(self) -> Optional[pulumi.Input[_builtins.int]]:
        """
        Max allowed errors on trying to dial the remote host. -1 set count to unlimited. Default value is 10.
        """
        return pulumi.get(self, "dial_error_limit")

    @dial_error_limit.setter
    def dial_error_limit(self, value: Optional[pulumi.Input[_builtins.int]]):
        pulumi.set(self, "dial_error_limit", value)

    @_builtins.property
    @pulumi.getter(name="hostKey")
    def host_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The expected host key to verify the server's identity. If not provided, the host key will be ignored.
        """
        return pulumi.get(self, "host_key")

    @host_key.setter
    def host_key(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "host_key", value)

    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The password we should use for the connection to the bastion host.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "password", value)

    @_builtins.property
    @pulumi.getter(name="perDialTimeout")
    def per_dial_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        """
        Max number of seconds for each dial attempt. 0 implies no maximum. Default value is 15 seconds.
        """
        return pulumi.get(self, "per_dial_timeout")

    @per_dial_timeout.setter
    def per_dial_timeout(self, value: Optional[pulumi.Input[_builtins.int]]):
        pulumi.set(self, "per_dial_timeout", value)

    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.float]]:
        """
        The port of the bastion host to connect to.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.float]]):
        pulumi.set(self, "port", value)

    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The contents of an SSH key to use for the connection. This takes preference over the password if provided.
        """
        return pulumi.get(self, "private_key")

    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "private_key", value)

    @_builtins.property
    @pulumi.getter(name="privateKeyPassword")
    def private_key_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The password to use in case the private key is encrypted.
        """
        return pulumi.get(self, "private_key_password")

    @private_key_password.setter
    def private_key_password(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "private_key_password", value)

    @_builtins.property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The user that we should use for the connection to the bastion host.
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "user", value)


