#!/usr/bin/env python3
"""
Auto-approve safe read-only Bash commands in Claude Code.

This script automatically approves Bash commands that are read-only
and don't contain dangerous shell operators that could bypass security.

Safe commands: ls, head, tail, wc, file, pwd, which, whoami, date, echo
Excluded: find, cat (can be dangerous with certain flags/redirects)

Security: Uses regex patterns to catch command injection attempts.
"""
import json
import re
import sys

try:
    hook_input = json.load(sys.stdin)
except json.JSONDecodeError:
    sys.exit(0)

command = hook_input.get("tool_input", {}).get("command", "")

# Dangerous shell operators that could allow command injection
DANGEROUS_PATTERNS = [
    r'[;&|]',           # Command chaining: ; && || |
    r'\$\(',            # Command substitution: $(...)
    r'`',               # Backtick command substitution
    r'\$\{',            # Variable expansion: ${...}
    r'>',               # Output redirection
    r'<',               # Input redirection
    r'\beval\b',        # eval command
    r'\bexec\b',        # exec command
    r'-exec\b',         # find -exec
    r'-ok\b',           # find -ok
    r'\bxargs\b',       # xargs can execute commands
]


def is_dangerous(cmd: str) -> bool:
    """Check if command contains dangerous shell operators."""
    for pattern in DANGEROUS_PATTERNS:
        if re.search(pattern, cmd):
            return True
    return False


# Safe read-only commands (excluded find/cat due to security risks)
SAFE_COMMANDS = {
    "ls", "head", "tail", "wc", "file",
    "pwd", "which", "whoami", "date", "echo",
}


def get_base_command(cmd: str) -> str:
    """Extract the base command from a command string."""
    stripped = cmd.strip()
    parts = stripped.split()
    if parts:
        # Get the command name without path (handles /usr/bin/ls)
        return parts[0].split('/')[-1]
    return ""


cmd_stripped = command.strip()
base_cmd = get_base_command(cmd_stripped)

# Only approve if:
# 1. The base command is in our safe list
# 2. No dangerous shell operators are present
if base_cmd in SAFE_COMMANDS and not is_dangerous(cmd_stripped):
    result = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "allow",
            "permissionDecisionReason": f"Auto-approved read-only command: {base_cmd}"
        }
    }
    print(json.dumps(result))

# Exit 0 to continue (no output = ask user)
sys.exit(0)
