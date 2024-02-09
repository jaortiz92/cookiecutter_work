import os
import subprocess

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"
GOOD_COLOR = "\x1b[92m"

project_slug = "{{ cookiecutter.project_slug }}"

print("{}INFO: The project {} is ready!!! {}".format(
        GOOD_COLOR, project_slug, RESET_ALL
    ))

print("{}INFO: Initializing a git repository... {}".format(
        GOOD_COLOR, RESET_ALL
    ))

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial Commit'])

print('Good bye')