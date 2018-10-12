import sys
from antlr4 import *
from grammar.ANCLALexer import ANCLALexer
from grammar.ANCLAParser import ANCLAParser
from CustomANCLAListener import CustomANCLAListener
 
def main(argv):
    #user_input = FileStream(argv[1])
    print('ANCLA Command Line')

    while (True):
        user_input = input("-> ")
        if user_input.lower() == "q" or user_input.lower() == "quit" or user_input.lower() == "exit":   
            break

        i_stream = InputStream(user_input)
        lexer = ANCLALexer(i_stream)
        stream = CommonTokenStream(lexer)
        parser = ANCLAParser(stream)
        parser.buildParseTrees = True
        tree = parser.line()
        if parser.getNumberOfSyntaxErrors() < 1:
            ANCLA = CustomANCLAListener()
            walker = ParseTreeWalker()
            walker.walk(ANCLA, tree)

if __name__ == '__main__':
    main(sys.argv)