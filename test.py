import imhdsk

print('Suggestions:')
suggestions = imhdsk.suggest('hlavna stanica')
for s in suggestions:
    print(s)

print('Routes:')
r = imhdsk.routes('zoo', 'hlavna stanica')
for d in r:
    print(d.drives)

print('Clear stop routes:')
a = (u'Zoo', u'Cintor\xedn Sl\xe1vi\u010die \xfadolie (Mlyny)')
r = imhdsk.routes(imhdsk.clear_stop(a[0]), imhdsk.clear_stop(a[1]))
for d in r:
    print(d.drives)
