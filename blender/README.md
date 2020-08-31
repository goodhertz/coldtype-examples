# Blender + Coldtype

## Preamble

Using Coldtype in Blender solves a problem that’s somewhat different than the main motivation of Coldtype itself, which is to rasterize complex typesetting done entirely in code.

The point in Blender is to make up for Blender very bad typesetting support by running small ad-hoc scripts to build up complex vectorized text that you can then further manipulate using standard Blender editing techniques. That is, the idea here is to work in a more hybrid style. You want a gigantic piece of 3d type that uses the second stylistic set of a font? Blender won't help you, but Coldtype can: write a short script in Python, using Coldtype to create the vector, and — voila — you have a gigantic piece of 3d type that you can move around and add materials to, etc.

__N.B.__ This means the point of a Coldtype script in Blender is not to return a `DATPen` or `DATPenSet` to a renderer, but to work interactively, creating or mutating existing objects available in the Blender data hierarchy in your project file.

## Using Python in Blender

Using python in Blender means using Blender’s bundled `python`, which is installed in the app bundle itself (on Mac, at least).

On my computer, I’ve aliased the Blender path (which is something like `/Applications/Blender.app/Contents/Resources/2.90/python/bin/python3.7m`) to `b3d_python`, and I’ve also aliased the Blender executable itself (something like, `/Applications/Blender.app/Contents/MacOS/blender`) to `b3d` (on a Mac you’ll want to start Blender by running it from the terminal, so you can see error output in the Terminal, since Blender doesn’t properly print errors anywhere when you launch it as a normal app on Mac).

To summarize, for version 3.9 of Blender, these are the aliases in my `~/.bash_profile`:

```
alias b3d_python='/Applications/Blender.app/Contents/Resources/2.90/python/bin/python3.7m'
alias b3d='/Applications/Blender.app/Contents/MacOS/blender'
```

## Installing Coldtype in Blender

Now that you have an easy way to call Blender’s python (as above), you can install Coldtype using Blender’s python’s `pip`.

Ala: `b3d -m pip install coldtype` (or `b3d -m pip install -e ~/path/to/coldtype` if you’re installing coldtype from the coldtype repository directly)

Unfortunately, though it should be that easy, it is not!

Remedying the error installation that results can be a little tricky, but should only require one weirdness, as outlined in [this Stack Overflow answer](https://blender.stackexchange.com/questions/81740/python-h-missing-in-blender-python)

Basically, we need to add some missing files to Blender’s installation, which means you'll need to download the source of the exact version of Python used in the Blender you have on your machine.

To find that, run `b3d_python --version`

For Blender 3.9, that’s python 3.7.7 — you can find the source for that here: https://www.python.org/downloads/release/python-377/

Once you’ve downloaded and unzipped the source, copy the `Include` files from the python 3.7.7 source into the `/Applications/Blender.app/Contents/Resources/2.90/python/`, something like:

```cp Include/* /Applications/Blender.app/Contents/Resources/2.90/python/include/python3.7m/```

Once you’ve done that, you should be able to install coldtype in the normal way, aka:

`b3d -m pip install coldtype` (or `b3d -m pip install -e ~/path/to/coldtype` if you’re installing coldtype from the coldtype repository directly)

## Using Coldtype in Blender itself

Once you’ve got all that squared away, you can launch Blender by calling it’s executable from the command line, ala `b3d` if you’ve followed the steps as above.

That should open the normal Blender interface. From there you’ll want to open a "Text Editor" window in Blender itself, and then verify that your Coldtype installation is working correctly by trying something like:

```python
from coldtype import *
from coldtype.pens.blenderpen import BlenderPen, BPH

BPH.Clear()

r = Rect(0, 0, 1000, 1000)
tc = BPH.Collection("Test")

(DATPen().rect(r)
    .f(hsl(0.9))
    .tag("Frame")
    .cast(BlenderPen)
        .draw(tc, plane=1))
```

You can run that with Alt+P. If all goes well, that should create a pink plane in your Blender world.

## Going further

The "problem" with Blender is that you kind of have to write the python scripts in the app itself, or else it’s a little annoying to have to reload them constantly from disk, since Blender does not do that automatically when a source .py file changes.

I've found it’s more fun to just write it in the app itself, as 