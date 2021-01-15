#!/usr/bin/env python3
"""
Generate an index.html and recipe.html files for each recipe in the ./SITE_DIR/
directory.
"""

import glob
import os
import re
import shutil
import sys
from datetime import datetime

import pytz
import yaml
from jinja2 import Environment, FileSystemLoader
from pyrfc3339 import generate


def get_recipe_data(source_dir):
    """glob the recipe dir and return the data"""

    def shortname(name):
        return os.path.splitext(os.path.split(name)[1])[0]

    mdfiles = [
        (shortname(x), x) for x in sorted(glob.glob(os.path.join(source_dir, "*.md")))
    ]
    output = []
    # load emoji from leading non-alphanumeric string component, or default
    for mdfilename, mdfile in mdfiles:
        with open(mdfile, "r") as mdfileio:
            line = mdfileio.readline()
            match = re.match(r"# ([^\w]+?) .*", line.strip())
            if match:
                emoji = match.group(1)
            else:
                # fallback emoji
                emoji = "📃"
            output.append((emoji, mdfilename, os.path.basename(mdfile)))
    return output


def get_index_lines(recipe_data):
    """get the index entries"""
    index_entry_template = "- [{} {}]({})"
    index_entries = "\n".join(
        [index_entry_template.format(x[0], x[1], x[1] + ".html") for x in recipe_data]
    )
    return index_entries


INDEX_FORMAT = """# 🌮 Recipes

{}
"""


def generate_index(recipe_data, outfile_name):
    """generate the index file"""
    # make the entries
    recipe_data = filter(lambda x: "cooking-equipment" not in x, recipe_data)
    index_entries = get_index_lines(recipe_data)

    data = INDEX_FORMAT.format(index_entries)
    with open(outfile_name, "w") as outfile:
        outfile.write(data)

        # write a line for the cooking equipment list
        outfile.write("---\n")
        outfile.write("- [{} {}]({})".format("🛠️", "cooking equipment", "cooking-equipment.html"))
        outfile.write("\n")


def render(output_dir, recipe_data, rfc3339_now_str):
    """render recipe data into jinja template"""
    # Capture our current directory
    this_dir = os.path.dirname(os.path.abspath(__file__))

    # Create the jinja2 environment.
    # Notice the use of trim_blocks, which greatly helps control whitespace.
    j2_env = Environment(
        loader=FileSystemLoader(this_dir), trim_blocks=True, lstrip_blocks=True
    )

    for emoji, name, path in recipe_data:
        with open(f"{output_dir}/{name}.html", "w") as outfile:
            outfile.write(
                j2_env.get_template("recipe-template.html.j2").render(
                    favicon=emoji,
                    shortname=name,
                    pathname=path,
                    timestamp=rfc3339_now_str,
                    isindex=(name == "index"),
                )
            )


def copy_r(src, dst):
    """copy recursively file or directory"""
    if dst_dir := os.path.dirname(dst):
        os.makedirs(dst_dir, exist_ok=True)
    if os.path.isdir(src):
        copier = lambda src, dst: shutil.copytree(src, dst, dirs_exist_ok=True)
    else:
        copier = shutil.copy
    copier(src, dst)


def generate_site(config, output_dir):
    """output the site files"""
    shutil.rmtree(output_dir, ignore_errors=True)

    copy_r(config["static-dir"], output_dir)
    copy_r(config["source-dir"], output_dir)

    # list of tuples of recipe info
    recipe_data = get_recipe_data(config["source-dir"])

    # gimme that sweet rfc3339 plz
    rfc3339_now_str = generate(datetime.utcnow().replace(tzinfo=pytz.utc))

    # index
    generate_index(recipe_data, f"./{output_dir}/README.md")
    recipe_data = recipe_data + [
        ("🌮", "index", "README.md"),
    ]

    # render the template for each file in recipe_data
    render(output_dir, recipe_data, rfc3339_now_str)


def load_config():
    """load site config"""
    with open("site.yaml", "r") as configfile:
        return yaml.load(configfile, Loader=yaml.Loader)


if __name__ == "__main__":
    output_dir = sys.argv[1] if len(sys.argv) > 1 else "public"
    cfg = load_config()
    generate_site(cfg, output_dir)
