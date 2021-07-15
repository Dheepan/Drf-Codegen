from string import Template

class generate_adminpy_code:

    def __init__(self,model_dict):
        self.model_dict=model_dict
        self.imports=['from django.contrib import admin','\nfrom .models import']
        self.body=''
        self.generate_imports_for_admin_file()
        self.generate_code_for_admin_file()
        self.write_admin_code_file()

    #generate code for the admin body file
    def generate_code_for_admin_file(self):

        class_str=Template('''\nclass $class_nameAdmin(admin.ModelAdmin):
    list_display = [$field_list]


admin.site.register($class_name, $class_nameAdmin)\n\n''')
        for key,value in self.model_dict.items():
            field_list=''
            for field in value:
                field_list+='\n        \''+field+'\','
            field_list=field_list.rstrip(", ")+"\n        "
            result=class_str.substitute(class_nameAdmin=key+'Admin', field_list=field_list, class_name=key)
            self.body += '\n#' + key + ' Admin'
            self.body+=result

    # generate code for imports
    def generate_imports_for_admin_file(self):
        import_str=''
        for key,value in self.model_dict.items():
            import_str+=" "+key+","
        self.imports[1]+=import_str.rstrip(", % ") # only happening on terminal

    # write the code to admin.py file
    def write_admin_code_file(self):
        f = open('project_code/admin.py', 'w+')
        for line in self.imports:
            f.write(line)
        f.write("\n\n")
        f.write(self.body)
        f.close()

