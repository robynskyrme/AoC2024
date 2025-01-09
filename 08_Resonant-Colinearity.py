# 8.1.2025

# AoC 2024 Day Eight: Resonant Colinearity, Part One

# Strange, this -- some unexpected behaviour in the "plot" function which I was about to iron out, before I noticed
#   it was (accidentally) doing exactly what the puzzle was asking me to do...



import time

polygons = []
gridwidth = 0

class polygon():
    edges = []
    antinodes = []
    character = ""
    def __init__(self,vcs):                  # vcs = vertices
        self.vcs = vcs

        starts = []
        ends = []
        for vx in vcs:
            starts.append(vx)
            ends.append(vx)

        for s in starts:
            for e in ends:
                if s != e:
                    if [s,e] not in self.edges and [e,s] not in self.edges:
                        self.edges.append([s,e])

        self.gen_antinodes()




    def gen_antinodes(self):
        for edge in self.edges:
            sa = edge[0][0]
            sb = edge[0][1]
            ea = edge[1][0]
            eb = edge[1][1]

            prenode = [sa * 2 - ea,sb * 2 - eb]
            postnode = [ea * 2 - sa,eb * 2 - sb]

            self.antinodes.append(prenode)
            self.antinodes.append(postnode)

def plot(polygon,antinodes,gridsize):

    grid = []

    vertices = polygon.vcs

    vectorints = set()

    for vx in range(len(polygon.vcs)):
        loc = vertices[vx][1] * gridsize + vertices[vx][0]
        vectorints.add(loc)

    for y in range(gridsize):
        row = []
        for x in range(gridsize):
            if y * gridsize + x in vectorints:
                 row.append(polygon.character)
            else:
                row.append("·")
        grid.append(row)

    if antinodes == True:
        antinodes = polygon.antinodes

        for antinode in antinodes:
            x = antinode[0]
            y = antinode[1]
            if x >= 0 and y >= 0 and x < gridsize and y < gridsize:
                grid[y][x] = "¤"


    slab = ""

    for row in grid:
        for point in row:
            slab += point + " "
        slab += "\n"

    print(slab)
    print("Total antinodes: " + str(slab.count("¤")))

def process(raw):
    slab = ""
    for c in range(len(raw)):
        if raw[c] != "\n":
            slab += raw[c]

    polyraw = {}

    for point in range(len(slab)):
        if slab[point] != ".":
            if slab[point] not in polyraw:
                polyraw.update({slab[point]:[]})
            x = point % gridwidth
            y = point // gridwidth
            polyraw[slab[point]].append([x,y])

    for p in polyraw:
        new_poly = polygon(polyraw[p])
        new_poly.character = p
        polygons.append(new_poly)


if __name__ == "__main__":
    stopwatch = time.time()

    file = open("08_puzzle.aoc","r")
    data = file.read()
    gridwidth = data.index("\n")
    file.close()

    process(data)

    for polygon in polygons:
        rs=19
        #plot(polygon,True,gridwidth)

    userinput = ""
    while userinput != "quit":
        slab = "Aerial sets marked with: "
        for p in polygons:
            slab += p.character + ", "
        userinput = input(slab)
        for p in polygons:
            if p.character == userinput:
                plot(p,False,gridwidth)

    print("\n/// done in " + str(time.time()-stopwatch) +" seconds ///")
