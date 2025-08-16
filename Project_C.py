#Exercise 3 || Project 3


#Creating the kbc game
#Display the question and hidden the answer and give the point if user give the correct point
#Display amount after playing game user taken away

import random #This function take the random question 

question = [ #Here is the question which is in the list of python like list=[{a},{b},{c}]
   
    {
        "question": "1. What does HTML stand for?",
        "options": ["Hyper Trainer Marking Language", "Hyper Text Markup Language", "Hyper Text Marketing Language", "Hyper Tool Markup Language"],
        "answer": "Hyper Text Markup Language"
    },
    {
        "question": "2. Which one is a programming language?",
        "options": ["HTML", "CSS", "Python", "HTTP"],
        "answer": "Python"
    },



# Each question is stored as a dictionary with three parts:
# "question" -> the text of the question
# "options"  -> a list of possible answers
# "answer"   -> the correct answer
# This structure makes it easy to shuffle questions, display options, and check answers. 


    {
        "question": "3. What symbol is used for comments in Python?",
        "options": ["//", "#", "/* */", "<!-- -->"],
        "answer": "#"
    },
    {
        "question": "4. What is the correct file extension for Python files?",
        "options": [".pt", ".pyt", ".py", ".python"],
        "answer": ".py"
    },
    {
        "question": "5. Which keyword is used to define a function in Python?",
        "options": ["function", "def", "define", "fun"],
        "answer": "def"
    },
    {
        "question": "6. What is the output of: print(2 ** 3)?",
        "options": ["6", "8", "9", "5"],
        "answer": "8"
    },
    {
        "question": "7. Which of the following is a loop in Python?",
        "options": ["for", "repeat", "do", "loop"],
        "answer": "for"
    },
    {
        "question": "8. Which data type is used to store True/False values?",
        "options": ["int", "float", "str", "bool"],
        "answer": "bool"
    },
    {
        "question": "9. What will this return: len('hello')?",
        "options": ["4", "5", "6", "Error"],
        "answer": "5"
    },
    {
        "question": "10. What is used to import a module in Python?",
        "options": ["load", "import", "include", "require"],
        "answer": "import"
    },
    {
        "question": "11. Which data type is immutable in Python?",
        "options": ["list", "set", "tuple", "dictionary"],
        "answer": "tuple"
    },
    {
        "question": "12. What will be the output of: print(10 // 3)?",
        "options": ["3.3", "3", "3.0", "Error"],
        "answer": "3"
    },
    {
        "question": "13. Which operator is used to check equality?",
        "options": ["=", "==", "!=", "==="],
        "answer": "=="
    },
    {
        "question": "14. What does IDE stand for?",
        "options": ["Integrated Data Environment", "Internal Development Editor", "Integrated Development Environment", "Internet Design Engine"],
        "answer": "Integrated Development Environment"
    },
    {
        "question": "15. What is a variable?",
        "options": ["A keyword", "A constant value", "A named storage for data", "An operator"],
        "answer": "A named storage for data"
    },
    {
        "question": "16. What is the correct way to create a list in Python?",
        "options": ["list = (1, 2, 3)", "list = [1, 2, 3]", "list = {1, 2, 3}", "list = <1, 2, 3>"],
        "answer": "list = [1, 2, 3]"
    },
    {
        "question": "17. Which keyword is used for a conditional statement?",
        "options": ["if", "when", "check", "for"],
        "answer": "if"
    },
    {
        "question": "18. Which symbol is used for 'not equal to' in Python?",
        "options": ["!=", "<>", "!==", "not="],
        "answer": "!="
    },
    {
        "question": "19. What does the 'input()' function do?",
        "options": ["Outputs data", "Takes user input", "Declares a variable", "Creates a loop"],
        "answer": "Takes user input"
    },
    {
        "question": "20. What is the purpose of indentation in Python?",
        "options": ["To make code look pretty", "To separate statements", "To define blocks of code", "To comment code"],
        "answer": "To define blocks of code"
    },
    {
        "question":"21. Why Pytho is popular among developers?",
        "options":["Easy","Hard to use","Beginner Friendly","Worst"],
        "answer":"Beginner Friendly"
    }
]

#Extended question 

