# Author: David Murphy
date_in_file = "."
from datetime import datetime
current_datetime = datetime.now()
current_date = current_datetime.date()
current_date_str = str(current_date)
def main():
    user_choice1 = input("Would you like to (1: Schedule an appointment) (2: View an appointment) (3: Cancel appointment) (4: exit) : ")
    if user_choice1 == "1":
        schedule_appointment()
    elif user_choice1 == "2":
        view_appointments()
    elif user_choice1 == "3":
        cancel_appointment()
    else:
        exit()
    while user_choice1 != "4":
        main()


def schedule_appointment():
    name = input("Enter your name: ")
    while len(name) > 20 or len(name) < 1:
        name = input("Enter your name: ")
    contact_number = input("Enter your phone number: ")
    while len(contact_number) != 10 or not contact_number.isdigit():
        print("Contact number needs to be a number of exactly 10 digits ")
        contact_number = (input("Enter your phone number: "))
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
    appointment_time = input("Enter your prefered time of appointment (hour:minute) : ")
    with open("patient_data.txt", "a") as file:
        file.write(f"\n{name}, {contact_number}, {appointment_date}, {appointment_time}")

def cancel_appointment():
    name_for_cancel = input("Enter your name: ")
    date_for_cancel = input("Enter appointment date: ")
    with open("patient_data.txt", "r") as file:
        for line in file:
            if name_for_cancel and date_for_cancel in line:
                line = ""
                file.write(line)

def view_appointments():
    user_choice2 = input("would you like to view appointments by date or name? (date/name) : ")
    if user_choice2 == "name":
        name = input("Enter the name: ")
        with open("patient_data.txt", "r") as file:
            for line in file:
                if name in line:
                    print(line)
                else:
                    print(f"{name} was not found in file ")
    if user_choice2 == "date":
        chosen_date = input("Enter the date of the appointment (yyyy-mm-dd) : ")
        with open("patient_data.txt", "r") as file:
            for line in file:
                if chosen_date in line:
                    print(line)
                    date_in_file = "yes"
            if date_in_file != "yes":
                print("There are no appointments on this date ")
def exit():
    print("Thank you for using our system")

main()