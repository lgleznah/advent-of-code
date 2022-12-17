def check_visible_trees(grid, position, direction, width, height):
    original_tree = grid[position[0]][position[1]]
    visible_trees = 0

    while position[0] != 0 and position[0] != height - 1 and position[1] != 0 and position[1] != width - 1:
        position[0], position[1] = position[0] + direction[0], position[1] + direction[1]
        visible_trees += 1
        if (grid[position[0]][position[1]] >= original_tree):
            break
    
    return visible_trees

def compute_scenic_score(grid, position, width, height):
    return check_visible_trees(grid, [position[0], position[1]], (-1,0), width, height) * \
           check_visible_trees(grid, [position[0], position[1]], (1,0), width, height) * \
           check_visible_trees(grid, [position[0], position[1]], (0,1), width, height) * \
           check_visible_trees(grid, [position[0], position[1]], (0,-1), width, height)

def main():
    with open("../inputs/input8", "r") as file:
        tree_grid = file.readlines()
        tree_grid = [[int(number) for number in row.strip()] for row in tree_grid]
        
        # Trees in the edge are always visible
        height, width = len(tree_grid), len(tree_grid[0])
        max_score = 0

        # Compute the scenic score of each tree on the inside
        # Trees on the outside have zero score by definition
        for i in range(1, height - 1):
            for j in range(1, width - 1):
                max_score = max(max_score, compute_scenic_score(tree_grid, (i,j), width, height))

        print(max_score)

if __name__ == "__main__":
    main()