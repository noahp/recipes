#!/usr/bin/env sh

# Extremely stupid, but i couldn't solve how to:
# 1. get mdbook to run a pre-build script 🙄
# 2. get docker-compose to forward command line to

set -ex

python3 generate-summary.py
mdbook serve --hostname '0.0.0.0'
