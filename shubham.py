import urllib
x=urllib.urlopen('https://api.telegram.org/bot320429258:AAE6F96ml5SAR7zOx1IeF1Nqf2lwv1hTm2E/getupdates?chat_id=426960508')
print(x.read())
