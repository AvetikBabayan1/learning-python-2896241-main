# 
# Example file for retrieving data from the internet
# LinkedIn Learning Python course by Joe Marini
#

import urllib.request
import urllib.response

def main():
    weburl=urllib.request.urlopen("http://espn.com")
    print(weburl.getcode())
    data = weburl.read()
    print(data)

if __name__ == "__main__":
    main()
