"""
Changelog:
    260607: initial setup, basic concept working



"""

from pathlib import Path
from minimenu import Selection_menu


class Work_folder:

    def __init__(self):

        self.current_dir = Path.cwd()
        


    def select_folder(self):

        contents_list = []
        name_list = []
        for item in self.current_dir.iterdir():
            contents_list.append(item)
            name_list.append(item.name)

        contents_list.append(self.current_dir.parent)
        name_list.append("cd ..")
                    
        mim = Selection_menu(name_list, "Select a folder", "folders are for the weak")
        result = mim.present(True)
        
        selected_item = contents_list[result]

        print(f"You selected {selected_item}")
        
        return selected_item
        


    def go_to_parent(self):

        self.current_dir = self.current_dir.parent

        self.select_folder()





def select_file():

    wf = Work_folder()
    result_file_path = ""
    file_selected = False

    while file_selected != True:

        current_item = wf.select_folder()
        if current_item.is_dir() == True:
            wf.current_dir = current_item
        else:
            return str(current_item)




def main():
    
    
    #test = Work_folder()
    #test.select_folder()
    #print("Testing go to parent")
    #test.go_to_parent()
    
    result = select_file()
    print(result)


if __name__ == "__main__":

    main()

