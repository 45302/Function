#Alexander Allan
#09/12/2014
#Functions Spot Check (1)

def Input_Password():
    Entered_Password = input("Password: ")
    Password_Length = len(Entered_Password)
    return (Password_Length)

def Password_Calculation(Password_Length):
    Password = "False"
    while Password is "False":
        Input_Password()
        if Password_Length < 8:
            print("Password is too short!")
        elif Password_Length >16:
            print("Password is too long")
        else:
            print("Password accepted")
            Password = "True"

#Main Program
Password_Calculation(Password_Length)
