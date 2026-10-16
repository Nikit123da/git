import os, subprocess, sys
from colorama import Fore
import hashlib

def git_init()->None:
        #create a .git folder with it's subfolders and files

    files = os.listdir('.')
    matches = [f for f in  files if '.bad_git' in f]

    print("len, ", matches)

    if matches:
        print(Fore.RED + "The directory already has a .git file")
    try:
        os.mkdir(".bad_git")
        with open(".bad_git/config" , "w") as f:
            pass
        with open(".bad_git/HEAD", "w") as f:
            pass
        os.mkdir(".bad_git/objects")
        os.mkdir(".bad_git/hooks")
        os.mkdir(".bad_git/objects/pack")
        os.mkdir(".bad_git/objects/info")
        os.mkdir(".bad_git/refs")
        print(Fore.GREEN + "bad git has been initializd ")
    except FileExistsError as e:
        print(e)

def hash_obj(obj)->str:
    #hashes any object into a string of a specified len
    return hashlib.sha1(obj).hexdigest()

def create_object_file(obj):
    #Create a file with the first two letter of the hash if not created yet, and insert the other remaining hash into it. 
    #!MIGHT NEED TO MAKE THE INTERNAL HASH AS AN OBJECT.
    try:
        os.mkdir(f"./bad_git/objects/{obj[0:2]}")
        #TODO:put the boj inside there.
        
    except FileExistsError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    pass

def main()->None:
    args_num = len(sys.argv)
    print(args_num)
    match args_num:
        case 2:
            print(Fore.RED + "Incompleat command ")
        case 3: 
            if sys.argv[1] == "bad_git" and sys.argv[2] == "init":
                git_init()
        case 4: 
            print(Fore.RED + "Too many arguments ")
        case _:
            print(Fore.RED +  "Not recognized")


if __name__ == "__main__":
    main()
