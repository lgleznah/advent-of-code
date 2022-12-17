from math import copysign

movement_dict = {
    'R': (1,0),
    'U': (0,1),
    'L': (-1,0),
    'D': (0, -1)
}

def update_tail_pos(head_pos, tail_pos):
    x_diff, y_diff = head_pos[0] - tail_pos[0], head_pos[1] - tail_pos[1]

    # First case: ortogonally or diagonally adjacent. Do not update
    if (max(abs(x_diff), abs(y_diff)) <= 1):
        return tail_pos

    # Second and third cases
    if ((abs(x_diff) == 2 and y_diff == 0) or (abs(y_diff) == 2 and x_diff == 0)):
        return (tail_pos[0] + x_diff // 2, tail_pos[1] + y_diff // 2)

    # Third case: different row/column
    return (int(tail_pos[0] + copysign(1, x_diff)), int(tail_pos[1] + copysign(1, y_diff)))

def main():
    with open("../inputs/input9", "r") as file:
        rope_parts = [(0,0) for _ in range(10)]
        tail_visited_locations = {(0,0)}

        for line in file.readlines():
            direction, amount = line.split()
            for _ in range(int(amount)):
                movement = movement_dict[direction]
                rope_parts[0] = (rope_parts[0][0] + movement[0], rope_parts[0][1] + movement[1])
                for i in range(1,10):
                    rope_parts[i] = update_tail_pos(rope_parts[i-1], rope_parts[i])
                tail_visited_locations.add(rope_parts[9])

        print(len(tail_visited_locations))

if __name__ == "__main__":
    main()