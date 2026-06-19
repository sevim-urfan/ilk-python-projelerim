masaNo=0
liste=['ali', 'can','miray','zeynep']
liste2=['bahar','talat']
isim=input('isminiz nedir?..')
if isim=='ali':
	masaNo=5
if isim=='can':
	masaNo=7
if isim=='miray':
	masaNo=2
if isim=='zeynep':
	masaNo=10
if isim in liste:
	print (masaNo,'Numaralı masada Rezervasyonunuz var')
elif isim in liste2:
	print ('Rezervasyonunuz bu akşam değil')
elif isim not in liste and isim not in liste2:
	print ('Rezervasyonunuz yok')
