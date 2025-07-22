#!/usr/bin/env sh

# Extremely stupid, but i couldn't solve how to:
# 1. get mdbook to run a pre-build script 🙄
# 2. get docker-compose to forward a full command through to /bin/sh inside the
#    container (why tho)
#
# So this just runs the generate-summary command before executing mdbook.

set -ex

python3 generate-summary.py

# if arg is "build", just build the book
if [ "$1" = "build" ]; then
    mdbook build

    # wipe off the .html extension
    perl -i -p -e 's{href="index.html"}{href="."}g' book/toc.js
    perl -i -p -e 's{(href="[a-zA-Z0-9.][^"]+)\.html"}{$1"}g' book/toc.js
    find book/ -name *.html | xargs perl -i -p -e 's{href="index.html"}{href="."}g'
    find book/ -name *.html | xargs perl -i -p -e 's{(href="[a-zA-Z0-9.][^"]+)\.html"}{$1"}g'

else
    mdbook serve --hostname '0.0.0.0'
fi
