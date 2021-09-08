#!/usr/bin/env python

import os
import sys

SUMMARY_MD_TEMPLATE = """# Summary

[Readme](readme.md)

{}"""

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == 'supports':
            # sys.argv[2] is the renderer name
            sys.exit(0)

    exclude_dirs = ("src/pics", "src")

    recipe_groups = {}

    for dirpath, dirnames, filenames in sorted(os.walk("src")):
        if dirpath in exclude_dirs:
            continue
        _, groupname = os.path.split(dirpath)
        recipe_groups[groupname] = filenames

    summary = ""

    for group in recipe_groups:
        summary += "- [{}]()\n".format(group)
        for recipe in sorted(recipe_groups[group]):
            summary += "  - [{recipename}]({group}/{recipename}.md)\n".format(
                recipename=os.path.splitext(recipe)[0], group=group
            )

    output = SUMMARY_MD_TEMPLATE.format(summary)

    with open("src/SUMMARY.md", "w") as outfile:
        outfile.write(output)
        outfile.write("\n")

    # required for running as mdbook preprocessor
    if not sys.stdin.isatty():
        import json
        data = sys.stdin.read()
        print(data, file=sys.stderr)
        if data:
            context, book = json.loads(data)
            json.dump(book, sys.stdout)
