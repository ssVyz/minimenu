"""
CHANGELOG:
260519: Started, keypresses via msvcrt
260527: Working on input lists
260528: Simple build frame and show frame methods
260529: presenting the select menu
260530: result list implemented


"""

##########################################
### Minimenu: tiny CLI menu for python ###
##########################################



import sys
import os

try:
    import msvcrt
    sys_code = "win"
except:
    raise Exception("No method found for keyboard support")






### The wrapper class that contains shared methods

class Menu:

    def __init__(self, input_list: list = None, header = None, footer = None, padding: int = 0):
        self.padding = padding
        self.display_frame = []
        self.pointer = 0
        self.limit = 0
        self.header = header
        self.footer = footer
        self.result = []

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
        print(self.header)
        print(self.footer)
    
    def build_frame(self):
        pass
        
    def show_frame(self):
        pass

    def move_pointer(self, key):
        pass

    def build_result(self):
        pass


    def present(self):
        confirmed_select = False
        self.limit = len(self.input_list)-1

        while confirmed_select == False:

            self.build_frame()
            self.show_frame()
            print(f"Current pointer: {self.pointer}, current limit: {self.limit}")
            key = decode_key(get_next_key())
            if key == "enter":
                confirmed_select = True
            else:
                if key is not None:
                    self.move_pointer(key)
        
        self.build_result()
        return self.result







### Subclass for the selection menu
    
class Selection_menu(Menu):

    def __init__(self, input_list: list = None, header = None, footer = None, padding: int = 0):
        super().__init__(input_list, header, footer, padding)

    def dump_subcontents(self):
        print(f"Type of list in selection menu: {type(self.input_list)}")
        print(self.input_list)
        print(self.header)
        print(self.footer)

    def build_frame(self):
        self.display_frame = []
        size_of_list = len(self.input_list)
        for i in range(0, size_of_list):
            a = ""
            if i == self.pointer:
                a = " --> "
            else:
                a = "     "
            b = self.input_list[i]
            self.display_frame.append((a, b))
        
    def show_frame(self):
        os.system("cls")
        print("")
        print(self.header)
        print("")
        for i in range(0, len(self.display_frame)):
            print(f"{self.display_frame[i][0]} {self.display_frame[i][1]}")
        print("")
        print(self.footer)

    def move_pointer(self, key):
        upper_bounds = self.limit
        if key == "up":
            self.pointer -= 1 if self.pointer > 0 else self.pointer
        if key == "left":
            self.pointer -= 1 if self.pointer > 0 else self.pointer
        if key == "down":
            self.pointer += 1
        if key == "right":
            self.pointer += 1
        if self.pointer > upper_bounds:
            self.pointer = upper_bounds

    def build_result(self):
        result_fields = len(self.input_list)
        result_list = []
        for i in range(result_fields):
            if i == self.pointer:
                result_list.append(1)
            else:
                result_list.append(0)
        self.result = result_list
        
        

            











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






### Running tests. Not run if called from the outside ###

def main():


    print("Running the test suite:")
    print(f"Detected system: {sys.platform}")
    
    '''
    key = get_next_key()
    print(key)
    print(decode_key(key))
    '''

    print("--Test 1--: load multiple strings directly into Menu object")
    test_menu = Menu()
    test_menu.add_item("This is item1")
    test_menu.add_item("This is item2")
    test_menu.dump_contents()
    input("continue")

    print("--Test 2--: Directly load an input list")
    test_menu = Menu(["Item1", "Item2"])
    test_menu.dump_contents()
    input("continue")

    print("--Test 3--: Testing selection menu")
    test_menu = Selection_menu(["Bad idea", "Use the toilette", "Run away screaming", "Take a bath"], "Breakfast is only the beginning", "Get to the bottom of this")
    test_menu.dump_subcontents()
    input("continue")
    test3_result = test_menu.present()
    print(test3_result)
    print(test_menu.result)




if __name__ == "__main__":
    main()





