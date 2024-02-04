import nltk
import re

print("-----------------------------")
# 1. LEXICAL ANALYZER
print('1. LEXICAL ANALYZER')
# Opening the file
file = open("input.py")

# Classifying every token according to its type, and linking them to their types using keys
operator = {'+': '- operator',
            '-': '- operator',
            '=': '- operator',
            '<': '- operator',
            '>': '- operator'}

operator_key = operator.keys()

punctuator = {';': '- punctuator',
              '(': '- punctuator',
              ')': '- punctuator',
              '{': '- punctuator',
              '}': '- punctuator'}

punctuator_key = punctuator.keys()

constant = {'1': '- constant',
            '2': '- constant',
            '3': '- constant',
            '4': '- constant',
            '5': '- constant',
            '6': '- constant',
            '7': '- constant',
            '8': '- constant',
            '9': '- constant',
            '0': '- constant'}

constant_key = constant.keys()

identifier = {'x': '- identifier',
              'y': '- identifier'}

identifier_key = identifier.keys()

reserved_word = {'while': '- reserved word',
                 'for': '- reserved word',
                 'if': '- reserved word',
                 'int': '- reserved word',
                 'float': '- reserved word',
                 'auto': '- reserved word'}

reserved_word_key = reserved_word.keys()

# Reading the file
fileread = file.read()
fileread_processed = re.split(' |\n', fileread)

# Counting the number of lines in the code
count = 0

# Splitting the input file back for Lexical Analysis
program = fileread.split("\n")
# Printing the input
print("-----------------------------")
print("Input Code: ")
print("-----------------------------")
for line in program:
    print(line)
print("-----------------------------")
print("Processing each line of code: ")
print("-----------------------------")
# Loop on file to count number of lines and identify different tokens
for line in program:
    count = count + 1
    tokens = line.split(' ')
    print(tokens)
    for token in tokens:
        if token in operator_key:
            print(token, operator[token])
        if token in punctuator_key:
            print(token, punctuator[token])
        if token in constant_key:
            print(token, constant[token])
        if token in identifier_key:
            print(token, identifier[token])
        if token in reserved_word_key:
            print(token, reserved_word[token])
    dataFlag = False
    print('')
# Printing the number of lines
print("Total number of lines = ", count)
print("-----------------------------")
print("2. CONTEXT-FREE GRAMMAR")
# 2. CONTEXT-FREE GRAMMAR
# Coming up with a CFG for all statements
grammar = nltk.CFG.fromstring("""

S -> identifier op E X | X
E -> E op num | E op E | num | identifier | 
X -> 'while' punc cond punc punc E punc | punc
cond -> identifier op identifier 
op -> '+' | '-' | '=' | '<' | '>'  
num -> '0' punc E | '1' punc E | '2' punc E | '3' punc E | '4' punc E | '5' punc E | '6' punc E | '7' punc E | '8' punc E | '9' punc E
punc -> ';' | ':' | '(' | ')' | '{' | '}' | 
identifier -> 'x' | 'y' | 

""")

# CFG Declarations
print("-----------------------------")
print("CFG: ", grammar)
print("-----------------------------")

# Start Symbol -> S
grammar.start()

# Accepted CFG Rules
#print(grammar.productions())

print("-----------------------------")
# 3. SYNTAX ANALYZER
print('3. SYNTAX ANALYZER')
# Processing the Parse Tree

print("-----------------------------")
print("Parse Tree: ")
print("-----------------------------")
exceptionFlag = 0
try:
    parser = nltk.ChartParser(grammar) # Check with grammar
    trees = list(parser.parse(fileread_processed)) # Input for building the tree from lexical analysis.
    trees[0].pretty_print()
except BaseException as exception:
    print("Oops!", exception, ", unable to print tree.")
    print("Review input code and try again!")
    print()
dataFlag = False

print("-----------------------------")

try:
    postfix_expressions = []
    # Obtaining the output expressions from Parse Tree
    expressions = trees[0].leaves()  # Output Expressions
    print("-----------------------------")
    print('Output of Parse tree: ', expressions)
    print("-----------------------------")
    expressions = ' '.join(expressions)  # Concatenated
    expressions = expressions.split(';', 2)  # Specifying separate experessions, as a string on their own.
    for i in range(3):
        expressions[i] = expressions[i].strip()  # Removing Whitespaces

    # While Conditions and Instructions
    whileInst = expressions[-1]
    whileInst = whileInst.replace('while ( ', '').replace('if ', '').replace(' ) ', '').replace(' }', '') # Removing the brackets
    whileInst = re.split('{ | ;', whileInst) # List of while condition and while statements + space
    del whileInst[-1]

    for i in range(3):
        whileInst[i] = whileInst[i].strip()
    expression_loop = expressions[-1]
    del expressions[-1]
    if 'while' in expression_loop:
        expression_loop = 'while'
    print('Output of SYNTAX ANALYZER: ')
    print('Expressions: ', expressions)
    print('While Loop Expressions: ', whileInst)
    print("-----------------------------")

