#Alexander Allan
#09/12/2014
#Functions Spot Check (1)

Password = "False"

while Password is "False":
    Entered_Password = input("Password: ")
    Password_Length = len(Entered_Password)
    if Password_Length < 8:
        print("Password is too short!")
    elif Password_Length >16:
        print("Password is too long")
    else:
        print("Password accepted")
        Password = "True"
exit()
