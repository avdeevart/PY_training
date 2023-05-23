import csv
import os

# Функция для загрузки контактов из CSV-файла
def load_contacts(file_name):
    contacts = []
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        pass
    return contacts

# Функция для сохранения контактов в CSV-файл
def save_contacts(file_name, contacts):
    with open(file_name, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

# Функция для вывода контактов на экран
def display_contacts(contacts):
    if not contacts:
        print("Нет доступных контактов.")
    else:
        # Вывод заголовка таблицы контактов
        print("{:<4} {:<14} {:<12} {:<14} {:<18}".format("№", "Фамилия", "Имя", "Отчество", "Номер телефона"))
        print("-" * 70)
        # Вывод каждого контакта в форматированной таблице
        for i, contact in enumerate(contacts, start=1):
            last_name, first_name, patronymic, phone_number = contact
            print("{:<4} {:<14} {:<12} {:<14} {:<18}".format(i, last_name, first_name, patronymic, phone_number))
        print("-" * 70)

# Функция для поиска контактов по ключевому слову
def search_contacts(contacts, keyword):
    keyword = keyword.lower()
    found_contacts = []
    for contact in contacts:
        # Проверка, начинается ли хотя бы одно поле контакта с ключевого слова
        if any(field.lower().startswith(keyword) for field in contact):
            found_contacts.append(contact)
    return found_contacts

# Функция для добавления нового контакта
def add_contact(contacts):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    contact = [last_name, first_name, patronymic, phone_number]
    contacts.append(contact)
    print("Контакт успешно добавлен.")

# Функция для редактирования контакта
def edit_contact(contacts, keyword):
    keyword = keyword.lower()
    found_contacts = []
    for i, contact in enumerate(contacts):
        if any(field.lower().startswith(keyword) for field in contact):
            found_contacts.append((i, contact))

    if not found_contacts:
        print("Контакты не найдены.")
    else:
        print("Найденные контакты:")
        display_contacts([contact for _, contact in found_contacts])

        choice = input("Введите номер контакта для редактирования: ")
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(found_contacts):
            print("Некорректный выбор контакта.")
            return

        index = int(choice) - 1
        _, contact = found_contacts[index]
        print("Текущая информация о контакте:")
        display_contacts([contact])

        new_last_name = input("Введите новую фамилию (оставьте пустым для без изменений): ")
        new_first_name = input("Введите новое имя (оставьте пустым для без изменений): ")
        new_patronymic = input("Введите новое отчество (оставьте пустым для без изменений): ")
        new_phone_number = input("Введите новый номер телефона (оставьте пустым для без изменений): ")

        # Обновление информации о контакте, если были введены новые значения
        if new_last_name:
            contact[0] = new_last_name
        if new_first_name:
            contact[1] = new_first_name
        if new_patronymic:
            contact[2] = new_patronymic
        if new_phone_number:
            contact[3] = new_phone_number

        print("Контакт успешно отредактирован.")

# Функция для удаления контакта
def delete_contact(contacts, keyword):
    keyword = keyword.lower()
    found_contacts = []
    for i, contact in enumerate(contacts):
        if any(field.lower().startswith(keyword) for field in contact):
            found_contacts.append((i, contact))

    if not found_contacts:
        print("Контакты не найдены.")
    else:
        print("Найденные контакты:")
        display_contacts([contact for _, contact in found_contacts])

        choice = input("Введите номер контакта для удаления: ")
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(found_contacts):
            print("Некорректный выбор контакта.")
            return

        index = int(choice) - 1
        _, contact = found_contacts[index]
        contacts.remove(contact)

        print("Контакт успешно удален.")

# Основная функция программы
def main():
    # Определение пути к файлу контактов
    file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contacts.csv")
    # Загрузка контактов из файла
    contacts = load_contacts(file_name)

    while True:
        # Вывод меню с возможными действиями
        print("1. Вывести все контакты")
        print("2. Добавить контакт")
        print("3. Сохранить контакты")
        print("4. Поиск контактов")
        print("5. Редактировать контакт")
        print("6. Удалить контакт")
        print("7. Выйти")

        choice = input("Выберите действие (1-7): ")
        print()

        if choice == "1":
            # Вывод всех контактов
            display_contacts(contacts)
        elif choice == "2":
            # Добавление нового контакта
            add_contact(contacts)
        elif choice == "3":
            # Сохранение контактов в файл
            save_contacts(file_name, contacts)
            print("Контакты успешно сохранены.")
        elif choice == "4":
            # Поиск контактов по ключевому слову
            keyword = input("Введите ключевое слово для поиска: ")
            found_contacts = search_contacts(contacts, keyword)
            display_contacts(found_contacts)
        elif choice == "5":
            # Редактирование контакта
            keyword = input("Введите ключевое слово для поиска: ")
            edit_contact(contacts, keyword)
        elif choice == "6":
            # Удаление контакта
            keyword = input("Введите ключевое слово для поиска: ")
            delete_contact(contacts, keyword)
        elif choice == "7":
            # Выход из программы
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите действие от 1 до 7.")

# Запуск основной функции программы
if __name__ == "__main__":
    main()
