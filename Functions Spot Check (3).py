#Alexander Allan
#09/12/2014
#Functions Spot Check (3)

#Functions

def Get_Input():
    Journey_Distance = int(input("Distance (miles): "))
    Miles_Per_Gallon = int(input("Miles per gallon: "))
    Price_Of_Fuel = int(input("Cost of fuel (litres and pence): "))
    return(Journey_Distance,Miles_Per_Gallon,Price_Of_Fuel)

def Calculate_Cost(Journey_Distance,Miles_Per_Gallon,Price_Of_Fuel):
    #4.55 litres = 1 gallon
    
