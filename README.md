# Coldtype (Examples)

## Prerequisites

- Python 3.8 (or 3.7) — installable from https://www.python.org/

## Setting up coldtype-examples

```
git clone https://github.com/goodhertz/coldtype.git (if you don’t already have this)
git clone https://github.com/goodhertz/coldtype-examples.git
cd coldtype-examples
python3.8 -m venv venv --prompt=coldtype-examples
source venv/bin/activate
pip install -e ../coldtype
```

## Verifying installation

```
coldtype --help
```

That should spit out a bunch of stuff.

```
coldtype animations/banner.py
```

That should pop up a window and display the text "COLDTYPE". Now you’re ready to code some typography.

## Animating

```
coldtype animations/808.py
```

When you run that command, the process will "hang," meaning you’ll have to hit `ctrl+c` in order to kill the process, or hit `cmd+Q` with the viewing window in the foreground.

While it’s hanging, you can type in little mnemonics in the terminal window (not the viewer) to trigger different actions in the coldtype renderer.

For instance, with the above process still running, try typing—

```
pf 30
```

—and then hitting `enter` on your keyboard. This will show you a different frame (frame 30) of the animation. The `pf` command stands for **p**review **f**rame.

You can type any number of frame indices here, to preview multiple frames at once, like so:

```
pf 35 36 37
```

If you hit `ra`, this will **r**ender **a**ll, and should take a little while to complete, depending on how fast your computer is.

```
ra
```

Once you do a `ra` command, you can import those frames into any NLE in order to see the actual animation in realtime, or simply jump to the viewer app and hit the space bar.
