"""
CHANGELOG:
260519: Started, keypresses via msvcrt


"""

##########################################
### Minimenu: tiny CLI menu for python ###
##########################################





try:
    import msvcrt
    sys_code = "win"
except:
    raise Exception("No method to receive key presses")











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
        else:
            return None






### Running tests. Not run when called from the outside ###

def main():
    print("Running the test suite:")
    key = get_next_key()
    print(key)
    print(decode_key(key))


if __name__ == "__main__":
    main()





