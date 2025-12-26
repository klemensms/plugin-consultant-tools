#!/usr/bin/env python3
"""
Auto-approve safe read-only Bash commands in Claude Code.

This script automatically approves Bash commands that are read-only
and don't contain command chaining that could bypass security checks.

Safe commands: grep, cat, head, tail, wc, find, ls, less, file

Security: Rejects commands with chaining operators (;, &&, |, ||, `)
"""
import json
import sys
import shlex

try:
    hook_input = json.load(sys.stdin)
except json.JSONDecodeError:
    sys.exit(0)

command = hook_input.get("tool_input", {}).get("command", "")

# Parse first command only (prevent chaining attacks)
try:
    tokens = shlex.split(command)
    first_cmd = tokens[0] if tokens else ""
except ValueError:
    # Malformed command, let user decide
    sys.exit(0)

# Safe read-only commands
safe_commands = {"grep", "cat", "head", "tail", "wc", "find", "ls", "less", "file"}

# Dangerous patterns that could chain commands
dangerous_patterns = [";", "&&", "||", "|", "`", "$(", "${"]

# Check if command is safe
is_safe_command = first_cmd in safe_commands
has_dangerous_pattern = any(p in command for p in dangerous_patterns)

if is_safe_command and not has_dangerous_pattern:
    result = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "allow",
            "permissionDecisionReason": f"Auto-approved read-only command: {first_cmd}"
        }
    }
    print(json.dumps(result))

# Exit 0 to continue (no output = ask user)
sys.exit(0)
