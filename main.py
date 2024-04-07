# Author: David Murphy
from datetime import datetime
current_datetime = datetime.now()
current_date = current_datetime.date()
print(current_date)
def main():
    schedule_appointment()
def schedule_appointment():
    name = input("Enter your name: ")
    while len(name) > 20 or len(name) < 1:
        name = input("Enter your name: ")
    contact_number = input("Enter your phone number: ")
    while len(contact_number) != 10 or not contact_number.isdigit():
        print("Contact number needs to be a number of exactly 10 digits ")
        contact_number = int(input("Enter your phone number: "))
    appointment_date = input("Enter appointment date (d/mm/yyyy) : ")
    appointment_time = input("Enter your prefered time of appointment (hour:minute) : ")

main()