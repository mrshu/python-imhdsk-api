import imhdsk

suggestions = imhdsk.suggest('hlavna stanica')
for s in suggestions:
    print (s)

r = imhdsk.routes('zoo', suggestions[0]['name'])
for d in r:
    print (d.drives)
