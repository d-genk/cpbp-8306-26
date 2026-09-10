lets start and keep it short  
  
Warm-up: What’s the difference between x = 5 and x == 5—and why does that distinction matter?  
  
One assigns and other checks if x is equal to 5.  
  
Exactly: one is a command, the other is a question. What do you predict Python does with if x = 10:?  
  
Error, Syntax error  
  
Yep, exactly. Problem 1: predict the types of a = 5, b = "5", c = 5.0, and d = True—what does type() return for each?  
  
int, string, float, boolean  
  
Right — Python calls those int, str, float, and bool. Now predict: a == c, a == b, and d == 1 — True or False for each?  
  
T, F, T  
  
Correct: True, False, True. Problem 2: if age_str = "42" and then result = age_str + 8, what do you predict: TypeError, "428", or 50?  
  
Typeerror  
  
Correct. Is Python refusing to guess here a good thing or a bad thing, and why?  
  
good otherwise it would mess up the result without the user being aware.   
  
Exactly—the error protects you from a silent wrong answer. What do you think whoever wrote it intended the result to be, and how would you fix the type mismatch?  
  
 turn the age_str into an integer  
  
Yep—if the intent is arithmetic, converting "42" to an integer makes sense. Problem 3: read the bottom line first—what is it actually complaining about?  
  
Traceback (most recent call last):  
  File "clean.py", line 27, in <module>  
    total = ages.sum() + max_age  
TypeError: unsupported operand type(s) for +: 'int' and 'str'  
There are different types: integer and string. So cannot be added together   
  
Exactly. Which of the two things being added do you think is the string, and how would you find out?  
  
Exactly—the AI could see the types, but not your intended meaning. What would you tell the AI in your prompt so it investigates the real bug instead of merely silencing the error?  
  
max_age is suppose to be an int  
  
Exactly. A stronger prompt would state that expectation and ask where the type changed. In one sentence: what’s the one thing about types you want to remember when using AI-written code?  
  
double check the type of every variable.   
  
Yep—that’s the core idea: check that types match what the variables are supposed to represent, not just that the code runs.  
  
Paste this conversation into the Session 2 participation assignment on Brightspace as-is.  
