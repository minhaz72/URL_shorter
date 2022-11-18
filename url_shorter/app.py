import pyshorteners 
url = input('enter your link; ')

make_tine= pyshorteners.Shortener()
short= make_tine.tinyurl.short(url)
print('  your short url is ', short )
