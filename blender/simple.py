# This code must be run from within Blender itself (see blender/README.md in this repo)

from coldtype import *
from coldtype.pens.blenderpen import BlenderPen, BPH

BPH.Clear()

r = Rect(0, 0, 1000, 1000)
tc = BPH.Collection("Test")

(DATPen().rect(r).f(hsl(0.9, s=1))
    .tag("Frame").cast(BlenderPen).draw(tc, plane=1))

Slug("COLD", Style("~/Goodhertz/coldtype/assets/MutatorSans.ttf", 180, wdth=0.5, wght=1)).pen().f(hsl(0.65, l=0.5, s=1)).align(r).translate(0, 80).tag("COLD").cast(BlenderPen).draw(tc)

Slug("TYPE", Style("~/Goodhertz/coldtype/assets/MutatorSans.ttf", 210, wdth=0.35, wght=0.25)).pen().f(hsl(0.15, s=1)).align(r).translate(0, -80).tag("TYPE").cast(BlenderPen).draw(tc)