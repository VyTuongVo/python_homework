# Write your code here.

# Task 1: Hello
def hello ():
    return "Hello!"
#task1()  # Self Test

###########################################################################

#Task 2: Greet With Formatted String

def greet(name):
    return f"Hello, {name}!"

#greet("Name")  # Self Test

###########################################################################

#Task 3: Calculator

def calc(x: int, y: int, z: str = "multiply"):
    try: 
        ans = 0
        if z == "add": 
            ans = x + y
        elif z == "subtract":
            ans = x - y
        elif z == "multiply":
            ans = x * y
        elif z == "divide": 
            ans = x/y
        elif z == "modulo":
            ans = x % y
        elif z == "int_divide":
            ans = x//y
        else: 
            return "Invade Operation, Please Try Again"
        return ans
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError: 
        return "You can't multiply those values!"


#TEST DRIVE!!
#print(calculator(5, 6))  # == 30  # Default: multiply
#print(calculator(5, 6, "add"))  # == 11
#print(calculator(20, 5, "divide"))  # == 4.0
#print(calculator(14, 2.0, "multiply"))  # == 28.0
#print(calculator(12.6, 4.4, "subtract"))  # == 8.2
#print(calculator(9, 5, "modulo"))  # == 4
#print(calculator(10, 0, "divide"))  # == "You can't divide by 0!"
#print(calculator("first", "second", "multiply"))  # == "You can't multiply those values!"
#print(calculator(10, 0, "modulo"))  # == "You can't divide by 0!"
#print(calculator(10, 0, "int_divide"))  # == "You can't divide by 0!"
#print(calculator(10, 2, "int_divide"))  # == 5
#print(calculator(5, 3, "power"))  # == "Invalid Operation, Please Try Again"

#print("All tests passed!")

###########################################################################

#Task 4: Data Type Conversion

def data_type_conversion(value, type): 
    try:
        if type == "int":
            return int(value)
        elif type == "str":
            return str(value)
        elif type == "float":
            return float(value)
        else:
            return f"Invalid data type requested of {type}"
    except ValueError: 
        return f"You can't convert {value} into a {type}."
    except TypeError: 
        return f"Invalid type: {value} cannot be converted to {type}."
    
#print(data_type_conversion("110", "int"))  # Expected: 110 (int)
#print(data_type_conversion("5.5", "float"))  # Expected: 5.5 (float)
#print(data_type_conversion(7, "float"))  # Expected: 7.0 (float)
#print(data_type_conversion(91.1, "str"))  # Expected: "91.1" (str)
#print(data_type_conversion("banana", "int"))  # Expected: "You can't convert banana into a int."
#print(data_type_conversion(None, "int"))  # Expected: "Invalid type: None cannot be converted to int."

###########################################################################

#Task 5: Grading system, Using *args

#Comment for self, * args allows you to put in list or multiple values

def grade(*args):
    try:
        my_list = []
        for i in args:
            my_list.append(float(i)) 
        
        average = sum(my_list) / len(my_list)  


        if average >= 90:
            return "A"
        elif 89 >= average >= 80:
            return "B"
        elif 79 >= average >= 70:
            return "C"
        elif 69 >= average >= 60:
            return "D"
        else:
            return "F"
    except ValueError:
        return "Invalid data was provided."
    except TypeError:
        return "Invalid data was provided."

#result = grade(75, 85, 95)
#print(result)  # Expected: "B"

#result = grade("three", "blind", "mice")
#print(result)  # Expected: "Invalid data was provided."

###########################################################################

#Task 6: Use a For Loop with a Range

def repeat (string, count):
    my_list = []
    for i in range(count):
        my_list.append(string)
        #print(my_list)
    return ''.join(my_list)

#result = repeat("up,", 4)
#print(result)  # Expected: "up,up,up,up,"


###########################################################################

#Task 7: Student Scores, Using **kwargs

## **kwagrs: allow you to do mom = 24, dad = 42, and so on... and find infor from that

def student_scores (parameter, **kwargs):
    if parameter == "best":
        return max(kwargs, key=kwargs.get)  
    elif parameter == "mean":
        return sum(kwargs.values()) / len(kwargs)  
    else:
        return "Invalid parameter added."


