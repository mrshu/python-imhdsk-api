import imhdsk

r = imhdsk.routes('zoo', 'estonska')
for d in r:
    print (d.drives)

suggestions = imhdsk.suggest('hlavna stanica')
for s in suggestions:
    print (s)
