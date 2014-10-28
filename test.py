import imhdsk

suggestions = imhdsk.suggest('hlavna stanica')
for s in suggestions:
    print (s)

a = (u'Zoo', u'Cintor\xedn Sl\xe1vi\u010die \xfadolie (Mlyny)')
r = imhdsk.routes('zoo', suggestions[0]['name'])
for d in r:
    print (d.drives)

r = imhdsk.routes(imhdsk.clear_stop(a[0]), imhdsk.clear_stop(a[1]))
for d in r:
    print (d.drives)
