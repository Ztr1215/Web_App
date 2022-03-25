import os, django, datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'freshmen_world.settings')
django.setup()
    
# All models imported for creating fake content
from WOF.models import University, Task, Course, StudentUser
from django.contrib.auth.models import User

def populate():
    # All dummy tasks and users in order to populate all aspects

    maclaurin_task = [
        {'name':'Theorise Power Series',
         'completed': True,
         'dueDate': datetime.datetime(2022, 10, 24), # 24/10/2022, 
         'timePlanned': datetime.time(18, 30),
         },
    ]

    matty_task = [
        {'name':'Walk the dog',
         'completed': False,
         'dueDate': datetime.datetime(2022, 6, 9), # 09/06/2022, 
         'timePlanned': datetime.time(3, 30),
         },
    ]

    ben_task = [
        {'name':'Submit English folio',
         'completed': True,
         'dueDate': datetime.datetime(2022, 5, 17), # 17/05/2022, 
         'timePlanned': datetime.time(9, 30),
         },
    ]

    bobbyd_task = [
        {'name':'Make more music',
         'completed': False,
         'dueDate': datetime.datetime(2022, 8, 22), # 22/08/2022, 
         'timePlanned': datetime.time(23, 30),
         },
    ]

    glasgow_users = [
        {'username': "BobbyD",
        'firstName': "Bob",
        'secondName': "Dylan",
        'password': "HeavensDoorKnocker",
        'degree': "Music History",
        'level': 3,
        'isAdmin': False,
        'tasks': bobbyd_task
        },
        {'username': "MaclaurinMan",
        'firstName': "Colin",
        'secondName': "Maclaurin",
        'password': "TaylorSeriesSucks",
        'degree': "Mathematics",
        'level': 4,
        'isAdmin': False,
        'tasks': maclaurin_task
        },
    ]

    stboswells_users = [
        {'username': "Matty",
        'firstName': "Matthew",
        'secondName': "Jackson",
        'password': "MatthewCantWalk",
        'degree': "Helping old people",
        'level': 3,
        'isAdmin': False,
        'tasks': matty_task
        },
        {'username': "BigBen",
        'firstName': "Ben",
        'secondName': "Jackson",
        'password': "BenDoesNotClean",
        'degree': "Dishwasher Cleaning",
        'level': 1,
        'isAdmin': False,
        'tasks': ben_task
        },
    ]

    glasgow_courses = [
        {'name':"Computer Systems",
        'level':1,
        'credits':10,
        'courseConvener': "Angelos Marnerides",
        'courseNumber': 'COMPSCI1018',
        },
        {'name': "Maths 2D: Modelling",
        'level': 2,
        'credits': 10,
        'courseConvener': "Dr Watson",
        'courseNumber': "MATHS2033"
        },
        {'name': "Maths 2F: Groups, Symmetric & Transformations",
        'level': 2,
        'credits': 10,
        'courseConvener': "Sira Gratz",
        'courseNumber': "MATHS2035"
        },
    ]

    stboswells_courses = [
        {'name': "Dealing with old people",
        'level': 3,
        'credits': 20,
        'courseConvener': "Andrew Jackson", 
        'courseNumber': "SBYT2000",
        },
        {'name': "Avoiding angry farmers",
        'level': 1,
        'credits': 10,
        'courseConvener': "Ross Taylor", 
        'courseNumber': "SBYT2002",
        },
    ]

    university_information = {
        "University of Glasgow" : {'courses' : glasgow_courses, 'users': glasgow_users, 
                                    'location' : "Glasgow"},
        "St Boswells University" : {'courses' : stboswells_courses, 'users': stboswells_users, 
                                    'location' : "St Boswells"},
    }
    
    for university_name, university_data in university_information.items():
        created_uni = add_university(university_name, university_data['location'])
        for course in university_data['courses']:
            add_course(created_uni, course['name'], course['level'], 
                        course['credits'], course['courseConvener'], 
                        course['courseNumber'])
        for user in university_data['users']:
            # Need returned value as to assign values
            created_user = add_user(created_uni, user['username'], user['firstName'], 
                            user['secondName'], user['password'], 
                            user['degree'], user['level'], user['isAdmin'])
            for task in user['tasks']:
            # Assign each task to specific user
                add_task(created_user, task['name'], task['completed'], task['dueDate'], task['timePlanned'])

    for uni in University.objects.all():
        for course in Course.objects.filter(university=uni):
            print(f"- {uni} : Course : {course}")
        for student in StudentUser.objects.filter(university=uni):
            print(f"- {uni} : Student :  {student}")
            for task in Task.objects.filter(studentUser=student):
                print(f"\t- {student} : Task : {task}")

    
    
def add_university(name : str, location : str):
    created_university = University.objects.get_or_create(name = name, location = location)[0]
    created_university.save()
    return created_university

def add_course(university, name : str, level : int, credits : int, courseConvener : str, courseNumber : str):
    created_course = Course.objects.get_or_create(university = university, name = name, level = level, credits = credits,
    courseConvener = courseConvener, courseNumber = courseNumber)[0]
    created_course.save()
    return created_course

def add_task(studentUser, name : str, completed : str, dueDate, timePlanned):
    created_task = Task.objects.get_or_create(studentUser = studentUser, name = name, completed = completed, dueDate = dueDate, timePlanned = timePlanned)[0]
    created_task.save()
    return created_task

def add_user(university, username : str, firstName : str, secondName : str,
                password : str, degree : str, level : int, isAdmin : bool):
    # Need to make users first in order to assign to studentUser model
    created_user = User.objects.get_or_create(username = username, password = password, first_name = firstName, last_name = secondName)[0]
    created_user.set_password(password)
    created_user.save()
    created_student_user = StudentUser.objects.get_or_create(user = created_user, university = university, degree = degree, level = level, isAdmin = isAdmin)[0]
    created_student_user.save()
    return created_student_user
   
if __name__ == '__main__':
    print('Starting population script...')
    populate()
