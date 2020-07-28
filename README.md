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

# rebuild everything on any file change and serve it with python
watchexec -s SIGKILL "./test.sh && python3 -m http.server --directory public"
```

Now open http://0.0.0.0:8000/ in your browser.
