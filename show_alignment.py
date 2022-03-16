import sys

f = open(sys.argv[1], "r")
f1 = open(sys.argv[2], "r")
f2 = open(sys.argv[3], "r")

lines = []
lens = []

for i in f:
    line = i.strip().split("|")[1].split()
    lines.apped()
    
for i in f1:
    lens.append([len(i.strip().split())])
    
cont = 0
for i in f2:
    lens[cont].append(len(i.strip().split()))
    cont += 1
    
for line in lines:
    
