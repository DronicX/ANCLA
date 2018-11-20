![ancla](https://user-images.githubusercontent.com/5660320/48219676-80626680-e363-11e8-856e-6ad1f488a4a1.png)
#
**Automatic Net Content &amp; Language Analysis (ANCLA) is a programming language that facilitates extracting and analyzing data from social media. It's main focus now is the Twitter Social Media analysis. :hatched_chick:**
#

**Features Included:**

 - [x] Configurations
 ```
       -> Datalog
       -> Verbose
 ```
 - [x] Functions 
 ```
       -> Mean
       -> Average
 ```
 - [x] Analysis
 ```
       -> Competitiveness
       -> Lexical
       -> Sentiment
 ```
 - [x] Average of: Likes, Retweets, Reach, among others etc.
 - [x] Graphical Results
  

## Configurations

 **Datalog Setting:**

This settings indicates whether or not you want to save in a file log the output of the functions that the user is using for analysis.

###### Usage: 
```
-- config-datalog false :    
        > sets datalog to false, not letting the data collected to be stored on a log file

-- config-datalog true  :   
       > sets datalog to true, letting the data collected on console to be saved or stored on a log file
```
###### Parameters:
```
	-- BOOLEAN  :   true | false
```
(see also: help-setting "verbose", "help-setting") For related topics.

**Verbose Setting:**

This settings indicates whether or not you want to view tweets text and additional information such as like,retweets,sentiment analysis, among others on the console, depending of function outputs. 

###### Usage: 
```
-- config-verbose false   sets verbose to false, doesn't let information of tweets to be shown on the console

-- config-verbose true    sets verbose to true, let's information of tweets to be shown on the console
```
###### Parameters:
```
	--  BOOLEAN     true | false
```
(see also: help-setting "datalog", "help-setting") For related topics.
  
  
