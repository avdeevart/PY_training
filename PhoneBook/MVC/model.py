import csv

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

# Функция для поиска контактов по ключевому слову
def search_contacts(contacts, keyword):
    keyword = keyword.lower()
    found_contacts = [contact for contact in contacts if any(field.lower().startswith(keyword) for field in contact)]
    return found_contacts
