import random
import re

name = ""
prompt_user = ""
response_greet = ""
prompt_computer = "\nComputer >>> "
school_chat_completed = False

GREET_FILE = "greetings.txt"
LIFE_FILE = "life_lines.txt"
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

    #check for the tone of response
    if check_tone():
        print("ok")
    else:
        choose_topic()
     

def start():
    """
    Start the chat
    """
    global greet_lines, family_lines, work_lines, school_lines, swear_lines, life_lines, negative_lines

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

    life_file = open(LIFE_FILE)
    life_content = life_file.read()
    life_file.close()
    life_lines = life_content.split("\n")

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

    print("Hi my name is Kedi. what is your name?")
    name = input(">>> ")
    prompt_user = f"{name} >>> "


def greet():
    """
    Greet the participant with a random line
    """
    global response_greet
    my_file = open(GREET_FILE)
    content = my_file.read()
    my_file.close()
    
    greet_phrases = content.split("\n")
    selected_greet_phrase = greet_phrases[random.randrange(len(greet_phrases))]

    print(f"{prompt_computer} {selected_greet_phrase} {name}. How are you?")
    response_greet = input(f"{prompt_user}")
    

def check_tone():
    """
    Check the tone of the response
    """
    global response_greet

    for swear_words in swear_lines:
        if response_greet.find(swear_words) >= 0:
            return True
        else:
            return False


def choose_topic():
    """
    Response to positive greeting. ask about either work, studies or family
    """
    # Choose topic
    topics = ["work", "life", "family", "school"]
    
    topic = set(topics)
    #topic_size = topics.__len__()

    #x = 0
    #while x < topic_size:
    for choice in topic:
        try:
            if choice == "work":
                # Call work function
                chat("work", work_lines, "Are you currently employed?")
            elif choice == "life":
                # Call life topics
                chat("life", life_lines, "In other news, how is life?")
            elif choice == "family":
                # Call family topics
                chat("family", family_lines, "Are you married?")
            else:
                # Call school topics
                chat("school", school_lines, "Are you a student?")
            #x = x + 1

        except Exception:
            print("Error in selecting topics. Contact Administrator.")
    

def chat(topic, lines, intro_qn):
    """
    Function to process all interactions related to work
    """
    
    print(f"{prompt_computer} {intro_qn}")
    response = input(f"{prompt_user}")
    yes_lines = ['yes', 'yeah', 'y', 'ofcourse', 'yeap', 'good']
    no_lines = ['no', 'nope', 'not', 'ain\'t', 'unemployed']

    for word in no_lines:
        if re.search(word, response, re.IGNORECASE):
            #proceed to next random topic
            return 

    for word in yes_lines:
        if re.search(word, response, re.IGNORECASE):
            questions = set(lines)
            qn_size = lines.__len__()

            x = 0
            while x < qn_size:
                try:
                    print(f"{prompt_computer} {questions.pop()}")
                    response = input(f"{prompt_user}")
                    x = x + 1

                except Exception:
                    print("Error in program. Please check your input.")

    

def negative_greet():
    """
    Response to negative greeting
    """


def neutral_greet():
    """
    Response to neutral greeting
    """

    
main()
