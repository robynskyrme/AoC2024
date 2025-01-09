# 8.1.2025

# AoC 2024 Day Eight: Resonant Colinearity, Part One

# Strange, this -- some unexpected behaviour in the "plot" function which I was about to iron out, before I noticed
#   it was (accidentally) doing exactly what the puzzle was asking me to do...



import time

polygons = []
gridwidth = 0
gridheight = 0

class polygon():

    def __init__(self,vcs,character):                  # vcs = vertices
        self.vcs = vcs

        self.character = character

        self.edges = []
        self.antinodes = []

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

#        self.gen_antinodes()
        self.gen_modified_antinodes()




    def gen_antinodes(self):
        rs=19
        for edge in self.edges:
            sa = edge[0][0]
            sb = edge[0][1]
            ea = edge[1][0]
            eb = edge[1][1]

            prenode = [sa * 2 - ea,sb * 2 - eb]
            postnode = [ea * 2 - sa,eb * 2 - sb]

            self.antinodes.append(prenode)
            self.antinodes.append(postnode)


    def gen_modified_antinodes(self):
        if self.character == "M":
            rs=19

        for edge in self.edges:
            sa = edge[0][0]
            sb = edge[0][1]
            ea = edge[1][0]
            eb = edge[1][1]

            xinc = ea-sa
            yinc = eb-sb

#            print(xinc,yinc)

            x = sa
            y = sb

            prenode = [sa * 2 - ea,sb * 2 - eb]
            self.antinodes.append(prenode)
            while x > 0 and y > 0 and x <= gridwidth and y <= gridheight:
                if [x,y] not in self.antinodes:
                    self.antinodes.append([x,y])
                x -= xinc
                y -= yinc


            x = ea
            y = eb

            postnode = [sa * 2 - ea,sb * 2 - eb]
            self.antinodes.append(postnode)
            while x > 0 and y > 0 and x <= gridwidth and y <= gridheight:
                if [x,y] not in self.antinodes:
                    self.antinodes.append([x,y])
                x += xinc
                y += yinc


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

        antinodes_set = polygon.antinodes

        for antinode in antinodes_set:
            x = antinode[0]
            y = antinode[1]
            if x >= 0 and y >= 0 and x < gridsize and y < gridsize:
                grid[y][x] = "¤"


    slab = ""

    for row in grid:
        for point in row:
            slab += point + ""
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
        if slab[point] != "." and slab[point] != "·":
            if slab[point] not in polyraw:
                polyraw.update({slab[point]:[]})
            x = point % gridwidth
            y = point // gridwidth
            polyraw[slab[point]].append([x,y])

    for p in polyraw:
        new_poly = polygon(polyraw[p],p)
        polygons.append(new_poly)


if __name__ == "__main__":
    stopwatch = time.time()

    file = open("08_puzzle.aoc","r")
    data = file.read()
    gridwidth = data.index("\n")
    gridheight = data.count("\n")
    print(gridheight)
    file.close()

    process(data)

    for polygon in polygons:
        rs=19
        #plot(polygon,True,gridwidth)



    userinput = ""
    while userinput != "quit":

        if userinput == "count":
            tally = []
            for p in polygons:
                for an in p.antinodes:
                    if an not in tally:
                        tally.append(an)
                for v in p.vcs:
                    print(v)
                    tally.append(v)
            print("Total antinodes: ",len(tally))

        slab = "Aerial sets marked with: "
        for p in polygons:
            slab += p.character + ", "
        slab = slab[:-2]
        userinput = input(slab)
        for p in polygons:
            if p.character == userinput:
                plot(p,True,gridwidth)


    print("\n/// done in " + str(time.time()-stopwatch) +" seconds ///")
