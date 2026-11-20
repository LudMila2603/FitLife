WATER_ML_PER_KG = 30
ML_PER_LITER = 1000
BMI_DECIMAL_PLACES = 1
WATER_DECIMAL_PLACES = 2

print("Привет! Я фитнес-бот FitLife.")
user_name = input("Как тебя зовут? ")
print(f"Привет, {user_name}!")

while True:
    age_text = input("Сколько тебе лет? Например, 25: ")
    try:
        user_age = int(age_text)
        if user_age <= 0:
            raise ValueError
        break
    except ValueError:
        print(f"Получено: «{age_text}». Нужен целый возраст больше нуля.")

while True:
    weight_text = input("Сколько ты весишь в кг? Например, 75.5: ")
    try:
        user_weight = float(weight_text)
        if user_weight <= 0:
            raise ValueError
        break
    except ValueError:
        print(f"Получено: «{weight_text}». Введи число больше нуля.")
        print("Дробную часть отделяй точкой, например 75.5.")

while True:
    height_text = input("Какой у тебя рост в метрах? Например, 1.75: ")
    try:
        user_height = float(height_text)
        if user_height <= 0:
            raise ValueError
        break
    except ValueError:
        print(f"Получено: «{height_text}». Введи число больше нуля.")
        print("Укажи рост в метрах через точку, например 1.75.")

bmi = user_weight / (user_height**2)
bmi = round(bmi, BMI_DECIMAL_PLACES)

water_needed = user_weight * WATER_ML_PER_KG
water_l = water_needed / ML_PER_LITER
water_l = round(water_l, WATER_DECIMAL_PLACES)

print()
print(f"Отчёт для пользователя: {user_name} (возраст: {user_age})")
print(f"Твой индекс массы тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l} л. в день")
print()
print("Расчёт окончен. Будь здоров!")
