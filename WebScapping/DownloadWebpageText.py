import requests

#reqObj=requests.get('https://automatetheboringstuff.com/files/rj.txt')


res = requests.get('https://automatetheboringstuff.com/chapter11/')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()
print(res.status_code)

if res.status_code==requests.status_codes.codes:
    print("True")
else:
    print("False")

print(len(res.text))

print(res.text[:250])

