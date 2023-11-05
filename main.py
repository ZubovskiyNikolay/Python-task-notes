import json

data = []
PATH = 'data.json'

with open(PATH, 'r', encoding='UTF-8') as file:
     data = json.load(file)

def save_data(data):
    with open(PATH, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def find_data(date_find):
    for items in data:
        if items['Дата'] == date_find:
            print("\nНашел: " + items['Дата'])
            print(items)
            # return
    # print("\nЗаметок нет!")

def del_data(del_id):

    for items in data:
        if items['id'] == del_id:
            data.remove(items)
            save_data(data)
            print("\nЗаметка удалена")
            return
    print("\nЗметка не найдена")

def print_data():
    for items in data:
        print()
        print(f"id: {items['id']}")
        print(f"Название: {items['Название']}")
        print(f"Содержание: {items['Содержание']}")
        print(f"Дата: {items['Дата']}")
        print(f"Время: {items['Время']}")
    print()
def edit_data(ch_id):
   for items in data:
        if items['id'] == ch_id:
            new_name = input("Название: ")
            new_content = input("Содержимое: ")
            new_data = input("Дата: ")
            new_time = input("Время: ")
            items['Название'] = new_name
            items['Содержание'] = new_content
            items['Дата'] = new_data
            items['Время'] = new_time
            save_data(data)
            print("\nЗаметка успешно сохранена\n")
            return
   print("\nid заметки не найдена")

def menu():
    menu_points = ['Добавить заметку',
                   'Редактировать заметку',
                   'Удалить заметку',
                   'Найти заметку',
                   'Список всех заметок',
                   'Выход']
    print('\nГлавное меню')
    [print(f'\t{i}.{item}') for i, item in enumerate(menu_points, 1)]
    choice = int(input('\nВыберите пункт меню: '))
    return choice


while True:
    choice = menu()
    match choice:
        case 1:
             id = input("\nid: ")
             name = input("Название: ")
             content = input("Содержание: ")
             date = input("Дата: ")
             time = input("Время: ")
             new = {
                'id': id,
                'Название': name,
                'Содержание': content,
                'Дата': date,
                'Время': time
              }
             data.append(new)
             save_data(data)
        case 2:
            ch_id = input("\nВведите id заметки для редактирования: ")
            edit_data(ch_id)
        case 3:
            del_id = input("\nВведите id для удаления: ")
            del_data(del_id)
        case 4:
            date_find = input("\nВведите дату заметки ДД/ММ/ГГ: ")
            find_data(date_find)
        case 5:
            print_data()
        case 6:
            print('\nДо свидания!')
            break
