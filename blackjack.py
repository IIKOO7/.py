from operator import truediv
import random
pelaajaMukana = True
jakajaMukana = True

#Blackjack -peli, jossa on jakaja ja pelaaja

# korttipakka / pelaajan ja jakajan käsi
pakka = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,
'J', 'Q','K','A','J', 'Q','K','A','J', 'Q','K','A','J', 'Q','K','A']
pelaajanKasi = []
jakajanKasi = []

#jaa kortit
def jaaKortti(vuoro):
    kortti = random.choice(pakka)
    vuoro.append(kortti)
    pakka.remove(kortti)

#laske kortit
def summa(vuoro):
    summa = 0
    kuva = ['J','K','Q']
    for kortti in vuoro:
        if kortti in range(1,11):
            summa += kortti
        elif kortti in kuva:
            summa += 10
        else:
            if summa > 11:
                summa += 1
            else:
                summa += 11
    return summa


#tarkasta voitto
def naytaJakajanKasi():
    if len(jakajanKasi) == 2:
        return jakajanKasi[0]
    elif len(jakajanKasi) > 2:
        return jakajanKasi[0], jakajanKasi[1]

#peli loop
for _ in range(2):
    jaaKortti(jakajanKasi)
    jaaKortti(pelaajanKasi)

while pelaajaMukana or jakajaMukana:
    print(f"Jakajalla on {naytaJakajanKasi()} ja X")
    print(f"Sinulla on {pelaajanKasi}, yhteensä {summa(pelaajanKasi)}")
    if pelaajaMukana:
        jaaTaiNosta = input("1: Jää tai 2: Nosta ")
    if summa(jakajanKasi) > 16:
        jakajaMukana = False
    else:
        jaaKortti(jakajanKasi)
    if jaaTaiNosta == '1':
        pelaajaMukana = False
    else:
        jaaKortti(pelaajanKasi)
    if summa(pelaajanKasi) >= 21:
        break
    elif summa(jakajanKasi) >= 21:
        break



if summa(pelaajanKasi) == 21:
    print(f"\nsinulla on {pelaajanKasi} joiden summa on {summa(pelaajanKasi)} ja jakajalla on  {jakajanKasi} joiden summa on, {summa(jakajanKasi)}")
    print("Sait BlackJackin ja voitit, onnittelut!")
elif summa(jakajanKasi) == 21:
    print(f"\nsinulla on {pelaajanKasi} joiden summa on {summa(pelaajanKasi)} ja jakajalla on  {jakajanKasi} joiden summa on, {summa(jakajanKasi)}")
    print("Blackjack! Jakaja voittaa.")
elif summa(pelaajanKasi) > 21:
    print(f"\nsinulla on {pelaajanKasi} joiden summa on {summa(pelaajanKasi)} ja jakajalla on  {jakajanKasi} joiden summa on, {summa(jakajanKasi)}")
    print("Ylitit summan 21! Jakaja Voittaa.")
elif summa(jakajanKasi) > 21:
    print("Jakaja ylitti luvun 21! Sinä voitit!")
elif 21 - summa(jakajanKasi) < 21 - summa(pelaajanKasi):
    print(f"\nsinulla on {pelaajanKasi} joiden summa on {summa(pelaajanKasi)} ja jakajalla on  {jakajanKasi} joiden summa on, {summa(jakajanKasi)}")
    print("Jakaja voittaa!")
elif 21 - summa(jakajanKasi) > 21 - summa(pelaajanKasi):
    print(f"\nsinulla on {pelaajanKasi}, joiden summa on {summa(pelaajanKasi)} ja jakajalla on  {jakajanKasi} joiden summa on, {summa(jakajanKasi)}")
    print("Sinä voitat!")





