import urllib
import json

serviceurl = 'https://api.exchangeratesapi.io/latest'
#serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    monnaie = raw_input('Enter currency: ')
    montant = raw_input('Enter your change: ')
    if len(monnaie) < 1 : break
    if len(montant) < 1: break
    if str(monnaie) == "QUIT" : break
    if str(montant) == "QUIT": break

    url = serviceurl
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read().decode()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    assert str(monnaie) in js["rates"], "La Currency n'est pas dans la base"
    print ('The change of {} EUR in {} is: '.format(str(montant),str(monnaie))),(js["rates"][str(monnaie)])*int(montant)
