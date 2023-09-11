#Yousaf Rajput
#I pledge my Honor that I have abided by the Stevens Honor System
Syntax = {
    'R0' : '00',
    'R1' : '01',
    'R2' : '10',
    'R3' : '11',
    'ADD' : '00100',
    'SUB' : '00101',
    'LD' : '10110', #because we dont have second input argument yet for LDR
    'MOV' : '01100'
}
fileInstructions = []
instructionMemory = []
with open('Code.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        fileInstructions += [line.split(" ")]
        #print(fileInstructions)
    
    for instruction in fileInstructions:
        binary = ''
        if(instruction[0] == 'MOV'):
            binary += Syntax.get(instruction[0])
            binary += str(format(int(instruction[2]), '04b'))
            binary += Syntax.get(instruction[1])
        else:
            for syntax in instruction:
                if syntax in Syntax:
                    binary += Syntax.get(syntax)
        if(binary != ''):
            binary = "{0:0>4x}".format(int(binary, 2))
            instructionMemory.append(binary)

count = 0
instrucLen = len(instructionMemory)
fileContent = ""
while(count < 256):
    if(count % 16 == 0):
        fileContent += "\n{0:0>2x}:".format(count)
    if(count < instrucLen):
        fileContent += " " + instructionMemory[count]
    else:
        fileContent += " 0000" 
    count += 1


with open('NewInstructions.txt', 'w') as newFile:
        newFile.write(fileContent)
    