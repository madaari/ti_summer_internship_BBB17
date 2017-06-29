import urllib
x=urllib.urlopen("http://api.telegram.org/bot320429258:AAE6F96ml5SAR7zOx1IeF1Nqf2lwv1hTm2E/getUpdates")
print(x.read())
y=urllib.urlopen("http://api.telegram.org/bot320429258:AAE6F96ml5SAR7zOx1IeF1Nqf2lwv1hTm2E/getFile?file_id=AwADBQADNQADGAABoFZmpxKzwHE4mQI")
print(y.read())
urllib.urlretrieve("http://api.telegram.org/bot320429258:AAE6F96ml5SAR7zOx1IeF1Nqf2lwv1hTm2E/voice/6241989186614722614.oga", "final2.wav")













