
class Vmtranslator:

    MEMORY_DIC = {"local": "LCL", "argument": "ARG", "this": "THIS", "that": "THAT", "0": "THIS", "1": "THAT"}
    label_index = 0

    def __init__(self, path):
        self.source = path
        self.target = path.replace(".vm", ".asm")
        #self.target = path + ".asm"
        self.file_name = self.get_file_name(path)



    def parse_file(self):
        asmfile = open(self.target, "a+")
        with open(self.source, "r") as vmfile:
            for line in vmfile:
                info = self.get_info(line)
                if info != []:
                    asmfile.write(self.comment(info) + "\n")
                    asmfile.write(self.translate(info)+ "\n")

        asmfile.close()


    def get_file_name(self, path):
        temp = path.split("\\")
        return temp[len(temp) - 1].split(".")[0]

    def get_info(self, vm_instruction):
        temp = vm_instruction.split("//")[0].strip("\n").split(" ")
        info = [item for item in temp if item != ""]
        return info

        
    def comment(self,info):
        return "// " + " ".join(info)
    
    def translate(self, info):
        command = ""
        if info[0] == "push":
            if info[1] == "constant":
                command = ("@{}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1".format(info[2]))
            elif info[1] == "local" or info[1] == "argument" or info[1] == "this" or info[1] == "that":
                command = ("@{}\nD=A\n@{}\nA=M\nM=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1".format(info[2], self.MEMORY_DIC[info[1]]))
            elif info[1] == "static":
                command = ("@{}.{}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1".format(self.file_name, info[2]))
            elif info[1] == "temp":
                command = ("@{}\nD=A\n@5\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1".format(info[2]))
            elif info[1] == "pointer":
                command = ("@{}\nA=M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1".format(self.MEMORY_DIC[info[2]]))

        if info[0] == "pop":
            if info[1] == "local" or info[1] == "argument" or info[1] == "this" or info[1] == "that":
                command = ("@{}\nD=A\n@{}\nD=D+M\n@address\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@address\nA=M\nM=D".format(info[2],self.MEMORY_DIC[info[1]]))
            elif [1] == "static":
                command = ("@SP\nM=M-1\nA=M\nD=M\n@{}.{}\nM=D".format(self.file_name, info[2]))
            elif info[1] == "temp":
                command = ("@{}\nD=A\n@5\nD=D+A\n@address\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@address\nA=M\nM=D".format(info[2]))
            elif info[1] == "pointer":
                command = ("@SP\nM=M-1\nA=M\D=M@{}\nA=M\nM=D".format(self.MEMORY_DIC[info[2]]))

        if info[0] == "add":
            command = ("@SP\nM=M-1\nA=M\nD=M\nA=A-1\nM=M+D")
        elif info[0] == "sub":
            command = ("@SP\nM=M-1\nA=M\nD=M\nA=A-1\nM=M-D")
        elif info[0] == "neg":
            command = ("@SP\nA=M-1\nM=-M")
        elif info[0] == "eq":
            command = ("@SP\nM=M-1\nA=M\nD=M\nA=A-1\nD=D-M\n@one{0}\nD;JEQ\n@SP\nA=M-1\nM=0\n@cont{0}\n0;JMP\n(one{0})\n@SP\nA=M-1\nM=-1\n(cont{0})".format(self.label_index))
            self.label_index += 1
        elif info[0] == "gt":
            command = ("@SP\nM=M-1\nA=M\nD=M\nA=A-1\nD=D-M\n@one{0}\nD;JLT\n@SP\nA=M-1\nM=0\n@cont{0}\n0;JMP\n(one{0})\n@SP\nA=M-1\nM=-1\n(cont{0})".format(self.label_index))
            self.label_index += 1
        elif info[0] == "lt":
            command = ("@SP\nM=M-1\nA=M\nD=M\nA=A-1\nD=D-M\n@one{0}\nD;JGT\n@SP\nA=M-1\nM=0\n@cont{0}\n0;JMP\n(one{0})\n@SP\nA=M-1\nM=-1\n(cont{0})".format(self.label_index))
            self.label_index += 1
        elif info[0] == "and":
            command = ("@SP\nM=M-1\nA=M\nD=M\nA=A-1\nM=D&M")
        elif info[0] == "and":
            command = ("@SP\nM=M-1\nA=M\nD=M\nA=A-1\nM=D|M")
        elif info[0] == "not":
            command = ("@SP\nA=M-1\nM=!M")

        return command


def main():
    example = Vmtranslator(r"C:\Users\Avraham\Desktop\nand2tetris\projects\07\MemoryAccess\BasicTest\BasicTest.vm")
    example.parse_file()

if __name__ == '__main__':
    main() 

