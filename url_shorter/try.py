import pyshorteners 
def url_shortener(link): 
    tine=pyshorteners.Shotener()
    short= tine.tinyurl.short(short)
    print(f' your short url is {short} ')
if __name__ ==  '__main__': 
    lin= input('enter your link  :')
    url_shortener(lin)