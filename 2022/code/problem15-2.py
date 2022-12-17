import re
from tqdm import tqdm

quadrant_movements = [
    (-1, -1),
    (-1, 1),
    (1, 1),
    (1, -1)
]

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def main():
    with open("../inputs/input15", "r") as file:
        sensor_distances = []
        beacon_locations = set()
        regex = r'.*x=(?P<x_sensor>\-?\d+), y=(?P<y_sensor>\-?\d+):.*x=(?P<x_beacon>\-?\d+), y=(?P<y_beacon>\-?\d+).*'
        min_x, max_x = 99999999999, -9999999999999

        for line in file.readlines():
            x_sensor, y_sensor, x_beacon, y_beacon = [int(coord) for coord in re.match(regex, line.strip()).groups()]
            sensor_beacon_distance = manhattan((x_sensor, y_sensor), (x_beacon, y_beacon))
            sensor_distances.append(((x_sensor, y_sensor), sensor_beacon_distance))
            if (x_sensor - sensor_beacon_distance < min_x):
                min_x = x_sensor - sensor_beacon_distance

            if (x_sensor + sensor_beacon_distance > max_x):
                max_x = x_sensor + sensor_beacon_distance

            beacon_locations.add((x_beacon, y_beacon))

        possible_locations = set()

        for i in range(len(sensor_distances)):
            scan_distance = sensor_distances[i][1] + 1
            iterating_coords = [sensor_distances[i][0][0] + scan_distance, sensor_distances[i][0][1]]
            number_movements = scan_distance * 4

            print(f"Scanning sensor {i}, located at {(sensor_distances[i][0][0], sensor_distances[i][0][1])}, at distance {scan_distance}")

            for mov in range(number_movements):
                # Update position and flags
                iterating_coords[0] += quadrant_movements[mov // scan_distance][0]
                iterating_coords[1] += quadrant_movements[mov // scan_distance][1]
                possible_location = True

                if (iterating_coords[0] > 4000000 or iterating_coords[1] > 4000000 or iterating_coords[0] < 0 or iterating_coords[1] < 0):
                    continue

                # Test against other sensors
                for j in range(len(sensor_distances)):
                    if (i == j):
                         continue
                    other_sensor, max_distance = sensor_distances[j][0], sensor_distances[j][1]
                    if manhattan(iterating_coords, other_sensor) <= max_distance or (iterating_coords[0], iterating_coords[1]) in beacon_locations:
                        possible_location = False
                        break

                if (possible_location):
                    print(f"Possible location at ({iterating_coords[0]}, {iterating_coords[1]})")
                    possible_locations.add((iterating_coords[0], iterating_coords[1]))

        if (len(possible_locations) > 1):
            print("Oops...")
        else:
            location = list(possible_locations)[0]
            print(location[0] * 4000000 + location[1])

if __name__ == "__main__":
    main()