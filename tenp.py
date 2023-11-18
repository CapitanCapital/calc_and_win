# Объявите класс Quest с методами и свойствами.
...
# В этих переменных содержатся значения, которые нужно передать
# в качестве аргументов в экземпляр класса Quest.
quest_name = 'Сбор пиксельники'
quest_goal = 'Соберите 12 ягод пиксельники.'
quest_description = '''
В древнем лесу Кодоборье растёт ягода "пиксельника".
Она нужна для приготовления целебных снадобий.
Соберите 12 ягод пиксельники.'''

from datetime import datetime
import time

class Quest:
    def __init__(self, name, description, goal):
        self.name = name
        self.description = description
        self.goal = goal
        self.start_time = None
        self.end_time = None

    def accept_quest(self):
        if self.end_time == None:
            self.start_time = datetime.now()
            return(f'Начало "{self.name}" положено.')
        else:
            return('С этим испытанием вы уже справились.')

    def pass_quest(self):
        if self.start_time != None:
            self.end_time = datetime.now()
            completion_time = self.end_time - self.start_time
            return(f'Квест "{self.name}" окончен. Время выполнения квеста: {completion_time}')
        else:
            return('Нельзя завершить то, что не имеет начала!')
    
    def __str__(self):
        if self.start_time != None and self.end_time != None:
            return(f'Цель квеста {self.name} - {self.goal}. Квест завершён.')
        else:
            return(f'Цель квеста {self.name} - {self.goal}. Квест выполняется.')

        

# Создайте экземпляр класса Quest.
new_quest = Quest(quest_name, quest_description, quest_goal)

print(new_quest.pass_quest())
print(new_quest.accept_quest())
time.sleep(3)
print(new_quest.pass_quest())
print(new_quest.accept_quest())

print(new_quest)