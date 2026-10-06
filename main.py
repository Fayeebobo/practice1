def student_name_validation() -> str:
    student_name = str(input("student name : "))
    return student_name

def validate_course() -> str:
    supported_courses=["BBIT","BIT","COMPUTER SCIENCE"]
    course_name=str(input("course name : "))
    course_name=course_name.upper()

    is_valid_course =False
    while is_valid_course ==  False:
        if course_name in supported_courses:
            is_valid_course=True
            return course_name
            
        else:
            print('Invalid input , please try again')

            course_name = str(input("course name : ")) 


def validate_year()->int:
    accepted_year=[1,2,3,4]
    course_year=int(input("Year of study : "))

    is_valid_year=False
    while is_valid_year == False :
        if course_year in accepted_year:
            is_valid_year=True
            return course_year
        else:
            print("Invalid input, Try again")
            course_year=int(input("Year of study : "))

def validate_document_type()->str:
    document_type = str(input("Document name : "))
    document_type= document_type.upper()
    

    is_valid_document_type=False
    while is_valid_document_type == False :
            if document_type  in   document_types:
                is_valid_document_type=True
                return document_type
            else:
                print("Invalid input, Try again")

            document_type = str(input("Document name : "))  

import os


def validate_file():
    allowed_file_type=[".pdf",".docx"]
    filename = input("Enter filename: ")

    
    extension = os.path.splitext(filename)[1].lower()

    if extension in allowed_file_type:
        return filename
    else:
        print(" File type not allowed.")
        



def submit_document():
    student_name = str(input("Enter student name: "))
    course_name = str(input("Enter course: "))
    course_year= int(input("Enter year: "))
    unit = str(input("Enter unit: "))
    title = str(input("Enter document title: "))

    document_type = validate_document_type()
    filename = validate_file()

    submission = {
        "student_name": student_name,    
        "course_name": course_name,
        "course_year": course_year,
        "unit": unit,
        "title": title,
        "type": document_type,
        "filename": filename
    }

    return submission



def view_submission(student_name, course_name, course_year, unit, title, document_type, filename):

    print(f"Student name: {student_name}")
    print(f"Course name: {course_name}")
    print(f"Course year: {course_year}")
    print(f"Unit: {unit}")
    print(f"Title: {title}")
    print(f"Type: {document_type}")
    print(f"Filename: {filename}")

run=True
while run:
    print("----------------------------------")
    print("STUDENT DOCUMENT SUBMISSION SYSTEM")
    print("----------------------------------")

    print("")

    print( "1.Submit Document")
    print( "2.View Submissions")
    print( "3.Exit")

    option = int(input("Choose an option: "))

    if option == 1:
        print("Submit Document Form")

        student_name = student_name_validation()
        course_name = validate_course()
        course_year= validate_year()
        document_types = ("PASTPAPER","CAT","ASSIGNMENT","NOTES","REVISION")
        filename=validate_file()
        


    elif option == 2:
        print("View Submissions")

        student_name, course_name, course_year, unit, title, document_type, filename = submit_document()


        view_submission(student_name, course_name, course_year, unit, title, document_type, filename)
                  



    elif option == 3:
        print("Exit")
        run = False
    else:
        print("Invalid option. Please try again.")







