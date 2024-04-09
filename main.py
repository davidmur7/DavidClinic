# Author: David Murphy

from datetime import datetime
current_datetime = datetime.now()
current_date = current_datetime.date()
current_date_str = str(current_date) # I will compare the appointment date to the current date
def main():
    while True:
        user_choice1 = input("Would you like to (1: Schedule an appointment) (2: View an appointment) (3: Cancel appointment) (4: View slots) (4: exit) : ")
        while user_choice1 not in ["1", "2", "3", "4"]:
            print("Enter 1, 2, 3 or 4")
            user_choice1 = input("Would you like to (1: Schedule an appointment) (2: View an appointment) (3: Cancel appointment) (4: exit) : ")
        if user_choice1 == "1":
            schedule_appointment()
        elif user_choice1 == "2":
            view_appointments()
        elif user_choice1 == "3":
            cancel_appointment()
        elif user_choice1 == "4":
            view_available_slots()
        elif user_choice1 == "5":
            exit()
            break


def schedule_appointment():
    name = input("Enter your name: ")
    while len(name) > 20 or len(name) < 1:
        name = input("Enter your name: ")
    contact_number = input("Enter your phone number: ")
    while len(contact_number) != 10 or not contact_number.isdigit():
        print("Contact number needs to be a number of exactly 10 digits ")
        contact_number = (input("Enter your phone number: "))
    appointment_date = input("Enter appointment date (yyyy-mm-dd) : ")
    while len(appointment_date) != 10:
        print("You need to enter the date in this format: (yyyy-mm-dd)")
        appointment_date = input("Enter appointment date (yyyy-mm-dd) : ")
    while int(appointment_date[0:4]) < int(current_date_str[0:4]):
        print("Incorrect date, year in the past ")
        appointment_date = input("Enter appointment date (yyyy-mm-dd) : ")
    while int(appointment_date[0:4]) == int(current_date_str[0:4]) and int(appointment_date[5:7]) < int(current_date_str[5:7]):
        print("Incorrect date, month in the past ")
        appointment_date = input("Enter appointment date (yyyy-mm-dd) : ")
    while int(appointment_date[0:4]) == int(current_date_str[0:4]) and int(appointment_date[5:7]) == int(current_date_str[5:7]) and int(appointment_date[8:10]) < int(current_date_str[8:10]):
        print("Incorrect date, day in the past ")
        appointment_date = input("Enter appointment date (yyyy-mm-dd) : ")
    appointment_time = input("Enter your preferred time of appointment (hour:minute) eg (9:30) (15:00) 9am to 5pm only : ")
    while int(appointment_time[0:2]) <9 or int(appointment_time[0:2]) > 17:
        print("We are unaviable at that time ")
        appointment_time = input("Enter your preferred time of appointment (hour:minute) eg (9:30) (11:00) 9am to 5pm only : ")
    is_time_available = "."
    with open("patient_data.txt", "r") as file:
        for line in file:
            if appointment_date and appointment_time in line:
                print("This time is not available, sorry ")
                is_time_available = "no"
    if is_time_available != "no":
        print(f"{appointment_time} is avaiable")

    with open("patient_data.txt", "a") as file:
        file.write(f"\n{name}, {contact_number}, {appointment_date}, {appointment_time}")

def cancel_appointment():
    name_for_cancel = input("Enter the name: ")
    while len(name_for_cancel) > 20 or len(name_for_cancel) < 1:
        name_for_cancel = input("Enter the name: ")
    date_for_cancel = input("Enter appointment date: ")
    while len(date_for_cancel) != 10:
        print("You need to enter the date in this format: (yyyy-mm-dd)")
        date_for_cancel = input("Enter appointment date: ")
    with open("patient_data.txt", "r") as file:
        lines = file.readlines()
    with open("patient_data.txt", "w") as file:
        for line in lines:
            if name_for_cancel and date_for_cancel not in line:
                file.write(line)



def view_appointments():
    user_choice2 = input("would you like to view appointments by date or name? (date/name) : ")
    while user_choice2 != "date" and user_choice2 != "name":
        print("Enter 'name' or 'date' please")
        user_choice2 = input("would you like to view appointments by date or name? (date/name) : ")
    if user_choice2 == "name":
        name = input("Enter the name: ")
        name_in_file = "."
        with open("patient_data.txt", "r") as file:
            for line in file:
                if name in line:
                    print(line)
                    name_in_file = "yes"
        if name_in_file != "yes":
            print(f"{name} was not found in file ")
    if user_choice2 == "date":
        chosen_date = input("Enter the date of the appointment (yyyy-mm-dd) : ")
        date_in_file = "."
        with open("patient_data.txt", "r") as file:
            for line in file:
                if chosen_date in line:
                    print(line)
                    date_in_file = "yes"
        if date_in_file != "yes":
            print("There are no appointments on this date ")

def view_available_slots():
    slots = ["9:00", "9:30", "10:00", "10:30", "11:00", "11:30", "12:00"]
    with open("patient_data.txt", "r") as file:
        lines = file.readlines()
    print("Monday")
    for i in range[9:17]:
        print(i) + ":00"
        print(i) + ":30"




def exit():
    print("Thank you for using our system")


main()