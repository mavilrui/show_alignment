import sys

f = open(sys.argv[1], "r")
f1 = open(sys.argv[2], "r")

lines = []
lens = []

def add_letter(line, letter):
    s_letter = str(letter)
    if len(s_letter) == 1:
        return line + " " + s_letter + " "
    else:
        return line + " " + s_letter
    
for i in f:
    lines.append(i.strip().split("|")[1].split())
    
for i in f1:
    lens.append(len(i.strip().split()))
    
cont = 0
for line in lines:
    aux_top = ""
    aux_bot = ""
    last_bot = 0
    for idx in range(len(line)):
        val = int(line[idx])
        if val == last_bot:
            aux_top = add_letter(aux_top, idx)
            aux_bot = add_letter(aux_bot, " ")
        elif val > last_bot:
            for aux in range(last_bot + 1, val):
                aux_top = add_letter(aux_top, " ")
                aux_bot = add_letter(aux_bot, aux)
            aux_top = add_letter(aux_top, idx)
            aux_bot = add_letter(aux_bot, val)
            last_bot = val
    if last_bot < lens[cont] - 1:
        for aux in range(last_bot + 1, lens[cont])
            aux_top = add_letter(aux_top, " ")
            aux_bot = add_letter(aux_bot, aux)
    print("*")
    print(aux_top)
    print(aux_bot)
    cont += 1
