import ast
from _ast import Call, Attribute, Name
from collections import OrderedDict

from ..constants import *


class FieldVisitor(ast.NodeVisitor):
    """
    A visitor that inspects model fields.
    """

    def __init__(self):
        self.field = []

    def visit_Assign(self, node):
        if not isinstance(node.value, Call):
            return
        attribute_name = node.targets[0].id
        if not self.to_be_skipped(attribute_name):
            self.field.append(attribute_name)

    def to_be_skipped(self, attribute_name):
        for item in SKIP_LIST:
            if attribute_name.__contains__(item):
                return True
        return False


class ModelVisitor(ast.NodeVisitor):
    """
    A visitor that detects django models.
    """

    def __init__(self):
        self.models = OrderedDict()

    def visit_ClassDef(self, node):
        base_class = None
        for base in node.bases:
            if isinstance(base, Attribute):
                base_class = base.attr
            if isinstance(base, Name):
                base_class = base.id

        if base_class in MODEL_BASE_CLASSES:
            visitor = FieldVisitor()
            visitor.visit(node)
            self.models[node.name] = visitor.field
