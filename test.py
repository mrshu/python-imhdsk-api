import imhdsk

r = imhdsk.routes('zoo', 'eston', time='22:00')
for d in r:
    print (d.drives)
