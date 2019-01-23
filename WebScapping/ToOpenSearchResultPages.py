import requests,sys,bs4,webbrowser

if len(sys.argv)>1:
    googleingText=' '.join(sys.argv[1:])
else:
    googleingText="I'm Feeling Lucky"

req=requests.get("http://google.com/search?q="+googleingText)

print(str(req.raise_for_status()))

soup=bs4.BeautifulSoup(req.text)
linkElements=soup.select('.r a')
numOpen = min(5, len(linkElements))
for i in range(numOpen):
    webbrowser.open("http://google.com"+linkElements[i].get('href'))


