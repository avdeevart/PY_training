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
    found_contacts = [(i, contact) for i, contact in enumerate(contacts) if any(field.lower().startswith(keyword) for field in contact)]

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
    found_contacts = [(i, contact) for i, contact in enumerate(contacts) if any(field.lower().startswith(keyword) for field in contact)]

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
