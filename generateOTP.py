# Header comments
from random import randrange

def generateOTP(maxDigit, length=6):
    pass  # Your code for generating OTP goes here

def main():
    # Generate the OTP
    OTP = ""  # empty string
    maxDigit = 9
    user
    
    
    
    OTP = " "
    
    while userOTP != OTP and userOTP != "quit":
        x = 0
        while x < 6:
            OTP += str(randrange(0, maxDigit + 1))  # 2nd arg value not included
            x += 1
        print("Your OTP is " + OTP + ".")
        
        # Get user input
        userOTP = input("Enter your OTP: ")
        counter = 1
        
        while userOTP != OTP and counter < 3:
            userOTP = input("Incorrect OTP. Enter your OTP: ")
            counter += 1
        
        if userOTP == OTP:  # Matches
            print("Access is granted!")
        elif counter == 3:
            print("Incorrect OTP entered 3 times. Generating a new OTP.")

if __name__ == "__main__":
    main()
