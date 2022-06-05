# Imports
import time
import random
import csv


def main():
    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
    user_name = get_user_name()
    print(f"Nice to meet you, {user_name}! Please answer the questions.")

    # Get user info
    user_weight = get_user_weight()
    user_height = get_user_height()
    user_age = get_user_age()
    user_gender = input("Gender[male, female]: ").lower()
    calories = calculate_daily_calorie_intake(
        user_gender, user_age, user_height, user_weight)
    carbs, protein, fat = get_carbs_protein_fat(calories)

    products = []

    with open('products.csv') as database:
        reader = csv.DictReader(database)
        for product in reader:
            product['calories'] = int(product['calories'])
            product['fat'] = int(product['fat'])
            product['carb'] = int(product['carb'])
            product['protein'] = int(product['protein'])
            products.append(product)

    print(
        f"Your ideal daily intakes are: \nCalories: {calories}.\nFat: {fat}.\nCarbs: {carbs}.\nProtein: {protein}.\n")

    for day in range(7):
        print("Recommended products on " + days[day] + ".", end="\n")
        product_list = get_list(products, calories, carbs, protein, fat)
        for line in product_list:
            print(line["product"].title(), end=", ")
        print("\n")


def get_user_name():
    print("Welcome To Healthy!")
    time.sleep(2)

    while True:
        try:
            name = (input("Please enter your name: "))
            if name.isnumeric():
                raise ValueError
            return name

        except ValueError:
            print("Invalid input. Please try again.")
            continue


def get_user_age():
    while True:
        try:
            age = int((input("Please enter your age: ")))
            return age

        except ValueError:
            print("Invalid input. Please try again.")
            continue


def get_user_weight():
    while True:
        try:
            age = int((input("Please enter your weight (kg): ")))
            return age

        except ValueError:
            print("Invalid input. Please try again.")
            continue


def get_user_height():
    while True:
        try:
            age = int((input("Please enter your height (cm): ")))
            return age

        except ValueError:
            print("Invalid input. Please try again.")
            continue


def calculate_daily_calorie_intake(user_gender, user_age, user_height, user_weight):
    # Miffin-St Jeor Equation
    if user_gender == 'male':
        calories = round(10*user_weight + 6.25*user_height - 5 * user_age + 5)
    elif user_gender == 'female':
        calories = round(10*user_weight + 6.25 *
                         user_height - 5 * user_age - 161)
    return calories


def get_carbs_protein_fat(calories):
    if calories <= 1000:
        carbs = 130
        protein = 45
        fat = 36
    elif calories > 1000 and calories <= 1100:
        carbs = 143
        protein = 50
        fat = 39
    elif calories > 1100 and calories <= 1200:
        carbs = 156
        protein = 54
        fat = 43
    elif calories > 1200 and calories <= 1300:
        carbs = 169
        protein = 59
        fat = 46
    elif calories > 1300 and calories <= 1400:
        carbs = 182
        protein = 63
        fat = 50
    elif calories > 1400 and calories <= 1500:
        carbs = 195
        protein = 68
        fat = 53
    elif calories > 1500 and calories <= 1600:
        carbs = 208
        protein = 72
        fat = 57
    elif calories > 1600 and calories <= 1700:
        carbs = 221
        protein = 77
        fat = 60
    elif calories > 1700 and calories <= 1800:
        carbs = 234
        protein = 81
        fat = 64
    elif calories > 1800 and calories <= 1900:
        carbs = 247
        protein = 86
        fat = 68
    elif calories > 1900 and calories <= 2000:
        carbs = 260
        protein = 90
        fat = 71
    elif calories > 2000 and calories <= 2100:
        carbs = 273
        protein = 95
        fat = 71
    elif calories > 2100 and calories <= 2200:
        carbs = 286
        protein = 99
        fat = 78
    elif calories > 2200 and calories <= 2300:
        carbs = 299
        protein = 104
        fat = 82
    elif calories > 2300 and calories <= 2400:
        carbs = 312
        protein = 108
        fat = 85
    elif calories > 2400 and calories <= 2500:
        carbs = 325
        protein = 113
        fat = 89
    return carbs, protein, fat


def get_list(products, calories, carbs, protein, fat):
    product_list = []
    temp_cal = 0
    temp_carb = 0
    temp_pro = 0
    temp_fat = 0
    while temp_cal <= calories and (temp_carb <= carbs or temp_pro or protein or temp_fat <= fat):
        random_product = random.choice(products)
        temp_cal += random_product['calories']
        temp_carb += random_product['fat']
        temp_pro += random_product['carb']
        temp_fat += random_product['protein']
        if random_product not in product_list:
            product_list.append(random_product)
    return product_list


if __name__ == '__main__':
    main()