except BaseException as exception:
    exceptionFlag = 1
    print("Oops!", exception, ", unable to process code.")
    print("Review input code and try again!")
    print()


# 4. SEMANTIC ANALYZER
if exceptionFlag != 1:
    print('4. SEMANTIC ANALYZER')
    # Priority Array for Infix to Postfix
    Priority = {'=': 1, '+': 2, '-': 2, '*': 3, '/': 3, '^': 4}


    def infixToPostfix(expression):  # Convert Infix Expression from Parse Tree to Postfix Expression for Syntax Tree
        stack = []
        output = ''
        for character in expression:
            if character not in operator_key:  # if an operand append in postfix expression
                output += character
            else:
                while stack and Priority[character] <= Priority[stack[-1]]:
                    output += stack.pop()
                stack.append(character)
        while stack:
            output += stack.pop()
        return output.strip()


    print("-----------------------------")
    print("Converting Infix Expressions to Postfix: ")
    print("-----------------------------")
    for i in range(2):
        exp = expressions[i].split(' ')
        print(expressions[i])
        postfix_expression = infixToPostfix(exp)
        print("-----------------------------")
        print("Infix: ", exp)
        print("Postfix: ", postfix_expression)
        print("-----------------------------")
        postfix_expressions.append(postfix_expression)

    for x in range(3):
        exp = whileInst[x].split(' ')
        print(whileInst[x])
        postfix_expression = infixToPostfix(exp)
        print("-----------------------------")
        print("Infix: ", exp)
        print("Postfix: ", postfix_expression)
        print("-----------------------------")
        postfix_expressions.append(postfix_expression)
    print("-----------------------------")
    print('Postfix Expressions: ', postfix_expressions)
    print("-----------------------------")


    class stack:
        # Stack Initialization
        def __init__(self):
            self.arr = []

        # Push
        def push(self, data):
            self.arr.append(data)

        # Pop
        def pop(self):
            try:
                return self.arr.pop(-1)
            except:
                pass

        # Top
        def top(self):
            try:
                return self.arr[-1]
            except:
                pass

        # Length
        def size(self):
            return len(self.arr)


    class whileNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.middle = None
            self.right = None


    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None


    # expression tree class
    class expTree:
        def __init__(self, postfix_exp):
            self.exp = postfix_exp
            self.root = None
            self.createTree(self.exp)

        def isOperator(self, char):
            if char in operator_key:
                return True
            return False

        def isReserved(self, char):
            if char in reserved_word_key:
                return True
            return False

        def createTree(self, exp, space=0):
            operatorspace = 0
            s = stack()
            opcount = 0
            self.root = Node(exp[-1])
            s.push(self.root)  # push operator in stack
            print(self.root.data)
            for i in "".join(reversed(exp[:-1])):  # traverse over rest of the expression
                for m in i:
                    if m in identifier_key:
                        opcount += 1
                currentNode = s.top()
                if not currentNode.right:  # if current node's right is null
                    currentNode.right = Node(i)
                    space += 10
                    if self.isOperator(i):
                        s.push(Node(i))
                        operatorspace = space
                    for l in range(space):
                        print(end=" ")
                    print(Node(i).data)
                else:  # if left node of current node is NULL
                    currentNode.left = Node(i)
                    # if no child node of current node is NULL
                    if opcount == 1:
                        for l in range(space):
                            print(end=" ")
                        print(Node(i).data)
                    else:
                        if operatorspace != 0:
                            space = operatorspace
                        for l in range(space):
                            print(end=" ")
                        print(Node(i).data)
                    s.pop()
                    if self.isOperator(i):
                        s.push(Node(i))

        def inorder(self, head):
            # inorder traversal of expression tree
            # inorder traversal = > left, root, right
            if head.left:
                self.inorder(head.left)
            print(head.data, end=" ")
            if head.right:
                self.inorder(head.right)

        def infixExp(self):  # Traversing the tree (INFIX)
            print('')
            print('Infix Expression: ', )
            self.inorder(self.root)
            print()


    if __name__ == "__main__":
        # Output of SEMANTIC ANALYZER
        print('Output of SEMANTIC ANALYZER: ')
        print("-----------------------------")
        w = whileNode('While')
        print(w.data)
        w.left = expTree(postfix_expressions[2])
        print(w.left.infixExp())
        print("-----------------------------")
        w.middle = expTree(postfix_expressions[3])
        print(w.middle.infixExp())
        print("-----------------------------")
        w.right = expTree(postfix_expressions[4])
        print(w.right.infixExp())
        print("-----------------------------")
        s = whileNode('Statements: ')
        print(s.data)
        s.left = expTree(postfix_expressions[0])
        print(s.left.infixExp())
        print("-----------------------------")
        s.middle = expTree(postfix_expressions[1])
        print(s.middle.infixExp())
        print("-----------------------------")
        s.right = w
else:
    print("-----------------------------")
    print('Code cannot be processed semantically. ')