more_questions = [
    {"question": "22. What does 'len()' function do in Python?",
     "options": ["Returns the length of an object", "Adds two numbers", "Deletes an element", "Prints output"],
     "answer": "Returns the length of an object"},

    {"question": "23. Which of these is a Python keyword?",
     "options": ["var", "function", "while", "loop"],
     "answer": "while"},

    {"question": "24. Which operator is used for floor division in Python?",
     "options": ["/", "//", "%", "**"],
     "answer": "//"},

    {"question": "25. Which of these is a mutable data type?",
     "options": ["tuple", "string", "list", "int"],
     "answer": "list"},

    {"question": "26. How do you start a block of code in Python?",
     "options": ["With braces {}", "With indentation", "With brackets []", "With colon ;"],
     "answer": "With indentation"},

    {"question": "27. What does '==' mean in Python?",
     "options": ["Assignment", "Comparison for equality", "Not equal", "Exponent"],
     "answer": "Comparison for equality"},

    {"question": "28. Which of these is used to create a set?",
     "options": ["{}", "[]", "()", "<>"],
     "answer": "{}"},

    {"question": "29. What keyword is used to handle exceptions?",
     "options": ["try", "except", "catch", "handle"],
     "answer": "try"},

    {"question": "30. How to comment a single line in Python?",
     "options": ["//", "#", "/* */", "<!-- -->"],
     "answer": "#"},

    {"question": "31. Which function converts a string to an integer?",
     "options": ["int()", "str()", "float()", "convert()"],
     "answer": "int()"},

    {"question": "32. Which of these is a Python loop?",
     "options": ["for", "repeat", "loop", "do"],
     "answer": "for"},

    {"question": "33. Which symbol is used for 'not equal' in Python?",
     "options": ["!=", "<>", "==", "==="],
     "answer": "!="},

    {"question": "34. What is the correct way to define a function?",
     "options": ["function myFunc():", "def myFunc():", "define myFunc():", "fun myFunc():"],
     "answer": "def myFunc():"},

    {"question": "35. Which of these is used to access modules in Python?",
     "options": ["import", "include", "require", "load"],
     "answer": "import"},

    {"question": "36. How do you create a dictionary in Python?",
     "options": ["{}", "[]", "()", "<>"],
     "answer": "{}"},

    {"question": "37. Which of these is immutable?",
     "options": ["list", "tuple", "set", "dictionary"],
     "answer": "tuple"},

    {"question": "38. Which keyword is used for a conditional statement?",
     "options": ["if", "for", "while", "switch"],
     "answer": "if"},

    {"question": "39. What does 'input()' do?",
     "options": ["Prints output", "Takes user input", "Adds numbers", "Starts a loop"],
     "answer": "Takes user input"},

    {"question": "40. How do you start a Python file?",
     "options": ["import python", "def main():", "#!/usr/bin/python", "start()"],
     "answer": "#!/usr/bin/python"},

    {"question": "41. What is the output of 3 * 3 ** 2?",
     "options": ["27", "18", "9", "36"],
     "answer": "27"},

    {"question": "42. Which method adds an element to a list?",
     "options": ["append()", "add()", "insert()", "extend()"],
     "answer": "append()"},

    {"question": "43. Which keyword exits a loop prematurely?",
     "options": ["stop", "break", "exit", "continue"],
     "answer": "break"},

    {"question": "44. What does 'str()' do in Python?",
     "options": ["Converts to string", "Converts to integer", "Converts to float", "Deletes a string"],
     "answer": "Converts to string"},

    {"question": "45. How do you start a multiline comment?",
     "options": ["'''", "\"\"\"", "#", "//"],
     "answer": "\"\"\""},

    {"question": "46. Which symbol is used for exponentiation?",
     "options": ["^", "**", "%", "*"],
     "answer": "**"},

    {"question": "47. Which of these is NOT a Python data type?",
     "options": ["int", "float", "char", "bool"],
     "answer": "char"},

    {"question": "48. What is used to check membership in a list?",
     "options": ["in", "not in", "has", "exists"],
     "answer": "in"},

    {"question": "49. How do you delete a key from a dictionary?",
     "options": ["del dict[key]", "remove(dict[key])", "dict.pop(key)", "Both A and C"],
     "answer": "Both A and C"},

    {"question": "50. What is the output of type([1,2,3])?",
     "options": ["list", "tuple", "set", "dict"],
     "answer": "list"},

    {"question": "51. Which keyword creates a class in Python?",
     "options": ["class", "object", "def", "type"],
     "answer": "class"},

    {"question": "52. How to concatenate two strings?",
     "options": ["str1 + str2", "str1 & str2", "str1 . str2", "str1 * str2"],
     "answer": "str1 + str2"},

    {"question": "53. Which method removes whitespace from the start/end of a string?",
     "options": ["strip()", "trim()", "remove()", "delete()"],
     "answer": "strip()"},

    {"question": "54. What does 'range(5)' return?",
     "options": ["0 to 4", "1 to 5", "5 numbers starting from 1", "Error"],
     "answer": "0 to 4"},

    {"question": "55. Which symbol is used for modulus?",
     "options": ["%", "/", "**", "//"],
     "answer": "%"}
]

question.extend(more_questions) #extending the question by using     question.extend(variable)

