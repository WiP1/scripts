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
    

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("USAGE: ")
        sys.exit()
    data = main() if len(sys.argv) == 2 else main(sys.argv[2])
    eax = sys.argv[-1]
    display(data, eax)
