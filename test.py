from minimenu import Selection_menu


AVAILABLE_TESTS = ["1. Not implemented", "2. Not implemented", "3. Not implemented"]


def main():

    test_menu = Selection_menu(AVAILABLE_TESTS, "Select from available tests", "Choose one", 1)
    test_choice = test_menu.present(True)
    
    print(f"You have chosen option {test_choice+1}, {AVAILABLE_TESTS[test_choice]}")



main()