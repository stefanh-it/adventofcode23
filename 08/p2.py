# TODO: This needs to be optimized. It's not fast enough to 
# solve the problem. Solution Chinese Remainder Theorem

def find_next_node(current_node, nodes, direction):
    if direction == "R":
        return nodes[current_node][1]
    elif direction == "L":
        return nodes[current_node][0]
    else:
        return None

def walk(directions, nodes, starting_nodes):
    directions = list(directions)
    while len(directions) < len(nodes) * 1000000:
        directions.extend(directions)

    current_nodes = starting_nodes
    #print(directions)
    step = 0
    #print(current_nodes)
    new_nodes = []
    while all("Z" in node[2] for node in current_nodes) is False:
        for i, node in enumerate(current_nodes):
            #print(current_nodes)
            # print(node)
            # print(i)
            new_node = find_next_node(node, nodes, directions[step])
            new_nodes.append(new_node)
        #print(new_nodes)
        current_nodes = new_nodes
        new_nodes = []
            # print(current_nodes)
        #     new_nodes.append(node)
        #     print(new_nodes)
    # while list(current_node[2]) != "X":
    #     #print(step)
    #     direction = directions[step]
    #     #print(current_node)
    #     current_node = find_next_node(current_node, nodes, direction)
        step += 1
        print(step)
    # print(current_node)
    return step


def main(input):
    
    instruction_sets = input.splitlines()
    directions = instruction_sets[0]
    nodes = {}
    starting_nodes = []
    # print(directions)
    for instruction in instruction_sets[2:]:
        # print(instruction)
        starting_node = instruction.split(" = ")[0]
        targets = instruction.split(" = ")[1]
        right = targets.split(", ")[1].rstrip(")")
        left = targets.split(", ")[0].lstrip("(")
        node = {starting_node: [left, right]}
        nodes.update(node)
        #print(list(starting_node))
        if starting_node[2] == 'A':
            #print("Found A")
            starting_nodes.append(starting_node)
    #print(nodes)
    print(starting_nodes)
    solution = walk(directions, nodes, starting_nodes)

    return solution

if __name__ == "__main__":
    main(input)