#result = student_scores("mean", Tom=75, Dick=89, Angela=91)
#assert result == (75 + 89 + 91) / 3
#print(result)  # Expected: (75 + 89 + 91) / 3 = 85.0

#result = student_scores("best", Tom=75, Dick=89, Angela=91, Frank=50)
#assert result == "Angela"
#print(result)  # Expected: "Angela"

###########################################################################

#Task 8: Titleize, with String and List Operations

def titleize (title: str):
    little_word = ["a", "on", "an", "the", "of", "and", "is", "in"]
    title= title.lower().split()

    for i in range(len(title)):  
        if i == 0:  # Cap First word
            title[i] = title[i].capitalize()

        if i == len(title) - 1:  # Cap Last word
            title[i] = title[i].capitalize()
        
        # Capitalize non-little words
        if title[i] not in little_word:
            title[i] = title[i].capitalize()
    return " ".join(title)

#Or another way using for i, word in enumerate(words):

def titleize(title: str):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = title.lower().split()  
    
    for i, word in enumerate(words):
        if i == 0:  
            words[i] = words[i].capitalize()
            
        if i == len(words) - 1:
            words[i] = words[i].capitalize()
        
        if words[i] not in little_words:
            words[i] = words[i].capitalize()

    return " ".join(words) 

#result = titleize("war and peace")
#assert result == "War and Peace"
#print(result)  # Expected: "War and Peace"

#result = titleize("a separate peace")
#assert result == "A Separate Peace"
#print(result)  # Expected: "A Separate Peace"

#result = titleize("after on")
#assert result == "After On"
#print(result)  # Expected: "After On"


###########################################################################

#Task 9: Hangman, with more String Operations

def hangman(secret: str, guess: str):
    ## I would first making everything "_______"
    empty_list = []
    for i in range(len(secret)):
        empty_list.append("_")
    
    ## I then would look at avaible in secret and if they match up with guess, it will replace ___
    for i in range(len(secret)):
        if secret[i] in guess:
            empty_list[i] = secret[i] 
    return "".join(empty_list)

#result = hangman("difficulty", "ic")
#assert result == "_i__ic____"
#print(result)  # Expected: "_i__ic____"

result = hangman("alphabet", "ab")
#print(result)  # Expected: "a___ab__"


###########################################################################

#Task 10: Pig Latin, Another String Manipulation Exercise

def pig_latin(a_string: str):
    orginal = a_string.split()
    vowel = ["a", "e", "i", "o", "u"]

    result = []   # to return final answer
    for i in range(len(orginal)):   # for sentences
        current_orginal = list(orginal[i])  
        if current_orginal[0] in vowel:
            result.append("".join(current_orginal) + "ay")  
        else:
            i = 0  
            while i < len(current_orginal):
                if current_orginal[0] in vowel:
                    result.append("".join(current_orginal) + "ay") 
                    break  # skip going into next elif

                elif current_orginal[0] == "q" and len(current_orginal) > 1 and current_orginal[1] == "u":
                    current_letter_q = current_orginal.pop(0) 
                    current_letter_u = current_orginal.pop(0)  
                    current_orginal.append(current_letter_q)  
                    current_orginal.append(current_letter_u)  
                    continue  # skip going into next elif

                elif current_orginal[0] not in vowel:
                    current_letter = current_orginal.pop(0) 
                    current_orginal.append(current_letter)  

                i = i + 1  


    return " ".join(result) 


            

#result = pig_latin("apple")
#assert result == "appleay"
#print(result)  # Expected: "appleay"

#result = pig_latin("banana")
#assert result == "ananabay"
#print(result)  # Expected: "ananabay"

#result = pig_latin("cherry")
#assert result == "errychay"
#print(result)  # Expected: "errychay"

#result = pig_latin("quiet")
#assert result == "ietquay"
#print(result)  # Expected: "ietquay"

#result = pig_latin("square")
#assert result == "aresquay"
#print(result)  # Expected: "aresquay"


#result = pig_latin("the quick brown fox")
#assert result == "aresquay"
#print(result)  # Expected: "ethay ickquay ownbray oxfay"