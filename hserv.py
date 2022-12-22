#!/usr/bin/env python3

from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from colorama import *
import argparse
import platform
import logging

#windows colorized output
if platform.system() == 'Windows' :
    init()
else:
    pass

banner = '''
 __    __       _______. _______ .______     ____    ____ 
|  |  |  |     /       ||   ____||   _  \    \   \  /   / 
|  |__|  |    |   (----`|  |__   |  |_)  |    \   \/   /  
|   __   |     \   \    |   __|  |      /      \      /   
|  |  |  | .----)   |   |  |____ |  |\  \----.  \    /    
|__|  |__| |_______/    |_______|| _| `._____|   \__/     
                                       zulfi0 Project
                                                          '''

print(Style.BRIGHT+Fore.BLUE+banner+Style.BRIGHT+Fore.RESET)

parser = argparse.ArgumentParser(allow_abbrev=False, description='Simple Python Server SSRF')
parser.add_argument('-p', '--port',required=True, help='port number to listen on')
args = parser.parse_args()

PORT = int(args.port)

logging.root.handlers = []
logging.basicConfig(level=logging.DEBUG,
    format="\n%(asctime)s %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler()
        ]
    )

class Handler(SimpleHTTPRequestHandler):

    #response to client
    def sen_response(self):
        self.send_response(200)
        self.send_header('Content-Type','text/html')
        self.end_headers()

    #redirect client with /redirect path
    def Redirect(self,location):
        self.send_response(302)
        self.send_header('Location', location)
        self.end_headers()

    def do_GET(self):
        #check path to redirect
        if "/redirect" in self.path :
            location = self.path.split("=")
            logging.info(f'\nGET {self.path} {self.request_version}\n{self.headers}')
            self.Redirect(location[1])
        else :
            logging.info(f'\nGET {self.path} {self.request_version}\n{self.headers}')
            self.sen_response()
            self.wfile.write("This is GET Request".encode("utf-8"))

    def do_POST(self):
        #handle empty data
        try :
            content_len = int(self.headers["Content-Length"])
            post_body = self.rfile.read(content_len)

            logging.info(f"\nPOST {self.path} {self.request_version}\n{self.headers}\n{post_body.decode('utf-8')}\n")
            #print(post_body.decode('utf-8'))

            self.sen_response()
            self.wfile.write("POST request".encode("utf-8"))

        except Exception :
            logging.info(f"\nPOST {self.path} {self.request_version}\n{self.headers}\n")

            self.sen_response()
            self.wfile.write("POST request.".encode("utf-8"))

    def do_HEAD(self):
        logging.info(f'\nHEAD {self.path} {self.request_version}\n{self.headers}')
        self.sen_response()

        
httpd = TCPServer(("", PORT), Handler)

try :
    print(Style.BRIGHT+Fore.GREEN+f'Server start on ::{PORT}'+Style.BRIGHT+Fore.RESET)
    httpd.serve_forever()
except KeyboardInterrupt :
    httpd.server_close()
    print(Style.BRIGHT+Fore.RED+'\nServer stopped'+Style.BRIGHT+Fore.RESET)
