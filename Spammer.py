import time  # adds time module
import keyboard  # adds keyboard module

i = 0  # declares a variable called i which has a value of 0


def main():  # function main
    global i  # ok
    spam = input("What do you wanna spam?: ")  # asks what you wanna spam
    if spam.lower() == "sex":  # if input of spam is equal to sex then
        print("haram")  # print haram
        main()  # calls the function main which basically restarts the code
    spam_times = int(input("How many times do you wanna say this phrase: "))  # pretty obvious
    time.sleep(1)  # waits for 1 second then does the code under it
    TimeToSleep = int(input("Enter the time (in seconds) you need to select textbar: "))  # pretty obvious
    time.sleep(TimeToSleep)  # waits for the amount of time given from input

    while i < spam_times:  # while loop: while i is less than spam_times then
        i += 1  # increase i by 1
        keyboard.write(spam)  # write the desiered spam (except sex)
        keyboard.send("enter")# presses enter
    
    print("Done!!")
    time.sleep(1.5)    
    
    restart = input("Do you wanna restart y/n: ")  # asks if you wanna restart
    if restart.lower() == "y":  # if restart equal to y then it calls main and restarts
        main()
    else:  # else it just closes
        print("Ok bye!!")
        time.sleep(1.0)


main()  # calls main to start all of this