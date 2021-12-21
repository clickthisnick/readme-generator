# -*- coding: utf-8 -*-
import json
from os import listdir
from os.path import isfile, join
import argparse

import src.sections.contributing as contributing
import src.sections.installation as installation
import src.sections.examples as examples
import src.sections.features as features
import src.sections.documentation as documentation
import src.sections.usage as usage
import src.sections.root_items as root_items
import src.sections.deploying as deploying
import src.sections.built_with as built_with
import src.sections.testing as testing
import src.sections.configuration as configuration
import src.sections.faqs as faqs
import src.sections.roadmap as roadmap
import src.sections.header as header
import src.sections.support as support

import src.util as util

CONSTANTS = {
    "section_start": "<!-- SECTION TITLE START ---->",
    "section_end": "<!-- SECTION TITLE END ---->",
    "section_value_end": "<!-- SECTION END ---->",
}


def files_to_description(filename: str) -> str:
    map = {
        "readme.md": "A markdown readme file which contains useful information.",
        "dockerfile": "Instructions on how to build a docker image.",
    }

    filename_lower = filename.lower()
    if filename_lower in map:
        return map[filename_lower]

    return ""


def read_current_readme():
    with open("README.md", encoding="utf-8") as f:
        contents = f.read()

    sections = contents.split(CONSTANTS["section_start"])

    section_json = {}

    for section in sections[1:]:
        section_name = (
            section.split(CONSTANTS["section_end"])[0].replace("#", "").strip()
        )
        section_value = (
            section.split(CONSTANTS["section_end"])[1]
            .split(CONSTANTS["section_value_end"])[0]
            .strip()
        )
        section_json[section_name] = section_value

    return section_json


def read_config():
    with open(".github/README_CONFIG.json", encoding="utf-8") as file:
        config = json.loads(file.read())
    return config


def write(contents: str) -> None:
    with open("README_generated.md", "w", encoding="utf-8") as readme:
        readme.write(contents)


def generate_file_directory_structure(path: str) -> str:
    file_contents = ""

    for f in listdir(path):
        if isfile(join(path, f)):
            return files_to_description(f)
    pass

def main(args):
    current_readme = read_current_readme()

    markdown = '<div id="top"></div>'
    markdown += util.new_line(2)

    sections = {}

    if args.skip_installation is None:
        sections["Installation"] = installation.generate()

    if args.skip_usage is None:
        sections["Usage"] = usage.generate()

    if args.skip_examples is None:
        sections["Examples"] = examples.generate()

    if args.skip_documentation is None:
        sections["Documentation"] = documentation.generate()

    if args.skip_features is None:
        sections["Features"] = features.generate()

    if args.skip_configuration is None:
        sections["Configuration"] = configuration.generate()

    if args.skip_testing is None:
        sections["Testing"] = testing.generate()

    if args.skip_deploying is None:
        sections["Deploying"] = deploying.generate()

    if args.skip_root_items is None:
        sections["Root Items"] = root_items.generate(args.path)

    if args.skip_built_with is None:
        sections["Built With"] = built_with.generate()

    if args.skip_roadmap is None:
        sections["Roadmap"] = roadmap.generate()

    if args.skip_faqs is None:
        sections["FAQs"] = faqs.generate()

    if args.skip_contributing is None:
        sections["Contributing"] = contributing.generate()

    if args.skip_support is None:
        sections["Support"] = support.generate()

    markdown += header.generate(sections)

    for section_name, section_value in sections.items():
        markdown += CONSTANTS["section_start"]
        markdown += util.new_line(2)
        markdown += f"## {section_name}"
        markdown += util.new_line(2)
        markdown += "<hr>"
        markdown += util.new_line(2)
        markdown += CONSTANTS["section_end"]
        markdown += util.new_line(1)
        markdown += section_value
        markdown += util.new_line(2)

        # Add back to top link
        markdown += '<p align="right">(<a href="#top">back to top</a>)</p>'
        markdown += util.new_line(2)

    write(markdown)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process the command line.")

    parser.add_argument("--skip-installation", action=argparse.BooleanOptionalAction)
    parser.add_argument("--skip-usage", action=argparse.BooleanOptionalAction)
    parser.add_argument("--skip-examples", action=argparse.BooleanOptionalAction)
    parser.add_argument("--skip-documentation", action=argparse.BooleanOptionalAction)
    parser.add_argument("--skip-features", action=argparse.BooleanOptionalAction)
    parser.add_argument("--skip-root-items", action=argparse.BooleanOptionalAction)
    parser.add_argument("--skip-built-with", action=argparse.BooleanOptionalAction)
    parser.add_argument("--skip-roadmap", action=argparse.BooleanOptionalAction)
    parser.add_argument("--skip-deploying", action=argparse.BooleanOptionalAction)
    parser.add_argument("--skip-faqs", action=argparse.BooleanOptionalAction)
    parser.add_argument("--skip-contributing", action=argparse.BooleanOptionalAction)
    parser.add_argument("--skip-support", action=argparse.BooleanOptionalAction)
    parser.add_argument("--skip-testing", action=argparse.BooleanOptionalAction)
    parser.add_argument("--skip-configuration", action=argparse.BooleanOptionalAction)
    parser.add_argument("--path", required=True, type=str)

    args = parser.parse_args()
    main(args)
