// Generated from c:\Users\madef\Documents\UPRM\2018-2019\First Semester\CIIC\ANCLA\grammar\ANCLA.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ANCLAParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, ACTION=4, SPECIFICATION=5, FUNCTION=6, VARIABLE=7, 
		WORD=8, NUMBER=9, LINK=10, USER=11, HASHTAG=12, EMAIL=13, STRING=14, WS=15, 
		NEWLINE=16;
	public static final int
		RULE_exp = 0, RULE_function = 1, RULE_line = 2, RULE_action = 3, RULE_parameter = 4;
	public static final String[] ruleNames = {
		"exp", "function", "line", "action", "parameter"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'('", "')'", "'-'", null, null, "'tendencies'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, "ACTION", "SPECIFICATION", "FUNCTION", "VARIABLE", 
		"WORD", "NUMBER", "LINK", "USER", "HASHTAG", "EMAIL", "STRING", "WS", 
		"NEWLINE"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "ANCLA.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ANCLAParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ExpContext extends ParserRuleContext {
		public List<FunctionContext> function() {
			return getRuleContexts(FunctionContext.class);
		}
		public FunctionContext function(int i) {
			return getRuleContext(FunctionContext.class,i);
		}
		public List<LineContext> line() {
			return getRuleContexts(LineContext.class);
		}
		public LineContext line(int i) {
			return getRuleContext(LineContext.class,i);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_exp);
		int _la;
		try {
			setState(20);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FUNCTION:
				enterOuterAlt(_localctx, 1);
				{
				setState(11); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(10);
					function();
					}
					}
					setState(13); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==FUNCTION );
				}
				break;
			case ACTION:
				enterOuterAlt(_localctx, 2);
				{
				setState(16); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(15);
					line();
					}
					}
					setState(18); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==ACTION );
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionContext extends ParserRuleContext {
		public TerminalNode VARIABLE() { return getToken(ANCLAParser.VARIABLE, 0); }
		public TerminalNode FUNCTION() { return getToken(ANCLAParser.FUNCTION, 0); }
		public LineContext line() {
			return getRuleContext(LineContext.class,0);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_function);
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(22);
			match(FUNCTION);
			setState(23);
			match(T__0);
			setState(24);
			line();
			setState(25);
			match(T__1);
			}
			setState(27);
			match(VARIABLE);
			1
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LineContext extends ParserRuleContext {
		public ActionContext action() {
			return getRuleContext(ActionContext.class,0);
		}
		public List<TerminalNode> WS() { return getTokens(ANCLAParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(ANCLAParser.WS, i);
		}
		public List<ParameterContext> parameter() {
			return getRuleContexts(ParameterContext.class);
		}
		public ParameterContext parameter(int i) {
			return getRuleContext(ParameterContext.class,i);
		}
		public LineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_line; }
	}

	public final LineContext line() throws RecognitionException {
		LineContext _localctx = new LineContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_line);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			action();
			setState(34);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(31);
					match(WS);
					}
					} 
				}
				setState(36);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			}
			setState(45);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==WS) {
				{
				{
				setState(38); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(37);
					match(WS);
					}
					}
					setState(40); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==WS );
				setState(42);
				parameter();
				}
				}
				setState(47);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ActionContext extends ParserRuleContext {
		public TerminalNode ACTION() { return getToken(ANCLAParser.ACTION, 0); }
		public TerminalNode SPECIFICATION() { return getToken(ANCLAParser.SPECIFICATION, 0); }
		public ActionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_action; }
	}

	public final ActionContext action() throws RecognitionException {
		ActionContext _localctx = new ActionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_action);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			match(ACTION);
			setState(49);
			match(T__2);
			setState(50);
			match(SPECIFICATION);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParameterContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(ANCLAParser.NUMBER, 0); }
		public TerminalNode LINK() { return getToken(ANCLAParser.LINK, 0); }
		public TerminalNode USER() { return getToken(ANCLAParser.USER, 0); }
		public TerminalNode HASHTAG() { return getToken(ANCLAParser.HASHTAG, 0); }
		public TerminalNode EMAIL() { return getToken(ANCLAParser.EMAIL, 0); }
		public TerminalNode STRING() { return getToken(ANCLAParser.STRING, 0); }
		public TerminalNode WORD() { return getToken(ANCLAParser.WORD, 0); }
		public ParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter; }
	}

	public final ParameterContext parameter() throws RecognitionException {
		ParameterContext _localctx = new ParameterContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_parameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(52);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << WORD) | (1L << NUMBER) | (1L << LINK) | (1L << USER) | (1L << HASHTAG) | (1L << EMAIL) | (1L << STRING))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\229\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16\n\2\r\2\16\2\17\3\2\6\2\23\n\2\r"+
		"\2\16\2\24\5\2\27\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\7\4#\n\4"+
		"\f\4\16\4&\13\4\3\4\6\4)\n\4\r\4\16\4*\3\4\7\4.\n\4\f\4\16\4\61\13\4\3"+
		"\5\3\5\3\5\3\5\3\6\3\6\3\6\2\2\7\2\4\6\b\n\2\3\3\2\n\20\29\2\26\3\2\2"+
		"\2\4\30\3\2\2\2\6 \3\2\2\2\b\62\3\2\2\2\n\66\3\2\2\2\f\16\5\4\3\2\r\f"+
		"\3\2\2\2\16\17\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2\20\27\3\2\2\2\21\23"+
		"\5\6\4\2\22\21\3\2\2\2\23\24\3\2\2\2\24\22\3\2\2\2\24\25\3\2\2\2\25\27"+
		"\3\2\2\2\26\r\3\2\2\2\26\22\3\2\2\2\27\3\3\2\2\2\30\31\7\b\2\2\31\32\7"+
		"\3\2\2\32\33\5\6\4\2\33\34\7\4\2\2\34\35\3\2\2\2\35\36\7\t\2\2\36\37\b"+
		"\3\1\2\37\5\3\2\2\2 $\5\b\5\2!#\7\21\2\2\"!\3\2\2\2#&\3\2\2\2$\"\3\2\2"+
		"\2$%\3\2\2\2%/\3\2\2\2&$\3\2\2\2\')\7\21\2\2(\'\3\2\2\2)*\3\2\2\2*(\3"+
		"\2\2\2*+\3\2\2\2+,\3\2\2\2,.\5\n\6\2-(\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/"+
		"\60\3\2\2\2\60\7\3\2\2\2\61/\3\2\2\2\62\63\7\6\2\2\63\64\7\5\2\2\64\65"+
		"\7\7\2\2\65\t\3\2\2\2\66\67\t\2\2\2\67\13\3\2\2\2\b\17\24\26$*/";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}