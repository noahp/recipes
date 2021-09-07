# 🌮 recipes

Collection of recipes I use.

See the formatted result at https://noahpendleton.com/recipes/ .

## development

I wrote the world's worst static site gen. Could've probably been bash tbh, but
wrote it in python out of sheer laziness.

For testing the site with auto reload, you might do the following (requires
Docker):

```bash
# file watcher
sudo apt install entr

# serve it with python, and rebuild everything on any file change
# entr will nicely kill the child process on change ❤️
git ls-files | \
  entr -r bash -c '(./test.sh && python3 -m http.server --directory public)'
```

Now open http://0.0.0.0:8000/ in your browser.
