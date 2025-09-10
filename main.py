#game matematika sederhana

import random


print("Jika memutuskan untuk bermain, maka tidak bisa keluar dari permainan sampai selesai")

hadiah = ["Jeruk", "Apel", "Anggur"]

tanya = input("Apakah kamu mau bermain? (ya/tidak) : ")


score = 0

if tanya == "ya":
  print("Mari kita mulai game ini")


  while score < 100:
    print("Berapakah hasil dari 234 * 80?")
    jawaban = int(input("Jawab: "))
    if jawaban == 18720:
      score += 25
      print("Jawabanmu benar")
    else:
      print("Salah")
    print()

    print("Berapakah hasil dari 530 + 234?")
    jawaban = int(input("Jawab: "))
    if jawaban == 764:
      score += 25
      print("Benarrr")
    else:
      print("Salah")
    print()

    print("Berapakah hasil 50 * 2?")
    jawaban = int(input("Jawab: "))
    if jawaban == 100:
      score += 25
      print("Benar")
    else:
      print("Salah")
    print()

    print("Berapakah hasil 144 / 2?")
    jawaban = int(input("Jawab: "))
    if jawaban == 72:
      score += 25
      print("Benar!")
    else:
      print("Salah")
    print()

    
    if score >= 100:
      print("Selamat! Ini score akhirmu:", score, "dan ini hadiahmu", "sekarung buah", random.choice(hadiah))
    else:
      print("Kamu tidak mencapai score yang ditentukan")
      break


else:
  print("Baiklah, sampai jumpa lagi")