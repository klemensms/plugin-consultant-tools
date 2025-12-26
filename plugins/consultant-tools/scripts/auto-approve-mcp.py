#!/usr/bin/env python3
"""
Auto-approve script for MCP tools in Claude Code.

This script automatically approves MCP tool calls that match the
PreToolUse hook matchers defined in hooks.json.

Usage:
  This script is called automatically by Claude Code's PreToolUse hook.
  The filtering is done by the matcher patterns in hooks.json.
"""
import json
import sys

try:
    # Read the tool use request from stdin
    input_data = json.load(sys.stdin)
except json.JSONDecodeError:
    # Invalid JSON input, continue to default behavior
    sys.exit(0)

# Auto-approve the MCP tool call
output = {
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "allow",
        "permissionDecisionReason": "Auto-approved MCP tool (matched by hooks.json)"
    }
}

# Output the approval response
print(json.dumps(output))
sys.exit(0)
