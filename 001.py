import f002
import pyautogui as bot
print('Hello World!!!')
f002.start()
bot.hotkey('win','r')
bot.typewrite('cmd')
bot.press('enter')
f002.finish()