# -*- coding: utf-8 -*-
import os
from src import util

FOLDER_EMOJI = ":file_folder:"
FILE_EMOJI = ":page_facing_up:"

DEFAULT_VALUE_MAP = {
    ".git": "The folder that git uses to track all the git files. You should not edit this directly.",
    ".gitignore": "The file which tells [git](https://git-scm.com/doc) the files to ignore. Ignored files will not be tracking and committed.",
    "readme.md": "The readme file which says various information about the repository.",
    "tox.ini": "The configuration file for [tox](https://tox.wiki/en/latest/index.html), which is a tool that manages python virtual envs and runs python commands within those virtual envs.",
    "dockerfile": "The instructions used to build a [docker](https://docs.docker.com/) image.",
    ".dockerignore": "Lists the files and directories which will be ignored when building a [docker](https://docs.docker.com/) image",
    ".pre-commit-config.yaml": "The configuration for the [pre-commit](https://pre-commit.com/) check. Which runs checks on every commit.",
    ".pylintrc": "The configuration for [pylint](https://pylint.pycqa.org/en/latest/). Which is a python code linter.",
    "pytest.ini": "The configuration for [pytest](https://docs.pytest.org/en/6.2.x/contents.html). Which is a python test framework.",
    ".coveragerc": "The configuration for the [coverage](https://coverage.readthedocs.io/en/latest/config.html) tool. It can be used to assert code coverage from tests must be at least a certain level.",
    ".github": "The directory which contains various [github files](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories), such as what markdown you would see when creating a pull request",
    ".vscode": "The directory which contains various [visual studio](https://docs.microsoft.com/en-us/visualstudio) configuration files.",
    "Jenkinsfile": "The instructions for what commands will run in the [Jenkins](https://www.jenkins.io/doc/) continuous integration environment.",
    "docker-compose.yml": "The instructions that [docker-compose](https://docs.docker.com/compose/) uses to run docker images as containers.",
    "pyproject.toml": "A standard python project setup [file](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/).",
    "requirements.txt": "A production python requirements file, used to list dependencies for production.",
    "requirements-dev.txt": "A development python requirements file, used to list dependencies for the development environment.",
    "setup.py": "A standard python project setup file. Possibly replaced by pyproject.toml",
}

skip = {".git"}


def generate(target_path):
    markdown = ""

    items = os.listdir(target_path)
    items.sort()

    for item in items:

        # TODO skip all items in .gitignore
        if item in skip:
            continue

        path = os.path.join(target_path, item)

        value = (
            DEFAULT_VALUE_MAP[item.lower()]
            if item.lower() in DEFAULT_VALUE_MAP
            else "TODO"
        )

        markdown += util.new_line(2)
        markdown += f"### {item} "

        if os.path.isdir(path):
            markdown += FOLDER_EMOJI
        elif os.path.isfile(path):
            markdown += FILE_EMOJI
        else:
            raise ValueError(f"{path} is not a file nor a directory.")

        markdown += util.new_line(2)
        markdown += value
        markdown += "<hr>"

    if markdown:
        markdown = f"""<details>
<summary>Click to expand, to see information about the files/directories in the root of this repo!</summary>
<hr>
{markdown}
</details>"""

    return markdown
