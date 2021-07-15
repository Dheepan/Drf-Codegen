from string import Template


# TBD: post and delete
class generate_viewspy_code:

    def __init__(self,model_dict):
        self.model_dict=model_dict
        self.imports=['from rest_framework import generics',
                      '\nfrom rest_framework.permissions import IsAuthenticated',
                      '\nfrom rest_framework.response import Response'
                      '\nfrom .models import']
        self.body=''
        self.generate_imports_for_views_file()
        self.generate_code_for_view()
        self.write_views_code_file()

    def generate_code_for_view(self):
        retrieve_class_str=Template('''\nclass $user_retrieve_api_view(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = $model_name_serializer

    def get_queryset(self):
        return $model_name.objects.all()
''')
        list_class_str = Template('''\nclass $user_list_api_view(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = $model_name_serializer

    def get_queryset(self):
        return $model_name.objects.all()
''')
        update_class_str = Template('''\nclass $user_update_api_view(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = $model_name_serializer

    def put(self, request, *args, **kwargs):
        serializer_data = request.data
        serializer = $model_name_serializer(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
''')

        for key in self.model_dict.keys():
            #rerieve class substitution
            result=retrieve_class_str.substitute(model_name_serializer=key+'Serializer',model_name=key,user_retrieve_api_view=key+"RetrieveAPIView")
            self.body+='\n#'+key+' retrieve API view'
            self.body+=result
            #list class substitution
            result = list_class_str.substitute(model_name_serializer=key + 'Serializer', model_name=key,
                                          user_list_api_view=key + "ListAPIView")
            self.body += '\n#' + key + ' list API view'
            self.body += result
            #update class substitution
            result = update_class_str.substitute(model_name_serializer=key + 'Serializer', model_name=key,
                                          user_update_api_view=key + "UpdateAPIView")
            self.body += '\n#' + key + ' update API view'
            self.body += result

    def generate_imports_for_views_file(self):
        import_str=''
        for key,value in self.model_dict.items():
            import_str+=" "+key+","
        self.imports[len(self.imports)-1]+=import_str.rstrip(", % ") # only happening on terminal


    def write_views_code_file(self):
        f = open('project_code/views.py', 'w+')
        for line in self.imports:
            f.write(line)
        f.write("\n\n")
        f.write(self.body)
        f.close()