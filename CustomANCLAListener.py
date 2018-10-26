import sys
from antlr4 import *
from grammar.ANCLAParser import ANCLAParser
from grammar.ANCLAListener import ANCLAListener
from processLine import processLine
from processFunction import processFunction

#Idea here is for the listener to just store important info
#and pass that info to some function that calls all our modules


class CustomANCLAListener(ANCLAListener) :

    def __init__(self):
        self.action = ""
        self.specification = ""
        self.parameter = []
        self.result = {}

    def exitAction(self, ctx:ANCLAParser.ActionContext):
        if ctx.ACTION() is not None and ctx.SPECIFICATION() is not None:
            print("You want to " + ctx.ACTION().getText() + " " + ctx.SPECIFICATION().getText())
            self.action = ctx.ACTION().getText()
            self.specification = ctx.SPECIFICATION().getText()

    def exitParameter(self, ctx:ANCLAParser.ParameterContext):
        if ctx.LINK() is not None :
            print("As a parameter, you provided a link: " + ctx.LINK().getText())
            self.parameter.append(ctx.LINK().getText())

        elif ctx.USER() is not None :
            print("As a parameter, you provided a twitter handle: " + ctx.USER().getText())
            self.parameter.append(ctx.USER().getText())

        elif ctx.HASHTAG() is not None :
            print("As a parameter, you provided a hashtag: " + ctx.HASHTAG().getText())
            self.parameter.append(ctx.HASHTAG().getText())
        
        elif ctx.EMAIL() is not None :
            print("As a parameter, you provided an email: " + ctx.EMAIL().getText())
            self.parameter.append(ctx.EMAIL().getText())

        elif ctx.STRING() is not None :
            print("As a parameter, you provided a string: " + ctx.STRING().getText())
            self.parameter.append((ctx.STRING().getText()).replace('"',""))

        elif ctx.NUMBER() is not None :
            print("As a parameter, you provided an integer: " + ctx.NUMBER().getText())
            self.parameter.append(int(ctx.NUMBER().getText()))

        elif ctx.WORD() is not None :
            print("As a parameter, you provided a word: " + ctx.WORD().getText())
            self.parameter.append(ctx.WORD().getText())

    def exitLine(self, ctx:ANCLAParser.ActionContext):
        #This function handles ALL analysis calls
        self.result = processLine(self.action, self.specification, self.parameter)

    def exitFunction(self, ctx:ANCLAParser.FunctionContext):
        processFunction(self.result, ctx.FUNCTION().getText(), self.action, self.specification)