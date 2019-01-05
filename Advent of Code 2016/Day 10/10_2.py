import queue
class Bot:
    def __init__(self, bot_id):
        self.bot_id = bot_id
        self.num1 = None
        self.num2 = None
        self.operations = queue.Queue()

    def addNum(self, num):
        if self.num1 is None:
            self.num1 = num
        elif self.num1 <= num:
            self.num2 = num
        else:
            self.num2 = self.num1
            self.num1 = num
        if self.num1 == 17 and self.num2 == 61:
            self.print()
        #self.print()
        
    def addOperation(self, operation):
        self.operations.put(operation)

    def print(self):
        print("Bot ID: " + str(self.bot_id) + " num1: " + str(self.num1) + " num2: " + str(self.num2))

    def process(self, bots, outputs):
        #get operation from queue
        if not self.operations.empty():
            line = self.operations.get()
            parts = line.split()
            #process low num
            #give to bot
            lowID = int(parts[6])
            highID = int(parts[11])
            if parts[5] == "bot":
                if lowID not in bots:
                    bots[lowID] = Bot(lowID)
                bots[lowID].addNum(self.num1)
                self.num1 = None
                #if bot that received number now has 2 numbers, process it
                if bots[lowID].ready():
                    bots[lowID].process(bots, outputs)
            #give to output
            else:
                outputs[lowID] = self.num1
                self.num1 = None
            #process high num
            if parts[-2] == "bot":          
                if highID not in bots:
                    bots[highID] = Bot(highID)
                bots[highID].addNum(self.num2)
                self.num2 = None
                #if bot that received number now has 2 numbers, process it
                if bots[highID].ready():
                    bots[highID].process(bots, outputs)
            else:
                outputs[highID] = self.num2
                self.num2 = None

    def ready(self):
        return self.num1 is not None and self.num2 is not None

bots = dict()
outputs = dict()
with open("input.txt") as input_file:
    for index, line in enumerate(input_file):
        parts = line.split()
        #parse lines to determine what action to take
        if parts[0] == "value":
            bot_id = int(parts[-1])
            #keep bots in dictionary
            if bot_id not in bots:
                bots[bot_id] = Bot(bot_id)
            bots[bot_id].addNum(int(parts[1]))
            #if bots have two numbers aka ready, process their next operation
            if bots[bot_id].ready():
                bots[bot_id].process(bots, outputs)
        #action is an "operation"
        elif parts[0] == "bot":
            bot_id = int(parts[1])
            if bot_id not in bots:
                bots[bot_id] = Bot(bot_id)
            #add operation to bots queue, then process if bot has 2 nums
            bots[bot_id].addOperation(line)
            if bots[bot_id].ready():
                bots[bot_id].process(bots, outputs)
print(outputs[0] * outputs[1] * outputs[2])