# Minimenu & file select

### Concept

This is a tiny, drop in python "library" that will provide you with a CLI selection menu and a CLI file browser.

###How to use###

**How to integrate it into a project:**

- Copy/paste the "minimenu.py" file into the project.
- In the relevant file: *from minimenu import Selection_menu, Checkbox_menu, select_file

--> Selection_menu and Checkbox_menu are classes. You may only need one of them depending on the purpose.
--> select_file is a function that uses the above classes. If you only need the file browser, you only need to import "select_file".

**How to use Selection_menu or Checkbox_menu:**

- define a class instance of either Selection_menu or Checkbox_menu with the following params:
  - list of strings which you want to select from (input_list)
  - Headline (string)
  - footnote (string)
- To present the menu to a user, call the "present" method and catch the result in a variable.
  - The default result will be a list of integers, whereby the unselected indecies are 0 and the selected index is 1. (especially relevant for the Checkbox as multiples can be checked.)
  - You can pass the present method "True" (bool) to receive a simplified result: an integer that represents where the pointer was when the user hit enter. This integer can be used as an index to retrieve the item they selected.

**How to use select_file:**

"select_file" is a function that you call either without parameter (defaults to pythons current working directory) or a custom directory as string. The function uses pathlib in conjunction with Selection_menu to be able to browse through the file system.

Functions:
- select a file and it will return the file path as string.
- press the s-key to return the current directory (i.e. user selected a directory instead of a file)
- press the q-key to quit the selection. This will return "None"