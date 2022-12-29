import random

name = ""
prompt_user = ""
prompt_computer = "Kedi>>>"

GREET_FILE = "greetings.txt"
FAMILY_FILE = "family_lines.txt"
WORK_FILE = "work_lines.txt"
SCHOOL_FILE = "school_lines.txt"


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
    global prompt_user
    print("Hi my name is Kedi. what is your name?\n")
    name = input(">>>")
    prompt_user = f"{name}>>>"


def greet():
    """
    Greet the participant with a random line
    """
    my_file = open(GREET_FILE)
    content = my_file.read()
    my_file.close()
    
    greet_phrases = content.split("\n")
    selected_greet_phrase = greet_phrases[random.randrange(len(greet_phrases))]

    print(f"{prompt_computer} {selected_greet_phrase} {name}. How are you?\n")
    response_tone = input(f"{prompt_user}")

    print(response_tone)


    


def positive_greet():
    """
    Response to positive greeting. ask about either work, studies or family
    """
    # Choose topic
    topics = ["work", "life", "family"]
    selected_topic = topics[random.randrange(len(topics))]
    print(selected_topic)


def negative_greet():
    """
    Response to negative greeting
    """


def neutral_greet():
    """
    Response to neutral greeting
    """

    
main()
