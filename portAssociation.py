# FoxAPT (Wes Miller)
# COP2002-0T2
# OCT 22, 2023
# Project5.py
# This program allows user to select preferred study methods to learn associated port names and port numbers as well as transition from studying methods by navigating to the menu and even exit the application. 


import random


def getRandomPort(portNumArray, portNameArray): # Function to get a random port and its associated protocol
    index = random.randint(0, len(portNumArray) - 1)
    return portNumArray[index], portNameArray[index]



def getInput(): # Function to get user input and ensure it's valid
    while True:
        userInput = input("Choice: ")
        if userInput in ["1", "2", "3", "m"]:
            return userInput
        else:
            print("Invalid input. Please enter 1, 2, 3, or 'm'.")


def option1(portNumArray, portNameArray): # Function for option 1: Identify the port's PROTOCOL
    print("Option 1: Identify the port's PROTOCOL.")
    print("----------------------------------------")
    while True:
        portNumber, correctProtocol = getRandomPort(portNumArray, portNameArray)
        userInput = input("\nWhat is the protocol for port {} (m=Main Menu)? ".format(portNumber))
        if userInput == "m":
            return
        if userInput == correctProtocol:
            print("Correct answer!")
        else:
            print("Incorrect. The correct answer is {}.".format(correctProtocol))


def option2(portNameArray, portNumArray): # Function for option 2: Identify the port's NUMBER
    print("Option 2: Identify the port's NUMBER.")
    print("----------------------------------------")
    while True:
        randomIndex = random.randint(0, len(portNameArray) - 1)
        randomProtocol = portNameArray[randomIndex] # Find all the port numbers associated with the random protocol
        associated_port_numbers = [portNumArray[i] for i, protocol in enumerate(portNameArray) if protocol == randomProtocol]
        userInput = input("\nWhat is the number for protocol {} (m=Main Menu)? ".format(randomProtocol))
        if userInput == "m":
            return
        if userInput in associated_port_numbers:
            print("Correct answer!")
        else:
            print("Incorrect. The correct answers are {}.".format(", ".join(associated_port_numbers)))


def main(): # Define the port numbers and their corresponding protocols
    portNumArray = ["20", "21", "22", "23", "25", "53", "67", "68", "80", "110", "137", "139", "143", "161", "162", "389", "443", "445", "3389"]
    portNameArray = ["FTP", "FTP", "SSH", "Telnet", "SMTP", "DNS", "DHCP", "HTTP", "HTTP", "POP3", "NetBIOS", "NetBIOS", "IMAP", "SNMP", "SNMP", "LDAP", "HTTPS", "SMB", "RDP"]

    while True: # Instructions for user to select how they prefer to study
        print("Main Menu:")
        print("1. Given a port number, identify the PROTOCOL (use abbreviation).")
        print("2. Given a port protocol, identify a port NUMBER.")
        print("3. Exit")
        choice = getInput()

        if choice == "1":
            option1(portNumArray, portNameArray)
        elif choice == "2":
            option2(portNameArray, portNumArray)
        elif choice == "3":
            print("Program Complete. I hope this has helped in studying for the CompTIA A+ certification.")
            return

if __name__ == "__main__": # Calling main fucntion
    main()
