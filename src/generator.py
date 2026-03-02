'''AI-Методист'''
#Модуль 1: Сбор данных для урока
#Модуль 2: Валидатор уровня (CEFR)

name = input ('Введите имя ученика: ')

topic = input ('Введите тему урока: ')

level = input ('Введите уровень ученика: A1 - C2 ').strip() .upper()
if level == 'A1' or level =='A2' or level == 'B1' or level == 'B2' or level =='C1' or level == 'C2':
         print (f'Методист готов! Ученик: {name} Уровень: {level} Тема: {topic}')
else:      
        
        print ('Ошибка: Неверный формат уровня. Используйте A1 - C2')
