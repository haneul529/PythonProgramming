import ch09_aex02_2

ch09_aex02_2.DoIt()

date1 = input("시작 날짜(연/월/일) --> ")
date2 = input("끝 날짜(연/월/일) --> ")

diffDays = ch09_aex02_2.countDays(date1, date2)
print(date1, '부터 ', date2, '까지는 ', diffDays, '일입니다.')