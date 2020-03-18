# Write a function that takes a 2D binary array and
# returns the number of 1 islands. An island consists
# of 1s that are connected to the north, south, east
# or west.

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

def island_counter(islands):
    visited = set()
    islands_list = []
    
    # go to every coord
    for y in range(len(islands)):
        for x in range(len(islands[y])):

            # if new island
            if not (x,y) in visited and read_matrix(islands, x, y):
                # dft to get an island
                island = []
                stack = [(x, y)]

                # append all connected coords to island and visited
                while len(stack):
                    x, y = stack.pop()
                    island.append((x, y))
                    visited.add((x, y))

                    n = (x, y-1)
                    if not n in visited and read_matrix(islands, *n):
                        stack.append(n)

                    s = (x, y+1)
                    if not s in visited and read_matrix(islands, *s):
                        stack.append(s)

                    e = (x+1, y)
                    if not e in visited and read_matrix(islands, *e):
                        stack.append(e)

                    w = (x-1, y)
                    if not w in visited and read_matrix(islands, *w):
                        stack.append(w)

                # add island to islands_list
                islands_list.append(island)

    # return length of islands_list
    return len(islands_list)

def read_matrix(matrix, x, y):
    if y < 0 or x < 0:
        return None
    try:
        return islands[y][x]
    except IndexError:
        return None

print(island_counter(islands)) # returns 4