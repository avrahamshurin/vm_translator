a= "push    pointer       1// sdfgd"
file_name = "temp"
b = a.split("//")[0].split(" ")
c = [item for item in b if item != ""]
memory_dic ={"local":"LCL","argument":"ARG","this":"THIS","that":"THAT","0":"THIS","1":"THAT"}
print(b)
print(c)
print("// " + " ".join(c))
num = 0

if c[0] == "push":
    if c[1] == "constant":
        print("@{}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1".format(c[2]))
    elif c[1] == "local" or c[1] =="argument" or c[1] =="this" or c[1]=="that":
        print("@{}\nD=A\n@{}\nA=M\nM=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1".format(c[2],memory_dic[c[1]]))
    elif c[1] =="static":
        print("@{}.{}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1".format(file_name,c[2]))
    elif c[1] == "temp":
        print("@{}\nD=A\n@5\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1".format(c[2]))
    elif c[1] =="pointer":
        print("@{}\nA=M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1".format(memory_dic[c[2]]))

if c[0] == "pop":
    if c[1] == "local" or c[1] =="argument" or c[1] =="this" or c[1]=="that":
        print("@{}\nD=A\n@{}\nD=D+M\n@address\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@address\nA=M\nM=D".format(c[2],memory_dic[c[1]]))
    elif c[1] =="static":
        print("@SP\nM=M-1\nA=M\nD=M\n@{}.{}\nM=D".format(file_name,c[2]))
    elif c[1] == "temp":
        print("@{}\nD=A\n@5\nD=D+A\n@address\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@address\nA=M\nM=D".format(c[2]))
    elif c[1] == "pointer":
        print("@SP\nM=M-1\nA=M\D=M@{}\nA=M\nM=D".format(memory_dic[c[2]]))




if c[0] == "add":
    print("@SP\nM=M-1\nA=M\nD=M\nA=A-1\nM=M+D")
elif c[0]=="sub":
    print("@SP\nM=M-1\nA=M\nD=M\nA=A-1\nM=M-D")
elif c[0] == "neg":
    print("@SP\nA=M-1\nM=-M")
elif c[0] == "eq":
    print("@SP\nM=M-1\nA=M\nD=M\nA=A-1\nD=D-M\n@one{0}\nD;JEQ\n@SP\nA=M-1\nM=0\n@cont{0}\n0;JMP\n(one{0})\n@SP\nA=M-1\nM=-1\n(cont{0})".format(num))
    num += 1
elif c[0] == "gt":
    print("@SP\nM=M-1\nA=M\nD=M\nA=A-1\nD=D-M\n@one{0}\nD;JLT\n@SP\nA=M-1\nM=0\n@cont{0}\n0;JMP\n(one{0})\n@SP\nA=M-1\nM=-1\n(cont{0})".format(num))
    num += 1
elif c[0] == "lt":
    print("@SP\nM=M-1\nA=M\nD=M\nA=A-1\nD=D-M\n@one{0}\nD;JGT\n@SP\nA=M-1\nM=0\n@cont{0}\n0;JMP\n(one{0})\n@SP\nA=M-1\nM=-1\n(cont{0})".format(num))
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

