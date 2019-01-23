"""from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = 'Welcome Saket Vats! This is Python Text To Speech Testing Application' \
         'How was you day ? What you have done Today ?'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
os.system("welcome.mp3")
"""

import urllib.request as urllib
from bs4 import BeautifulSoup

url = "https://www.bloomberg.com/quote/SPX:IND"
#"http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = urllib.urlopen(url)
soup = BeautifulSoup(html)


# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out
# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = [line.strip() for line in text.splitlines()]
print(lines)
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

#print(text)