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
