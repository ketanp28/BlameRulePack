import understand

db = understand.open('/Users/ketanpatil/Desktop/bugattribution/firstdata_fdinet.udb')

for c in db.ents('Class ~Unknown'):
    print(c.longname())