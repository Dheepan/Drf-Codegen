from string import Template
from codegen.gen.gen_admin import  generate_adminpy_code
from codegen.gen.gen_view import generate_viewspy_code
from codegen.gen.gen_serializers import generate_serializerpy_code
from codegen.gen.parser import load
from codegen.constants import *
import os
from collections import OrderedDict

class CodeGenDriver:

    def __init__(self):
        self.model_dict = load(MODEL_FILE_LOCATION)

    def run(self):
        go_ahead=self.display_menu()
        if go_ahead:
            generate_adminpy_code(self.model_dict)
            generate_serializerpy_code(self.model_dict)
            generate_viewspy_code(self.model_dict)
            print("Code generation completed please check the project_code folder..")
        else:
            print("Skipping code gen..")
            os._exit(0)

    def display_menu(self):
        model_dict=dict(self.model_dict)
        model_index_number=1
        # clear the screen
        os.system('clear')
        # print the menu
        for key in model_dict.keys():
            print(str(model_index_number)+".",key)
            model_index_number+=1
        print("0. For all models")
        # get the choices
        choice_input = input("\nChoose the Models separated by spaces:")
        print("\n")
        choices_list= list(filter(None,choice_input.split(" ")))
        keys_list = list(self.model_dict.items())
        selected_keys = []
        if choices_list==['0']:
            for i in range(1,len(self.model_dict)+1):
                model_name = keys_list[i - 1][0]
                print(i, ".", model_name)
                selected_keys.append(model_name)
        else:
            for choice in choices_list:
                    model_name=keys_list[int(choice)-1][0]
                    print(choice,".",model_name)
                    selected_keys.append(model_name)
        # confirm the choices
        confirm = input("\nConfirm selected models [y/n]:")
        print("\n")
        # confirm and verify the fields
        if confirm.lower() == "y":
            #return self.proceed_further(selected_keys)
            model_dict = OrderedDict()
            for selected_key in selected_keys:
                if selected_key in self.model_dict:
                    model_dict[selected_key] = self.model_dict[selected_key]
                    print(selected_key, ":")
                    for field_name in model_dict[selected_key]:
                        print("    ", field_name)
            self.model_dict = model_dict

            # get model fields verification confirmation
            confirm = input("\nAll model fields looks good? [y/n]:")
            if confirm.lower() == "y":
                return True
            else:
                return False

        else:
            return False

if __name__=="__main__":
    c = CodeGenDriver()
    c.run()