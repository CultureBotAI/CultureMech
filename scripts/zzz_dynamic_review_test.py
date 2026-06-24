"""Scratch file planted to verify the /dynamic-review workflow. DO NOT MERGE — delete."""
import subprocess


def run_user_cmd(user_input):
    # Planted SECURITY bug: shell injection from unsanitized user input.
    return subprocess.run("echo " + user_input, shell=True)


def average(values):
    # Planted LOGIC bug: off-by-one denominator, and divides by zero on empty input.
    return sum(values) / (len(values) + 1)
