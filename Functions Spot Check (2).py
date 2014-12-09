# define functions def GetGridRow(aRowLength):
# draws a single row using |_ for each square thisRow = '|_' * (aRowLength)
# add closing | to row thisRow = thisRow + '|' return thisRow def DisplayGrid(aGridSize, aRow):
# display top of grid using _ as top of each square print(' _' * aGridSize)
# display rows of |_| for each row for rowCount in range(aGridSize): print(aRow)
# main program rowToDraw = GetGridRow(5) DisplayGrid(5, rowToDraw)

def Grid_Size_Input():
    GridSize = int(input("Please enter the size of the grid (max 20): "))
    return(GridSize)
def Printing_Of_Grid(GridSize):
    Top = "_"
    Rest = "|_"
    End = "|"

