## netflix-cookie-bot
cookies checker for netflix.
convert the netscape format cookies into json cookies and check for the validity of the cookies.
<br>

## Disclaimer
This script is intended for educational purposes and personal use only. Use it responsibly and respect the terms of service of the websites you're checking cookies for.

## Installation
>  **Note:** requires python 3.10 and git(optional) installed on your pc.
```cmd
  git clone https://github.com/whitedevil-glitch/netflix-cookie-bot.git
  cd Netflix-cookie-checker
  pip install -r requirements.txt
```
### or

```cmd
  click on code and download zip
  unzip the folder
  open a terminal in that directory
  run pip install -r requirements.txt
```
## Usage

1. first, run the ```cookie_converter.py``` and convert the ```netscape cookies``` format to ```json```.
2. next, run the ```main.py``` which will check the cookies and place the valid cookies into ```"working_cookies"``` folder.
>  **Note:** If you already have json cookies, paste it in "json_cookies" folder.
<br>

## Credits
This project was inspired by <a href="https://github.com/matheeshapathirana/Netflix-cookie-checker/">Matheesh Pathirana</a> <br>
This project doesn't use selenium unlike the mentioned repo. I used <code>requests</code>,<code>batch-processing</code> and <code>parallel-execution</code> to make the workflow fast.<br><br>
<b>It is 50 times faster than the Matheesh's repository.</b>
<br>
<br>
Made with ❤️ by whitedevil-glitch
