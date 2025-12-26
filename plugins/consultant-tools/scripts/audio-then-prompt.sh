#!/bin/bash
# Play audio notification then ask user for permission
#
# NOTE: This script is macOS-only and is included as an optional feature.
# It is NOT active by default. See README for how to enable it.

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Play audio in background (using python3 for portability)
python3 "$SCRIPT_DIR/play-audio.py" &

# Return JSON telling Claude Code to show permission prompt
# Using proper hookSpecificOutput format
echo '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"Audio notification played, awaiting user decision"}}'
exit 0
