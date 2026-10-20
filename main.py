# Лабораторна робота №5, варіант 5
# Завдання 1: чи починається рядок з https:// і далі є текст без пробілів
# Завдання 2: виділити HOST із рядка https://HOST/PATH
# Підвищена складність №5: знайти всі збіги сигнатури (з перекриттям)

PREFIX = "https://"

# ---------- Завдання 1 ----------
print("Завдання 1")
text = input("Введіть рядок: ")   # рядок не обрізаємо, пробіли важливі
rest = text[len(PREFIX):]
has_space = any(ch.isspace() for ch in rest)
if text[:len(PREFIX)].lower() == PREFIX and rest != "" and not has_space:
    print("Так")
else:
    print("Ні")

# ---------- Завдання 2 ----------
print("\nЗавдання 2")
url = input("Введіть рядок https://HOST/PATH: ")
if url[:len(PREFIX)].lower() != PREFIX:
    print("Помилка: рядок має починатися з https://")
elif any(ch.isspace() for ch in url):
    print("Помилка: рядок не повинен містити пробілів")
else:
    host = url[len(PREFIX):].split("/")[0]   # усе до першого "/"
    if host == "":
        print("Помилка: HOST порожній")
    else:
        print(host)

# ---------- Підвищена складність №5 ----------
print("\nПошук усіх збігів")
text = input("Введіть текст: ")
signature = input("Введіть сигнатуру: ")
if signature == "":
    print("Помилка: сигнатура не може бути порожньою")
else:
    indexes = []
    pos = text.find(signature)
    while pos != -1:
        indexes.append(pos)
        pos = text.find(signature, pos + 1)   # +1, щоб знаходити збіги, що перекриваються
    if indexes:
        print("Індекси:", ", ".join(str(i) for i in indexes))
    else:
        print("Не знайдено")
    print("Кількість:", len(indexes))
