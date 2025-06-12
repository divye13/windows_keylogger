🛡️ Key Input Logger
A simple Windows-based key input logger built with Python, intended strictly for ethical and educational purposes such as studying system behavior, input logging, and understanding vulnerabilities.

⚠️ Disclaimer:
This tool must only be used on systems you own or have permission to test. Unauthorized usage may be illegal and unethical.

📁 Features
>Logs all keystrokes using pynput
>Saves logs to a hidden file in AppData
>Realistic simulation of keylogging behavior
>Includes error handling and file hiding

🛠️ Requirements
>Python 3.x
>Libraries: pynput

🚀 Usage
▶️ Run Script (Directly)
>python keylogger.py
⚙️ Convert to Executable
>pip install pyinstaller
?pyinstaller --noconsole --onefile keylogger.py
(Executable will be in the dist/ folder.)

🧪 Test Instructions (Windows)
1. Exclude the .exe from Windows Defender
   (Windows Security > Virus & threat protection > Manage Settings > Add Exclusion)
2. Run as Administrator for realistic behavior
3. View Logs in:
   C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Logs\keylog.txt
   
🧼 Cleanup
>Delete .exe, build files, and the log file manually
>Remove Defender exclusion if added
