# 🌮 recipes

Collection of recipes I use.

See the formatted result at https://noahpendleton.com/recipes/ .

## development

I wrote the world's worst static site gen. Could've probably been bash tbh, but
wrote it in python out of sheer laziness.

For testing the site gen, you might do the following:

```bash
# janky file watcher
sudo apt install entr

# http server
python3 -m http.server --directory public &

# rebuild everything on any file change (requires Docker)
git ls-files | entr ./test.sh
```

Now open http://0.0.0.0:8000/ in your browser.
