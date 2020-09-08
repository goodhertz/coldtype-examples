from coldtype import *
from defcon import Font
import noise

df = "~/Type/fonts/fonts/DigestiveVariable.ttf"

def style_a(f, hit):
    dps:DATPenSet = StyledString("Digestive", Style(df, 300+30*(1-hit), wdth=0, ro=1, t=-10*(1-hit))).pens().align(f.a.r)
    def alter(idx, p):
        fr = p.getFrame()
        rng = 10+75*hit
        x_seed = (f.i+idx)*0.1
        fs = (250-rng)+noise.pnoise1(x_seed, repeat=18)*rng
        if p.glyphName != "space":
            return StyledString(p.glyphName, Style(df, fs, wdth=1, ro=1)).fit(fr.w).pens().align(fr)[0]
        else:
            return DATPen()
    return dps.map(alter)

t = Timeline(180, storyboard=[0, 179])

@animation(rect=(1200,300), timeline=t)
def render(f):
    a:Animation = f.a
    dps = style_a(f, 1)
    bg = hsl(0, l=0.97)

    return DATPenSet([
        DATPen().rect(f.a.r).f(bg),
        dps.f(hsl(0.9, l=0.6, s=0.7))
    ])