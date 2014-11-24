#Alexander Allan
#24/11/2014
#Calculate Pay Program

#Define Functions
def Calculate_Basic_Pay(Hours,Rate):
    Total = (Hours * Rate)
    return Total

def Calculate_Overtime_Pay(Hours,Rate):
    Overtime_Hours = (Hours - 40)
    Overtime_Pay = (Overtime_Hours * Rate * 1.5)
    Basic_Pay = (40 * Rate)
    Total = (Overtime_Pay * Basic_Pay)
    return Total

def Calculate_Total_Pay(Hours,Rate):
    if Hours <= 40:
        Total = Calculate_Basic_Pay(Hours,Rate)
    else:
        Total = Calculate_Overtime_Pay(Hours,Rate)
    return Total
def Work_Information():
    Hours = int(input("Please enter the amount of hours you have worked: "))
    Rate = float(input("Please enter your rate of pay: £"))
    return Hours,Rate

def Display_Total_Pay(Hours,Rate,Total):
    print("Because you did {0} hours, and your rate of pay is {1}, you will be payed £{2}.".format(Hours,Rate,Total))

def Calculate_Pay(Hours,Rate):
    Hours, Rate = Work_Information()
    return Total

#Main Program
Hours,Rate = Work_Information()

Calculate_Total_Pay(Hours,Rate)

Calculate_Total_Pay(Hours,Rate)

Display_Total_Pay(Hours,Rate,Total)
