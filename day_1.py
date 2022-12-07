from utils.inputManager import getInputData

data=getInputData("https://adventofcode.com/2022/day/1/input")
elflist=list()
for elf in data.strip().split('\n\n'):
    elflist.append(sum([int(food) for food in elf.split('\n')]))
elflist=sorted(elflist)
print(f"Top 3 elfs : {elflist[-3:]}, total : {sum(elflist[-3:])}")