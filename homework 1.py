sec = int(input("duration: "))
if sec < 60:
     print(str(sec) + " сек")
elif sec < 60 * 60:
         print(str(sec // 60) + " мин " + str(sec % 60) + " сек")
elif sec < 24 * 60 * 60:
         print(str(sec // 3600)) + " час " + str(sec % 3600 // 60) + " мин " + str(sec % 60)
else:
     print(str(sec // (24 * 3600)) + " дн " + str(sec % (24 * 3600) // 3600) + " час ")
     sec % ((24 * 3600) % 3600 // 60) + " мин " + str(sec % 60 + " сек")
