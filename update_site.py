#!/usr/bin/env python3
"""
Generate an index.html and recipe.html files for each recipe in the ./SITE_DIR/
directory.
"""

import glob
import os
import re
import shutil
import subprocess
from datetime import datetime

import pytz
from jinja2 import Environment, FileSystemLoader
from pyrfc3339 import generate

SITE_DIR = "public"


def get_recipe_data():
    """glob the recipe dir and return the data"""

    def shortname(name):
        return os.path.splitext(os.path.split(name)[1])[0]

    mdfiles = [(shortname(x), x) for x in sorted(glob.glob("./recipes/*.md"))]
    for index, mdfile in enumerate(mdfiles):
        with open(mdfile[1], "r") as mdfileio:
            line = mdfileio.readline()
            match = re.match(r"# ([^\w]+?) .*", line.strip())
            if match:
                emoji = match.group(1)
            else:
                # fallback emoji
                emoji = "📃"
            mdfiles[index] = (emoji, mdfile[0], mdfile[1])
    return mdfiles


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
    index_entries = get_index_lines(recipe_data)

    data = INDEX_FORMAT.format(index_entries)
    with open(outfile_name, "w") as outfile:
        outfile.write(data)


## yasha command line render... slow though
# def render(recipe_data, rfc3339_now_str):
#     """render with yasha command line"""
#     cmdline = (
#         'yasha -o {site_dir}/{name}.html --shortname="{name}" '
#         '--favicon="{emoji}" --pathname="{path}" '
#         '--timestamp="{rfc3339_now_str}" --isindex={isindex} recipe-template.html.j2'
#     )
#
#     # gnu parallel <_<
#     cmdlines = "\n".join(
#         [
#             cmdline.format(
#                 site_dir=SITE_DIR,
#                 emoji=emoji,
#                 name=name,
#                 path=path,
#                 rfc3339_now_str=rfc3339_now_str,
#                 isindex=(name == "index"),
#             )
#             for emoji, name, path in recipe_data
#         ]
#     )
#
#     subprocess.check_call(f"parallel -I% % <<EOF\n{cmdlines}\nEOF", shell=True)


def render(recipe_data, rfc3339_now_str):
    """render recipe data into jinja template"""
    # Capture our current directory
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))

    # Create the jinja2 environment.
    # Notice the use of trim_blocks, which greatly helps control whitespace.
    j2_env = Environment(
        loader=FileSystemLoader(THIS_DIR), trim_blocks=True, lstrip_blocks=True
    )

    for emoji, name, path in recipe_data:
        with open(f"{SITE_DIR}/{name}.html", "w") as outfile:
            outfile.write(
                j2_env.get_template("recipe-template.html.j2").render(
                    favicon=emoji,
                    shortname=name,
                    pathname=path,
                    timestamp=rfc3339_now_str,
                    isindex=(name == "index"),
                )
            )


def generate_site():
    """output the site files"""
    shutil.rmtree(f"./{SITE_DIR}", ignore_errors=True)
    os.makedirs(f"./{SITE_DIR}", exist_ok=True)
    shutil.copytree("./recipes", f"./{SITE_DIR}/recipes")
    shutil.copytree("./recipes/pics", f"./{SITE_DIR}/pics")
    shutil.copy("./gh-fork-ribbon.css", f"./{SITE_DIR}/gh-fork-ribbon.css")
    shutil.copy("./styles.css", f"./{SITE_DIR}/styles.css")

    # list of tuples of recipe info
    recipe_data = get_recipe_data()

    # gimme that sweet rfc3339 plz
    rfc3339_now_str = generate(datetime.utcnow().replace(tzinfo=pytz.utc))

    # index
    generate_index(recipe_data, f"./{SITE_DIR}/README.md")
    recipe_data = recipe_data + [
        ("🌮", "index", "README.md"),
    ]

    render(recipe_data, rfc3339_now_str)


if __name__ == "__main__":
    try:
        generate_site()
    except KeyboardInterrupt:
        exit(0)
