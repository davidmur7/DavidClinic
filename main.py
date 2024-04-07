# Author: David Murphy
def main():
    schedule_appointment()
def schedule_appointment():
    name = input("Enter your name: ")
    contact_number = int(input("Enter your phone number: "))
    appointment_date = input("Enter appointment date (d/mm/yyyy) : ")
    appointment_time = input("Enter your prefered time of appointment (hour:minute) : ")
