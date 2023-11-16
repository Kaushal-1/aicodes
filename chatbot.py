import os
import time
import subprocess


def wish_me():
    current_time = time.localtime()
    if current_time.tm_hour < 12:
        print("Good Morning Sir")

    elif 12 <= current_time.tm_hour < 17:
        print("Good Afternoon Sir")

    else:
        print("Good Evening Sir")


def get_date_time():
    current_time = time.ctime()
    print("The date and time is:")
    print(current_time)

def main():
#if __name__ == "__main__":
    print("\t\t\t<============================= W E L C O M E =============================>")
    print("\t\t\t<============================= I'M A VIRTUAL ASSISTANT =============================>")

    password = input("Enter your password: ")

    while password != "chauhan":
        print(
            "\n<======================================================================= ===========================>\n")
        print("\t\t<============================= W E L C O M E =============================>")
        print("\t\t<============================= I'M VIRTUAL ASSISTANT =============================>")
        print("\n=======================")
        print("| Incorrect Password |")
        print("=======================")
        password = input("\nEnter your password: ")
        print(
            "\n<======================================================================= ===========================>\n")

    wish_me()

    while True:
        print(
            "\n<======================================================================= ===========================>\n")
        user_input = input("\nHow can I help you, sir: ")

        if user_input.lower() in ["hi", "hey", "hello"]:
            print("Hello Sir...")
            os.system("espeak 'Hello Sir'")
        elif user_input.lower() in ["bye", "stop", "exit"]:
            print("Goodbye, sir. Have a nice day!")
            os.system("espeak 'Goodbye, sir. Have a nice day'")
            break
        elif user_input.lower() in ["who are you", "tell me about yourself", "about"]:
            print("I'm a virtual assistant created by Aditi!")
            os.system("espeak 'I am a virtual assistant created by Aditi'")
        elif user_input.lower() in ["how are you", "whatsup", "how is your day"]:
            print("I'm good, sir. Tell me, how can I help you?")
            os.system("espeak 'I'm good, sir. Tell me, how can I help you'")
        elif user_input.lower() in ["time", "date"]:
            get_date_time()
        elif user_input.lower() == "open notepad":
            print("Opening Notepad...")
            os.system("espeak 'Opening Notepad'")
            subprocess.Popen(["notepad.exe"])


        '''elif user_input.lower() == "open google":
            print("Opening Google...")
            os.system("espeak 'Opening Google'")
            subprocess.Popen(["start", "https://www.google.com"])
        elif user_input.lower() == "open youtube":
            print("Opening YouTube...")
            os.system("espeak 'Opening YouTube'")
            subprocess.Popen(["start", "https://www.youtube.com"])
        elif user_input.lower() == "open instagram":
            print("Opening Instagram...")
            os.system("espeak 'Opening Instagram'")
            subprocess.Popen(["start", "https://www.instagram.com"])
        else:
            print("Sorry, I could not understand your query. Please try again!")
            os.system("espeak 'Sorry, I could not understand your query. Please try again'")'''
main()
