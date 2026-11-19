print("Привет! Я фитнес-бот FitLife.")
user_name = input("Как тебя зовут? ")
print(f"Привет, {user_name}!")
user_age = int(input("Сколько тебе лет? "))
user_weight = float(input("Сколько ты весишь в килограммах? "))
user_height = float(input("Какой у тебя рост в метрах? Например, 1.75: "))

bmi = user_weight / (user_height**2)
bmi = round(bmi, 1)
water_needed = user_weight * 30
water_l = water_needed / 1000
water_l = round(water_l, 2)

print(f"Отчёт для пользователя: {user_name} (возраст: {user_age})")
print(f"Твой индекс массы тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l} л. в день")
print()
print("Расчёт окончен. Будь здоров!")
