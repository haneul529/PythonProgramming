money, w50, w10, w5, w1 = 0, 0, 0, 0, 0

money = int(input("지폐로 교환할 돈은 얼마?"))

w50 = money // 50000
money %= 50000

w10 = money // 10000
money %= 10000

w5 = money // 5000
money %= 5000

w1 = money // 1000
money %= 1000

print("50000원짜리 ==> %d장" % w50)
print("10000원짜리 ==> %d장" % w10)
print("5000원짜리 ==> %d장" % w5)
print("1000원짜리 ==> %d장" % w1)
print("제폐로 바꾸지 못한 돈 ==> %d원" % money)
