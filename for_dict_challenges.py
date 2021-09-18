import collections
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
ex1 = 'Exercise 1 \n'
students1 = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

def check_sex(input):
    sex = ''
    if is_male.get(input):
        sex = 'Male'
    elif is_male.get(input) is False:
        sex = 'Female'
    else:
        sex = 'Not defined'
    return sex


print('Ex1')
counter = collections.Counter()
for student in students1:
    counter[student['first_name']] += 1
for name in counter:
    print(f'{name} : {counter[name]}')

# # Задание 2
# # Дан список учеников, нужно вывести самое часто повторящееся имя
# # Пример вывода:
# # Самое частое имя среди учеников: Маша
students2 = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
# # ???
print('\nEx2 \n')
counter.clear()
for student in students1:
    counter[student['first_name']] += 1
most_common = dict(counter.most_common(1))
for key, value in most_common.items():
    print(f'Most frequent name is {key}, counted {value} time(s) \n' )

# # Задание 3
# # Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# # Пример вывода:
# # Самое частое имя в классе 1: Вася
# # Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],
    [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
print('\nEx3 \n')
counter.clear()
for class_num, students in enumerate(school_students, 1):
    counter.clear()
    for student in students:
        counter[student['first_name']] += 1
    most_common = dict(counter.most_common(1))
    for key, value in most_common.items():
        print(f'Most frequent name in class {class_num} is {key}, counted {value} time(s) \n')

# # ???


# # Задание 4
# # Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# # Пример вывода:
# # Класс 2a: девочки 2, мальчики 0 
# # Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

print('\nEx4\n')
counter.clear()
for school_class in school:
    counter.clear()
    sex_list_class = []
    class_letter =school_class.get('class')
    for students in school_class.get('students'):
        name = students.get('first_name')
        sex_list_class.append({'sex': check_sex(name)})
    for sex in sex_list_class:
        counter[sex['sex']] += 1
    females = counter['Female']
    males = counter['Male']
    print(f"Class {class_letter} has females: {females}, males: {males}")

# # Задание 5
# # По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# # Пример вывода:
# # Больше всего мальчиков в классе 3c
# # Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'},  {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Оля'}]},
    {'class': '2c', 'students': [{'first_name': 'Маша'}, {'first_name': 'Маша'}, {'first_name': 'Оля'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# # ???
print('\nEx5\n')
max_sex_per_class = {}
female_num = 0
male_num = 0

for school_class in school:
    counter.clear()
    sex_list_class = []
    class_letter = school_class.get('class')
    for students in school_class.get('students'):
        name = students.get('first_name')
        sex_list_class.append({'sex': check_sex(name)})
    for sex in sex_list_class:
        counter[sex['sex']] += 1
    most_common = counter.most_common(1)
    if counter['Female'] > female_num:
        Female = class_letter
        max_sex_per_class.update({'Female': class_letter})
    if counter['Male'] > male_num:
        Male = class_letter
        max_sex_per_class.update({'Male': class_letter})       
for sex, school_class in max_sex_per_class.items():
    print(f'The class with most {sex} is {school_class}')