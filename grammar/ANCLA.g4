grammar ANCLA;

/*
 * Parser Rules
 */

exp                 : function+ | line+;

function            : (FUNCTION '(' line ')') VARIABLE? ;

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

SPECIFICATION       : FAV | RT | 'user' | 'credentials' | 'hashtags' | 'sentiment' | 'datalog' | 'verbose' | 'setting' | 'function' | 'action' | 'lexical' | 'competitor' | 'tweets' ;

FUNCTION            : 'average' | 'print' ;

VARIABLE            : '.tweet_id' | '.tweet_created' | '.text' | '.favorites' | '.retweets' | '.replies' | '.user_name' | '.user_handle' | '.verified' | '.followers' | '.friends' | '.user_likes' | '.user_tweets' | '.user_created' ;

WORD				: (LOWERCASE | UPPERCASE | DIGIT | '_')+ ;

NUMBER              : DIGIT+ ;

LINK                : ('http://' | 'https://') (WORD | '-')+ ('.com' | '.edu' | '.org' | '.gov') ;

USER				: '@' WORD ;

HASHTAG             : '#' WORD ;

EMAIL               :  WORD '@' WORD ('.com' | '.edu' | '.org' | '.gov') ;

STRING              : '"' WORD ((WS | '-')* WORD)* '"' ;

WS			        : (' ' | '\t')+ ;

NEWLINE				: ('\r'? '\n' | '\r')+ ;