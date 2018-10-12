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
		T__0=1, FUNCTION=2, SPECIFICATION=3, WORD=4, NUMBER=5, LINK=6, USER=7, 
		HASHTAG=8, EMAIL=9, STRING=10, WS=11, NEWLINE=12;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "LOWERCASE", "UPPERCASE", "DIGIT", "FAV", "RT", "FUNCTION", "SPECIFICATION", 
		"WORD", "NUMBER", "LINK", "USER", "HASHTAG", "EMAIL", "STRING", "WS", 
		"NEWLINE"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'-'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, "FUNCTION", "SPECIFICATION", "WORD", "NUMBER", "LINK", "USER", 
		"HASHTAG", "EMAIL", "STRING", "WS", "NEWLINE"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16\u0111\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6"+
		"\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\5\6K\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7"+
		"i\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b"+
		"\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u0081\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3"+
		"\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00a5\n\t\3\n\3\n\3\n\3\n\6\n\u00ab"+
		"\n\n\r\n\16\n\u00ac\3\13\6\13\u00b0\n\13\r\13\16\13\u00b1\3\f\3\f\3\f"+
		"\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00c3\n\f\3\f\3\f"+
		"\6\f\u00c7\n\f\r\f\16\f\u00c8\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f"+
		"\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00db\n\f\3\r\3\r\3\r\3\16\3\16\3\16\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\3\17\3\17\3\17\5\17\u00f6\n\17\3\20\3\20\3\20\3\20\3\20\7\20\u00fd"+
		"\n\20\f\20\16\20\u0100\13\20\3\20\3\20\3\21\6\21\u0105\n\21\r\21\16\21"+
		"\u0106\3\22\5\22\u010a\n\22\3\22\3\22\6\22\u010e\n\22\r\22\16\22\u010f"+
		"\2\2\23\3\3\5\2\7\2\t\2\13\2\r\2\17\4\21\5\23\6\25\7\27\b\31\t\33\n\35"+
		"\13\37\f!\r#\16\3\2\6\3\2c|\3\2C\\\3\2\62;\4\2\13\13\"\"\2\u012f\2\3\3"+
		"\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2"+
		"\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3"+
		"\2\2\2\3%\3\2\2\2\5\'\3\2\2\2\7)\3\2\2\2\t+\3\2\2\2\13J\3\2\2\2\rh\3\2"+
		"\2\2\17\u0080\3\2\2\2\21\u00a4\3\2\2\2\23\u00aa\3\2\2\2\25\u00af\3\2\2"+
		"\2\27\u00c2\3\2\2\2\31\u00dc\3\2\2\2\33\u00df\3\2\2\2\35\u00e2\3\2\2\2"+
		"\37\u00f7\3\2\2\2!\u0104\3\2\2\2#\u010d\3\2\2\2%&\7/\2\2&\4\3\2\2\2\'"+
		"(\t\2\2\2(\6\3\2\2\2)*\t\3\2\2*\b\3\2\2\2+,\t\4\2\2,\n\3\2\2\2-.\7h\2"+
		"\2./\7c\2\2/\60\7x\2\2\60\61\7q\2\2\61\62\7t\2\2\62\63\7k\2\2\63\64\7"+
		"v\2\2\64\65\7g\2\2\65K\7u\2\2\66\67\7h\2\2\678\7c\2\289\7x\2\29:\7g\2"+
		"\2:K\7u\2\2;<\7n\2\2<=\7k\2\2=>\7m\2\2>?\7g\2\2?K\7u\2\2@A\7n\2\2AB\7"+
		"k\2\2BC\7m\2\2CK\7g\2\2DE\7j\2\2EF\7g\2\2FG\7c\2\2GH\7t\2\2HI\7v\2\2I"+
		"K\7u\2\2J-\3\2\2\2J\66\3\2\2\2J;\3\2\2\2J@\3\2\2\2JD\3\2\2\2K\f\3\2\2"+
		"\2LM\7t\2\2MN\7g\2\2NO\7v\2\2OP\7y\2\2PQ\7g\2\2QR\7g\2\2RS\7v\2\2Si\7"+
		"u\2\2TU\7t\2\2Ui\7v\2\2VW\7t\2\2WX\7v\2\2Xi\7u\2\2YZ\7u\2\2Z[\7j\2\2["+
		"\\\7c\2\2\\]\7t\2\2]^\7g\2\2^i\7u\2\2_`\7t\2\2`a\7v\2\2ab\7y\2\2bi\7v"+
		"\2\2cd\7t\2\2de\7v\2\2ef\7y\2\2fg\7v\2\2gi\7u\2\2hL\3\2\2\2hT\3\2\2\2"+
		"hV\3\2\2\2hY\3\2\2\2h_\3\2\2\2hc\3\2\2\2i\16\3\2\2\2jk\7c\2\2kl\7p\2\2"+
		"lm\7c\2\2mn\7n\2\2no\7{\2\2op\7|\2\2p\u0081\7g\2\2qr\7u\2\2rs\7g\2\2s"+
		"t\7c\2\2tu\7t\2\2uv\7e\2\2v\u0081\7j\2\2wx\7u\2\2xy\7v\2\2yz\7q\2\2z{"+
		"\7t\2\2{\u0081\7g\2\2|}\7n\2\2}~\7k\2\2~\177\7x\2\2\177\u0081\7g\2\2\u0080"+
		"j\3\2\2\2\u0080q\3\2\2\2\u0080w\3\2\2\2\u0080|\3\2\2\2\u0081\20\3\2\2"+
		"\2\u0082\u00a5\5\13\6\2\u0083\u00a5\5\r\7\2\u0084\u0085\7w\2\2\u0085\u0086"+
		"\7u\2\2\u0086\u0087\7g\2\2\u0087\u00a5\7t\2\2\u0088\u0089\7e\2\2\u0089"+
		"\u008a\7t\2\2\u008a\u008b\7g\2\2\u008b\u008c\7f\2\2\u008c\u008d\7g\2\2"+
		"\u008d\u008e\7p\2\2\u008e\u008f\7v\2\2\u008f\u0090\7k\2\2\u0090\u0091"+
		"\7c\2\2\u0091\u0092\7n\2\2\u0092\u00a5\7u\2\2\u0093\u0094\7j\2\2\u0094"+
		"\u0095\7c\2\2\u0095\u0096\7u\2\2\u0096\u0097\7j\2\2\u0097\u0098\7v\2\2"+
		"\u0098\u0099\7c\2\2\u0099\u009a\7i\2\2\u009a\u00a5\7u\2\2\u009b\u009c"+
		"\7u\2\2\u009c\u009d\7g\2\2\u009d\u009e\7p\2\2\u009e\u009f\7v\2\2\u009f"+
		"\u00a0\7k\2\2\u00a0\u00a1\7o\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3\7p\2\2"+
		"\u00a3\u00a5\7v\2\2\u00a4\u0082\3\2\2\2\u00a4\u0083\3\2\2\2\u00a4\u0084"+
		"\3\2\2\2\u00a4\u0088\3\2\2\2\u00a4\u0093\3\2\2\2\u00a4\u009b\3\2\2\2\u00a5"+
		"\22\3\2\2\2\u00a6\u00ab\5\5\3\2\u00a7\u00ab\5\7\4\2\u00a8\u00ab\5\t\5"+
		"\2\u00a9\u00ab\7a\2\2\u00aa\u00a6\3\2\2\2\u00aa\u00a7\3\2\2\2\u00aa\u00a8"+
		"\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac"+
		"\u00ad\3\2\2\2\u00ad\24\3\2\2\2\u00ae\u00b0\5\t\5\2\u00af\u00ae\3\2\2"+
		"\2\u00b0\u00b1\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\26"+
		"\3\2\2\2\u00b3\u00b4\7j\2\2\u00b4\u00b5\7v\2\2\u00b5\u00b6\7v\2\2\u00b6"+
		"\u00b7\7r\2\2\u00b7\u00b8\7<\2\2\u00b8\u00b9\7\61\2\2\u00b9\u00c3\7\61"+
		"\2\2\u00ba\u00bb\7j\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd\7v\2\2\u00bd\u00be"+
		"\7r\2\2\u00be\u00bf\7u\2\2\u00bf\u00c0\7<\2\2\u00c0\u00c1\7\61\2\2\u00c1"+
		"\u00c3\7\61\2\2\u00c2\u00b3\3\2\2\2\u00c2\u00ba\3\2\2\2\u00c3\u00c6\3"+
		"\2\2\2\u00c4\u00c7\5\23\n\2\u00c5\u00c7\7/\2\2\u00c6\u00c4\3\2\2\2\u00c6"+
		"\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2"+
		"\2\2\u00c9\u00da\3\2\2\2\u00ca\u00cb\7\60\2\2\u00cb\u00cc\7e\2\2\u00cc"+
		"\u00cd\7q\2\2\u00cd\u00db\7o\2\2\u00ce\u00cf\7\60\2\2\u00cf\u00d0\7g\2"+
		"\2\u00d0\u00d1\7f\2\2\u00d1\u00db\7w\2\2\u00d2\u00d3\7\60\2\2\u00d3\u00d4"+
		"\7q\2\2\u00d4\u00d5\7t\2\2\u00d5\u00db\7i\2\2\u00d6\u00d7\7\60\2\2\u00d7"+
		"\u00d8\7i\2\2\u00d8\u00d9\7q\2\2\u00d9\u00db\7x\2\2\u00da\u00ca\3\2\2"+
		"\2\u00da\u00ce\3\2\2\2\u00da\u00d2\3\2\2\2\u00da\u00d6\3\2\2\2\u00db\30"+
		"\3\2\2\2\u00dc\u00dd\7B\2\2\u00dd\u00de\5\23\n\2\u00de\32\3\2\2\2\u00df"+
		"\u00e0\7%\2\2\u00e0\u00e1\5\23\n\2\u00e1\34\3\2\2\2\u00e2\u00e3\5\23\n"+
		"\2\u00e3\u00e4\7B\2\2\u00e4\u00f5\5\23\n\2\u00e5\u00e6\7\60\2\2\u00e6"+
		"\u00e7\7e\2\2\u00e7\u00e8\7q\2\2\u00e8\u00f6\7o\2\2\u00e9\u00ea\7\60\2"+
		"\2\u00ea\u00eb\7g\2\2\u00eb\u00ec\7f\2\2\u00ec\u00f6\7w\2\2\u00ed\u00ee"+
		"\7\60\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0\7t\2\2\u00f0\u00f6\7i\2\2\u00f1"+
		"\u00f2\7\60\2\2\u00f2\u00f3\7i\2\2\u00f3\u00f4\7q\2\2\u00f4\u00f6\7x\2"+
		"\2\u00f5\u00e5\3\2\2\2\u00f5\u00e9\3\2\2\2\u00f5\u00ed\3\2\2\2\u00f5\u00f1"+
		"\3\2\2\2\u00f6\36\3\2\2\2\u00f7\u00f8\7$\2\2\u00f8\u00fe\5\23\n\2\u00f9"+
		"\u00fa\5!\21\2\u00fa\u00fb\5\23\n\2\u00fb\u00fd\3\2\2\2\u00fc\u00f9\3"+
		"\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff"+
		"\u0101\3\2\2\2\u0100\u00fe\3\2\2\2\u0101\u0102\7$\2\2\u0102 \3\2\2\2\u0103"+
		"\u0105\t\5\2\2\u0104\u0103\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0104\3\2"+
		"\2\2\u0106\u0107\3\2\2\2\u0107\"\3\2\2\2\u0108\u010a\7\17\2\2\u0109\u0108"+
		"\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u010e\7\f\2\2\u010c"+
		"\u010e\7\17\2\2\u010d\u0109\3\2\2\2\u010d\u010c\3\2\2\2\u010e\u010f\3"+
		"\2\2\2\u010f\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110$\3\2\2\2\24\2Jh\u0080"+
		"\u00a4\u00aa\u00ac\u00b1\u00c2\u00c6\u00c8\u00da\u00f5\u00fe\u0106\u0109"+
		"\u010d\u010f\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}