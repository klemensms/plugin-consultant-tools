#!/usr/bin/env python3
"""
Audio playback and notification script for Claude notification hooks.
Plays a notification sound and shows a macOS notification when called.

NOTE: This script is macOS-only and is included as an optional feature.
It is NOT active by default. See README for how to enable it.
"""

import subprocess
import sys
import os


def show_notification(title="Claude Code", message="Need input", subtitle=""):
    """Show a macOS notification using osascript."""
    try:
        script = f'display notification "{message}" with title "{title}"'
        if subtitle:
            script = f'display notification "{message}" with title "{title}" subtitle "{subtitle}"'
        subprocess.run(["osascript", "-e", script], check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass  # Silently fail on non-macOS systems


def play_notification_sound():
    """Play a notification sound using macOS built-in sounds."""
    default_sounds = [
        "/System/Library/Sounds/Glass.aiff",
        "/System/Library/Sounds/Ping.aiff",
        "/System/Library/Sounds/Pop.aiff",
        "/System/Library/Sounds/Purr.aiff",
        "/System/Library/Sounds/Sosumi.aiff"
    ]

    sound_file = None
    for sound in default_sounds:
        if os.path.exists(sound):
            sound_file = sound
            break

    if not sound_file:
        try:
            subprocess.run(["osascript", "-e", "beep"], check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass
        return

    try:
        subprocess.run(["afplay", sound_file], check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        try:
            subprocess.run(["osascript", "-e", "beep"], check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass


def main():
    """Main function to parse args, play audio, and show notification."""
    custom_message = "Need input"
    custom_title = "Claude Code"
    audio_file = None

    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == "--message" and i + 1 < len(sys.argv):
            custom_message = sys.argv[i + 1]
            i += 2
        elif arg == "--title" and i + 1 < len(sys.argv):
            custom_title = sys.argv[i + 1]
            i += 2
        elif arg == "--audio" and i + 1 < len(sys.argv):
            audio_file = sys.argv[i + 1]
            i += 2
        elif os.path.exists(arg):
            audio_file = arg
            i += 1
        else:
            i += 1

    show_notification(title=custom_title, message=custom_message)

    if audio_file and os.path.exists(audio_file):
        try:
            subprocess.run(["afplay", audio_file], check=True)
            return
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass

    play_notification_sound()


if __name__ == "__main__":
    main()
