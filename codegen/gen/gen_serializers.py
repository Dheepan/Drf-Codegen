from string import Template

class generate_serializerpy_code:

    def __init__(self,model_dict):
        self.model_dict=model_dict
        self.imports=['from rest_framework import serializers','\nfrom .models import ']
        self.body='\n\n'
        self.generate_imports_for_serializers_file()
        self.generate_code_for_serializers_file()
        self.write_serializers_code_file()

    def generate_code_for_serializers_file(self):

        class_str=Template('''\nclass $model_name_serializer(serializers.ModelSerializer):
    class Meta:
        model = $model_name
        fields = (
$field_list        )\n\n''')
        for key,value in self.model_dict.items():
            field_list=''
            for field in value:
                field_list+='        \''+field+'\',\n'
            result=class_str.substitute(model_name_serializer=key+'Serializer', field_list=field_list, model_name=key)
            self.body += '\n#' + key + ' Serializer'
            self.body+=result

    def generate_imports_for_serializers_file(self):
        import_str=''
        for key,value in self.model_dict.items():
            import_str+=" "+key+","
        self.imports[1]+=import_str.rstrip(", % ") # only happening on terminal
        # for code in self.imports:
        #     print(code,end='')

    def write_serializers_code_file(self):
        f = open('project_code/serializers.py', 'w+')
        for line in self.imports:
            f.write(line)
        f.write(self.body)
        #print(self.body)
        f.close()

