second = 0
minute = 0
hour = 0
day = 0
for _ in range(4):
    dur = int(input("duration = "))
    if dur < 60:
        print(dur, "сек")
    elif 60 <= dur < 3600:
        minute = dur // 60
        second = dur % 60
        print(minute, "мин", second, "сек")
    elif 3600 <= dur < 86400:
        hour = dur // 3600
        dur %= 3600
        minute = dur // 60
        second = dur % 60
        print(day, "дней", hour, "час", minute, "мин", second, "сек")