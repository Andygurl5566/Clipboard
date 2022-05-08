# the following modules come with Python
import sys
import clipboard
import json 


SAVED_DATA = "clipboard.json"

# creates json file of key value pairs 
def save_data(filepath, data):
    with open(filepath, "w" ) as f:
        json.dump(data, f)
    print("You data has been saved!")

# reads file and gives the python dictionary representation of this file, if nothing exists a new dictionary is created
def load_data(filepath):
 try:
    with open(filepath, "r") as f:
        data = json.load(f)
        return data
 except:
     return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)

    elif command == "load":
        print("load")
    elif command == "list":
        print("list")
    else:
        print("Sorry, I don't recognize that command. Womp womp")



