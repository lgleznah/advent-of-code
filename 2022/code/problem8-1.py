def test_tree_visible_direction(grid, position, direction, width, height):
    original_tree = grid[position[0]][position[1]]

    while position[0] != 0 and position[0] != height - 1 and position[1] != 0 and position[1] != width - 1:
        position[0], position[1] = position[0] + direction[0], position[1] + direction[1]
        if (grid[position[0]][position[1]] >= original_tree):
            return False
    
    return True

def main():
    with open("../inputs/input8", "r") as file:
        tree_grid = file.readlines()
        tree_grid = [[int(number) for number in row.strip()] for row in tree_grid]
        
        # Trees in the edge are always visible
        height, width = len(tree_grid), len(tree_grid[0])
        visible_trees = width * 2 + (height - 2) * 2

        # Test each individual tree on the inside
        for i in range(1, height - 1):
            for j in range(1, width - 1):
                if (test_tree_visible_direction(tree_grid, [i,j], (-1,0), width, height) or
                    test_tree_visible_direction(tree_grid, [i,j], (1,0), width, height) or
                    test_tree_visible_direction(tree_grid, [i,j], (0,1), width, height) or
                    test_tree_visible_direction(tree_grid, [i,j], (0,-1), width, height)):
                    
                    visible_trees += 1
        
        print(visible_trees)

if __name__ == "__main__":
    main()