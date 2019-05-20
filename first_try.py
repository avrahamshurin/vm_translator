a= "eq     constant       8// sdfgd"
b = a.split("//")[0].split(" ")
c = [item for item in b if item != ""]
print(b)
print(c)
print("// " + " ".join(c))
num = 0

if c[0] == "push":
    if c[1] == "constant":
        print("@{}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1".format(c[2]))




if c[0] == "add":
    print("@SP\nM=M-1\nA=M\nD=M\nA=A-1\nM=M+D")
elif c[0]=="sub":
    print("@SP\nM=M-1\nA=M\nD=M\nA=A-1\nM=M-D")
elif c[0] == "neg":
    print("@SP\nA=M-1\nM=-M")
elif c[0] == "eq":
    print("@SP\nM=M-1\nA=M\nD=M\nA=A-1\nD=D-M\n@one{}\nD;JEQ\n@SP\nA=M-1\nM=0\n@cont{}\n0;JMP\n(one{})\n@SP\nA=M-1\nM=-1\n(cont{})".format(num,num,num,num))
    num += 1
elif c[0] == "gt":
    print("@SP\nM=M-1\nA=M\nD=M\nA=A-1\nD=D-M\n@one{}\nD;JLT\n@SP\nA=M-1\nM=0\n@cont{}\n0;JMP\n(one{})\n@SP\nA=M-1\nM=-1\n(cont{})".format(num,num,num,num))
    num += 1
elif c[0] == "lt":
    print("@SP\nM=M-1\nA=M\nD=M\nA=A-1\nD=D-M\n@one{}\nD;JGT\n@SP\nA=M-1\nM=0\n@cont{}\n0;JMP\n(one{})\n@SP\nA=M-1\nM=-1\n(cont{})".format(num,num,num,num))
    num += 1
elif c[0] == "and":
    print("@SP\nM=M-1\nA=M\nD=M\nA=A-1\nM=D&M")
elif c[0] == "and":
    print("@SP\nM=M-1\nA=M\nD=M\nA=A-1\nM=D|M")
elif c[0] == "not":
    print("@SP\nA=M-1\nM=!M")
file = open("result.txt", "w")
file.write("// " + " ".join(c) + "\n")

'''''
if c[0] == "push":
    if c[1] == "constant":

        file.write("@{}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1".format(c[2]))
file.close()
'''

