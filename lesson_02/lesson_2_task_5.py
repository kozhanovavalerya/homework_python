def month_to_season(month_num):
    if month_num in [12, 1, 2]:
        print("Зима")
    elif month_num in [3, 4, 5]:
        print("Весна")
    elif month_num in [6, 7, 8]:
        print("Лето")
    else:
        print("Осень")
