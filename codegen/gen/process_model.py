import collections


class ProcessModelFile:

    def __init__(self):
        self.code_lines = []
        self.model_names = collections.OrderedDict()
        self.flag = False
        self.current_class_name = ''
        self.attribute_line = ''
        # self.skip_list = ['related_name', 'def', 'return', 'to_field', '@property', 'CHOICES', 'FIELD', '(', ')',
        #                   'blank', 'null', 'objects']
        self.skip_list = ['related','def', 'return', 'to_field', '@property', 'CHOICES', 'FIELD', '(', ')',
                          'blank', 'null', 'objects']
        self.class_level_skip_list = ['Meta:', 'Mixin']
        self.process_file_to_list()
        self.process_each_line()
        self.final_cleanup()
        print(self.model_names)

    def process_file_to_list(self):
        f = open('project_code/models.py', 'r')
        for line in f.readlines():
            self.code_lines.append(line)
        # print(self.code_lines)

    def process_each_line(self):
        for line in self.code_lines:
            line = line.strip(' ').strip("\n").strip("\t")
            if line.startswith('from'):  # skip if its imports
                continue
            if line.startswith('class'):  # check if its class.
                self.current_class_name = line.split(' ')[1].split('(')[0]  # find model class name.
                if not self.to_be_skipped(self.current_class_name):
                    self.model_names[self.current_class_name] = []
                else:
                    continue

            elif self.current_class_name:
                self.attribute_line = line.split("=")[0].strip(' ')
                if not self.to_be_skipped(self.attribute_line) and self.attribute_line:
                    self.model_names[self.current_class_name].append(self.attribute_line)
                else:
                    continue

    def final_cleanup(self):
        for key in list(self.model_names.keys()):
            if self.final_cleanup_skip(key):
                del self.model_names[key]

    def to_be_skipped(self, skip_line):
        for item in self.skip_list:
            if skip_line.__contains__(item) or skip_line.isupper() or item.__contains__(skip_line):
                return True
        return False

    def final_cleanup_skip(self, skip_line):
        for item in self.class_level_skip_list:
            if skip_line.__contains__(item) or skip_line.isupper() or item.__contains__(skip_line):
                return True
        return False
