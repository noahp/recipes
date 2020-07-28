#!/usr/bin/env python3
"""
Update the README.md index, and output index.html and recipe.html in the
./SITE_DIR/ directory.
"""

import glob
import os
import re
import shutil
import subprocess
import sys
from multiprocessing import Pool

SITE_DIR = "public"


def get_recipe_data():
    """glob the recipe dir and return the data"""

    def shortname(x):
        return os.path.splitext(os.path.split(x)[1])[0]

    mdfiles = [(shortname(x), x) for x in sorted(glob.glob("./recipes/*.md"))]
    for index, mdfile in enumerate(mdfiles):
        with open(mdfile[1], "r") as mdfileio:
            line = mdfileio.readline()
            m = re.match(r"# ([^\w]+?) .*", line.strip())
            if m:
                emoji = m.group(1)
            else:
                # fallback emoji
                emoji = "📃"
            mdfiles[index] = (emoji, mdfile[0], mdfile[1])
    return mdfiles


def get_index_lines(recipe_data):
    """get the index entries"""
    index_entry_template = "- [{} {}]({})"
    index_entries = "\n".join([index_entry_template.format(*x) for x in recipe_data])
    return index_entries


def update_index(infile_name, recipe_data):
    """update the index file"""
    # make the entries
    index_entries = get_index_lines(recipe_data)

    # insert between the start-end indicators
    with open(infile_name, "r") as infile:
        infiledata = infile.read()
    match = re.match(
        r"(.*<!-- start index -->).*(<!-- end index -->.*)",
        infiledata,
        re.DOTALL + re.MULTILINE,
    )
    assert match, "WTF"
    infiledata = match.group(1) + "\n" + index_entries + "\n" + match.group(2)
    with open(infile_name, "w") as infile:
        infile.write(infiledata)


def gen_recipe(cmdline_formatted):
    # subprocess.check_call(cmdline_formatted, shell=True)
    print(cmdline_formatted)


def generate_site(readme, recipe_data):
    """output the site files"""
    shutil.rmtree(f"./{SITE_DIR}", ignore_errors=True)
    os.makedirs(f"./{SITE_DIR}", exist_ok=True)
    shutil.copytree("./recipes", f"./{SITE_DIR}/recipes")
    shutil.copy("./gh-fork-ribbon.css", f"./{SITE_DIR}/gh-fork-ribbon.css")

    # .md->.html
    shutil.copy("./README.md", f"./{SITE_DIR}/README.md")
    with open(f"./{SITE_DIR}/README.md", "r") as infile:
        data = infile.read()
    data = re.sub(r"\./recipes/(.*)\.md", r"\g<1>.html", data)
    with open(f"./{SITE_DIR}/README.md", "w") as infile:
        infile.write(data)

    recipe_data = recipe_data + [
        ("🌮", "index", "README.md"),
    ]

    cmdline = 'yasha -o {site_dir}/{name}.html --shortname="{name}" --favicon="{emoji}" --pathname="{path}" recipe-template.html.j2'

    cmdlines = "\n".join(
        [
            cmdline.format(site_dir=SITE_DIR, emoji=emoji, name=name, path=path)
            for emoji, name, path in recipe_data
        ]
    )

    subprocess.check_call(f"parallel -I% % <<EOF\n{cmdlines}\nEOF", shell=True)

    # for emoji, name, path in recipe_data:
    #     gen_recipe(cmdline.format(emoji=emoji, name=name, path=path))

    # with Pool(6) as p:
    #     p.map(gen_recipe, (cmdline.format(emoji=emoji, name=name, path=path),))


def main():
    """main cli entrance point"""
    infile_name = "README.md"

    recipe_data = get_recipe_data()

    update_index(infile_name, recipe_data)

    generate_site(infile_name, recipe_data)


if __name__ == "__main__":
    main()