male = ["ram","shyam","hari","krishna","abishek","aayush","ramesh","anas","sonu","sudip","unish","pankaj","gaurav","gaurab","shreekrishna"]                 #List of male 
female =["sita","gita","rita","reeta","geeta","sweeta","menuka","dipika","sunita","Kripa","kalpana"]                  
                       #List of female
prize_amounts = prize_amounts = [
    500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000,         # 1-10
    10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, # 11-20
    20000, 22000, 24000, 26000, 28000, 30000, 32000, 34000, 36000, 38000, # 21-30
    40000, 42000, 44000, 46000, 48000, 50000, 55000, 60000, 65000, 70000, # 31-40
    80000, 90000, 100000, 120000, 150000, 200000, 300000, 400000, 450000, 500000 # 41-50
]     #list of prize


name = input("Enter the participant first name only in lowcase:\n").lower().strip().replace(" ", "")                                                            #taking input  
print()
if name in male:                                                                                                                              #check if in male list have input name print this statement
    print("Hello Mr.",name,",","we are from the KBC India,we just want to ask you that do you want to play game")
elif name in female:
    print("Hello Mrs.",name,",","we are from the KBC India, we just want to ask you that do you want to play game")                           #check if in female list have input name print this statement
else:
    print("You cannot participant")                                                                                                             #if list dpesnot match with input show this
    exit()                                                                                                                                      #it simply exit the system cuz participant must within the list no ohers

elminate_names=[]
while True:                                                                                                                                     #Asking question infinite until the it find break statement
    print()
    ask = input("Do you want to enter the game Y/N: ");print()
    if ask == 'Y': #== compare the ask and input of the user Y/N
       print("Great, Let's Start the game");print()
       age =int(input("Enter your age: "));print()
       if(age<=16):                             #It doesnot take less than 17 and if less want play game eliminate system
           print("You cannot participent this game,Thankyou")
           break
       else:                                            #sause of the main file
            print("Great, Let's Start the game")
            random.shuffle(question)                    #This is used to shuffle or rearange the question in random way 
            score=0                                          
            question_count = 0                          #counting questions for user must consistence and also for giving prize

                #Each card = a dictionary with question + options + answer
                # for q in question: → pick one card at a time and do something with it (like show it to the player)

            for q in question:                             #goes through each question in your list, one by one.
             #question_count += 1                            #adds 1 to the counter every time a new question is asked. || Loop through each question, and increase question_count to track the current question number
             print("\n "+q["question"]);                       #print question from dictionary q=each and ["question"]


             options = q["options"].copy()                  # Make a copy of options so original list stays safe
             random.shuffle(options)                        # Shuffle options randomly for this question

             for i in range (4):                            # Print all 4 options for the player to choose from
              print(f"{i+1}.{options [i]}");

                    
             try:                                              #try catch like java in python try and except 
                choice=int(input("choose the option between 1-4: "))  #it take the option between 1 to 4
                if options[choice-1] == q["answer"]:                                                          #Python starting from 0 index while human 1 so choice is 1-1=0 in python 0 index and == to corect answer
                  print()
                  print("correct your score is increase by 50")                                              #encouraging the player
                  score+=50;                                                                                             #leveling up the player score when they give corrext answer
                  question_count += 1  # <-- Only increase question_count if correct 

                  
                  if question_count <= len(prize_amounts):                                              # If the current question number is within the prize list range      
     # Display the prize amount based on how many questions the user has answered correctly
    # We subtract 1 from question_count because lists in Python start at index 0     


                   print(f"You have won: ₹{prize_amounts[question_count-1]}") 

                     # Show how many questions the player has completed so far                
                   print("Question Complete: ",question_count)

                else:
                   # If the answer is wrong OR we've somehow gone beyond the prize list, show the correct answer
                  print(f"wrong answer correct one is a {q["answer"]}");  # 'q' is the current question answer
                  elminate_names.append(name)
                  print()
                  print("Dont give up",elminate_names)
                  break


             except: # If the user types something invalid (like a letter instead of a number), handle it here
                print("Invalid Input")
                break                                         # stop game on wrong answer
        


            print("\n quiz is over")
  # If the player got at least 1 question right and the question count is within the prize list range

            if question_count > 0 and question_count <= len(prize_amounts):                         #If the player got at least 1 answer right → show cash prize from the list.
             print(f"Your total prize amount is: ₹{prize_amounts[question_count-1]}")   
        
            else:
             print(f"Your total score is: {score}")                                                    # If they failed the first question → just show their score (0).

       
                
            '''
🔸 if question_count > 0

Means the user got at least 1 answer correct (because question_count is only increased for correct answers).

🔸 and question_count <= len(prize_amounts)

Makes sure you're not trying to access a prize that doesn't exist in the list.
            
            
            
            '''
               

        
    





































       break
    elif ask == 'N':
        print("Maybe next time. Thank you for your time!")
        break
    else:
     print("Please give answer between Y/N")