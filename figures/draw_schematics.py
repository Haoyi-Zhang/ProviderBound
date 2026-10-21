"""Draw the manuscript schematics directly as font-embedded vector PDFs.

Run: python figures/draw_schematics.py --output figures
Requires Python 3.9+ and Matplotlib. No TeX engine or network is used.
The diagrams express the defined model; they are not measurement plots.
"""
import argparse
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle, FancyArrowPatch

plt.rcParams.update({'font.family':'STIXGeneral', 'mathtext.fontset':'stix',
                     'font.size':9, 'pdf.fonttype':42, 'ps.fonttype':42,
                     'text.usetex':False, 'axes.unicode_minus':False})
CM = 1 / 2.54

class Drawing:
    def __init__(self, bounds):
        x0,y0,x1,y1 = bounds
        self.fig = plt.figure(figsize=((x1-x0)*CM,(y1-y0)*CM))
        self.ax = self.fig.add_axes([0,0,1,1], xlim=(x0,x1), ylim=(y0,y1))
        self.ax.set_aspect('equal'); self.ax.axis('off')
        self.nodes = {}
        self.labels = []

    def text(self,x,y,label,size=9,ha='center',va='center'):
        artist=self.ax.text(x,y,label,fontsize=size,ha=ha,va=va,
                            linespacing=1.15,clip_on=False,zorder=4)
        self.labels.append([artist,None])
        return artist

    def box(self,name,x,y,w,h,label,dashed=False,shape='rect',size=9):
        style = {'edgecolor':'black','facecolor':'white','linewidth':.55,
                 'linestyle':(0,(4,3)) if dashed else 'solid', 'zorder':2}
        if shape == 'diamond':
            obj = Polygon([(x-w/2,y),(x,y+h/2),(x+w/2,y),(x,y-h/2)],**style)
        elif shape == 'circle': obj = Circle((x,y),w/2,**style)
        else: obj = Rectangle((x-w/2,y-h/2),w,h,**style)
        self.ax.add_patch(obj); self.text(x,y,label,size)
        self.labels[-1][1]=(x-w/2,y-h/2,x+w/2,y+h/2)
        self.nodes[name] = (x,y,w,h,shape)

    def point(self,name,side):
        x,y,w,h,_ = self.nodes[name]
        return {'n':(x,y+h/2),'s':(x,y-h/2),'e':(x+w/2,y),
                'w':(x-w/2,y),'nw':(x-w/2,y+h/2),
                'ne':(x+w/2,y+h/2),'c':(x,y)}[side]

    def line(self,points,dashed=False):
        xs,ys=zip(*points)
        self.ax.plot(xs,ys,color='black',linewidth=.55,
                     linestyle=(0,(4,3)) if dashed else 'solid',zorder=1)

    def arrow(self,p,q,dashed=False,via=()):
        points=[p,*via,q]
        if via:self.line(points[:-1],dashed)
        self.ax.add_patch(FancyArrowPatch(points[-2],points[-1],
                         arrowstyle='-|>',mutation_scale=7.5,linewidth=.55,
                         color='black',shrinkA=0,shrinkB=0,
                         linestyle=(0,(4,3)) if dashed else 'solid',zorder=1))

    def edge(self,a,b,sa='s',sb='n',**kwargs):
        self.arrow(self.point(a,sa),self.point(b,sb),**kwargs)

    def frame(self,x,y,w,h):
        self.ax.add_patch(Rectangle((x,y),w,h,fill=False,edgecolor='black',
                                   linewidth=.55,linestyle=(0,(4,3)),zorder=0))

    def save(self,out,name):
        # Fixed physical canvas: do not enlarge or rasterize the scientific figure.
        self.fig.canvas.draw()
        renderer=self.fig.canvas.get_renderer()
        x0,x1=self.ax.get_xlim();y0,y1=self.ax.get_ylim()
        for artist,node in self.labels:
            b=artist.get_window_extent(renderer).transformed(self.ax.transData.inverted())
            if b.x0<x0-.02 or b.x1>x1+.02 or b.y0<y0-.02 or b.y1>y1+.02:
                raise ValueError(name+': clipped label '+repr(artist.get_text()))
            if node and (b.x0<node[0]-.02 or b.x1>node[2]+.02 or b.y0<node[1]-.02 or b.y1>node[3]+.02):
                raise ValueError(name+': label exceeds node '+repr(artist.get_text()))
        self.fig.savefig(out/(name+'.pdf'),format='pdf',
                         metadata={'Creator':'Python Matplotlib','Producer':None,
                                   'CreationDate':None,'ModDate':None})
        plt.close(self.fig)

def draw(out):
    d=Drawing((-1.9,-2.9,6.05,.95))
    d.box('a',0,0,3.4,1.4,'$a$: developer\ntarget $=x$\nprobe $=u$',size=9)
    d.box('b',4.1,0,3.4,1.4,'$b$: library $L$\ntarget $=x$\nprobe $=v$, $v\\ne u$',size=9)
    d.box('output',2.05,-2.0,4,1.4,'Observed output\ntarget $=x$\nprobe $=u$',size=9)
    d.edge('a','output','s','nw');d.edge('b','output','s','ne');d.save(out,'coupled-boundary')

    d=Drawing((-2.5,-8.35,10.1,1.6))
    for name,x,y,label in [
        ('archives',0,0,'provider archives\nand output bytes'),
        ('facts',0,-2.5,'owner labels and\nprecedence facts'),
        ('lowerp',4,0,'producer-side\nsafe lowering'),
        ('producer',8,0,'world/force\nquery producer'),
        ('cert',8,-2.5,'normalized graph\nand certificate'),
        ('lowerc',4,-5,'checker-side\nsafe lowering'),
        ('checker',8,-5,'graph comparison\nand independent\nreplay'),
        ('answer',8,-7.5,'accepted exact\nowner sets')]:
        d.box(name,x,y,3.15,1.2,label,size=8.5)
    d.ax.add_patch(Rectangle((8-3.15/2+.06,-5-1.2/2+.06),3.15-.12,1.2-.12,fill=False,linewidth=.55,edgecolor='black',zorder=3))
    d.edge('archives','lowerp','e','w')
    d.arrow(d.point('facts','e'),d.point('lowerp','s'),via=[(2.2,-2.5),(2.2,-1.3),(4,-1.3)])
    d.edge('lowerp','producer','e','w');d.edge('producer','cert')
    d.edge('cert','checker')
    d.edge('lowerc','checker','e','w');d.edge('checker','answer')
    # The outer archive route enters below the facts route, avoiding a false junction.
    d.arrow(d.point('archives','w'),(4-3.15/2,-5.2),via=[(-2.2,0),(-2.2,-5.2)])
    d.arrow(d.point('facts','s'),(4-3.15/2,-4.8),via=[(0,-4.8)])
    d.frame(2.125,-.9,7.75,1.8);d.text(6,1.25,'untrusted production',size=8.5)
    d.frame(2.125,-5.9,7.75,1.8);d.text(6,-6.25,'replay boundary',size=8.5)
    d.save(out,'protocol-pipeline')

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,default=Path(__file__).resolve().parent)
    output=parser.parse_args().output
    output.mkdir(parents=True,exist_ok=True)
    draw(output)
