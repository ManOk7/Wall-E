# Wall-E Virtual Assistant

Wall-E is a Python-based **voice-controlled virtual assistant** that can
perform tasks such as:\
- Answering questions using **Wikipedia**\
- Opening websites like YouTube, Chrome, KV Noida site\
- Controlling **system volume** (increase, decrease, mute)\
- Starting the **webcam**\
- Telling the **time**\
- Joining **Microsoft Teams classes** automatically\
- Introducing itself and interacting with the user

------------------------------------------------------------------------

## 🚀 Features

-   **Voice Interaction**: Uses `speech_recognition` and `pyttsx3` for
    natural interaction.\
-   **Task Automation**: Automates Chrome, websites, and MS Teams via
    Selenium.\
-   **Audio Control**: Adjusts system volume with `pycaw`.\
-   **Webcam Control**: Starts webcam feed with `OpenCV`.\
-   **Classroom Automation**: Logs in and joins Teams classes with
    stored credentials.

------------------------------------------------------------------------

## 📦 Requirements

Make sure you have **Python 3.8+** installed. Install dependencies
using:

``` bash
pip install pyttsx3 SpeechRecognition wikipedia selenium pycaw opencv-python comtypes
```

Additionally, install:\
- **Google Chrome** (latest version)\
- **ChromeDriver** matching your Chrome version ([Download
here](https://chromedriver.chromium.org/downloads))

------------------------------------------------------------------------

## ⚙️ Setup

1.  Clone or download this repository.\

2.  Update your **Teams credentials** in the script:

    ``` python
    CREDS = {
        'email': 'your_email@domain.com',
        'passwd': 'your_password'
    }
    ```

3.  Update the **path to ChromeDriver**:

    ``` python
    driver = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe")
    ```

4.  Run the script:

    ``` bash
    python assistant.py
    ```

------------------------------------------------------------------------

## 🎤 Voice Commands

Here are some example commands you can say:

  Command                       Action
  ----------------------------- -------------------------------------
  "Wikipedia Albert Einstein"   Reads out summary from Wikipedia
  "Tell me about yourself"      Introduces Wall-E
  "The time"                    Tells current time
  "Join English"                Opens Teams and joins English class
  "Join Maths"                  Opens Teams and joins Maths class
  "Open YouTube"                Opens YouTube in browser
  "Open Chrome"                 Launches Chrome
  "Decrease Volume"             Lowers system volume
  "Increase Volume"             Raises system volume
  "Mute"                        Mutes system volume
  "Start Webcam"                Opens webcam using OpenCV
  "Who developed you"           Says developer name
  "Stop"                        Exits assistant

------------------------------------------------------------------------
    