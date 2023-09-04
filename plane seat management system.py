#create class and iniatialize variable
class PlaneSeatPlan:
    def __init__(self, rows, cols):
        self.seat = []
        self.rows = rows
        self.cols = cols
    
    #function to create the 2d matrix for the seat plan
    def create_seat(self):  
        for row in range(9):
            row_data = []
            for col in range(9):
               row_data.append('*')
            self.seat.append(row_data)
        return self.seat
    
    #prints the seat plan created by the create_seat function
    def print_seat(self): 
        print('\t', end='')
        for col in range(self.cols):
            print(chr(65+col), end='\t')
        print()
        for i, row in enumerate(self.seat):
            print(f"Row {i + 1}: ", end='\t')
            print('\t'.join(row))

     #function to reserve seat
    def reserve_seat(self, row, col): 
        #check if the seat is in range
        if row < 1 or row > self.rows or col < 1 or col > self.cols: 
            print("Invalid seat!")

            #check if the seat is already reserved
        elif self.seat[row - 1][col - 1] == 'X': 
            print("Seat is already reserved!")

            #if not, reserved the seat and put an X to indicate reserved
        else:
            self.seat[row - 1][col - 1] = 'X'
            print(f"Seat {chr(65+row)} - {col} successfully reserved!")
        plane.print_seat()



plane = PlaneSeatPlan(9, 9)

#function call
plane.create_seat()
plane.print_seat()

#get user input for the row and col of seat they want
print("\nEnter the seat you want")
row = int(input("Seat Row you want: "))
col = int(input("Seat Column you want: "))

#pass the value of the user input to the reserve_Seat function
plane.reserve_seat(row, col)
