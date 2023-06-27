class Student:
    def __init__(self,name):
        self.name=name
        self.grades=[]

#klasa Dziennik
class Logbook:
    def __init__(self):
        self.grades=[]

#dodaj ocene
    def add_grade(self,grade):
        if grade in range(1,6):
            self.grades.append(grade)
            print(f"The grade {grade} is added to Your logbook")
        else:
            print("Invalid grade.Please enter a grade between 1 and 5")

    def show_grades(self):
        if len(self.grades)==0:
            print("No grades recognized")
        else:
            print("Your grades are:")
            for grade in self.grades:
                print(grade)
    def change_grade(self,old_grade,new_grade):
        if old_grade in self.grades:
            index=self.grades.index(old_grade)
            self.grades[index]=new_grade
            print(f"the old grade {old_grade} has been changed to a new grade {new_grade}")
        else:
            print("Grade not found")
    def calculate_average(self):
        if len(self.grades)==0:
            return None
        else:
            return sum(self.grades)/len(self.grades)

    def promote_to_next_class(self):
        if len(self.grades)>=5:
            average_grade=self.calculate_average()
            if average_grade is not None:
                if average_grade>=3:
                    print("Congratulations!!! You are promoted to the next class. See You soon.")
                else:
                    print("I am so sorry! Your average grade is below 3. You need to improve grades below 3")
                    print("Grades below 3:")
                    for grade in self.grades:
                        if grade<3:
                            print(grade)
            else:
                print("Error calculating average grade")
        else:
            print("You need at least 5 grades to get promotion to next class")

logbook = Logbook()

logbook.add_grade(4)
logbook.add_grade(3)
logbook.add_grade(5)
logbook.add_grade(2)
logbook.add_grade(3)
logbook.add_grade(6)

logbook.show_grades()

logbook.change_grade(5, 4)

average_grade = logbook.calculate_average()
print(f"Average grade: {average_grade}")

logbook.promote_to_next_class()

