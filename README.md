# gpi-url-shortener
A demo of how github can be made into a url shortener

Made for [CMU GPI](http://cs.cmu.edu/~07131)

# Getting started using your own url shortener

1. Fork this repo
2. Clone your forked repo.
```
git clone git@github.com:[your github username]/gpi-url-shortener.git
```
3. Rename the `example_github_config.py` to `github_config.py`, add your github username or custom github url in the file, and put the absolute path to your repo. Remember that when inside the repo `pwd` can give you the current directory's absolute path.
4. Make sure that you have ssh keys setup for your github. If you are not sure how to do this, you can follow [this tutorial](https://www.youtube.com/watch?v=H5qNpRGB7Qw).
5. Add to your `.bashrc`, `.bash_profle`, `.zshrc`, etc. the following:

```
alias shorten_url="python3 /absolute/path/to/gpi-url-shortener/url_shortener.py"
```
Don't forget to re-`source` your `rc` file!!

6. In the repository settings turn on ghpages from the master branch
7. You're all set!! Simply from terminal run:
```
shorten_url
```
And you should be walked through the process of shortening a url.

You should see something like this:

```
what url do you want to shorten?
url to be shortened: http(s)://thebomb.com.net.gov
shorten to https://[your github id].github.io/gpi-url-shortener/this_is_super_short
doing some stuff....
url has been shortened to: https://[your github id].github.io/gpi-url-shortener/this_is_super_short/
it might take ~5 mins for the link to become active
```

8. If you have a custom domain you want to use with your url shortener, you can set it up for the github repo by following the instructions [here](https://help.github.com/en/articles/using-a-custom-domain-with-github-pages).

Have fun and let us know if you have any questions on piazza!!!

Don't forget to hit the quan and yell YEAAAAAHHHH DONNER :ok_hand: :ok_hand: :ok_hand: :ok_hand:
