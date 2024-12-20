# G-Logger
Basic keylogger in python, for educational purposes and personal use only.
Cchange the email adress to yours. (mail in code is a random one)
Set application password for your mail adress and put it in pwd variable.

In order to not hardcode it, i put mine in bashrc with export GMAIL_PASSWORD="yourPassword"

Run logger.py and thats it. The script will create a klog.txt file and send it to your mail every minute (you can change the delay).
It also clears the log after sending it.
