import sys, os

path = os.path.dirname(os.path.realpath(__file__))

def main(arg="32"):
    name = path+"/.data"+arg
    f = open(name)
    syscalls = {}
    title = f.readline().split("\t") 
    for i in f.readlines():
        data = i.split("\t")
        syscalls[data[0]] = []
        for n in range(1, len(data)):
            syscalls[data[0]].append((title[n].strip(), data[n])) 
    f.close()
    return syscalls

def display(syscall, call):
    call = str(call)
    title = [w[0] for w in syscall[call]]
    data = [w[1] for w in syscall[call]]
    for i in range(len(data)):
        print(title[i], "\t\t", data[i])
    return data[0]
    
def manual(func):
    prompt = input("Display manual entry (y/n)? ")
    if prompt == "y":
        call = "man " + func.strip("sys_")
        os.system(call)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("USAGE: python3 sys_call.py [int(eax)] [64 or 32] [-m]")
        sys.exit()
    eax = sys.argv[1]
    man = "m" in sys.argv
    arch = sys.argv[2] if not man and len(sys.argv) > 2 else "32"
    data = main(arch)
    name = display(data, eax)
    if man:
        manual(name)
