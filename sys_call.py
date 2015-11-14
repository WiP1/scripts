import sys, os, argparse

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
    parser = argparse.ArgumentParser()
    parser.add_argument("eax", help="Enter the contents of EAX here, as an int", type=int)
    parser.add_argument("-a", help="Enter the word size of CPU (32/64)")
    parser.add_argument("-m", help="Enter m to view manual entry on function", action='store_true')
    args = parser.parse_args()
    table = main(args.a) if args.a else main()
    call = display(table, args.eax)
    if args.m:
        manual(call)
