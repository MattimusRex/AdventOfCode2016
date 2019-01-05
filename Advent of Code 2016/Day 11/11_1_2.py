import sys
import queue
import copy
import re


class Floor:
    def __init__(self, chips, generators, level):
        self.chips = chips
        self.generators = generators
        self.level = level

class Game_State:
    def __init__(self, floors, cur_floor, counter):
            self.floors = floors
            self.counter = counter
            self.cur_floor = cur_floor
            self.steps = []

    def build_state_from_id(self, state_id):
        test = re.compile(r"\d[A-Z]*")
        parts = test.findall(state_id)
        floors = dict()
        floor_1 = Floor(parts[1][1:], parts[2][1:], 1)
        floor_2 = Floor(parts[3][1:], parts[4][1:], 2)
        floor_3 = Floor(parts[5][1:], parts[6][1:], 3)
        floor_4 = Floor(parts[7][1:], parts[8][1:], 4)
        floors[1] = floor_1
        floors[2] = floor_2
        floors[3] = floor_3
        floors[4] = floor_4
        return Game_State(floors, parts[0], 0)

    def get_id(self):
        string = str(self.cur_floor)
        for key in self.floors:
            temp = str(key)
            for chip in self.floors[key].chips:
                temp += chip
            string += "".join(sorted(temp))
            temp = str(key)
            for generator in self.floors[key].generators:
                temp += generator
            string += "".join(sorted(temp))   
        return string

    def get_moves_list(self, visited):
        moves = []
        cur_floor = self.floors[self.cur_floor]
        TM = next((chip for chip in cur_floor.chips if chip == "T"), None)
        TG = next((generator for generator in cur_floor.generators if generator == "T"), None)

        if self.cur_floor < 4:
            #move 2 chips, no TM
            found = False
            for i, chip in enumerate([x for x in cur_floor.chips if x != "T"]):
                for chip2 in [x for x in cur_floor.chips[i+1:] if x != "T" and x != chip]:
                    temp = self.move_chips_up(chip, chip2)
                    if temp.is_valid() and not found:
                        moves.append(temp)
                        found = True
                    else:
                        visited.add(temp.get_id())

            #move TG and another generator up
            if TG != None:
                found = False
                for generator in [x for x in cur_floor.generators if x != "T"]:
                    temp = self.move_generators_up(TG, generator)
                    if temp.is_valid() and not found:
                        moves.append(temp)
                        found = True
                    else:
                        visited.add(temp.get_id())
            
            #move TM and another chip up
            if TM != None:
                found = False
                for chip in [x for x in cur_floor.chips if x != "T"]:
                    temp = self.move_chips_up(TM, chip)
                    if temp.is_valid() and not found:
                        moves.append(temp)
                        found = True
                    else:
                        visited.add(temp.get_id())         
           
        if self.cur_floor > 1:
            middle_floor_count = len(self.floors[2].chips) + len(self.floors[2].generators) + len(self.floors[3].chips) + len(self.floors[3].generators)
            if self.cur_floor != 2 or middle_floor_count <= 3:             
                #move TM down
                if TM != None:
                    temp = self.move_chip_down(TM)
                    if temp.is_valid():
                        moves.append(temp)

                #move TG down
                if TG != None:
                    temp = self.move_generator_down(TG)
                    if temp.is_valid():
                        moves.append(temp)
                    
                #move 1 chip
                found = False
                for chip in [x for x in cur_floor.chips if x != "T"]:
                    temp = self.move_chip_down(chip)
                    if temp.is_valid() and not found:
                        moves.append(temp)
                        found = True
                    else:
                        visited.add(temp.get_id())

        return moves

    #if a floor has generators, make sure any chips 
    # on that floor have their matching generator
    def is_valid(self):
        for key in self.floors:
            if len(self.floors[key].generators) > 0 and len(self.floors[key].chips) > 0:
                for chip in self.floors[key].chips:
                    if chip not in self.floors[key].generators:
                        return False
        return True

    def make_copy(self, floor_change):
        temp = copy.deepcopy(self)
        temp.counter += 1
        temp.cur_floor += floor_change
        return temp

    def move_chip_down(self, chip):
        temp = self.make_copy(-1)
        temp.floors[temp.cur_floor].chips.append(chip)
        temp.floors[temp.cur_floor + 1].chips.remove(chip)
        temp.steps.append(temp.get_id())
        return temp
        
    def move_chips_up(self, chip1, chip2):
        temp = self.make_copy(1)
        temp.floors[temp.cur_floor].chips.append(chip1)
        temp.floors[temp.cur_floor].chips.append(chip2)
        temp.floors[temp.cur_floor - 1].chips.remove(chip1)
        temp.floors[temp.cur_floor - 1].chips.remove(chip2)
        temp.steps.append(temp.get_id())
        return temp

    def move_generator_down(self, generator):
        temp = self.make_copy(-1)
        temp.floors[temp.cur_floor].generators.append(generator)
        temp.floors[temp.cur_floor + 1].generators.remove(generator)
        temp.steps.append(temp.get_id())
        return temp

    def move_generators_up(self, generator1, generator2):
        temp = self.make_copy(1)
        temp.floors[temp.cur_floor].generators.append(generator1)
        temp.floors[temp.cur_floor].generators.append(generator2)
        temp.floors[temp.cur_floor - 1].generators.remove(generator1)
        temp.floors[temp.cur_floor - 1].generators.remove(generator2)
        temp.steps.append(temp.get_id())
        return temp

    def print(self):
            print("Game State")
            print("Level: " + str(self.cur_floor))
            print("ID: " + self.get_id())
            print("Counter " + str(self.counter))
            for key in self.floors:
                print(str(key) +": ", end="")
                for chip in self.floors[key].chips:
                    print(str(chip) + "M ", end="")
                for generator in self.floors[key].generators:
                    print(str(generator) + "G ", end="")
                print("")
            print("")


    def solve(self, visited):
        q = queue.Queue()
        q.put(self)
        cur_state = self
        while True:
            try:
                cur_state = q.get(False)
            except queue.Empty:
                return -1
            else:
                if len(cur_state.floors[4].chips) + len(cur_state.floors[4].generators) == AMOUNT:
                    for step in cur_state.steps:
                        cur_state.build_state_from_id(str(step)).print()
                    return cur_state.counter
                else:
                    if cur_state.get_id() not in visited:
                        visited.add(cur_state.get_id())
                        moves_list = cur_state.get_moves_list(visited)
                        for move in moves_list:
                            if move.get_id() not in visited:
                                q.put(move)

#ignore floor 0
floors = dict()
visited = set()
AMOUNT = 14
floor_1 = Floor(["P", "S", "E"], ["P", "S", "E"], 1)
floor_2 = Floor(["R", "C", "D"], ["T", "R", "C", "D"], 2)
floor_3 = Floor(["T"], [], 3)
floor_4 = Floor([], [], 4)
floors[1] = floor_1
floors[2] = floor_2
floors[3] = floor_3
floors[4] = floor_4
state_1 = Game_State(floors, 2, 1)
state_1.steps.append(state_1.get_id())
steps = state_1.solve(visited)
print(steps)