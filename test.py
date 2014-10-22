import imhdsk

r = imhdsk.routes('zoo', 'eston')
for d in r:
    print (d.drives)
