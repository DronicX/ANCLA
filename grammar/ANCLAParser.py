# Generated from ANCLA.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("!\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\7\2\13\n\2\f\2\16\2")
        buf.write("\16\13\2\3\2\6\2\21\n\2\r\2\16\2\22\3\2\7\2\26\n\2\f\2")
        buf.write("\16\2\31\13\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\2\2\5\2\4\6")
        buf.write("\2\3\3\2\6\f\2 \2\b\3\2\2\2\4\32\3\2\2\2\6\36\3\2\2\2")
        buf.write("\b\f\5\4\3\2\t\13\7\r\2\2\n\t\3\2\2\2\13\16\3\2\2\2\f")
        buf.write("\n\3\2\2\2\f\r\3\2\2\2\r\27\3\2\2\2\16\f\3\2\2\2\17\21")
        buf.write("\7\r\2\2\20\17\3\2\2\2\21\22\3\2\2\2\22\20\3\2\2\2\22")
        buf.write("\23\3\2\2\2\23\24\3\2\2\2\24\26\5\6\4\2\25\20\3\2\2\2")
        buf.write("\26\31\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\3\3\2\2")
        buf.write("\2\31\27\3\2\2\2\32\33\7\4\2\2\33\34\7\3\2\2\34\35\7\5")
        buf.write("\2\2\35\5\3\2\2\2\36\37\t\2\2\2\37\7\3\2\2\2\5\f\22\27")
        return buf.getvalue()


class ANCLAParser ( Parser ):

    grammarFileName = "ANCLA.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "FUNCTION", "SPECIFICATION", 
                      "WORD", "NUMBER", "LINK", "USER", "HASHTAG", "EMAIL", 
                      "STRING", "WS", "NEWLINE" ]

    RULE_line = 0
    RULE_action = 1
    RULE_parameter = 2

    ruleNames =  [ "line", "action", "parameter" ]

    EOF = Token.EOF
    T__0=1
    FUNCTION=2
    SPECIFICATION=3
    WORD=4
    NUMBER=5
    LINK=6
    USER=7
    HASHTAG=8
    EMAIL=9
    STRING=10
    WS=11
    NEWLINE=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class LineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def action(self):
            return self.getTypedRuleContext(ANCLAParser.ActionContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(ANCLAParser.WS)
            else:
                return self.getToken(ANCLAParser.WS, i)

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ANCLAParser.ParameterContext)
            else:
                return self.getTypedRuleContext(ANCLAParser.ParameterContext,i)


        def getRuleIndex(self):
            return ANCLAParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = ANCLAParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.action()
            self.state = 10
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 7
                    self.match(ANCLAParser.WS) 
                self.state = 12
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ANCLAParser.WS:
                self.state = 14 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 13
                    self.match(ANCLAParser.WS)
                    self.state = 16 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ANCLAParser.WS):
                        break

                self.state = 18
                self.parameter()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ActionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(ANCLAParser.FUNCTION, 0)

        def SPECIFICATION(self):
            return self.getToken(ANCLAParser.SPECIFICATION, 0)

        def getRuleIndex(self):
            return ANCLAParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)




    def action(self):

        localctx = ANCLAParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(ANCLAParser.FUNCTION)
            self.state = 25
            self.match(ANCLAParser.T__0)
            self.state = 26
            self.match(ANCLAParser.SPECIFICATION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ANCLAParser.NUMBER, 0)

        def LINK(self):
            return self.getToken(ANCLAParser.LINK, 0)

        def USER(self):
            return self.getToken(ANCLAParser.USER, 0)

        def HASHTAG(self):
            return self.getToken(ANCLAParser.HASHTAG, 0)

        def EMAIL(self):
            return self.getToken(ANCLAParser.EMAIL, 0)

        def STRING(self):
            return self.getToken(ANCLAParser.STRING, 0)

        def WORD(self):
            return self.getToken(ANCLAParser.WORD, 0)

        def getRuleIndex(self):
            return ANCLAParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = ANCLAParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ANCLAParser.WORD) | (1 << ANCLAParser.NUMBER) | (1 << ANCLAParser.LINK) | (1 << ANCLAParser.USER) | (1 << ANCLAParser.HASHTAG) | (1 << ANCLAParser.EMAIL) | (1 << ANCLAParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





