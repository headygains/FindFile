__author__ = 'headygains'
from itertools import chain
import shlex,os



filelist = []
# these are the Paths that the script will search
paths = ["C:\\","F:\\","K:\\","X:\\","I:\\","U:\\"]
# input you're own default file path here to have the files written to a folder of your choice.
defaultFilePath = "C:\\"
cmd = ""


def listDirByExt(directory,param):
    for root, dirs, files in chain.from_iterable(os.walk(directory)for directory in paths):
        for file in files:
            if file.endswith(param):
                filelist.append(os.path.join(root, file))


def listDirByName(directory,searchParam,):
    count = 0
    for root, dirs, files in chain.from_iterable(os.walk(directory)for directory in paths):
        for file in files:
            _tmp = file.split('/')
            if any(searchParam in s for s in _tmp):
                filelist.append(os.path.join(root, file))
                count += 1
            else:
                proc = 'Processing: '+str(count)
                print(proc, end='\n')


def write(info,filepath):
    if filepath == "":
        filepath = defaultFilePath+"save.txt"
    target = open(defaultFilePath+filepath, 'w')
    for name in info:
        target.write(name)
        target.write("\n")
    target.close()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def genhelp():
    print("General Trunch Help", end='\n')
    print("? - List General Commands", end='\n')
    print("?[command] - List Specific Command Information", end='\n')
    print("search [param] [arg] [outputarg.txt]", end='\n')


def searchHelp():
    print("search [ext/name] [extension param/name param] [outputfile]", end='\n')
    print("ext - denotes search by file extension", end='\n')
    print("name - denotes search by file extension", end='\n')
    print("extension param - denotes which file extension to search for e.g. .accdb", end='\n')
    print("name param - denotes which filename to search for", end='\n')
    print("outputfile - denotes a file path e.g. C:\\Users\\Dumbass", end='\n')


def killHelp():
    print("kill without arguments will end the program", end='\n')


def main():
    while True:
        cmd, *args = shlex.split(input('#!'))

        if cmd == 'search':
            arg1, arg2, arg3 = args
            if arg1 == 'ext':
                clear()
                listDirByExt(paths,arg2)
                write(filelist,arg3)
            elif arg1 == 'name':
                clear()
                listDirByName(paths,arg2)
                write(filelist,arg3)
            else:
                clear()
                break
        elif cmd == 'kill':
            clear()
            break
        elif cmd == '?kill':
            clear()
            killHelp()
        elif cmd == '?':
            clear()
            genhelp()
        elif cmd == '?search':
            clear()
            searchHelp()
        else:
            clear()
            print("Uknown Command Use ? For Help.")

if __name__ == '__main__':
    clear()
    main()

