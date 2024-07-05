grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_mod = list(students) # Преобразуем множество в список
students_mod.sort() # Сортируем в алфавитном порядке элементы списка студентов для соотв. оценкам
grades_mod = [] # Создаем пустой список
for item in grades: # Перебираем элементы списка оценок в цикле
    aver = sum(item) / len(item) # Находим среднее арифм. каждого элемента списка оценок
    grades_mod.append(aver) # Добавляем среднее арифм. оценок в новый список
# print(grades_mod)
dict_stud = dict(zip(students_mod, grades_mod)) # Объединяем модифицированные списки
print(dict_stud)