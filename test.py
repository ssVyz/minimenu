from minimenu import Selection_menu, Checkbox_menu


AVAILABLE_TESTS = ["1. Checkbox simple", "2. Not implemented", "3. Not implemented"]

CHECKBOX_TEXT = ["This is option 1", "This is option 2", "This is option 3"]



def test_checkbox():
    checkbox_menu = Checkbox_menu(CHECKBOX_TEXT, "Test the checkboxes", "Use left and right to change checked status")
    checkbox_menu.add_item("All your test are belong to us")
    checkbox_result = checkbox_menu.present()
    print(checkbox_result)


def main():

    test_menu = Selection_menu(AVAILABLE_TESTS, "Select from available tests", "Choose one", 1)
    test_choice = test_menu.present(True)
    
    print(f"You have chosen option {test_choice+1}, {AVAILABLE_TESTS[test_choice]}")

    if test_choice == 0:
        test_checkbox()




main()