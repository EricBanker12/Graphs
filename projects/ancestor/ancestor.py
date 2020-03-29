
def earliest_ancestor(ancestors, starting_node):
    ancestries = []
    stack = []
    stack.append([starting_node])

    # dft all ancestries O(n^2)
    while len(stack):
        ancestry = stack.pop()
        
        no_ancestor = True
        for parent_child in ancestors:
            if parent_child[1] == ancestry[-1]:
                stack.append([*ancestry, parent_child[0]])
                no_ancestor = False

        if no_ancestor:
            ancestries.append(ancestry)

    # find longest ancestry length O(n)
    longest = 1
    for ancestry in ancestries:
        length = len(ancestry)
        if length > longest:
            longest = length

    # if no ancestors, return -1
    if longest == 1:
        return -1
    
    # filter ancestries to longest length O(n)
    ancestries = filter(lambda arr: len(arr) == longest, ancestries)

    # return smallest id last ancestor O(n)
    return min(ancestries, key=lambda arr: arr[-1])[-1]