#!/usr/bin/python3
import os, argparse
path = os.path.dirname(os.path.realpath(__file__))

f = path+"/.asm_reference"

def load():
    db = {}
    data = open(f)
    for i in data.readlines():
        key, value = i.split("\t")
        db[key] = value
    return db

def remove(command):
    data = open(f)
    dump = data.readlines()
    data.close()
    for line in dump:
        if line.startswith(command):
            dump.remove(line)
    data = "".join(dump)
    w = open(f, "w")
    w.write(data)
        

def fetch(db, command):
    try:
        print(db[command])
    except KeyError:
        choice = input("Command Not Found! Enter in a description? (y/n) ")
        if choice.lower() == "y":
            store(command)

def store(command):
    if command in load().keys():
        c = input("[!] This commands already exists!\n Would you like to replace "\
        "the description? (y/n) ")
        if c.lower() == "y":
            remove(command)
        else:
            print("[+] Displaying entry for %s" % command)
            fetch(load(), command)
            return 0
    data = open(f, "a")
    description = input("Enter Description: ")
    data.write(command+"\t"+description)
    data.write("\n")
    data.close()
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="Enter command to either read or write")
    parser.add_argument("-w", help="Write new description for command", action=\
                                                                    "store_true")
    args = parser.parse_args()
    data = load()
    if not args.w:
        fetch(data, args.command)
    else:
        store(args.command)
