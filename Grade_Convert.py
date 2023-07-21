def scoreconv():
    score=(input("Masukkan nilai anda "))
    scorefin=int(score)
    if scorefin>100:
        print("Nilai yang anda masukkan invalid")
    elif 100>scorefin>85:
        print("Grade anda adalah A")
    elif 85>scorefin>80:
        print("Grade anda adalah A-")
    elif 80>scorefin>75:
        print("Grade anda adalah B")
    elif 75>scorefin>70:
        print("Grade anda adalah B-")
    elif 0<scorefin<70:
        print("Anda harus mengulang")
    elif scorefin<0:
        print("Nilai yang anda masukkan invalid")
while True:
    score=(input("Masukkan nilai anda "))
    scorefin=int(score)
    if scorefin>100:
        print("Nilai yang anda masukkan invalid")
    elif 100>scorefin>85:
        print("Grade anda adalah A")
    elif 85>scorefin>80:
        print("Grade anda adalah A-")
    elif 80>scorefin>75:
        print("Grade anda adalah B")
    elif 75>scorefin>70:
        print("Grade anda adalah B-")
    elif 0<scorefin<70:
        print("Anda harus mengulang")
    elif scorefin<0:
        print("Nilai yang anda masukkan invalid")
    if (input("Ulangi program? (Y/N) "))!="Y":
        continue
    elif 0<scorefin<100:
        break
