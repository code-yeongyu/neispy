from neispy import *
day = int(input("덕현중학교의 급식이 궁금하세요? 무슨요일 급식이 궁금하세요?\n월 : 0, 화 : 1, 수 : 2, 목 : 3, 금 : 4\n여기에 입력하세요 : "))
if day < 0 or day > 4 :
    print("수를 제대로 입력해주세요.")
    exit()
day = day + 7
o = get_meals(day, "J100005133")
print(o)