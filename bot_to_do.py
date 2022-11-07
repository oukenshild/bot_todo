import random
from package_data.data import help, tasks, random_tasks


class Todolist:
    def __init__(self, date, task):
        self.date = date
        self.task = task

    @classmethod
    def help_todo(cls):
        print(help)

    def add_todo(self, date, task):
        if date in tasks:
            # Дата есть в словаре
            # Добавляем в список задачу
            tasks[date].append(task)
        else:
            # Даты в словаре нет
            # Создаем запись с ключом date
            tasks[date] = []
            tasks[date].append(task)
        print('Задача', task, 'добавлена на дату', date)


def main():
    todolist = Todolist('26 ноября', 'Помыть голову')
    print('Приветствую!')
    while True:
        command = input('Введите команду: ')
        if command == 'help':
            todolist.help_todo()
        elif command == 'show':
            date = input('Введите дату для отображения списка задач: ')
            if date in tasks:
                for task in tasks[date]:
                    print('- ', task)
            else:
                print('Такой даты нет')
        elif command == 'add':
            date = input('Введите дату для добавления задачи: ')
            task = input('Введите название задачи: ')
            todolist.add_todo()
        elif command == 'exit':
            print('Спасибо за использование! До свидания!')
            break
        elif command == 'random':
            task = random.choice(random_tasks)
            todolist.add_todo('Сегодня', task)
        elif command == 'random_date':
            todolist.add_todo(date, random_tasks)
        else:
            print('Неизвестная команда')
            break


if __name__ == '__main__':
    main()
