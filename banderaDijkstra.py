from ast import Lambda
from curses.ascii import alt
import heapq
from operator import itemgetter
import heapq
import array
from platform import node
def banderaDijkstra(grid,source):
    def _bandera(dist,vis,prev,nod):
        if not nod:
            return (dist,prev)
        else:
            (best,vertex)=heapq.heappop(nod)
            (y,x)=vertex
            vis.add((y,x))
            for (yy,xx) in [c for c in neigh((y,x)) if not c in vis]:
                cost=dist[yy*h+xx]
                alt=best+int(grid[yy][xx])
                if alt<cost:
                    dist[yy*h+xx]=alt
                    prev[yy*h+xx]=y*h+x
                    heapq.heappush(nod,(alt,(yy,xx)))
        return _bandera(dist,vis,prev,nod)
    h=len(grid)
    w=len(grid[0])
    dist=array.array("I",[1<<24-1]*h*w)
    (y0,x0)=source
    vis=set()
    dist[y0*h+x0]=0
    nod=[(0,source)]
    prev=array.array("I",[i for i in range(h*w)])
    neigh= Lambda node, m=grid,h=h,w=w:neighbours(m,h,w,node)
    return _bandera(dist,vis,prev,nod)