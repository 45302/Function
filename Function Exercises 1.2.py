#Alexander Allan
#25/11/2014
#Functions Exercise 1.2

#Functions
def Stars():
    Star = "*"
    Triangle_Number = int(input("Please insert an odd number: "))
    Printed = (Star * Triangle_Number) 
    for Line_Counter in range(Triangle_Number):
        print("{0:^50}".format(Printed))
        Triangle_Number = (Triangle_Number - 2)
        Printed = (Star * Triangle_Number)     
Stars()
