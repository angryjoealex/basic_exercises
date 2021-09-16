# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
counter = 0
word = 'Архангельск'
for letter in word:
    if letter.lower() == 'а':
        counter += 1
print(f'Word {word} has {counter} \'a\' char(s) \n')


# Вывести количество гласных букв в слове

word = 'Архангельск'
vowels =['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
vowels_counter = 0
for letter in word:
    if letter.lower() in vowels:
        vowels_counter += 1
print(f'Word {word} has {vowels_counter} vowel(s) \n')

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
print(f'Sentence \"{sentence}\" has  {len(words)} word(s) \n')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split()
for word in words:
    print(f'The first letter of the word \"{word}\" is {word[0]} \n')

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
count_letter = []
for word in words:
    count_letter.append(len(word))
avg = sum(count_letter)/len(sentence.split())
print(avg)