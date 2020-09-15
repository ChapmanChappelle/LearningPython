import datetime as dt

#fields
cost = (30/3600)


#table (holds pool table info)
class Table: 
    def __init__(self, table_num, cost):
        self.table_num = table_num
        self.start_time = 0
        self.end_time = 0
        self.cost = cost
        self.status = False

    def display_table(self):
        if(self.status == True):
            print(f"Table {self.table_num+1}: OCCUPIED")
            print(f"Time start: {self.start_time}")
        else:
            print(f"Table {self.table_num+1}: UNOCCUPIED")

    def open_table(self):
        self.status = True
        self.start_time = dt.datetime.now()
        print(f"Table {self.table_num+1} is now occupied")
        print(f"Start time is {self.start_time}")

    def close_table(self):
        self.status = False
        time_diff = (dt.datetime.now() - self.start_time)
        diff = time_diff.total_seconds()
        print(f"Total Cost of table: ${str(round(self.cost*diff , 2))}")
        if(diff >= 60 and diff <= 3600):
            print(f"Table {self.table_num+1} is unoccupied again after {str(round((diff/60) , 2))} minutes")
        elif(diff < 60):
            print(f"Table {self.table_num+1} is unoccupied again after {str(round(diff , 2))} seconds")
        elif(diff >= 3600):
            print(f"Table {self.table_num+1} is unoccupied again after {str(round( (diff/3600) , 2)) } hours")
        else:
            print("ERROR")



#menu
def menu():
    print ("""
    1.Display all tables
    2.Look at an individual table
    3.Start a table
    4.Close out a table
    5.Exit
    """)
    choice = input("Choose an option: ") 
    if choice == "1": 
        print("\nDisplaying tables....") 
        for obj in room:
                obj.display_table()
    elif choice == "2":
         user_input = int(input("Which table? "))
         room[user_input-1].display_table()
    elif choice == "3":
        user_input = int(input("Which table? "))
        room[user_input-1].open_table()
    elif choice == "4":
        user_input = int(input("Which table? "))
        room[user_input-1].close_table()
    elif choice == "5":
        print("\nSee you later!") 
        quit()
    elif choice !="":
        print("\nInvalid Imput") 
    menu()

#creating room of 12 tables  
room = []
for i in range(0,12):
    room.append(Table(i, cost))


#running program
menu()