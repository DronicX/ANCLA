# Generated from ANCLA.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("\66\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16")
        buf.write("\n\2\r\2\16\2\17\3\2\6\2\23\n\2\r\2\16\2\24\5\2\27\n\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\3\4\7\4 \n\4\f\4\16\4#\13\4\3")
        buf.write("\4\6\4&\n\4\r\4\16\4\'\3\4\7\4+\n\4\f\4\16\4.\13\4\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\2\2\7\2\4\6\b\n\2\3\3\2\t\17")
        buf.write("\2\66\2\26\3\2\2\2\4\30\3\2\2\2\6\35\3\2\2\2\b/\3\2\2")
        buf.write("\2\n\63\3\2\2\2\f\16\5\4\3\2\r\f\3\2\2\2\16\17\3\2\2\2")
        buf.write("\17\r\3\2\2\2\17\20\3\2\2\2\20\27\3\2\2\2\21\23\5\6\4")
        buf.write("\2\22\21\3\2\2\2\23\24\3\2\2\2\24\22\3\2\2\2\24\25\3\2")
        buf.write("\2\2\25\27\3\2\2\2\26\r\3\2\2\2\26\22\3\2\2\2\27\3\3\2")
        buf.write("\2\2\30\31\7\b\2\2\31\32\7\3\2\2\32\33\5\6\4\2\33\34\7")
        buf.write("\4\2\2\34\5\3\2\2\2\35!\5\b\5\2\36 \7\20\2\2\37\36\3\2")
        buf.write("\2\2 #\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\",\3\2\2\2#!\3\2")
        buf.write("\2\2$&\7\20\2\2%$\3\2\2\2&\'\3\2\2\2\'%\3\2\2\2\'(\3\2")
        buf.write("\2\2()\3\2\2\2)+\5\n\6\2*%\3\2\2\2+.\3\2\2\2,*\3\2\2\2")
        buf.write(",-\3\2\2\2-\7\3\2\2\2.,\3\2\2\2/\60\7\6\2\2\60\61\7\5")
        buf.write("\2\2\61\62\7\7\2\2\62\t\3\2\2\2\63\64\t\2\2\2\64\13\3")
        buf.write("\2\2\2\b\17\24\26!\',")
        return buf.getvalue()


class ANCLAParser ( Parser ):

    grammarFileName = "ANCLA.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'-'", "<INVALID>", "<INVALID>", 
                     "'tendencies'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ACTION", "SPECIFICATION", "FUNCTION", "WORD", "NUMBER", 
                      "LINK", "USER", "HASHTAG", "EMAIL", "STRING", "WS", 
                      "NEWLINE" ]

    RULE_exp = 0
    RULE_function = 1
    RULE_line = 2
    RULE_action = 3
    RULE_parameter = 4

    ruleNames =  [ "exp", "function", "line", "action", "parameter" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    ACTION=4
    SPECIFICATION=5
    FUNCTION=6
    WORD=7
    NUMBER=8
    LINK=9
    USER=10
    HASHTAG=11
    EMAIL=12
    STRING=13
    WS=14
    NEWLINE=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ANCLAParser.FunctionContext)
            else:
                return self.getTypedRuleContext(ANCLAParser.FunctionContext,i)


        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ANCLAParser.LineContext)
            else:
                return self.getTypedRuleContext(ANCLAParser.LineContext,i)


        def getRuleIndex(self):
            return ANCLAParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = ANCLAParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ANCLAParser.FUNCTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 10
                    self.function()
                    self.state = 13 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ANCLAParser.FUNCTION):
                        break

                pass
            elif token in [ANCLAParser.ACTION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 16 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 15
                    self.line()
                    self.state = 18 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ANCLAParser.ACTION):
                        break

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(ANCLAParser.FUNCTION, 0)

        def line(self):
            return self.getTypedRuleContext(ANCLAParser.LineContext,0)


        def getRuleIndex(self):
            return ANCLAParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = ANCLAParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(ANCLAParser.FUNCTION)
            self.state = 23
            self.match(ANCLAParser.T__0)
            self.state = 24
            self.line()
            self.state = 25
            self.match(ANCLAParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

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
        self.enterRule(localctx, 4, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.action()
            self.state = 31
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 28
                    self.match(ANCLAParser.WS) 
                self.state = 33
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ANCLAParser.WS:
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 34
                    self.match(ANCLAParser.WS)
                    self.state = 37 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ANCLAParser.WS):
                        break

                self.state = 39
                self.parameter()
                self.state = 44
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

        def ACTION(self):
            return self.getToken(ANCLAParser.ACTION, 0)

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
        self.enterRule(localctx, 6, self.RULE_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(ANCLAParser.ACTION)
            self.state = 46
            self.match(ANCLAParser.T__2)
            self.state = 47
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
        self.enterRule(localctx, 8, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
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





