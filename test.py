import imhdsk

r = imhdsk.routes('zoo', 'eston', time='22:00', date='25.10.2014')
for d in r:
    print (d.drives)
