import time

def simulate(grid, spawn_point):
    num_grains = 0

    while (True):
        sand_position = spawn_point
        while (True):
            if (grid[sand_position[1] + 1][sand_position[0]] == '.'):
                sand_position = (sand_position[0], sand_position[1] + 1)
                continue

            elif (grid[sand_position[1] + 1][sand_position[0] - 1] == '.'):
                sand_position = (sand_position[0] - 1, sand_position[1] + 1)
                continue

            elif (grid[sand_position[1] + 1][sand_position[0] + 1] == '.'):
                sand_position = (sand_position[0] + 1, sand_position[1] + 1)
                continue

            grid[sand_position[1]][sand_position[0]] = 'O'
            num_grains += 1
            if (sand_position[0] == 500 and sand_position[1] == 0):
                print(f"Sand stuck at sand grain number {num_grains}!")
                return
            break


def main():
    with open("../inputs/input14", "r") as file:
        # For lowering memory consumption, only generate the board in the range ((min_x-1, 0) - (max_x+1, max_y+1))
        max_y = -99999999
        lines_list = []
        for line in file.readlines():
            line_points = line.strip().split(" -> ")
            parsed_line = []
            for point in line_points:
                x, y = [int(coord) for coord in point.split(',')]
                parsed_line.append((x,y))
                max_y = max(y, max_y)
            
            lines_list.append(parsed_line)

        lines_list.append([(0, max_y+2), (999, max_y+2)])
        caves = [['.' for _ in range(1000)] for _ in range(max_y + 3)]
        
        for line in lines_list:
            segment_idx = 0
            while segment_idx < len(line) - 1:
                (x_begin, y_begin), (x_end, y_end) = line[segment_idx], line[segment_idx+1]
                if (x_begin == x_end):
                    for y in range(min(y_begin,y_end), max(y_begin,y_end)+1):
                        caves[y][x_begin] = "#"

                if (y_begin == y_end):
                    for x in range(min(x_begin,x_end), max(x_begin,x_end)+1):
                        caves[y_begin][x] = "#"

                segment_idx += 1

        sand_spawn = (500, 0)

        simulate(caves, sand_spawn)

if __name__ == "__main__":
    main()