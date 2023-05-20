class Dijkstra:
    def __init__(self, nodes):
        self.nodes = nodes
    def __minNode(self, arr=[], finish=None):
        if (len(arr) == 0):
            return None
        min = None
        for i in arr:
            if i.checked:
                continue
            if min == None:
                min = i
            if i.cost < min.cost:
                min = i
        if min.checked or min.name == finish.name:
            return None

        min.checked = True
        return min

# It takes two arguments representing the start and end nodes of the path.
    def findShortestPath(self, a, b):
        import math
        if not isinstance(a, Node) or not isinstance(b, Node):
            print("A and B are not nodes...")
            return None
        self.resetNodes(self.nodes)
        a.cost = 0
        arr = [a]

        while (True):
            min = self.__minNode(arr, b)
            if (min == None):
                break

            for i in min.connections:
                arr.append(i)
                #Euclidean distance formula 
                distance = min.cost + math.sqrt((i.coords[0] - min.coords[0]) ** 2 + (i.coords[1] - min.coords[1]) ** 2)
                if (i.cost == -1 or i.cost > distance):
                    i.cost = distance
                    i.parent = min

        arr.clear()
        arr = [b]
        while (arr[-1].name != a.name):
            arr.append(arr[-1].parent)
        return arr

    def resetNodes(self, nodes):
        for i in nodes:
            i.cost = -1
            i.parent = None
            i.checked = False

class Node:
    def __init__(self, name, coords=(0,0)):
        self.name = name
        self.coords = coords
        self.connections = []
        self.cost = -1
        self.parent = None
        self.checked = False

    def __repr__(self):
        return str(f"Node({self.name})")
