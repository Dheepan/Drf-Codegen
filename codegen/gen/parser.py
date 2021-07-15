import ast
from .visitors import  ModelVisitor

def load(file_name):
    file=open(file_name, 'r')
    node = ast.parse(file.read())
    visitor = ModelVisitor()
    visitor.visit(node)
    return visitor.models
