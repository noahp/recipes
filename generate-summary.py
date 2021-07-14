#!/usr/bin/env python

import os

SUMMARY_MD_TEMPLATE = """# Summary

{}

---

- [Cooking Equipment]()
  - [Cooking Equipment](./cooking-equipment.md)"""

if __name__ == "__main__":

    exclude_dirs = ("src/pics", "src")

    recipe_groups = {}

    for dirpath, dirnames, filenames in os.walk("src"):
        if dirpath in exclude_dirs:
            continue
        _, groupname = os.path.split(dirpath)
        recipe_groups[groupname] = filenames

    summary = ""

    for group in recipe_groups:
        summary += "- [{}]()\n".format(group)
        for recipe in recipe_groups[group]:
            summary += "  - [{recipename}]({group}/{recipename}.md)\n".format(
                recipename=os.path.splitext(recipe)[0], group=group
            )

    print(SUMMARY_MD_TEMPLATE.format(summary))
