import re
from functools import lru_cache
from itertools import product


def solve(tunnels_and_valves):

    @lru_cache(maxsize=None)
    def find_solution_recursive(person_cave, elephant_cave, time_left, opened_caves):
        if time_left == 0:
            return 0

        best_solution = 0

        # Case 1: both open their valves (assuming they are closed and non-zero)
        if tunnels_and_valves[person_cave][0] != 0 and tunnels_and_valves[elephant_cave][0] != 0 and person_cave not in opened_caves and elephant_cave not in opened_caves:
            # If they are in the same room, fallback to other cases
            if (person_cave != elephant_cave):
                new_opened_caves = tuple(sorted(opened_caves + (person_cave,elephant_cave)))
                opened_final_flow = tunnels_and_valves[person_cave][0] * (time_left - 1) + tunnels_and_valves[elephant_cave][0] * (time_left - 1)
                best_solution = max(best_solution, opened_final_flow + find_solution_recursive(person_cave, elephant_cave, time_left - 1, new_opened_caves))

        # Case 2: both move
        for other_cave_person, other_cave_elephant in product(tunnels_and_valves[person_cave][1], tunnels_and_valves[elephant_cave][1]):
            first_move, second_move = min(other_cave_person, other_cave_elephant), max(other_cave_person, other_cave_elephant)
            best_solution = max(best_solution, find_solution_recursive(first_move, second_move, time_left - 1, opened_caves))

        # Case 3: one moves, the other opens a valve
        for other_cave_person in tunnels_and_valves[person_cave][1]:
            if tunnels_and_valves[elephant_cave][0] != 0 and elephant_cave not in opened_caves:
                new_opened_caves = tuple(sorted(opened_caves + (elephant_cave,)))
                opened_final_flow = tunnels_and_valves[elephant_cave][0] * (time_left - 1)
                first_move, second_move = min(other_cave_person, elephant_cave), max(other_cave_person, elephant_cave)
                best_solution = max(best_solution, opened_final_flow + find_solution_recursive(first_move, second_move, time_left - 1, new_opened_caves))

        for other_cave_elephant in tunnels_and_valves[elephant_cave][1]:
            if tunnels_and_valves[person_cave][0] != 0 and person_cave not in opened_caves:
                new_opened_caves = tuple(sorted(opened_caves + (person_cave,)))
                opened_final_flow = tunnels_and_valves[person_cave][0] * (time_left - 1)
                first_move, second_move = min(other_cave_elephant, person_cave), max(other_cave_elephant, person_cave)
                best_solution = max(best_solution, opened_final_flow + find_solution_recursive(first_move, second_move, time_left - 1, new_opened_caves))

        return best_solution
    
    return find_solution_recursive('AA', 'AA', 26, tuple()) 


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