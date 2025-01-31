# netflix-cookie-bot
cookies checker for netflix. 
 
this converts the netscape format cookies into json cookies and check if they still work on netflix.

## disclaimer
this script is for educational purposes & personal use only. don't be dumb, use it responsibly & respect the website's terms of service.

## installation
> **note:** needs python 3.10 & git (optional).  
```cmd
  git clone https://github.com/whitedevil-glitch/netflix-cookie-bot.git
  cd netflix-cookie-checker
  pip install -r requirements.txt
```
## or

```cmd
  click on code & download zip  
  unzip the folder  
  open a terminal in that directory  
  run pip install -r requirements.txt
```

## usage

1. first, run this in terminal:

`cmd
python cookie_converter.py `

this will convert netscape cookies into json.


2. then run:

`cmd 
 python main.py `

this checks the cookies & moves the valid ones to "working_cookies" folder.



> note: if you already have json cookies, just drop them in "json_cookies" folder.



## credits

this project was inspired by <a href="#"><b>matheesh pathirana</b></a> but unlike that repo, this one doesn't use selenium. instead, it runs on requests, batch-processing, and parallel-execution to make it fast af.

it's <b>50x faster</b> than matheesh's repo.

made with ❤️ by whitedevil-glitch.

Just save this as `README.md`, and it’ll be properly formatted for GitHub or any markdown viewer.

