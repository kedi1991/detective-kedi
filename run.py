import random

name = ""
prompt_user = ""
prompt_computer = "Kedi>>>"

GREET_FILE = "greetings.txt"
FAMILY_FILE = "family_lines.txt"
WORK_FILE = "work_lines.txt"
SCHOOL_FILE = "school_lines.txt"
SWEAR_FILE = "swear.txt"
POSITIVE_RESPONSE = "response_positive.txt"
NEGATIVE_RESPONSE = "response_negative.txt"


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
    global greet_lines, family_lines, work_lines, school_lines, swear_lines, positive_lines, negative_lines

    #load all files and contents
    greet_file = open(GREET_FILE)
    greet_content = greet_file.read()
    greet_file.close()
    greet_lines = greet_content.split("\n")

    family_file = open(FAMILY_FILE)
    family_content = family_file.read()
    family_file.close()
    family_lines = family_content.split("\n")

    work_file = open(WORK_FILE)
    work_content = work_file.read()
    work_file.close()
    work_lines = work_content.split("\n")

    school_file = open(SCHOOL_FILE)
    school_content = school_file.read()
    school_file.close()
    school_lines = school_content.split("\n")

    swear_file = open(SWEAR_FILE)
    swear_content = swear_file.read()
    swear_file.close()
    swear_lines = swear_content.split("\n")

    positive_file = open(POSITIVE_RESPONSE)
    positive_content = positive_file.read()
    positive_file.close()
    positive_lines = positive_content.split("\n")

    negative_file = open(NEGATIVE_RESPONSE)
    negative_content = negative_file.read()
    negative_file.close()
    negative_lines = negative_content.split("\n")


    global name
    global prompt_user
    print("Hi my name is Kedi. what is your name?\n")
    name = input(">>> ")
    prompt_user = f"{name}>>> "


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
    response_greet = input(f"{prompt_user}")

    #check response for positive, negative or abusive language
    for x in swear_lines:
        if (x in response_greet):
            print("come on ...")
        else:
            print("okay good!!!")



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
