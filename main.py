# -*- coding: utf-8 -*-
import os

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
VERSION = "1.0"
MARKDOWN = ""

# Functions and Strings
C = {
    "section_start": lambda section: f"<hr>{C['br'](2)} ## {section}",
    "section_end": lambda section: f"<p align=\"right\">({C['link']('#top', 'back to top')})</p>",
    "modifiable_text_start": "<!-- MANUALLY MODIFY WITHIN THESE COMMENT THE REST IS AUTO GENERATED:",
    "modifiable_text_end": "-->",
    "modifiable_section": lambda section: f"{C['modifiable_text_start']}{section}{C['modifiable_text_end']}",
    "modifiable_area": lambda section: f"{C['modifiable_section'](k)}{C['modifiable_section'](k)}",
    "default_text": "TODO",
    "hide": ":-HIDE",
    "value": lambda k, v: v()
    if C["modifiable_area"](k) in v()
    else f"{v()}{C['br'](2)}{C['modifiable_area'](k)}",
    "link": lambda url, text: f'<a href="{url}">{text}</a>',
    "br": lambda count=1: count * "\n",
    "sections": {
        # Add :-HIDE to the key to keep the section rendered text but hide the boilerplate
        "Title :-HIDE": lambda: f"<h1 align='center'>{C['br']()}{C['modifiable_area'](k)}{C['br']()}</h1>",
        "Short Description :-HIDE": lambda: f"<h4 align='center'>{C['br']()}{C['modifiable_area'](k)}{C['br']()}</h4>",
        "Badges :-HIDE": lambda: C["modifiable_area"](k),
        "Index :-HIDE": lambda: '<p align="center">'
        + " • ".join(
            [
                f"<a href='#{s.lower().replace(' ', '-')}'>{s}</a>"
                for s in C["sections"]
                if C["hide"] not in s
            ]
        )
        + "</p>",
        "Description": lambda: C["modifiable_area"](k),
        "Diagram": lambda: C["modifiable_area"](k),
        "Development": lambda: C["modifiable_area"](k),
        "Testing": lambda: C["modifiable_area"](k),
        "Deployment": lambda: C["modifiable_area"](k),
        "Logs": lambda: C["modifiable_area"](k),
        "Troubleshooting": lambda: C["modifiable_area"](k),
        "Misc": lambda: C["modifiable_area"](k),
    },
}


def get_previous_readme_text():
    custom_text = {}

    readme = "".join(
        [file for file in os.listdir(SCRIPT_PATH) if file.lower() == "readme.md"]
    )
    if readme:
        with open(readme) as r:
            existing_readme = r.readlines()

        found = ""
        for line in existing_readme:
            if found and line.startswith(C["modifiable_text_start"]):
                custom_text[found] = custom_text[found].strip()
                found = ""
            elif line.startswith(C["modifiable_text_start"]):
                found = (
                    line.replace(C["modifiable_text_start"], "")
                    .replace(C["modifiable_text_end"], "")
                    .strip()
                )
                custom_text[found] = ""
            elif found:
                custom_text[found] += line

    return custom_text


CUSTOM_TEXT = get_previous_readme_text()
MARKDOWN = [f"<!-- VERSION: {VERSION} -->", '<div id="top"></div>']

for k, v in C["sections"].items():
    custom = CUSTOM_TEXT[k] if k in CUSTOM_TEXT else ""
    MARKDOWN.append(C["section_start"](k)) if C["hide"] not in k else ""
    MARKDOWN.append(
        C["value"](k, v).replace(
            C["modifiable_section"](k),
            f"{C['modifiable_section'](k)}{C['br']()}{custom}{C['br']()}",
            1,
        )
    )
    MARKDOWN.append(C["section_end"](k)) if C["hide"] not in k else ""

MARKDOWN_STR = C["br"]().join(MARKDOWN)

with open("readme.md", "w", encoding="utf-8") as readme:
    readme.write(MARKDOWN_STR)
