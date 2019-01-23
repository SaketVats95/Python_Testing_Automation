import webbrowser,sys

webbrowser.open("http://inventwithpython.com/")

if len(sys.argv)>1:
    address=' '.join(sys.argv[1:])

else:
    address="Puranik City Reserva, Kasalvadavali, Ghorbandar Road, Thane West, Mumbai, India"

webbrowser.open("https://www.google.com/maps/place/"+address)
