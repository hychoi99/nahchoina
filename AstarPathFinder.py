from heapq import heappush, heappop
import math

class HeapNode:
    """ The nodes that we are storing in our open and closed nodes
    lists. They record their g, h, and f value.
    """
    def __init__ (self, f, g, h, p, path_from_start):
        self.f = f
        self.g = g
        self.h = h
        self.p = p
        self.path = path_from_start

    def __str__ (self):
        return str(self.p) +" f="+str(self.f)+" g="+str(self.g)+" h="+str(self.h)

    def __eq__(self,other):
            '''allows for comparison of nodes, for use in the "is in" list comprehension'''
            #where p is a tuple (x,y)
            return self.p == other.p


class AStarRunner:

    def __init__ (self, grid):

        self.grid = grid

        self.open_nodes = []
        self.closed_nodes = []
        self.current = None
        self.goal = None
        self.already_seen = []

    def handle_events(self,keymap):
            if keymap.has_key(pygame.K_r) and keymap[pygame.K_r]:
                    print "resetting"
                    self.reset()               


    def reset (self):

        self.open_nodes = []
        self.closed_nodes = []
        self.current = None
        self.goal = None
        self.already_seen = []


    def are_we_done_yet (self):

        return self.current.p == self.goal


    def estimate_distance(self, startp, endp):
        (endx,endy) = endp
        (startx,starty) = startp

        return math.sqrt(pow(endx - startx,2) + pow(endy - starty,2))

    def inbounds(self,p):
        (x,y) = p
        return (x >= 0) and (x < len(self.grid)) and (y >= 0) and (y < len(self.grid[0]))

    def neighbors(self, p):

        (x,y) = p
        #print 'neighbors of: ', str(p)
        outvec = []
        north = (x,y - 1)
        south = (x,y + 1)
        east = (x + 1, y)
        west = (x - 1,y)
        coords = [north,south,east,west]

        outvec = [loc for loc in coords if self.inbounds(loc)]

        return outvec

    def valueAtPoint(self, p):

    	(x,y) = p
    	#print p
    	return self.grid[x][y]

    def search (self, start_loc, end_loc):
        """ start_node and end_node should be names of two nodes in
        the graph."""

        self.reset()

        # initialize
        start_g = 0 #cost to get here
        start_h = self.estimate_distance(start_loc, end_loc)
        start_f = start_g + start_h #cost to get here plus estimate to end
        path_so_far = []
        heapnode = HeapNode(start_f, start_g, start_h, start_loc, path_so_far)
        heappush (self.open_nodes, (heapnode.f,heapnode))

        self.already_seen = [heapnode]
        self.goal = end_loc

        # search
        (val,self.current) = heappop(self.open_nodes)
        
        while not self.are_we_done_yet() :

            for neighbor in self.neighbors(self.current.p):

                #put neighbor into heapnode
                neighbornode = HeapNode (0, 0, 0, neighbor, [])

                if neighbornode not in self.already_seen:
                    #cost to get to neighbor includes
                    # g is the cost to get from start to here
                    neighbornode.g = self.current.g + self.valueAtPoint(neighbor)
                    #h is an estimate of distance from here to end point
                    neighbornode.h = self.estimate_distance(neighbor, self.goal)
                    # so f = g +h
                    neighbornode.f = neighbornode.g + neighbornode.h

                    #just store locations, not node data in path
                    path_so_far = self.current.path + [neighbor]

                    neighbornode.path = path_so_far
                    #heapnode = HeapNode (f, g, h, neighbor, path_so_far)
                    #python asks us to implement priority queues
                    # of custom objects as tuples (p,obj)
                    # which leads to this (somewhat inelegant) syntax
                    heappush (self.open_nodes, (neighbornode.f,neighbornode))
                    self.already_seen.append(neighbornode)

            self.closed_nodes.append(self.current)
            #self.print_astar_info ()
            (val,self.current) = heappop (self.open_nodes)

        # Loop has ended: we must be done

        return [start_loc] + self.current.path
