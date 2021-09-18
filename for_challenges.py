# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
# ???\
ex1 = 'Excersise 1 \n'
for name in names:
   print(name) 

# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4
ex2 = 'Excersise 2 \n'
names2 = ['Оля', 'Петя', 'Вася', 'Маша']
for name2 in names2:
    print( f'{name2}: {len(name2)}')

# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика
ex3 = 'Excersise 3 \n'
is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}
names3 = ['Оля', 'Петя', 'Вася', 'Маша', 'Бобр']
for name3 in names3:
    sex = is_male.get(name3)
    if sex:
        print(f'{name3} is male')
    elif sex is False:
        print(f'{name3} is female')
    else:
        print(f'Sex is not defined for {name3}')


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.
ex4 = 'Excersise4 \n'
groups4 = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]
ttl_groups = len(groups4)
print(f'Total groups: {ttl_groups}')
for group_number, group in enumerate(groups4,1):
    student_count = len(group) 
    print(f'Group {group_number} has {student_count} student(s)')

# # Задание 5
# # Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# # Пример вывода:
# # Группа 1: Вася, Маша
# # Группа 2: Оля, Петя, Гриша
ex5 = 'Excersise5 \n'
groups5 = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]
for group_number, students in enumerate(groups5, 1):
    all_students = ", ".join(students)
    print(f'Group {group_number} has following student(s) {all_students} \n')