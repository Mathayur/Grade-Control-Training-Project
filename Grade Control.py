#Grade Control

school_students = {}
students_data = {}



def include():
    while True:
        students_data.clear()
        grades = ['','','']
        choice = int(input('''1 = ADD STUDENT\n2 = RETURN TO MENU\nChoose your option:  '''))
        if choice == 1:
            while True:
                print('Type 0000 to return.')
                student_number = input('Type the student code 3 digits(xxx) only: ')
                if len(student_number) == 3 and student_number not in school_students.keys():
                    student_name = input('Student Name: ')
                    students_data['Name'] = student_name
                    student_class = input('Student class: ')
                    students_data['Class'] = student_class
                    students_data['Grades'] = grades.copy()
                    school_students[student_number] = students_data.copy()
                    following = input('Continue? Y/N: ').upper()
                    if following == 'N':
                        break
                    if following == "Y":
                        continue
                    
                elif student_number == '0000':
                    print('Returning')
                    break     
                else:
                   print('Wrong code or code already taken, pick again.')
                   break
                if following == 'N':
                    print('Returning to MENU.')
                    break  
                    
        if choice == 2:
            print('Returning to MENU.')
            break    
        elif choice >= 3:
            print('Wrong code, try again.')
            break 
           
                                
                         
def exclude():
    while True:
        if len(school_students) == 0:
            print('There is no student registered, pick another choice.')   
            break
        else:
            while len(school_students) != 0:
                for key, value in school_students.items():
                    print("('{}': '{}')".format(key, tuple(value.items())[0]))
                choice = int(input('''1 = DELETE STUDENT\n2 = RETURN TO MENU\nChoose your option:  '''))
                if choice == 1:
                    while True:
                        print('Type 0000 to return.')
                        student_number_del = input('What is the student code that you want to delete: ')
                        if student_number_del in school_students and len(school_students) != 0:
                            del school_students[student_number_del]
                            following = input('Continue? Y/N: ').upper()
                            if following == 'N':
                                break
                            if following == "Y":
                                continue
                            else:
                                print('Wrong choice, pick again.')
                                break
                        elif student_number == '0000':
                            print('Returning')
                            break     
                        else:
                            print('Wrong code, try again.')
                            break 
                elif choice ==2:
                    print('Returning to MENU.')
                    break         
                #else:
            
           
        
def grade_add_control():
    while True:    
        choice = input('''1 = ADD GRADE\n2 = CHANGE GRADE\n3 = RETURN TO MENU\nChoose your option:  ''')
        if choice == '1':
            while True:
                print('Type 0000 to return.')
                student_number = input('Type the student code 3 digits(xxx) only: ')
                if len(student_number) == 3 and student_number in school_students.keys():
                    
                    while any('' in x['Grades'] for x in school_students.values()):
                        
                        grade_number = int(input('GRADE 1\nGRADE 2\nGRADE 3\n Choose the Grade: '))
                        
                        if  grade_number == 1 and school_students[student_number]['Grades'][0] == '':
                            grade_1 = int(input('Add Grade 1: '))
                            school_students[student_number]['Grades'][0] = grade_1
                            add_new_grade = input('Add new grade? Y/N: ').upper()
                        elif grade_number == 1 and school_students[student_number]['Grades'][0] != '':
                            print('Grade already filled.')
                            break    
                        
                        if  grade_number == 2 and school_students[student_number]['Grades'][1] == '':
                            grade_2 = int(input('Add Grade 2: '))
                            school_students[student_number]['Grades'][1] = grade_2
                            add_new_grade = input('Add new grade? Y/N: ').upper()
                        elif grade_number == 2 and school_students[student_number]['Grades'][1] != '':
                            print('Grade already filled.')
                            break    
                        
                        if  grade_number == 3 and school_students[student_number]['Grades'][2] == '':
                            grade_3 = int(input('Add Grade 3: '))
                            school_students[student_number]['Grades'][2] = grade_3
                            add_new_grade = input('Add new grade? Y/N: ').upper()
                        elif grade_number == 3 and school_students[student_number]['Grades'][2] != '':
                            print('Grade already filled.')
                            break
                        
                        elif add_new_grade == 'N':
                            break
                        elif add_new_grade == "Y":
                            continue
                        else:
                            print('Wrong choice, pick again.')
                            break             
                    else:
                        print('All grades for this student are already filled.')
                        break
                elif student_number == '0000':
                    print('Returning')
                    break        
                else:
                    print('Wrong code, try again.')
                    break    
                    
        elif choice == '2':
            student_number = input('Type the student code 3 digits(xxx) only: ')
            if len(student_number) == 3 and student_number in school_students.keys():
                pick_grade = int(input('Choose the grade to change 1,2 or 3: '))
                                   
                grade_index = pick_grade - 1
                
                if grade_index == 0:
                    new_grade1 = int(input('Grade 1 change to: '))
                    school_students[student_number]['Grades'][0] = new_grade1
                elif grade_index == 1:    
                    new_grade2 = int(input('Grade 2 change to: '))
                    school_students[student_number]['Grades'][1] = new_grade2
                elif grade_index == 2:    
                    new_grade3 = int(input('Grade 3 change to: '))
                    school_students[student_number]['Grades'][2] = new_grade3
            else:
                    print('Wrong code, try again.')
                    
        elif choice == '3':
            print('Returning to MENU.')
            break
                    
        else:
            print('Wrong Number try again.') 
            break

def display_school():
    while True:
        if len(school_students) == 0:
            print('There are no entries to display')
            break
        elif len(school_students) > 0:
            for key, value in school_students.items():
                print(key, value)  
            break  
def check_grades():
    while True:
        if len(student_number) == 3 and student_number in school_students.keys():
            for key, value in school_students.items():
                print(key[student_number], value)
        
        else:
            print('Wrong code, try again.')

def check_situation():
    while True:
        print('Type 0000 to return.')
        student_number = input('Type the student code 3 digits(xxx) only: ')
        if len(student_number) == 3 and student_number in school_students.keys():
            school_students[student_number].key(2)
        elif student_number == '0000':
            print('Returning')
            break   


def save_backup():
    pass


def recover_backup():
    pass


def end():
    print('Exiting Program.')
    exit()    
    
    
    
internal_menu = {
    1:include,
    2:exclude,
    3:grade_add_control,
    4:display_school,
    5:check_grades,
    6:check_situation,
    7:save_backup,
    8:recover_backup,
    9:end
}


while True:
    print('''-----------------MENU---------------
        1 - INCLUDE STUDENT
        2 - EXCLUDE STUDENT
        3 - ADD OR CHANGE GRADES
        4 - DISPLAY ALL STUDENTS
        5 - CHECK GRADES
        6 - CHECK SITUATION
        7 - SAVE BACKUP
        8 - RESTORE BACKUP
        9 - CLOSE PROGRAM
        ''')
    menu_choice = int(input('Choose number: '))
    if menu_choice in range(1,10):
        internal_menu[menu_choice]()
        
print(school_students)
            
