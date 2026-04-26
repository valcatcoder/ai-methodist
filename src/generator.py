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


#Модуль 3: Анализатор сложности текста

#подсчет слов в тексте + предобработка (без учета регистра и с учетом окончания текста)
s = input ().lower () + ' ' #для пробела в конце текста
total_words = s.count (' ') 
print (total_words)

#идентификация грамматических маркеров и complexity index на их основе

count_ed = s.count('ed ')
count_ing = s.count('ing ')
print (count_ed)
print (count_ing)

total_markers =  (count_ed) + (count_ing)
print (total_markers)

if total_words > 1: 
  complexity_index = ((total_markers) / (total_words) ) * 100
  print ("Индекс сложности:", round(complexity_index, 2), "%")
else: 
  print ("Текст не введен")

#Модуль 4:

#очистка текста от символов, знаков и чувствительности к регистру

raw_text = input().lower ()
punctuation_del = ("{}[].,!?:;()")
clean_chars = []

for char in (raw_text):
    if char not in punctuation_del:
        clean_chars.append (char)
print (clean_chars) 

clean_text ="".join (clean_chars)
print (clean_text) 

clean_text_list = clean_text.split()
print (clean_text_list)



