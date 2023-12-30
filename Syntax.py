#!/usr/bin/env python
# coding: utf-8

# In[1]:


from lark import Lark, tree, Transformer

# Define the grammar
grammar = """
start: expression
expression: atom | expression "+" expression
atom: NUMBER | "(" expression ")"
%import common.NUMBER
%import common.WS
%ignore WS
"""

# Create the parser
parser = Lark(grammar, start='start', parser='lalr')


# Define a transformer to build the syntax tree
class TreeBuilder(Transformer):
    def expression(self, items):
        if len(items) == 1:
            return items[0]
        else:
            return tree.Tree("expression", items)

    def atom(self, items):
        return items[0]

    def NUMBER(self, token):
        return tree.Tree("number", [tree.Tree("value", [int(token)])])


# Function to check syntax and display the syntax tree
def check_syntax(input_str):
    try:
        tree = parser.parse(input_str)
        print(f"Syntax is correct. Syntax Tree:\n{tree.pretty()}")
        return True
    except Exception as e:
        print(f"Syntax error: {e}")
        return False


# Example usage
input_string = "3 + (4 + 5)"
check_syntax(input_string)


# In[ ]:




