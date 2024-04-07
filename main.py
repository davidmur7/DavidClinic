# Author: David Murphy
from datetime import datetime
current_datetime = datetime.now()
current_date = current_datetime.date()
current_date_str = str(current_date)
def main():
    schedule_appointment()
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
        file.write(f"{name}, {contact_number}, {appointment_date}, {appointment_time}")

cancel_appointment():
    name_for_cancel = input("Enter your name: ")
    date_for_cancel = input("Enter appointment date: ")

main()