# Coldtype (Examples)

## Prerequisites

- Python 3.8 (or 3.7) — installable from https://www.python.org/
- The Coldtype app — installable from https://coldtype.goodhertz.co

## Setting up coldtype-examples

```
git clone https://github.com/goodhertz/coldtype.git
git clone https://github.com/goodhertz/coldtype-examples.git
cd coldtype-examples
python3.8 -m venv venv --prompt=coldtype-examples
source venv/bin/activate
pip install -e ../coldtype
pip install git+https://github.com/typemytype/drawbot # optional, for mac rendering
```

## Verifying installation

```
coldtype --help
```

That should spit out a bunch of stuff.

Now you can open up the Coldtype app. This will need to be open (& remain open) whenever you’re working on a coldtype python file.

Once the app is open, head back to a terminal & try this:

```
coldtype animations/banner.py
```

That should display the text "COLDTYPE" in the Coldtype app. Now you’re ready to code some typography.

## Animating

When working on an animation, it’s usually best to pass the `-w` flag when you run the `coldtype` command-line tool.

```
coldtype animations/808.py -w
```

When you run that command, the process will "hang," meaning you’ll have to hit `ctrl+c` in order to kill the process.

While it’s hanging, you can type in little mnemonics to trigger different actions in the coldtype renderer.

For instance, with the above process still running, try typing—

```
pf 30
```

—and then hitting `enter` on your keyboard. This will show you a different frame (frame 30) of the animation. The `pf` command stands for **p**review **f**rame.

You can type any number of frame indices here, to preview multiple frames at once, like so:

```
pf 35, 36, 37
```

If you hit `ra`, this will **r**ender **a**ll, and should take a little while to complete, depending on how fast your computer is.

```
ra
```

Once you do a `ra` command, you can import those frames into any NLE in order to see the actual animation in realtime.
