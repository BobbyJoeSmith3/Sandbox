# create a person object
class Person():
    def __init__(self, first_name, last_name, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def __str__(self):
        return "The person's name is " + self.first_name + " " + self.last_name + ". Their birth year is " + str(self.birth_year)

    def full_name(self):
        return self.first_name + " " + self.last_name

    def age(self, current_year):
        return current_year - self.birth_year


class Student():
    def __init__(self, person, pwd):
        self.person = person
        self.password = str(pwd)
        self.projects = []

    def get_name(self):
        return self.person.full_name()

    def check_password(self, pwd):
        return self.password == pwd

    def get_projects(self):
        return self.projects

    def add_project(self, project_name):
        self.projects.append(project_name)

# calculate the average age of a list of people created with Person class
def average_age(people, current_year):
    combined_age = 0
    num_people = len(people)
    for p in people:
        combined_age += p.age(current_year)
    return combined_age/float(num_people)
