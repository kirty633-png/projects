import sqlite3

db = sqlite3.connect("students.db")
cur = db.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    grade TEXT
)
""")

db.commit()


def get_name():
    while True:
        name = input("Ім'я: ").strip()

        if name.replace(" ", "").isalpha():
            return name

        print("❌ Ім'я повинно містити тільки літери!")


def get_age():
    while True:
        age = input("Вік: ")

        if age.isdigit() and 5 <= int(age) <= 100:
            return int(age)

        print("❌ Вік має бути числом (5–100)!")


def get_grade():
    while True:
        grade = input("Клас (наприклад 9-А): ").strip()

        if len(grade) >= 2:
            return grade

        print("❌ Невірний формат класу!")


while True:
    print("\n" + "=" * 35)
    print("      СИСТЕМА ОБЛІКУ УЧНІВ")
    print("=" * 35)
    print("1. Додати учнів")
    print("2. Показати всіх учнів")
    print("3. Пошук учнів")
    print("4. Видалити учнів")
    print("5. Вихід")

    choice = input("\nОберіть пункт: ")

    # ДОБАВЛЕННЯ
    if choice == "1":
        count = input("Скільки учнів додати? ")

        if not count.isdigit():
            print("❌ Треба число!")
            continue

        count = int(count)

        for i in range(count):
            print(f"\nУчень #{i + 1}")

            name = get_name()
            age = get_age()
            grade = get_grade()

            cur.execute(
                "INSERT INTO students(name, age, grade) VALUES(?,?,?)",
                (name, age, grade)
            )

        db.commit()
        print(f"\n✅ Додано {count} учнів!")

    # ПОКАЗАТИ ВСІХ
    elif choice == "2":
        cur.execute("SELECT * FROM students")
        data = cur.fetchall()

        print("\n=== СПИСОК УЧНІВ ===")

        if not data:
            print("Список порожній.")
        else:
            for s in data:
                print(f"ID:{s[0]} | {s[1]} | {s[2]} років | {s[3]}")

    # ПОШУК
    elif choice == "3":
        name = input("Ім'я (Enter пропустити): ")
        grade = input("Клас (Enter пропустити): ")

        sql = "SELECT * FROM students WHERE 1=1"
        params = []

        if name:
            sql += " AND name LIKE ?"
            params.append(f"%{name}%")

        if grade:
            sql += " AND grade LIKE ?"
            params.append(f"%{grade}%")

        cur.execute(sql, params)
        result = cur.fetchall()

        print("\n=== РЕЗУЛЬТАТ ===")

        if result:
            for s in result:
                print(f"ID:{s[0]} | {s[1]} | {s[2]} | {s[3]}")
        else:
            print("❌ Нічого не знайдено")

    # ВИДАЛЕННЯ
    elif choice == "4":
        ids = input("ID через кому: ").split(",")

        deleted = 0

        for i in ids:
            if i.strip().isdigit():
                cur.execute("DELETE FROM students WHERE id=?", (int(i),))
                deleted += cur.rowcount

        db.commit()
        print(f"✅ Видалено {deleted} учнів")

    # ВИХІД
    elif choice == "5":
        print("👋 Вихід...")
        break

    else:
        print("❌ Невірний вибір!")

db.close()