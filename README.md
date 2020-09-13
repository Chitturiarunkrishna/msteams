# Automating MS Teams

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) [![ForTheBadge built-by-Me](http://ForTheBadge.com/images/badges/built-by-developers.svg)](https://github.com/Chitturiarunkrishna/)  [![Generic badge](https://img.shields.io/github/license/Chitturiarunkrishna/msteams)](https://github.com/Chitturiarunkrishna/msteams) [![Generic badge](https://img.shields.io/github/stars/Chitturiarunkrishna/msteams)](https://github.com/Chitturiarunkrishna/msteams) [![Generic badge](https://img.shields.io/github/forks/Chitturiarunkrishna/msteams)](https://github.com/Chitturiarunkrishna/msteams) [![Generic badge](https://img.shields.io/github/issues/Chitturiarunkrishna/msteams)](https://github.com/Chitturiarunkrishna/msteams) [![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/Chitturiarunkrishna/msteams)

Most of us are aware that Teams is a video conferencing app which allows us to attend/conduct meetings. And because of this pandemic situation, the usage of these video conferencing apps also increased and most of the classes and lectures and conferences are conducted in Teams now a days.

# New Features!

  Let us see how I have automated Teams so that it automatically logs into one's meetings/classes on time.

# Pre-requisites:
Microsoft Teams application - Download the exe file from official website
Python 3.x
Pyautogui
Intervals

# Install Packages:
```sh
pip install pyautogui
pip install python-intervals
```

# Execution:
```sh
python teams.py
```

# Working (Behind the scenes) :
> An infinite loop keeps checking the current time of the system using datetime.now() funtion.
> The Teams app is opened using os.startfile().
> pyautogui.locateCenterOnScreen() function locates the center of the first found instance of the image on the screen.
> pyautogui.moveTo() moves the cursor to that location.
> pyautogui.click() performs a click operation.
> Intervals package is used to set hourly intervals

This text you see here is *actually* written in Markdown! To get a feel for Markdown's syntax, type some text into the left window and watch the results in the right.

### Tech

* [Python](https://www.python.org/) - Python 3.x


### Explaination

### PyAutoGUI
PyAutoGUI is a cross-platform GUI automation Python module. It programmatically controls the mouse & keyboard. It has screen shot features and also image finding features.

Before using the script make sure that the Teams application is closed in such a way that all the teams are displayed as shown in the below figure.

![Teams2](https://user-images.githubusercontent.com/36875148/93000449-38f02700-f546-11ea-8088-f10f4f173ab1.png)

### Import the necessary modules

```sh
import os             
import pyautogui
import intervals as I
import time
from time import sleep
from datetime import datetime
```

### Open Teams

```sh
os.startfile("C:/Users/username/AppData/Local/Microsoft/Teams/current/Teams.exe") 
```

Next, take the screenshot of settings button and use the below chunk of code to move the mouse to that button and click it.

![settings](https://user-images.githubusercontent.com/36875148/93000496-781e7800-f546-11ea-90cb-634493b0ed0f.PNG)

```sh
settings = pyautogui.locateCenterOnScreen("settings.PNG") 
pyautogui.moveTo(settings)
pyautogui.click()
time.sleep(2)
```

Now we need to click on Manage Teams button to get a list of teams vertically.

![manageteams](https://user-images.githubusercontent.com/36875148/93000513-92585600-f546-11ea-9e75-b198ebef85b5.PNG)

```sh
manageteams = pyautogui.locateCenterOnScreen("manageteams.PNG") 
pyautogui.moveTo(manageteams)
pyautogui.click()
time.sleep(2)
```

then we will get the screen like this

![Teams](https://user-images.githubusercontent.com/36875148/93000523-aa2fda00-f546-11ea-804b-fa210f77c472.png)

Now we run the below code snippet in an infintie loop.

We get the current time and compare it with the class ending time . For example if current time is 17:00 and my class is at 17:00 but the meeting has started. If I give my class ending time i.e 18:00 then as soon as meeting starts the scripts automatically clicks on join button with camera and microphone turned off.

Join button is given below.

![join](https://user-images.githubusercontent.com/36875148/93000545-d0557a00-f546-11ea-8793-cf9779d1d177.PNG)

Camera and microphone button is given below.

![audiooff](https://user-images.githubusercontent.com/36875148/93000557-e82cfe00-f546-11ea-8522-501bc74f2620.PNG)

Similarily take the screenshot of your class name too.

![Andromeda](https://user-images.githubusercontent.com/36875148/93000587-04309f80-f547-11ea-911b-5b78f15c9eb5.PNG)

```sh
if now < '18:00':
    Andromeda =pyautogui.locateCenterOnScreen("Andromeda.PNG") 
    pyautogui.moveTo(Andromeda)
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
```

Similarily you can do it for n number of classes. In the below code I have done it for 2 classes.

```sh
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
    now = datetime.now().strftime("%H:%M")
    if now < '18:00':
        Andromeda = pyautogui.locateCenterOnScreen("Andromeda.PNG") 
        pyautogui.moveTo(Andromeda)
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
    elif now <'17:00': 
        Automation = pyautogui.locateCenterOnScreen("Automation.PNG") 
        pyautogui.moveTo(Automation)
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
```

Suppose if you want to set the time interval and check for meeting to start and then join please see this

```sh
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
```

### Then the entire code is in Teams.py file

License
----
MIT
**Free Software, Hell Yeah!**
