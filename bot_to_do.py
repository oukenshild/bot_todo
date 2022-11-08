import random
from package_data.data import help, tasks, random_tasks


class Todolist:
    def __init__(self, date, task):
        self.date = date
        self.task = task

    @classmethod
    def help_todo(cls):
        print(help)

    @classmethod
    def add_todo(cls):
        date = input('Введите дату для добавления задачи: ')
        task = input('Введите название задачи: ')
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

    @classmethod
    def show_todo(cls):
        date = input('Введите дату для отображения списка задач: ')
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        else:
            print('Такой даты нет')


def main():
    todolist = Todolist('26 ноября', 'Помыть голову')
    print('Приветствую!')
    while True:
        command = input('Введите команду: ')
        if command == 'help':
            todolist.help_todo()
        elif command == 'show':
            todolist.show_todo()
        elif command == 'add':
            todolist.add_todo()
        elif command == 'random':
            task = random.choice(random_tasks)
            todolist.add_todo('Сегодня', task)
        elif command == 'random_date':
            todolist.add_todo(date, random_tasks)
        elif command == 'exit':
            print('Спасибо за использование! До свидания!')
            break
        else:
            print('Неизвестная команда')
            break


if __name__ == '__main__':
    main()
