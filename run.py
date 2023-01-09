import random

name = ""
prompt_user = ""
response_greet = ""
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

    #check for the tone of response
    if check_tone():
        print("ok")
    else:
        choose_topic()
     

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
    global response_greet
    my_file = open(GREET_FILE)
    content = my_file.read()
    my_file.close()
    
    greet_phrases = content.split("\n")
    selected_greet_phrase = greet_phrases[random.randrange(len(greet_phrases))]

    print(f"{prompt_computer} {selected_greet_phrase} {name}. How are you?\n")
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
    selected_topic = topics[random.randrange(len(topics))]
    print(selected_topic)
    
    if selected_topic == "work":
        # Call work function
        work_chat()
    elif selected_topic == "life":
        # Call life topics
        life_chat()
    elif selected_topic == "family":
        # Call family topics
        family_chat()
    else:
        # Call school topics
        school_chat()


def work_chat():
    """
    Talk about work related activities
    """
    print(work_lines)
    #random.randrange(len(greet_phrases))]

    #print(f"{prompt_computer} {selected_greet_phrase} {name}. How are you?\n")
    #response_greet = input(f"{prompt_user}")


def life_chat():
    print("life_lines")


def family_chat():
    print(family_lines)


def school_chat():

    school_chat_activated = True
    
    print(f"{prompt_computer} Are you a student?")
    response = input(f"{prompt_user}")
    yes_lines = ['yes', 'yeah', 'y', 'ofcourse', 'yeap']
    no_lines = ['no', 'nope', 'not', 'ain\'t']

    for word in yes_lines:
        if response.find(word) >= 0:
            #proceed
            print(f"{prompt_computer} What is the name of the institution?")
            response = input(f"{prompt_user}")
        
    for word in no_lines:
        if response.find(word) >= 0:
            #proceed to next random topic
            print("another topic")
            response = input(f"{prompt_user}")    

        


    print(f"{prompt_computer} {school_lines[1]}")
    response_greet = input(f"{prompt_user}")


def negative_greet():
    """
    Response to negative greeting
    """


def neutral_greet():
    """
    Response to neutral greeting
    """

    
main()
