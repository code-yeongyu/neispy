import telebot, time, datetime, neispy, api_key

x = 0

API_TOKEN = api_key.API_TOKEN
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message) :
    bot.reply_to(message, "경기도 양주시에 위치한, 덕현중학교의 급식을 받아오는 텔레그램 봇 입니다.\n나이스 홈페이지에서 식단표를 파싱해옵니다.")
    bot.reply_to(message, "명령어 목록\n/week 이번주의 급식을 모두 받기")

@bot.message_handler(commands=['week'])
def send_meal(message) :
    for i in range(7, 12) :
        if i == 7 :
            st = "--월--"
        elif i == 8 :
            st = "--화--"
        elif i == 9 :
            st = "--수--"
        elif i == 10 :
            st = "--목--"
        elif i == 11 :
            st = "--금--"
        #send weekday

        bot.reply_to(message, st)
        m = neispy.meals(i)
        m.get_meals_menu()
        meal = m.return_meals_menu()
        bot.reply_to(message, meal)

#Prevent exiting
bot.polling()
