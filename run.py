import random
import re

name = ""
sex = ""
prompt_user = ""
response_greet = ""
prompt_computer = '\033[94m' + "\nK-Bot >>> " + '\033[0m'
school_chat_completed = False
validator = True

GREET_FILE = "./resources/question_pool/greeting/greetings.txt"
BYE_FILE = "./resources/question_pool/greeting/bye.txt"
LIFE_FILE = "./resources/question_pool/life/life_lines.txt"
FAMILY_FILE = "./resources/question_pool/family/family_lines.txt"
WORK_FILE = "./resources/question_pool/work/work_lines.txt"
SCHOOL_FILE = "./resources/question_pool/school/school_lines.txt"
SWEAR_FILE = "./resources/question_pool/life/swear.txt"


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
    global greet_lines, bye_lines, family_lines, work_lines, school_lines, swear_lines, life_lines

    #load all files and contents
    greet_file = open(GREET_FILE)
    greet_content = greet_file.read()
    greet_file.close()
    greet_lines = greet_content.split("\n")

    family_file = open(FAMILY_FILE)
    family_content = family_file.read()
    family_file.close()
    family_lines = family_content.split("\n")

    bye_file = open(BYE_FILE)
    bye_content = bye_file.read()
    bye_file.close()
    bye_lines = bye_content.split("\n")

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

    global name, sex, salute
    global prompt_user

    print('\033[33m' + "\n\n********************************************************************\n" + 
        "This is a chat bot with limited AI capability. \nThe program does not limit your responses to specific words. \nPlease express your answers freely and keep you responses as brief as possible for better results\n" + "********************************************************************\n" + '\033[0m')

    print("Hi my name is K-BOT. what is your name?")
    name = input(">>> ")
   
    global validator
    while (validator):
        print("How should I address you? (1)Ms or (2)Mr?")
        salute_chk = input(">>> ")
        
        if re.search("1", salute_chk) or re.search("ms", salute_chk, re.IGNORECASE):
            salute = "Ms."
            validator = False
        elif re.search("2", salute_chk) or re.search("mr", salute_chk, re.IGNORECASE):
            salute = "Mr."
            validator = False
        else:
            print("Response not understood. Please re-phrase.")

    prompt_user = '\033[32m' + f"{salute} {name} >>> " + '\033[0m'


def greet():
    """
    Greet the participant with a random line
    """
    global response_greet
    selected_greet_phrase = greet_lines[random.randrange(len(greet_lines))]

    print(f"{prompt_computer} {selected_greet_phrase} {salute } {name}. How are you?")
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
            elif choice == "school":
                # Call school topics
                chat("school", school_lines, "Are you a student?")

        except Exception:
            print("Error in selecting topics. Contact Administrator.")

    selected_bye_phrase = bye_lines[random.randrange(len(bye_lines))]
    print(f"\n\nIt was nice knowing you {salute} {name}\n {selected_bye_phrase}")
    

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


main()
