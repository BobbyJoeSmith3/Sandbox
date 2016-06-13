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


def average_age(people, current_year):
    combined_age = 0
    num_people = len(people)
    i = num_people - 1
    while i  >= 0:
        combined_age += people[i].age(current_year)
        i -= 1
    return combined_age/num_people
