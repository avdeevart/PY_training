import os
import model
import view

# Основная функция программы
def main():
    # Определение пути к файлу контактов
    file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contacts.csv")
    # Загрузка контактов из файла
    contacts = model.load_contacts(file_name)

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
            view.display_contacts(contacts)
        elif choice == "2":
            # Добавление нового контакта
            view.add_contact(contacts)
        elif choice == "3":
            # Сохранение контактов в файл
            model.save_contacts(file_name, contacts)
            print("Контакты успешно сохранены.")
        elif choice == "4":
            # Поиск контактов по ключевому слову
            keyword = input("Введите ключевое слово для поиска: ")
            found_contacts = model.search_contacts(contacts, keyword)
            view.display_contacts(found_contacts)
        elif choice == "5":
            # Редактирование контакта
            keyword = input("Введите ключевое слово для поиска контакта: ")
            view.edit_contact(contacts, keyword)
        elif choice == "6":
            # Удаление контакта
            keyword = input("Введите ключевое слово для поиска контакта: ")
            view.delete_contact(contacts, keyword)
        elif choice == "7":
            # Выход из программы
            break
        else:
            print("Некорректный выбор.")

        print()

    print("Программа завершена.")

if __name__ == "__main__":
    main()
