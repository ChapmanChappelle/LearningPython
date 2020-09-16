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
    
    def file_writing(self):
        time_diff = (dt.datetime.now() - self.start_time)
        diff = time_diff.total_seconds()
        total_cost = round(self.cost*diff, 2)
        if(diff >= 60 and diff <= 3600):
            diff= str(diff) + " minutes"
        elif(diff < 60):
            diff = str(diff) + " seconds"
        elif(diff >= 3600):
            diff = str(diff) + " hours"
        else:
            print("ERROR")
        file_name = dt.datetime.now().strftime("%Y-%m-%d")
        with open(f"{file_name}","a") as file_object:
            file_object.write(f"Table Number: {self.table_num+1}\n")
            file_object.write(f"  Start Time: {self.start_time}\n")
            file_object.write(f"    End Time: {dt.datetime.now()}\n")
            file_object.write(f"  Total Time: {diff}\n")
            file_object.write(f"  Total Cost: ${total_cost}\n\n")

    def open_table(self):
        self.status = True
        self.start_time = dt.datetime.now()
        print(f"Table {self.table_num+1} is now occupied")
        print(f"Start time is {self.start_time}")

    def close_table(self):
        if(self.status == False):
            print(f"TABLE {self.table_num} is already unoccupied")
        else:
            self.status = False
            time_diff = (dt.datetime.now() - self.start_time)
            diff = time_diff.total_seconds()
            print(f"Total Cost of table: ${str(round(self.cost*diff , 2))}")
            if(diff >= 60 and diff <= 3600):
                print(f"Table {self.table_num+1} is unoccupied again after {str(round((diff/60) , 2))} minutes")
            elif(diff < 60):
                print(f"Table {self.table_num+1} is unoccupied again after {str(round(diff , 2))} seconds")
            elif(diff >= 3600):
                print(f"Table {self.table_num+1} is unoccupied again after {str(round((diff/3600) , 2)) } hours")
            else:
                print("ERROR")
            self.file_writing()

        
  

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
         user_input = int(input("\nWhich table? "))
         room[user_input-1].display_table()
    elif choice == "3":
        user_input = int(input("\nWhich table? "))
        room[user_input-1].open_table()
    elif choice == "4":
        user_input = int(input("\nWhich table? "))
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