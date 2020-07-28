# 🌮 recipes

Collection of recipes I use.

See the formatted result at https://noahpendleton.com/recipes/ .

## development

I wrote the world's worst static site gen. Could've probably been bash tbh, but
wrote it in python out of sheer laziness.

For testing the site gen, you might do the following (requires Docker):

```bash
# file watcher
cargo install watchexec

# serve it with python, and rebuild everything on any file change.
# the trap nonsense see https://stackoverflow.com/a/22644006
(trap "exit" INT TERM; trap "kill 0" EXIT; python3 -m http.server --directory public & watchexec "./test.sh" & wait)
```

Now open http://0.0.0.0:8000/ in your browser.
