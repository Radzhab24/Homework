for i in range(1, 101):
    if 10 < i < 20:
        print(f"{i} процентов")
    elif i % 10 == 1:
        print(f"{i} процент")
    elif i % 10 == 2 or i % 10 == 3 or i % 10 == 4:
        print(f"{i} процента")
    else:
        print(f"{i} процентов")