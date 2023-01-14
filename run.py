import random
import re

name = ""
prompt_user = ""
response_greet = ""
prompt_computer = '\033[94m' + "\nK-Bot >>> " + '\033[0m'
school_chat_completed = False
validator = True

GREET_FILE = "./resources/question_pool/greeting/greetings.txt"
BYE_FILE = "./resources/question_pool/greeting/bye.txt"
LIFE_FILE = "./resources/question_pool/life/life_lines.txt"
FAMILY_FILE_MR = "./resources/question_pool/family/family_lines_mr.txt"
FAMILY_FILE_MS = "./resources/question_pool/family/family_lines_ms.txt"
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
    global greet_lines, bye_lines, family_lines_ms, family_lines_mr, work_lines, school_lines, swear_lines, life_lines

    #load all files and contents
    greet_file = open(GREET_FILE)
    greet_content = greet_file.read()
    greet_file.close()
    greet_lines = greet_content.split("\n")

    family_file_mr = open(FAMILY_FILE_MR)
    family_content_mr = family_file_mr.read()
    family_file_mr.close()
    family_lines_mr = family_content_mr.split("\n")

    family_file_ms = open(FAMILY_FILE_MS)
    family_content_ms = family_file_ms.read()
    family_file_ms.close()
    family_lines_ms = family_content_ms.split("\n")

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

    global name, salute, prompt_user

    print('\033[33m' + "\n\n********************************************************************\n" + 
        "This is a chat bot with limited AI capability. \nThe program does not limit your responses to specific words. \nPlease express your answers freely and keep you responses as brief as possible for better results\n" + "********************************************************************\n" + '\033[0m')

    while name == "":
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
                if re.search(salute, "mr.", re.IGNORECASE):
                    chat("family", family_lines_mr, "Are you married?")
                else:
                    print(salute)
                    chat("family", family_lines_ms, "Are you married?")

            elif choice == "school":
                # Call school topics
                chat("school", school_lines, "Are you a student?")

        except Exception:
            print("Error in selecting topics. Contact Administrator.")

    selected_bye_phrase = bye_lines[random.randrange(len(bye_lines))]
    print(f"\n\n{prompt_computer} It was nice knowing you {salute} {name}. {selected_bye_phrase}")
    

def chat(topic, lines, intro_qn):
    """
    Function to process all interactions related to work
    """
    
    print(f"{prompt_computer} {intro_qn}")
    response = input(f"{prompt_user}")

    if response == "":
        print(f"{prompt_computer} Come on don't be quiet :(")

    yes_lines = ['yes', 'yeah', 'y', 'ofcourse', 'yeap', 'good']
    no_lines = ['no', 'nope', 'not', 'ain\'t', 'unemployed']

    for word in no_lines:
        if re.search(word, response, re.IGNORECASE):
            #proceed to next random topic
            return 

    for word in yes_lines:
        if re.search(word, response, re.IGNORECASE):
            questions = set(lines)

            for qn in questions:
                try:
                    print(f"{prompt_computer} {qn}")
                    response = input(f"{prompt_user}")
                    if response == "":
                        print(f"{prompt_computer} Come on don't be quiet :(")
                    else:
                        check_figures(qn)

                except Exception:
                    print("Error in program. Please check your input.")


def check_figures(text):
    """
    Checks for numbers in responses
    """

    if re.search(text, "children do you have", re.IGNORECASE):
        result = re.findall(r'\d+', text)

        if result.__len__() < 1:
            print(f"{prompt_computer} Naaaaah, but let's move on :)")
        else:
            print(f"{prompt_computer} Amazing ...")
    
    if re.search(text, "long have you been married?", re.IGNORECASE):
        result = re.findall(r'\d+', text)
        if result.__len__() < 1:
            print(f"{prompt_computer} I know you are single :), but let's move on :)")
        else:
            print(f"{prompt_computer} Nice :)")

    if re.search(text, "did you graduate?", re.IGNORECASE):
        result = re.findall(r'\d+', text)
        if result.__len__() < 1:
            print(f"{prompt_computer} You lied :), but let's move on :)")
        else:
            print(f"{prompt_computer} Read hard mehn!!!")

    if re.search(text, "How long have you been working", re.IGNORECASE):
        result = re.findall(r'\d+', text)
        if result.__len__() < 1:
            print(f"{prompt_computer} You have not worked much :), but let's move on :)")
        else:
            print(f"{prompt_computer} Good job!!!")

main()
