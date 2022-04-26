# hserv

Simple python http server that logs incoming requests.
Currently support GET, HEAD, POST and 302 Redirect and logs all incoming requests to log.txt file.

## Features
* [+] Support: GET, POST, HEAD
* [+] Redirect

POST :
```
POST / HTTP/1.1
Host: 0.0.0.0:8080
User-Agent: curl/7.68.0
Accept: */*
Content-Length: 7
Content-Type: application/x-www-form-urlencoded                                                                               

foo=bar
```

REDIRECT :

Simply add /redirect in your url path ie. http://privateserver.com/redirect=https://foo.bar/.

## Installation
1. Clone this project
```
git clone https://github.com/zulfi0/hserv
```
2. Install Module
 ```bash
 python3 -m pip install colorama
 ```
3. Run
```bash
cd hserv && cp hserv.py /usr/bin && hserv
```
## Usage
Simply run the script with -p switch.

```bash
hserv -p 80
```
