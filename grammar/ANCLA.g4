grammar ANCLA;

/*
 * Parser Rules
 */

line				: action (WS parameter)+ ;

action              : FUNCTION '-' SPECIFICATION ;

parameter           : NUMBER | LINK | USER | HASHTAG | EMAIL | STRING | WORD;

/*
 * Lexer Rules
 */

fragment LOWERCASE  : [a-z] ;
fragment UPPERCASE  : [A-Z] ;
fragment DIGIT      : [0-9] ;
fragment FAV        : 'favorites' | 'faves' | 'likes' | 'like' | 'hearts';
fragment RT         : 'retweets' | 'rt' | 'rts' | 'shares' | 'rtwt' | 'rtwts';

FUNCTION            : 'analyze' | 'search' | 'store' | 'live' | 'config' ;

SPECIFICATION       : FAV | RT | 'user' | 'credentials' | 'hashtags' | 'sentiment' | 'datalog' ;

WORD				: (LOWERCASE | UPPERCASE | DIGIT | '_')+ ;

NUMBER              : DIGIT+ ;

LINK                : ('http://' | 'https://') (WORD | '-')+ ('.com' | '.edu' | '.org' | '.gov') ;

USER				: '@' WORD ;

HASHTAG             : '#' WORD ;

EMAIL               :  WORD '@' WORD ('.com' | '.edu' | '.org' | '.gov') ;

STRING              : '"' WORD (WS WORD)* '"' ;

WS			        : (' ' | '\t')+ ;

NEWLINE				: ('\r'? '\n' | '\r')+ ;