import sys
from antlr4 import *
from grammar.ANCLALexer import ANCLALexer
from grammar.ANCLAParser import ANCLAParser
from CustomANCLAListener import CustomANCLAListener
from settingHandler import loadSettings
 
def main(argv):
    print('ANCLA Command Line')
    
    while (True):
        settings = loadSettings()
        print("\nCurrent settings:\n" + str(settings))
        user_input = input("-> ")
        if user_input.lower() == "q" or user_input.lower() == "quit" or user_input.lower() == "exit":   
            break
        
        if user_input.lower() == "help" or user_input.lower() == "manual" or user_input.lower() == "man":
            with open("help/manual.txt", 'r') as helpFile:
                for line in helpFile:
                    print(line)
        else:
            #Boilerplate code for antlr4
            i_stream = InputStream(user_input)
            lexer = ANCLALexer(i_stream)
            stream = CommonTokenStream(lexer)
            parser = ANCLAParser(stream)
            parser.buildParseTrees = True
            #Here we parse our input as a line
            tree = parser.exp()
            
            if parser.getNumberOfSyntaxErrors() < 1:
                ANCLA = CustomANCLAListener()
                walker = ParseTreeWalker()
                walker.walk(ANCLA, tree)

if __name__ == '__main__':
    main(sys.argv)