import csv
import os


def load_contacts(file_name):
    """
    Загружает контакты из файла.

    Параметры:
        file_name (str): Имя файла.

    Возвращает:
        list: Список контактов.
    """
    contacts = []
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        pass
    return contacts


def save_contacts(file_name, contacts):
    """
    Сохраняет контакты в файле.

    Параметры:
        file_name (str): Имя файла.
        contacts (list): Список контактов.
    """
    with open(file_name, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)


def display_contacts(contacts):
    """
    Выводит контакты на экран в формате телефонного справочника.

    Параметры:
        contacts (list): Список контактов.
    """
    if not contacts:
        print("Нет доступных контактов.")
    else:
        print("{:<14} {:<12} {:<14} {:<18}".format("Фамилия", "Имя", "Отчество", "Номер телефона"))
        print("-" * 60)
        for contact in contacts:
            last_name, first_name, patronymic, phone_number = contact
            print("{:<14} {:<12} {:<14} {:<18}".format(last_name, first_name, patronymic, phone_number))
        print("-" * 60)




def search_contacts(contacts, keyword):
    """
    Ищет контакты по заданному ключевому слову.

    Параметры:
        contacts (list): Список контактов.
        keyword (str): Ключевое слово для поиска.

    Возвращает:
        list: Список найденных контактов.
    """
    keyword = keyword.lower()
    found_contacts = []
    for contact in contacts:
        if any(keyword in field.lower() for field in contact):
            found_contacts.append(contact)
    return found_contacts


def main():
    file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contacts.csv")
    contacts = load_contacts(file_name)

    while True:
        print("1. Вывести все контакты")
        print("2. Добавить контакт")
        print("3. Сохранить контакты")
        print("4. Поиск контактов")
        print("5. Выйти")

        choice = input("Выберите действие (1-5): ")
        print()

        if choice == "1":
            display_contacts(contacts)
        elif choice == "2":
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            patronymic = input("Введите отчество: ")
            phone_number = input("Введите номер телефона: ")
            contact = [last_name, first_name, patronymic, phone_number]
            contacts.append(contact)
            print("Контакт успешно добавлен.")
        elif choice == "3":
            save_contacts(file_name, contacts)
            print("Контакты успешно сохранены.")
        elif choice == "4":
            keyword = input("Введите ключевое слово для поиска: ")
            found_contacts = search_contacts(contacts, keyword)
            display_contacts(found_contacts)
        elif choice == "5":
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите действие от 1 до 5.")


if __name__ == "__main__":
    main()
