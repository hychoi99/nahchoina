import math
#import pygame

from vector import Vector

class LineSegment:

    def __init__(self,p1,p2):
        #make copies of incoming vector points
        self.p1 = Vector(p1.x,p1.y)
        self.p2 = Vector(p2.x,p2.y)

#    def draw(self,window):
#        pygame.draw.line(window,pygame.color.Color("red"),(int(self.p1.x),int(self.p1.y)),(int(self.p2.x),int(self.p2.y)),2)
#
    def orthog(self):
        n = self.p2.minus(self.p1)
        n = n.normalize()
        return Vector(n.y,-n.x)


#Suppose the two line segments run
#from p to p + r
#and from q to q + s.
#Then any point on the first line is representable as
#p + t r (for a scalar parameter t)
#and any point on the second line as q + u s (for a scalar parameter u).
    def intersects(self,other):
        p = self.p1
        r = self.p2.minus(p)
        q = other.p1
        s = other.p2.minus(q)
        #solving for t = (q-p) x s / (r x s)
        qmp = q.minus(p)
        qmpxs = qmp.cross(s)
        rxs = r.cross(s)
        if rxs == 0: #lines are parallel
            return None
        t = qmpxs/rxs
        #solving for u = (q-p) x r / (r x s)
        qmpxr = qmp.cross(r)
        u = qmpxr/rxs
        
        #so now we can get the coordinates by normalizing r, scaling by t
    
        tscale = r.times(t)
        intersection1 = p.plus(tscale)
        sscale = s.times(u)
        intersection2 = q.plus(sscale)

        if (u <= 1.0) and (u >= 0) and (t <= 1.0) and (t >= 0):
            #print t, u
            rscale = r.times(t)
            intersection1 = p.plus(rscale)
            sscale = s.times(u)
            intersection2 = q.plus(sscale)
            #print rscale,sscale,intersection1,intersection2
        
            #assert intersection1.equals(intersection2)
            return rscale
        else:
            return None
        

   

    def distToPoint(self, point): # x3,y3 is the point
        px = self.p2.x-self.p1.x
        py = self.p2.y-self.p1.y

        something = px*px + py*py

        u =  ((point.x - self.p1.x) * px + (point.y - self.p1.y) * py) / float(something)

        if u > 1:
            u = 1
        elif u < 0:
            u = 0

        x = self.p1.x + u * px
        y = self.p1.y + u * py

        dx = x - point.x
        dy = y - point.y

        # Note: If the actual distance does not matter,
        # if you only want to compare what this function
        # returns to other results of this function, you
        # can just return the squared distance instead
        # (i.e. remove the sqrt) to gain a little performance

        dist = math.sqrt(dx*dx + dy*dy)

        return dist    
