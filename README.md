# 🌮 recipes

Collection of recipes I use.

See the formatted result at https://noahpendleton.com/recipes/ .

## development

This uses [mdBook](https://github.com/rust-lang/mdBook) for static site
generation.

```bash
# assumes you have rust + cargo installed already
cargo install mdbook
mdbook serve
# now open the generated site to view locally
```

You can also use these commands to serve the book from docker, without
installing anything locally (requires docker-compose):

```bash
# mdbook serve until ctrl+c
DOCKER_USER="$(id -u):$(id -g)" docker-compose run mdbook

# to just build into ./book/ and exit
DOCKER_USER="$(id -u):$(id -g)" MDBOOK_JUST_BUILD=1 docker-compose up --build
```
