import random

name = ""
prompt_user = f"/n{name}>>>"
prompt_computer = "Kedi>>>"

GREET_FILE = "greetings.txt"


def main():
    """
    Main function controlling access to all the other functions
    """
    start()
    greet()
     

def start():
    """
    Start the chat
    """
    global name
    print("Hi my name is Kedi. what is your name?\n")
    name = input(">>>")


def greet():
    """
    Greet the participant
    """
    my_file = open(GREET_FILE)
    content = my_file.read()
    my_file.close()
    
    greet_phrases = content.split("\n")
    selected_greet_phrase = greet_phrases[random.randrange(len(greet_phrases))]

    print(f"{selected_greet_phrase} {name} :)\n") 


def positive_greet():
    """
    Response to positive greeting
    """


def negative_greet():
    """
    Response to negative greeting
    """


def neutral_greet():
    """
    Response to neutral greeting
    """

    
main()
