// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.Command.Local
{
    [EnumType]
    public readonly struct Logging : IEquatable<Logging>
    {
        private readonly string _value;

        private Logging(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        /// <summary>
        /// Capture stdout in logs but not stderr
        /// </summary>
        public static Logging Stdout { get; } = new Logging("stdout");
        /// <summary>
        /// Capture stderr in logs but not stdout
        /// </summary>
        public static Logging Stderr { get; } = new Logging("stderr");
        /// <summary>
        /// Capture stdout and stderr in logs
        /// </summary>
        public static Logging StdoutAndStderr { get; } = new Logging("stdoutAndStderr");
        /// <summary>
        /// Capture no logs
        /// </summary>
        public static Logging None { get; } = new Logging("none");

        public static bool operator ==(Logging left, Logging right) => left.Equals(right);
        public static bool operator !=(Logging left, Logging right) => !left.Equals(right);

        public static explicit operator string(Logging value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is Logging other && Equals(other);
        public bool Equals(Logging other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}