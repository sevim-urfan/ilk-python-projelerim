def alan (u,g):
	A=u*g
	return A
def cevre (u,g):
	C=2*(u+g)
	return C
	
u=int(input('dikdötgenin uzun kenarını gir:'))
g=int(input('dikdötgenin kısa kenarını gir:'))
print ('Dikdörtgenin Alanı =',alan(u,g),'m^2')
print ('Dikdörtgenin Çevresi =',cevre(u,g), 'm')
