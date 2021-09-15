# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
# ???\
ex1 = 'Excersise 1 \n'
for name in names:
    ex1 += name+'\n'
print(ex1) 
# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4
ex2 = 'Excersise 2 \n'
names2 = ['Оля', 'Петя', 'Вася', 'Маша']
for name2 in names2:
    ex2 += f'{name2}: {len(name2)} \n'
print(ex2)
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
    if is_male.get(name3) is True:
        ex3 += name3 + ' is male \n'
    elif is_male.get(name3) is False:
        ex3 += name3 + ' is female \n'
    else:
        ex3 += 'Sex is not defined for ' + name3 + '\n'
print(ex3)

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
ex4 += f'Total groups: {len(groups4)} \n'
for group in groups4:
    ex4 += f'Group {groups4.index(group)+1} has {len(group)} student(s) \n'
print(ex4)

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
for group in groups5:
    students = ''
    for student in group:
        students += student
        if student != group[-1]:
            students += ', '
    ex5 += f'Group {groups5.index(group)+1} has following student(s) {students} \n'
print(ex5)