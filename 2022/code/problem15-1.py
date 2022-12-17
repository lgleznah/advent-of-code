import re
from tqdm import tqdm

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def main():
    with open("../inputs/input15", "r") as file:
        sensor_distances = {}
        beacon_locations = set()
        regex = r'.*x=(?P<x_sensor>\-?\d+), y=(?P<y_sensor>\-?\d+):.*x=(?P<x_beacon>\-?\d+), y=(?P<y_beacon>\-?\d+).*'
        min_x, max_x = 99999999999, -9999999999999
        impossible_locations = 0

        for line in file.readlines():
            x_sensor, y_sensor, x_beacon, y_beacon = [int(coord) for coord in re.match(regex, line.strip()).groups()]
            sensor_beacon_distance = manhattan((x_sensor, y_sensor), (x_beacon, y_beacon))
            sensor_distances[(x_sensor, y_sensor)] = sensor_beacon_distance
            if (x_sensor - sensor_beacon_distance < min_x):
                min_x = x_sensor - sensor_beacon_distance

            if (x_sensor + sensor_beacon_distance > max_x):
                max_x = x_sensor + sensor_beacon_distance

            beacon_locations.add((x_beacon, y_beacon))

        for x in tqdm(range(0, 4000000)):
            coords = (x, 2000000)
            for sensor, distance in sensor_distances.items():
                if manhattan(coords, sensor) <= distance and not coords in beacon_locations:
                    impossible_locations += 1
                    break

        print(impossible_locations)

if __name__ == "__main__":
    main()