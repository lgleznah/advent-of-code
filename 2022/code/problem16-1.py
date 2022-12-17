import re
from functools import lru_cache

def solve(tunnels_and_valves):

    @lru_cache(maxsize=None)
    def find_solution_recursive(cave, time_left, opened_caves):
        if time_left == 0:
            return 0

        best_solution = 0
        if tunnels_and_valves[cave][0] != 0 and cave not in opened_caves:
            new_opened_caves = tuple(sorted(opened_caves + (cave,)))
            best_solution = tunnels_and_valves[cave][0] * (time_left - 1) + find_solution_recursive(cave, time_left - 1, new_opened_caves)
        for other_cave in tunnels_and_valves[cave][1]:
            best_solution = max(best_solution, find_solution_recursive(other_cave, time_left - 1, opened_caves))

        return best_solution
    
    return find_solution_recursive('AA', 30, tuple())


def main():
    with open("../inputs/input16", "r") as file:
        regex_parser = r'^Valve (?P<name>[A-Z][A-Z]).*rate=(?P<flow_rate>\d+).*valves? (?P<other_valves>.*)'
        tunnels_and_valves = {}
        for line in file.readlines():
            name, flow_rate, others = re.match(regex_parser, line.strip()).groups()
            flow_rate = int(flow_rate)
            others = tuple([other.strip() for other in others.split(',')])
            tunnels_and_valves[name] = (flow_rate, others)

        print(solve(tunnels_and_valves))

if __name__ == "__main__":
    main()