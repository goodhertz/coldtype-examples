from coldtype import *

co = Font("ç/ColdtypeObviously.designspace")

def mod_o(idx, dp):
    if dp.glyphName == "O":
        # push the counter over a little for balance
        o_outer, o_counter = dp.explode()
        return o_outer.record(o_counter.translate(25, 0))

@iconset(rect=(1024, 1024), sizes=(128, 1024), dst=Path(__file__).parent.parent / "viewer")
def appicon(r, size):
    grade = Gradient.Horizontal(r, (0.95, 0.1, 0.3), (0.3, 0.1, 0.85))
    outline = 15
    oval = DATPen().f(grade).oval(r.inset(15))
    if size <= 128:
        st = Style(co, 700, slnt=1, wght=1, wdth=1, fill=1, r=1, t=-30, ro=1)
        pen = Slug("CT", st).pens().align(r, th=1, tv=1)
        return [oval, pen.interleave(lambda p: p.outline(outline).f(grade)).translate(0, 20)]
    else:
        s = Style(co, 500, fill=1, tu=-70, wdth=0.9, overlap_outline=outline, kern_pairs={("C","O"):-90, ("O  ","L"):-78, ("T","Y"):-90, ("Y","P"):-20, ("P","E"):-247}, r=1, ro=1)
        dps = Graf([StyledString(t, s) for t in ["COLD", "TYPE"]], r.inset(90, 0), leading=10).fit().pens().reversePens().mmap(lambda idx, dps: dps.translate([80, -90][idx], 0)).flatten().map(mod_o).interleave(lambda p: p.outline(outline).f(grade)).scale(0.9, center=False).align(r)
        return [oval, dps]