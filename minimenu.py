"""
CHANGELOG:
260519: Started, keypresses via msvcrt
260527: Working on input lists


"""

##########################################
### Minimenu: tiny CLI menu for python ###
##########################################



import sys

try:
    import msvcrt
    sys_code = "win"
except:
    raise Exception("No method found for keyboard support")






class Menu:

    def __init__(self, input_list=None):
        if input_list is not None:
            self.input_list = input_list
        else:
            self.input_list = []

    def add_item(self, new_item: str):
        if isinstance(new_item, str):
            self.input_list.append(new_item)
        else:
            raise Exception("Tried adding item that is not a string")
        
    def load_list(self, new_list: list):
        if isinstance(new_list, list):
            self.input_list = new_list
        else:
            raise Exception("Tried loading something other than a list")
        
    def dump_contents(self):
        print(f"Type of list: {type(self.input_list)}")
        print(self.input_list)
        

    










### Keyboard operrations ###

def empty_key_buffer():
    if sys_code == "win":
        while msvcrt.kbhit():
            msvcrt.getch()

def get_next_key() -> str:
    if sys_code == "win":
        empty_key_buffer()
        current_key = msvcrt.getch()
        if current_key == b'\xe0':
            return msvcrt.getch()
        return current_key
    
def decode_key(key):
    if sys_code == "win":
        if key == b'H':
            return "up"
        elif key == b'P':
            return "down"
        elif key == b'K':
            return "left"
        elif key == b'M':
            return "right"
        elif key == b'\r':
            return "enter"
        else:
            return None






### Running tests. Not run when called from the outside ###

def main():
    print("Running the test suite:")
    print(f"Detected system: {sys.platform}")
    
    key = get_next_key()
    print(key)
    print(decode_key(key))

    print("--Test 1--: load multiple strings directly into Menu object")
    test_menu = Menu()
    test_menu.add_item("This is item1")
    test_menu.add_item("This is item2")
    test_menu.dump_contents()

    print("--Test 2--: Directly load an input list")
    test_menu = Menu(["Item1", "Item2"])
    test_menu.dump_contents()

if __name__ == "__main__":
    main()





