#Basic school administration tool
import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0: #To make sure The file is empty.
            writer.writerow(["Name", "Student ID", "Age", "Contact Number", "E-mail ID"])
        writer.writerow(info_list)

def check(val):
    student_num = 1
    while(val):
        student_info = input("\nEnter some student information for student_{} in the folowing format (Name Student_id Age Contact_Number E-mail_ID): ".format(student_num))

        #splitting the entered information
        student_info_list = student_info.split(' ')

        print("\nThe entered information is:- \nName: {}\nStudent ID: {}\nAge: {}\nContact_number: {}\nE-mail ID: {}".format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3], student_info_list[4]))
        choice_check = input("Is the entered information correct?(yes/no): ")

        if choice_check == "no":
            print("\nPlease re-enter the values!");
        elif choice_check == "yes":
            write_into_csv(student_info_list)

            condition_check = input("Enter(yes/no) if you want to enter information for another student: ")
            if condition_check == "yes":
                val = True
                student_num = student_num + 1
            elif condition_check == "no":
                val = False
            else:
                print("Wrong input!! Now please re-enter the values.");
        else:
            print("\nWrong input!! Now please re-enter the values.");

if __name__ == '__main__':
    condition = True
    print("\n***********SCHOOL ADMINISTRATION SYSTEM**********\n")
    check(condition)
