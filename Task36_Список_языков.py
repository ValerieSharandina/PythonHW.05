'''
Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
['python', 'c#']
[1,2]
Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
[(1,'PYTHON'), (2,'C#')]
Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
[сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
[(1,'PYTHON'), (102,'C#')]
Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком
'''
from functools import reduce

file_with_languages = open('list_of_programming_languages.txt', 'r')
languages = file_with_languages.readlines()
numbering = [i for i in range(1, len(languages) + 1)]
tuples_list = list(zip(numbering, [word.upper() for word in languages]))
#print(tuples_list)

def filter_by_points(tuples_list):
    result_list = []
    result = 0
    for number, language in tuples_list:#range(len(), 0, -1)
        points = reduce(lambda a,b: a+b, [ord(char) for char in language])
        if points % number == 0:
            result += points
            result_list.append((points, language))
    del tuples_list
    return result, result_list
print(filter_by_points(tuples_list))