// Generated from c:\Users\madef\Documents\UPRM\2018-2019\First Semester\CIIC\ANCLA\grammar\ANCLA.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ANCLALexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, ACTION=4, SPECIFICATION=5, FUNCTION=6, VARIABLE=7, 
		WORD=8, NUMBER=9, LINK=10, USER=11, HASHTAG=12, EMAIL=13, STRING=14, WS=15, 
		NEWLINE=16;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "T__1", "T__2", "LOWERCASE", "UPPERCASE", "DIGIT", "FAV", "RT", 
		"ACTION", "SPECIFICATION", "FUNCTION", "VARIABLE", "WORD", "NUMBER", "LINK", 
		"USER", "HASHTAG", "EMAIL", "STRING", "WS", "NEWLINE"
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


	public ANCLALexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "ANCLA.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22\u0177\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\3\3\3\3\3\4\3\4"+
		"\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3"+
		"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b"+
		"\5\bW\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tu\n\t\3\n\3\n"+
		"\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3"+
		"\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u0097\n\n\3\13"+
		"\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13"+
		"\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13"+
		"\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13"+
		"\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13"+
		"\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00d8\n\13\3\f\3\f\3\f\3\f\3\f\3\f"+
		"\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3"+
		"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r"+
		"\3\r\3\r\3\r\5\r\u0106\n\r\3\16\3\16\3\16\3\16\6\16\u010c\n\16\r\16\16"+
		"\16\u010d\3\17\6\17\u0111\n\17\r\17\16\17\u0112\3\20\3\20\3\20\3\20\3"+
		"\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u0124\n\20"+
		"\3\20\3\20\6\20\u0128\n\20\r\20\16\20\u0129\3\20\3\20\3\20\3\20\3\20\3"+
		"\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u013c\n\20"+
		"\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23"+
		"\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0157\n\23"+
		"\3\24\3\24\3\24\3\24\7\24\u015d\n\24\f\24\16\24\u0160\13\24\3\24\7\24"+
		"\u0163\n\24\f\24\16\24\u0166\13\24\3\24\3\24\3\25\6\25\u016b\n\25\r\25"+
		"\16\25\u016c\3\26\5\26\u0170\n\26\3\26\3\26\6\26\u0174\n\26\r\26\16\26"+
		"\u0175\2\2\27\3\3\5\4\7\5\t\2\13\2\r\2\17\2\21\2\23\6\25\7\27\b\31\t\33"+
		"\n\35\13\37\f!\r#\16%\17\'\20)\21+\22\3\2\6\3\2c|\3\2C\\\3\2\62;\4\2\13"+
		"\13\"\"\2\u01a0\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\23\3\2\2\2\2\25"+
		"\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2"+
		"\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2"+
		"\2\3-\3\2\2\2\5/\3\2\2\2\7\61\3\2\2\2\t\63\3\2\2\2\13\65\3\2\2\2\r\67"+
		"\3\2\2\2\17V\3\2\2\2\21t\3\2\2\2\23\u0096\3\2\2\2\25\u00d7\3\2\2\2\27"+
		"\u00d9\3\2\2\2\31\u0105\3\2\2\2\33\u010b\3\2\2\2\35\u0110\3\2\2\2\37\u0123"+
		"\3\2\2\2!\u013d\3\2\2\2#\u0140\3\2\2\2%\u0143\3\2\2\2\'\u0158\3\2\2\2"+
		")\u016a\3\2\2\2+\u0173\3\2\2\2-.\7*\2\2.\4\3\2\2\2/\60\7+\2\2\60\6\3\2"+
		"\2\2\61\62\7/\2\2\62\b\3\2\2\2\63\64\t\2\2\2\64\n\3\2\2\2\65\66\t\3\2"+
		"\2\66\f\3\2\2\2\678\t\4\2\28\16\3\2\2\29:\7h\2\2:;\7c\2\2;<\7x\2\2<=\7"+
		"q\2\2=>\7t\2\2>?\7k\2\2?@\7v\2\2@A\7g\2\2AW\7u\2\2BC\7h\2\2CD\7c\2\2D"+
		"E\7x\2\2EF\7g\2\2FW\7u\2\2GH\7n\2\2HI\7k\2\2IJ\7m\2\2JK\7g\2\2KW\7u\2"+
		"\2LM\7n\2\2MN\7k\2\2NO\7m\2\2OW\7g\2\2PQ\7j\2\2QR\7g\2\2RS\7c\2\2ST\7"+
		"t\2\2TU\7v\2\2UW\7u\2\2V9\3\2\2\2VB\3\2\2\2VG\3\2\2\2VL\3\2\2\2VP\3\2"+
		"\2\2W\20\3\2\2\2XY\7t\2\2YZ\7g\2\2Z[\7v\2\2[\\\7y\2\2\\]\7g\2\2]^\7g\2"+
		"\2^_\7v\2\2_u\7u\2\2`a\7t\2\2au\7v\2\2bc\7t\2\2cd\7v\2\2du\7u\2\2ef\7"+
		"u\2\2fg\7j\2\2gh\7c\2\2hi\7t\2\2ij\7g\2\2ju\7u\2\2kl\7t\2\2lm\7v\2\2m"+
		"n\7y\2\2nu\7v\2\2op\7t\2\2pq\7v\2\2qr\7y\2\2rs\7v\2\2su\7u\2\2tX\3\2\2"+
		"\2t`\3\2\2\2tb\3\2\2\2te\3\2\2\2tk\3\2\2\2to\3\2\2\2u\22\3\2\2\2vw\7c"+
		"\2\2wx\7p\2\2xy\7c\2\2yz\7n\2\2z{\7{\2\2{|\7|\2\2|\u0097\7g\2\2}~\7u\2"+
		"\2~\177\7g\2\2\177\u0080\7c\2\2\u0080\u0081\7t\2\2\u0081\u0082\7e\2\2"+
		"\u0082\u0097\7j\2\2\u0083\u0084\7u\2\2\u0084\u0085\7v\2\2\u0085\u0086"+
		"\7q\2\2\u0086\u0087\7t\2\2\u0087\u0097\7g\2\2\u0088\u0089\7n\2\2\u0089"+
		"\u008a\7k\2\2\u008a\u008b\7x\2\2\u008b\u0097\7g\2\2\u008c\u008d\7e\2\2"+
		"\u008d\u008e\7q\2\2\u008e\u008f\7p\2\2\u008f\u0090\7h\2\2\u0090\u0091"+
		"\7k\2\2\u0091\u0097\7i\2\2\u0092\u0093\7j\2\2\u0093\u0094\7g\2\2\u0094"+
		"\u0095\7n\2\2\u0095\u0097\7r\2\2\u0096v\3\2\2\2\u0096}\3\2\2\2\u0096\u0083"+
		"\3\2\2\2\u0096\u0088\3\2\2\2\u0096\u008c\3\2\2\2\u0096\u0092\3\2\2\2\u0097"+
		"\24\3\2\2\2\u0098\u00d8\5\17\b\2\u0099\u00d8\5\21\t\2\u009a\u009b\7w\2"+
		"\2\u009b\u009c\7u\2\2\u009c\u009d\7g\2\2\u009d\u00d8\7t\2\2\u009e\u009f"+
		"\7e\2\2\u009f\u00a0\7t\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2\7f\2\2\u00a2"+
		"\u00a3\7g\2\2\u00a3\u00a4\7p\2\2\u00a4\u00a5\7v\2\2\u00a5\u00a6\7k\2\2"+
		"\u00a6\u00a7\7c\2\2\u00a7\u00a8\7n\2\2\u00a8\u00d8\7u\2\2\u00a9\u00aa"+
		"\7j\2\2\u00aa\u00ab\7c\2\2\u00ab\u00ac\7u\2\2\u00ac\u00ad\7j\2\2\u00ad"+
		"\u00ae\7v\2\2\u00ae\u00af\7c\2\2\u00af\u00b0\7i\2\2\u00b0\u00d8\7u\2\2"+
		"\u00b1\u00b2\7u\2\2\u00b2\u00b3\7g\2\2\u00b3\u00b4\7p\2\2\u00b4\u00b5"+
		"\7v\2\2\u00b5\u00b6\7k\2\2\u00b6\u00b7\7o\2\2\u00b7\u00b8\7g\2\2\u00b8"+
		"\u00b9\7p\2\2\u00b9\u00d8\7v\2\2\u00ba\u00bb\7f\2\2\u00bb\u00bc\7c\2\2"+
		"\u00bc\u00bd\7v\2\2\u00bd\u00be\7c\2\2\u00be\u00bf\7n\2\2\u00bf\u00c0"+
		"\7q\2\2\u00c0\u00d8\7i\2\2\u00c1\u00c2\7x\2\2\u00c2\u00c3\7g\2\2\u00c3"+
		"\u00c4\7t\2\2\u00c4\u00c5\7d\2\2\u00c5\u00c6\7q\2\2\u00c6\u00c7\7u\2\2"+
		"\u00c7\u00d8\7g\2\2\u00c8\u00c9\7u\2\2\u00c9\u00ca\7g\2\2\u00ca\u00cb"+
		"\7v\2\2\u00cb\u00cc\7v\2\2\u00cc\u00cd\7k\2\2\u00cd\u00ce\7p\2\2\u00ce"+
		"\u00d8\7i\2\2\u00cf\u00d0\7h\2\2\u00d0\u00d1\7w\2\2\u00d1\u00d2\7p\2\2"+
		"\u00d2\u00d3\7e\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5\7k\2\2\u00d5\u00d6"+
		"\7q\2\2\u00d6\u00d8\7p\2\2\u00d7\u0098\3\2\2\2\u00d7\u0099\3\2\2\2\u00d7"+
		"\u009a\3\2\2\2\u00d7\u009e\3\2\2\2\u00d7\u00a9\3\2\2\2\u00d7\u00b1\3\2"+
		"\2\2\u00d7\u00ba\3\2\2\2\u00d7\u00c1\3\2\2\2\u00d7\u00c8\3\2\2\2\u00d7"+
		"\u00cf\3\2\2\2\u00d8\26\3\2\2\2\u00d9\u00da\7v\2\2\u00da\u00db\7g\2\2"+
		"\u00db\u00dc\7p\2\2\u00dc\u00dd\7f\2\2\u00dd\u00de\7g\2\2\u00de\u00df"+
		"\7p\2\2\u00df\u00e0\7e\2\2\u00e0\u00e1\7k\2\2\u00e1\u00e2\7g\2\2\u00e2"+
		"\u00e3\7u\2\2\u00e3\30\3\2\2\2\u00e4\u00e5\7\60\2\2\u00e5\u00e6\7h\2\2"+
		"\u00e6\u00e7\7c\2\2\u00e7\u00e8\7x\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea"+
		"\7t\2\2\u00ea\u00eb\7k\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed\7g\2\2\u00ed"+
		"\u0106\7u\2\2\u00ee\u00ef\7\60\2\2\u00ef\u00f0\7v\2\2\u00f0\u00f1\7g\2"+
		"\2\u00f1\u00f2\7z\2\2\u00f2\u0106\7v\2\2\u00f3\u00f4\7\60\2\2\u00f4\u00f5"+
		"\7x\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8\7k\2\2\u00f8"+
		"\u00f9\7h\2\2\u00f9\u00fa\7k\2\2\u00fa\u00fb\7g\2\2\u00fb\u0106\7f\2\2"+
		"\u00fc\u00fd\7\60\2\2\u00fd\u00fe\7t\2\2\u00fe\u00ff\7g\2\2\u00ff\u0100"+
		"\7v\2\2\u0100\u0101\7y\2\2\u0101\u0102\7g\2\2\u0102\u0103\7g\2\2\u0103"+
		"\u0104\7v\2\2\u0104\u0106\7u\2\2\u0105\u00e4\3\2\2\2\u0105\u00ee\3\2\2"+
		"\2\u0105\u00f3\3\2\2\2\u0105\u00fc\3\2\2\2\u0106\32\3\2\2\2\u0107\u010c"+
		"\5\t\5\2\u0108\u010c\5\13\6\2\u0109\u010c\5\r\7\2\u010a\u010c\7a\2\2\u010b"+
		"\u0107\3\2\2\2\u010b\u0108\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010a\3\2"+
		"\2\2\u010c\u010d\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e"+
		"\34\3\2\2\2\u010f\u0111\5\r\7\2\u0110\u010f\3\2\2\2\u0111\u0112\3\2\2"+
		"\2\u0112\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113\36\3\2\2\2\u0114\u0115"+
		"\7j\2\2\u0115\u0116\7v\2\2\u0116\u0117\7v\2\2\u0117\u0118\7r\2\2\u0118"+
		"\u0119\7<\2\2\u0119\u011a\7\61\2\2\u011a\u0124\7\61\2\2\u011b\u011c\7"+
		"j\2\2\u011c\u011d\7v\2\2\u011d\u011e\7v\2\2\u011e\u011f\7r\2\2\u011f\u0120"+
		"\7u\2\2\u0120\u0121\7<\2\2\u0121\u0122\7\61\2\2\u0122\u0124\7\61\2\2\u0123"+
		"\u0114\3\2\2\2\u0123\u011b\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0128\5\33"+
		"\16\2\u0126\u0128\7/\2\2\u0127\u0125\3\2\2\2\u0127\u0126\3\2\2\2\u0128"+
		"\u0129\3\2\2\2\u0129\u0127\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u013b\3\2"+
		"\2\2\u012b\u012c\7\60\2\2\u012c\u012d\7e\2\2\u012d\u012e\7q\2\2\u012e"+
		"\u013c\7o\2\2\u012f\u0130\7\60\2\2\u0130\u0131\7g\2\2\u0131\u0132\7f\2"+
		"\2\u0132\u013c\7w\2\2\u0133\u0134\7\60\2\2\u0134\u0135\7q\2\2\u0135\u0136"+
		"\7t\2\2\u0136\u013c\7i\2\2\u0137\u0138\7\60\2\2\u0138\u0139\7i\2\2\u0139"+
		"\u013a\7q\2\2\u013a\u013c\7x\2\2\u013b\u012b\3\2\2\2\u013b\u012f\3\2\2"+
		"\2\u013b\u0133\3\2\2\2\u013b\u0137\3\2\2\2\u013c \3\2\2\2\u013d\u013e"+
		"\7B\2\2\u013e\u013f\5\33\16\2\u013f\"\3\2\2\2\u0140\u0141\7%\2\2\u0141"+
		"\u0142\5\33\16\2\u0142$\3\2\2\2\u0143\u0144\5\33\16\2\u0144\u0145\7B\2"+
		"\2\u0145\u0156\5\33\16\2\u0146\u0147\7\60\2\2\u0147\u0148\7e\2\2\u0148"+
		"\u0149\7q\2\2\u0149\u0157\7o\2\2\u014a\u014b\7\60\2\2\u014b\u014c\7g\2"+
		"\2\u014c\u014d\7f\2\2\u014d\u0157\7w\2\2\u014e\u014f\7\60\2\2\u014f\u0150"+
		"\7q\2\2\u0150\u0151\7t\2\2\u0151\u0157\7i\2\2\u0152\u0153\7\60\2\2\u0153"+
		"\u0154\7i\2\2\u0154\u0155\7q\2\2\u0155\u0157\7x\2\2\u0156\u0146\3\2\2"+
		"\2\u0156\u014a\3\2\2\2\u0156\u014e\3\2\2\2\u0156\u0152\3\2\2\2\u0157&"+
		"\3\2\2\2\u0158\u0159\7$\2\2\u0159\u0164\5\33\16\2\u015a\u015d\5)\25\2"+
		"\u015b\u015d\7/\2\2\u015c\u015a\3\2\2\2\u015c\u015b\3\2\2\2\u015d\u0160"+
		"\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0161\3\2\2\2\u0160"+
		"\u015e\3\2\2\2\u0161\u0163\5\33\16\2\u0162\u015e\3\2\2\2\u0163\u0166\3"+
		"\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0167\3\2\2\2\u0166"+
		"\u0164\3\2\2\2\u0167\u0168\7$\2\2\u0168(\3\2\2\2\u0169\u016b\t\5\2\2\u016a"+
		"\u0169\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d\3\2"+
		"\2\2\u016d*\3\2\2\2\u016e\u0170\7\17\2\2\u016f\u016e\3\2\2\2\u016f\u0170"+
		"\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0174\7\f\2\2\u0172\u0174\7\17\2\2"+
		"\u0173\u016f\3\2\2\2\u0173\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0173"+
		"\3\2\2\2\u0175\u0176\3\2\2\2\u0176,\3\2\2\2\27\2Vt\u0096\u00d7\u0105\u010b"+
		"\u010d\u0112\u0123\u0127\u0129\u013b\u0156\u015c\u015e\u0164\u016c\u016f"+
		"\u0173\u0175\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}