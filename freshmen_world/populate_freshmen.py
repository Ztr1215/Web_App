import os, django, datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'freshmen_world.settings')
django.setup()

from WOF.models import University, Task, Course

def populate():

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
        "University of Glasgow" : {'courses' : glasgow_courses, 'location' : "Glasgow"},
        "St Boswells University" : {'courses' : stboswells_courses, 'location' : "St Boswells"},
    }


    # Task data
    task_information = [
        {'name':'Lab exam 1S',
         'completed': False,
         'dueDate': datetime.datetime(2022, 10, 24), # 24/10/2022, 
         'timePlanned': datetime.time(18, 30),
         },
         {'name':'Lab exam 1P',
         'completed': True,
         'dueDate': datetime.datetime(2022, 12, 10), # 10/12/2022,
         'timePlanned': datetime.time(6, 30),
         },
    ]
    
    for university_name, university_data in university_information.items():
        created_uni = add_university(university_name, university_data['location'])
        for course in university_data['courses']:
            add_course(created_uni, course['name'], course['level'], 
                        course['credits'], course['courseConvener'], 
                        course['courseNumber'])
        
    for task in task_information:
        add_task(task['name'], task['completed'], task['dueDate'], task['timePlanned'])

    for uni in University.objects.all():
        for course in Course.objects.filter(university=uni):
            print(f"- {uni} : {course}")

    for task in Task.objects.all():
        print(f"- {task}")
    
    
def add_university(name : str, location : str):
    u = University.objects.get_or_create(name = name, location = location)[0]
    u.save()
    return u

def add_course(university : str, name : str, level : int, credits : int, courseConvener : str, courseNumber : str):
    c = Course.objects.get_or_create(university = university, name = name, level = level, credits = credits,
    courseConvener = courseConvener, courseNumber = courseNumber)[0]
    c.save()
    return c

def add_task(name : str, completed : str, dueDate, timePlanned):
    t = Task.objects.get_or_create(name = name, completed = completed, dueDate = dueDate, timePlanned = timePlanned)[0]
    t.save()
    return t
   
if __name__ == '__main__':
    print('Starting population script...')
    populate()
