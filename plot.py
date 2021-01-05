import sys

if (len(sys.argv) < 3):
    print("usage python plot.py {input file} {output file}")
    exit()

inputFile = sys.argv[1]
outputFile = sys.argv[2]
print(inputFile)
print(outputFile)

data = ''
hpglFile = open(inputFile, 'r')
data = hpglFile.read()
hpglFile.close()
hpcommands = data.split(';')
#print(hpcommands)

rglCommands = []
for hpcommand in hpcommands:
    if (hpcommand.startswith("PU")):
        rglCommands.append(hpcommand.replace("PU","M"))
    if (hpcommand.startswith("PD")):
        rglCommands.append(hpcommand.replace("PD","D"))
#print(rglCommands)

jointCommands = ""
for rglCommand in rglCommands:
    jointCommands += rglCommand
    jointCommands += "\r\n"
#print(jointCommands)

printfile = open(outputFile,"w")
printfile.write("\x1ba\r\n\x1bb\r\nM500,-500\r\nI\r\n")
printfile.write(jointCommands)
printfile.write("\r\n\r\n\x1ba\r\n")
printfile.close()