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


def count_items_per_dict(input_list):
    counted = {}
    for item in input_list:
        for key, value in item.items():
            if item[key] not in counted:
                counted[item[key]] = 1
            else:
                counted[item[key]] += 1
    return counted


def count_items_per_list_per_dict(input_list):
    output = []
    for counter, content in enumerate(input_list, start=1):
        counted = {}
        for item in content:
            for key, value in item.items():
                if item[key] not in counted:
                    counted[item[key]] = 1
                else:
                    counted[item[key]] += 1
        output.insert(counter, [counter, counted])
    return output


def find_max(input):
    max_num = 0
    max_name = ''
    for name, counter in input.items():
        if counter > max_num:
            max_num = counter
            max_name = name
    return max_name, max_num


def check_sex(input):
    sex = ''
    if is_male.get(input) is True:
        sex = 'Male'
    elif is_male.get(input) is False:
        sex = 'Female'
    else:
        sex = 'Not defined'
    return sex


print('Ex1')
count = count_items_per_dict(students1)
for name, counter in count.items():
    print(f'{name} : {counter}')

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
count = count_items_per_dict(students2)
max_name, max_num = find_max(count)
print(f'Most frequent name is {max_name}, counted {max_num} time(s) \n' )

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
count = count_items_per_list_per_dict(school_students)
for school_classes in count:
    school_class, counted_names = school_classes
    max_name, max_num = find_max(counted_names)
    print(f'Most frequent name in class {school_class} is {max_name}, counted {max_num} time(s) \n')

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
for school_class in school:
    sex_list_class = []
    for num, content in enumerate(school_class.get('students'), start=1):
        name = content.get('first_name')
        sex_list_class.insert(num, {'sex': check_sex(name)})
    sex_counted = count_items_per_dict(sex_list_class)
    print(f"Class {school_class.get('class')} has females: {sex_counted.get('Female',0)}, males: {sex_counted.get('Male',0)}")

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

female_num = 0
male_num = 0
for school_class in school:
    sex_list_class = []
    for num, content in enumerate(school_class.get('students'), start=1):
        name = content.get('first_name')
        sex_list_class.insert(num, {'sex': check_sex(name)})
    sex_counted = count_items_per_dict(sex_list_class)
    sex, num = find_max(sex_counted)
    if sex == 'Female':
        if num > female_num:
            female_class = school_class.get('class')
            female_num = num
    elif sex == 'Male':
        if num > male_num:
            male_class = school_class.get('class')
            male_num = num
print(f'The class with most females is {female_class} with {female_num} female(s) \n'  )   
print(f'The class with most males is {male_class} with {male_num} male(s)  \n')    