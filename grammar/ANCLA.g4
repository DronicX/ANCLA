grammar ANCLA;

/*
 * Parser Rules
 */

exp                 : function+ | line+;

function            : (FUNCTION '(' line ')') VARIABLE{1} ;

line				: action WS* (WS+ parameter)* ;

action              : ACTION '-' SPECIFICATION ;

parameter           : NUMBER | LINK | USER | HASHTAG | EMAIL | STRING | WORD;

/*
 * Lexer Rules
 */

fragment LOWERCASE  : [a-z] ;
fragment UPPERCASE  : [A-Z] ;
fragment DIGIT      : [0-9] ;
fragment FAV        : 'favorites' | 'faves' | 'likes' | 'like' | 'hearts';
fragment RT         : 'retweets' | 'rt' | 'rts' | 'shares' | 'rtwt' | 'rtwts';

ACTION              : 'analyze' | 'search' | 'store' | 'live' | 'config' | 'help' ;

SPECIFICATION       : FAV | RT | 'user' | 'credentials' | 'hashtags' | 'sentiment' | 'datalog' | 'verbose' | 'setting' | 'function';

FUNCTION            : 'tendencies' ;

VARIABLE            : '.favorites' | '.text' | '.verified' | '.retweets' ;

WORD				: (LOWERCASE | UPPERCASE | DIGIT | '_')+ ;

NUMBER              : DIGIT+ ;

LINK                : ('http://' | 'https://') (WORD | '-')+ ('.com' | '.edu' | '.org' | '.gov') ;

USER				: '@' WORD ;

HASHTAG             : '#' WORD ;

EMAIL               :  WORD '@' WORD ('.com' | '.edu' | '.org' | '.gov') ;

STRING              : '"' WORD ((WS | '-')* WORD)* '"' ;

WS			        : (' ' | '\t')+ ;

NEWLINE				: ('\r'? '\n' | '\r')+ ;