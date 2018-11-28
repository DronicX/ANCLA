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
       -> Print
       -> Average
 ```
 - [x] Analysis
 ```
       -> Competitiveness
       -> Lexical
       -> Sentiment
 ```
 - [x] Graphical Results
  

## :anchor: Configurations

Configurations in ANCLA are a tool or medium to make your programming enviroment more comfortable, offering a variety of settings to change at your dispossal to ease the coding experience. 

**+ Generic Helper Setting:**
 
Default setting that gives information of all other settings and configurations

###### Usage: 
```
-- help-setting
	> Gives a generic definition of the configurations or settings that can be changed in ANCLA
```
###### Parameters:
```
	NULL
```
(see also: help-setting "verbose", help-setting "datalog")

**+ Datalog Setting:**

This settings indicates whether or not you want to save in a file log the output of the functions that the user is using for analysis.

###### Usage: 
```
-- config-datalog false    
        > sets datalog to false, not letting the data collected to be stored on a log file

-- config-datalog true     
       > sets datalog to true, letting the data collected on console to be saved or stored on a log file
```
###### Parameters:
```
	-- BOOLEAN  :   true | false
```
(see also: help-setting "verbose", "help-setting") For related topics.

**+ Verbose Setting:**

This settings indicates whether or not you want to view tweets text and additional information such as like,retweets,sentiment analysis, among others on the console, depending of function outputs. 

###### Usage: 
```
-- config-verbose false   
	> sets verbose to false, doesn't let information of tweets to be shown on the console

-- config-verbose true    
	> sets verbose to true, let's information of tweets to be shown on the console
```
###### Parameters:
```
	--  BOOLEAN :   true | false
```
(see also: help-setting "datalog", "help-setting") For related topics.
  
## :anchor: Functions

**+ Generic Helper Function:**
 
The help-function in ANCLA is a useful function call that displays a guide to know which functions are available. There are general descriptions to know what each function does, and several call suggestion in depth description of specific functions.

###### Usage: 
```
-- help-function
	> Gives a generic definition of the functions available in ANCLA
```
###### Parameters:
```
	NULL
```
(see also: help-function "print" , help-function "average")

 **+ Print Function:**

The print function prints a specified characteristic or all characteristics of a set of tweets.

###### Usage: 
```
-- print([ACTION]).VARIABLE*    
        > Sample Call: print(search-tweets "Text" 100).faves
```
###### Parameters:
```
  -- Required :     ACTION speficied ACTION to retrieve tweets (i.e. search)
  -- Optional :     VARIABLE variable to print per tweet (i.e. faves)
```
(see also: help-function "print", "help-function") For related topics.

**+ Average Function:**

The average function calculates the average of all quantifiable or a specified quantifiable variable.

###### Usage: 
```
-- average([ACTION]).variable   
	> Sample Call: 
```
###### Parameters:
```
  -- Required :     ACTION speficied ACTION to retrieve tweets (i.e. search)
  -- Optional :     VARIABLE variable to print per tweet (i.e. faves)
```
(see also: help-function "average", "help-function") For related topics.

## :anchor: Analysis

**+ Analysis Helper Function:**
 
The help-action in ANCLA is a useful action call that displays a guide to know which actions are available. There are general descriptions to know what each action does, and several call suggestion to more in depth description of specific actions.

###### Usage: 
```
-- help-action
	> Gives a generic definition of the actions or analysis available in ANCLA
```
###### Parameters:
```
	NULL
```
(see also: help-action "analyze-sentiment" , help-action "live-sentiment")

 **+ Analyze Sentiment:**

The analyze-sentiment action uses TextBlob's sentiment analysis implementation to determine the attitude of the author of a text with respect to some specified topic. The implementtion uses a polarity score, which is a float from -1 to 1. It signifies the emotion expressed in the text. It can be positive, negative or neutral. One being positive, 0 neutral, and negative -1.

###### Usage: 
```
-- analyze-sentiment ["STRING"] [NUMBER]* [NUMBER]*    
        > Sample Call: analyze-sentiment "Donald Trump" 100 10
```
###### Parameters:
```
  -- Required :     STRING specified text to retrieve tweets that contain it
  -- Optional :     NUMBER quantity of tweets to be retrieved
  -- Optional :     NUMBER quantity of tweets per backup
```
###### Related Graph:
![static-sentiment](https://user-images.githubusercontent.com/5660320/49119532-0a289400-f27f-11e8-9f1a-5cc4cb8a0773.png)

(see also: help-action "analyze-sentiment", "help-action") For related topics.

**+ Live Sentiment:**

The live-sentiment action uses TextBlob's sentiment analysis implementation to determine the attitude of the author of a text with respect to some specified topic. It also uses Tweepy's live streaming API to retrieve Tweets in real time. The implementtion uses a polarity score, which is a float from -1 to 1. It signifies the emotion expressed in the text. It can be positive, negative or neutral. One being positive, 0 neutral, and negative -1.

The call generates a scatter plot of the polarity of all the tweets: positive in blue, negative in red, and the sum of both in purple.

###### Usage: 
```
-- live-sentiment ["STRING"] [NUMBER]* [NUMBER]* [NUMBER]*   
	> Sample Call: 
```
###### Parameters:
```
  -- Required :     STRING specified text to retrieve tweets that contain it
  -- Optional :     NUMBER quantity of tweets to be retrieved
  -- Optional :     NUMBER time in seconds before program stops running
  -- Optional :     NUMBER quantity of tweets per backup
```
###### Related Graph:
![live-sentiment](https://user-images.githubusercontent.com/5660320/49121341-807cc480-f286-11e8-859d-5b16be6d6b47.png)

(see also: help-action "live-sentiment", "help-action") For related topics.

**+ Lexical Diversity:**

Mathematically, the lexical diversity is an expression of the number of unique tokens in the text divided by the total number of tokens in the text. Lexical Diversity is a quantitative measure of an individual's or group's vocabulary.

The call generates a scatter plot of the individual lexical diversity value of each tweet.

###### Usage: 
```
-- analyze-lexical ["STRING"] [NUMBER]*   
	> Sample Call: analyze-lexical "Coca Cola" 50
```
###### Parameters:
```
  -- Required :     STRING specified text to retrieve tweets that contain it
  -- Optional :     NUMBER quantity of tweets to be retrieved
```
###### Related Graph:
![lexical-diversity](https://user-images.githubusercontent.com/5660320/49120031-61c7ff00-f281-11e8-8a9f-f9af84c86cc0.png)

(see also: help-action "live-sentiment", "help-action") For related topics.

**+ Competitiveness Analysis:**

Compare the number of Followers, Tweets, Favorites and Friends of two specified Twitter users.

###### Usage: 
```
-- analyze-competitor @USER @USER   
	> Sample Call: analyze-competitor @katyperry @justinbieber 
```
###### Parameters:
```
  -- Required :     USER First Twitter user to compare
  -- Required :     USER Twitter user to compare with
```
###### Related Ouput:
![competitor](https://user-images.githubusercontent.com/5660320/49120916-06980b80-f285-11e8-9233-51f568dc514f.png)

(see also: help-action "analyze-competitor", "help-action") For related topics.
## :anchor: Demo
## :anchor: About Us
## :anchor: Future Plans
- **The inclusion of several social media to our platform: Facebook, Instagram, etc. :computer:**
- **The integration or adaptation of multilines of code implementation**
- **:anchor: ANCLA IDE:**
- ![beta gui ancla](https://user-images.githubusercontent.com/5660320/49120932-157ebe00-f285-11e8-93d6-8bec3d83c443.jpeg)
