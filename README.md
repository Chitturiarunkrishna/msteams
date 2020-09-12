# Automating MS Teams

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
python teams.py

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

 - A clear explaination is available in this  [post](https://dev.to/chitturiarunkrishna/automating-ms-teams-43n6)

License
----
MIT
**Free Software, Hell Yeah!**
