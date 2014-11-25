#Alexander Allan
#25/11/2014
#Function Exercises 1.1

#Functions
def OutputSymbols():
    Amount_Of_Symbols = int(input("Please enter the amount of symbols you want on the line: "))
    Which_Symbol = input("Please insert the symbol you would like to be copied multiple times: ")
    Printed = Which_Symbol*Amount_Of_Symbols
    print(Printed)

#Main Program
OutputSymbols()
