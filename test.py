# To bedzie plik na ktorym bedziemy pracowali z repo
def hello(name):
	return "Hello" + str(name)

def odejmij(a,b):
	wynik = float(a) - float(b)
	return wynik

def dodaj(a,b):
	wynik = float(a) + float(b)
	return wynik

pierwsza = input()
druga = input()

#To jest komentarz, ktory dodam tylko zeby sprawdzic czy dziala commit po ssh

print (dodaj(pierwsza, druga))
