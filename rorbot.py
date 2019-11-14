import telepot
token = '844016178:AAG97jlj1Al_kyNbPCvVO7pZ_clyX-epIqo'
TelegramBot = telepot.Bot(token)

print(TelegramBot.getMe())