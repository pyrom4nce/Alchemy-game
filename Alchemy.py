import random
import json

# --- Список всех рецептов (кортежи) ---
recipes = [
    ("вода", "огонь", "пар"),
    ("вода", "воздух", "туман"),
    ("вода", "земля", "растение"),
    ("воздух", "воздух", "ветер"),
    ("воздух", "огонь", "пожар"),
    ("воздух", "земля", "пыль"),
    ("земля", "огонь", "лава"),
    ("пар", "воздух", "облако"),
    ("туман", "ветер", "метель"),
    ("растение", "земля", "дерево"),
    ("растение", "вода", "водоросли"),
    ("лава", "вода", "камень"),
    ("лава", "воздух", "обсидиан"),
    ("пыль", "земля", "песок"),
    ("метель", "воздух", "холод"),
    ("песок", "огонь", "стекло"),
    ("дерево", "пожар", "лесной пожар"),
    ("дерево", "огонь", "уголь"),
    ("облако", "вода", "дождь"),
    ("дождь", "ветер", "шторм"),
    ("холод", "огонь", "температура"),
    ("камень", "земля", "гора"),
    ("камень", "дерево", "инструменты"),
    ("обсидиан", "инструменты", "украшения")
]

# --- Список возможных целевых элементов ---
targets = [
    "песок", "стекло", "лесной пожар", "уголь", "дождь",
    "шторм", "температура", "гора", "инструменты", "украшения"
]

# --- Выбираем случайный целевой элемент ---
goal = random.choice(targets)

# --- Стартовый набор элементов ---
elements = ["вода", "огонь", "воздух", "земля"]

moves = 0

print("Добро пожаловать в игру 'Алхимик'!")
print("Ваша цель: создать элемент —", goal)
print("Доступные элементы:", ", ".join(elements))
print("Введите два элемента через пробел. Для выхода напишите 'стоп'.")
print()

def get_hint():
    for r1, r2, result in recipes:
        if recipes == goal:
            if r1 in elements and r2 in elements:
                return f"Попробуйте соединить: {r1} + {r2}"
    return "Подсказок пока нет."

def save_game():
    data = {
        "elements": elements,
        "goal": goal
    }

    with open("save.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Игра сохранена")

while True:
    user_input = input("Смешать: ").lower().strip()

    if user_input == "стоп":
        print("Вы вышли из игры.")
        break

    if user_input == "/hint":
        print("💡", get_hint())
        print()
        continue

    if user_input == "/stats":
        print()
        print("Статистика")
        print("Ходов сделано", moves)
        print("Открыто элементов:", len(elements))
        print()
        continue

    if user_input == "/save":
        save_game()
        print()
        continue

    parts = user_input.split()

    if len(parts) != 2:
        print("Введите ровно два элемента!")
        continue

    a, b = parts[0], parts[1]

    # Проверяем, есть ли элементы у игрока
    if a not in elements:
        print("У вас нет элемента:", a)
        continue
    if b not in elements:
        print("У вас нет элемента:", b)
        continue

    # Ищем рецепт
    result = None
    for r1, r2, res in recipes:
        if (a == r1 and b == r2) or (a == r2 and b == r1):
            result = res
            break

    if result is None:
        print("Ничего не получилось.")
        continue

    print("Получилось:", result)

    # Добавляем новый элемент, если его ещё нет
    if result not in elements:
        elements.append(result)
        print("Новый элемент добавлен в доступные!")

    # Проверяем победу
    if result == goal:
        print("\nПоздравляем! Вы создали целевой элемент:", goal)
        print("Игра окончена.")
        break

    print("Доступные элементы:", ", ".join(elements))
    print()