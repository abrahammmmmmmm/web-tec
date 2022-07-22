def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    greeting = func("hi, i am created by a function \
                     passed as an argument")
        print(greeting)
        
        greet(shout)
        greet(whisper)
