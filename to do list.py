import datetime

today = datetime.date.today()
file_name = str(today) + "_to_do_list.txt"

with open(file_name, "w") as file:       
    file.write("TO DO LIST for " + str(today) + ":\n") 
    
    while True:
        to_do = input("enter things to do for today (or 'exit' to finish): ")
        if to_do.lower() == "exit":
            break
        file.write("-" + to_do + "\n")

print("TO DO LIST for " + str(today) + " has been saved to " + file_name)
