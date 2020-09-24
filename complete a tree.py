edge_list = []
with open('rosalind_tree.txt') as input_data:
    edges = input_data.read().strip().split('\n')
    n = int(edges.pop(0))
    for edge in edges:
        edge = [int(i) for i in edge.split()]
        edge_list.append(edge)

# List of sets of nodes which are connected to eachother.
# Initially start with completely disconnected nodes.
connected_nodes =  list(range(1, n + 1))

for edge in edge_list:
    temp_nodes = set()
    del_nodes = []
    for nodes in connected_nodes:
        # If both nodes in the edge are already connected, we're done.
        if (edge[0] == nodes) and (edge[1] == nodes):
            break

        # Check if only one end of the edge is in a given set of node.  If so, store the nodes.
        elif (edge[0] == nodes) or (edge[1] == nodes):
            # Add all the nodes to a temporary set.  Store the connected nodes for deletion.
            temp_nodes.add(nodes)
            del_nodes.append(nodes)
            # If we've found matches in two separate nodes, we're guaranteed to be done searching.
            if len(del_nodes) == 2:
                break

    # Check if an update is necessary.
    if len(del_nodes) != 0:
        # Make sure both nodes in the edge get added.
        temp_nodes.add(edge[0])
        temp_nodes.add(edge[1])
        # Remove the old connected nodes.
        for nodes in del_nodes:
            connected_nodes.remove(nodes)
        # Add one new connected node containing all the nodes.
        connected_nodes.append(temp_nodes)


print(len(connected_nodes) - 1)
with open('032_TREE.txt', 'w') as output_data:
    output_data.write(str(len(connected_nodes) - 1))

# 这种解决方式都是不完整的，我觉得可以考虑递归的算法
# 不断对元素进行取集合
