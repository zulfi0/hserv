# hserv

Simple python http server that logs incoming requests.
Currently support GET, POST and 302 Redirect.

> Note : Only use for basic testing.

## Installation
1. Clone this project
```
git clone https://github.com/zulfi0/hserv
```
2. Run
```python
python3 hserv.py
```
## Usage
Simply run the script with -p switch and the server should be started on port 80

```python
python3 hserv.py -p 80
```
For trigger the redirect add /redirect in your path ie. https://example.com/redirect=https://foo.bar/
This will redirect you to https://foo.bar automatically

GET :
![IMG_20211129_134900](https://user-images.githubusercontent.com/68773572/143817074-21c5a572-2e49-4a16-bfb6-ef771b55aed4.jpg)

POST :
![IMG_20211129_135012](https://user-images.githubusercontent.com/68773572/143817161-8e5f63d9-a046-4c7f-b89b-2160b5f8b063.jpg)

REDIRECT :
![IMG_20211129_135331](https://user-images.githubusercontent.com/68773572/143817234-a5d08be1-34ae-4cbc-a300-76b1472f5b60.jpg)

