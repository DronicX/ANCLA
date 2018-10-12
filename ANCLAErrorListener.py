import sys
from antlr4 import *
from grammar.ANCLAParser import ANCLAParser
from grammar.ANCLAListener import ANCLAListener
from antlr4.error.ErrorListener import *
import io
 
class ANCLAErrorListener(ErrorListener):
 
    def __init__(self, output):
        self.output = output        
        self._symbol = ''
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):        
        self.output.write(msg)
        self._symbol = offendingSymbol.text
 
    @property        
    def symbol(self):
        return self._symbol