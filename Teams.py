import os             
import pyautogui
import intervals as I
import time
from time import sleep
from datetime import datetime


try:
	# open MS Teams application
	os.startfile("C:/Users/username/AppData/Local/Microsoft/Teams/current/Teams.exe") 
	sleep(2)
	# settings
	settings = pyautogui.locateCenterOnScreen("settings.PNG") 
	pyautogui.moveTo(settings)
	pyautogui.click()
	time.sleep(2)
	# manageteams.PNG
	manageteams = pyautogui.locateCenterOnScreen("manageteams.PNG") 
	pyautogui.moveTo(manageteams)
	pyautogui.click()
	time.sleep(2)
except Exception as e:
	print(e)

while True:
	#andromeda
	k = datetime.now().strftime("%H")
	now = int(k)
	if now in I.closed(16, 17):
		andromeda = pyautogui.locateCenterOnScreen("Andromeda.PNG") 
		pyautogui.moveTo(andromeda)
		pyautogui.click()
		time.sleep(2)
		join = pyautogui.locateCenterOnScreen("join.PNG") 
		pyautogui.moveTo(join)
		pyautogui.click()
		time.sleep(2)
		audiooff = pyautogui.locateCenterOnScreen("audiooff.PNG") 
		pyautogui.moveTo(audiooff)
		pyautogui.click()
		time.sleep(2)
		if now == 17:
			cut = pyautogui.locateCenterOnScreen("cut.PNG") 
			pyautogui.moveTo(cut)
			pyautogui.click()
			time.sleep(2)
			dismiss = pyautogui.locateCenterOnScreen("dismiss.PNG") 
			pyautogui.moveTo(dismiss)
			pyautogui.click()
			time.sleep(2)
			back = pyautogui.locateCenterOnScreen("back.PNG") 
			pyautogui.moveTo(back)
			pyautogui.click()
			time.sleep(2)
	elif now in I.closed(17, 18):
		automation = pyautogui.locateCenterOnScreen("automation.PNG") 
		pyautogui.moveTo(automation)
		pyautogui.click()
		time.sleep(2)
		join = pyautogui.locateCenterOnScreen("join.PNG") 
		pyautogui.moveTo(join)
		pyautogui.click()
		time.sleep(2)
		audiooff = pyautogui.locateCenterOnScreen("audiooff.PNG") 
		pyautogui.moveTo(audiooff)
		pyautogui.click()
		time.sleep(2)
		if now == 18:
			cut = pyautogui.locateCenterOnScreen("cut.PNG") 
			pyautogui.moveTo(cut)
			pyautogui.click()
			time.sleep(2)
			dismiss = pyautogui.locateCenterOnScreen("dismiss.PNG") 
			pyautogui.moveTo(dismiss)
			pyautogui.click()
			time.sleep(2)
			back = pyautogui.locateCenterOnScreen("back.PNG") 
			pyautogui.moveTo(back)
			pyautogui.click()
			time.sleep(2)