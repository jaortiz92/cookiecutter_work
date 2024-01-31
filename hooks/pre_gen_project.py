import os
import sys

project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

if len(project_slug) < 4:
    print("{}ERROR: {} is not a valid name for this template. {}".format(
        ERROR_COLOR, project_slug, RESET_ALL
    ))
    sys.exit(1)

else:
    print("{}INFO: the project {} is building in {}. {}".format(
        MESSAGE_COLOR, project_slug, os.getcwd(), RESET_ALL
    ))