# Genlog

## What is it?

Genlog is a tool to automatically commit all code in its current state, along
with a thumbnail based on the most recently generated file. The commit is added
in the currently active branch.

This tool only works if you generate png files named after the convention of
`fn` listed in the requirements below.

## Usage

If you run `./example.py && genlog res` the following things will happen:

- `example.py` will create a file named something like
  `res/20160520-183502-785780-14de7ef-94310b2.png`. This is to emulate the
  result of some script.
- Genlog will then create a thumbnail of this file and store it in `.genlog`.
- Genlog will proceed to commit all files in the repo (`git commit -A`), along
  with the thumbnail. If there are no changes, only the thumbnail will be
  commited.

`res` is the name of the directory where Genlog should look for images. If you
simply run `genlog` it will look in the current directory.

You can also run genlog seperately:

    ./example.py
    genlog res

And you can add information to the commit message:

    genlog res -m "this was a good result."

You can export an environment variable to make genlog commit as a different
author. This string needs to be a valid email (preferably associated with your
Github account):

    export GENLOG_USER_EMAIL='youremail+genlog@gmail.com'

## What is the purpose of this?

I frequently experiment with generative algorithms. This tool is an attempt to
make it easier to store various results along the way.

Please note that this does create a lot of extra commits, which is probably not
what you want in your projects in practice.

Some more discussion on twitter:
https://twitter.com/inconvergent/status/732522970619465728

## Requires

*    `fn`: https://github.com/inconvergent/fn
*    `python-imaging`: `apt-get install python3-imaging`

## Install

Install using either (as `sudo`)

  `./setup.py install`

Or

  `./setup.py develop`

The latter is most convenient if you will be editing the code.

## Todo

- Introduce Large File Storage? https://git-lfs.github.com/
- optipng to reduce file size.

## Notes

This could be useful:

https://git-scm.com/blog/2010/08/25/notes.html

