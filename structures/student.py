class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_number_of_marks(self):
        return len(self.marks)

    def get_total_sum_of_marks(self):
        return sum(self.marks)

    def determine_maximun_mark(self):
        return max(self.marks)

    def determine_minimun_mark(self):
        return min(self.marks)

    def determine_averange(self):
        return self.get_total_sum_of_marks() / self.get_number_of_marks()

    def add_new_mark(self, new_mark):
        self.marks.append(new_mark)

    def remove_mark_at_index(self, index):
        del self.marks[index]

    pass


students = [ Student('Artur', [9.5,8.3,7.4,10.0]), Student('Manu', [10.0, 9.5, 8.5]) ]

def show_info_object_students():

    for i, s in enumerate(students):
        print(f'The student {s.name}')
        print(f'Student[get_number_of_marks-{s.get_number_of_marks()}]')
        print(f'Student[get_total_sum_of_marks-{s.get_total_sum_of_marks()}]')
        print(f'Student[determine_minimun_mark-{s.determine_minimun_mark()}]')
        print(f'Student[determine_maximun_mark-{s.determine_maximun_mark()}]')
        print(f'Student[determine_averange-{s.determine_averange()}]')
        print(f'Student[determine_maximun_mark-{s.determine_maximun_mark()}]')
        print(f'************************************************************')
        print()


show_info_object_students()

students[0].add_new_mark(7)
students[1].add_new_mark(9)

show_info_object_students()

students[0].remove_mark_at_index(0)
students[1].remove_mark_at_index(0)

show_info_object_students()






