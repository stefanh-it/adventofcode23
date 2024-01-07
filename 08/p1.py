def find_next_node(current_node, nodes, direction):
    if direction == "R":
        return nodes[current_node][1]
    elif direction == "L":
        return nodes[current_node][0]
    else:
        return None

def walk(directions, nodes, starting_node):
    directions = list(directions)
    while len(directions) < len(nodes) * 100:
        directions.extend(directions)

    current_node = starting_node
    #print(directions)
    step = 0
    while current_node != "ZZZ":
        #print(step)
        direction = directions[step]
        #print(current_node)
        current_node = find_next_node(current_node, nodes, direction)
        step += 1
# print(current_node)
    return step


def main(input):
    
    instruction_sets = input.splitlines()
    directions = instruction_sets[0]
    nodes = {}
    # print(directions)
    for instruction in instruction_sets[2:]:
        # print(instruction)
        starting_node = instruction.split(" = ")[0]
        targets = instruction.split(" = ")[1]
        right = targets.split(", ")[1].rstrip(")")
        left = targets.split(", ")[0].lstrip("(")
        node = {starting_node: [left, right]}
        nodes.update(node)
    #print(nodes)
    solution = walk(directions, nodes, starting_node="AAA")

    return solution

if __name__ == "__main__":
    main(input)
