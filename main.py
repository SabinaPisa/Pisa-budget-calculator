# Pisa Student Budget Calculator - SabinaPisa
print("🇮🇹 Pisa da Talaba Byudjeti")

ism = input("Ismingiz: ")

ijara = float(input("Ijara (euro): "))
ovqat = float(input("Ovqat (euro): "))
transport = float(input("Transport (euro): "))
kitob = float(input("Kitob va boshqa (euro): "))

oylik = ijara + ovqat + transport + kitob
yillik = oylik * 12

print(f"\n--- {ism} uchun natija ---")
print(f"Oylik xarajat: {oylik} euro")
print(f"Yillik xarajat: {yillik} euro")

if oylik < 600:
    print("Zo'r! Pisa uchun juda tejamkor byudjet!")
elif oylik < 900:
    print("Normal byudjet, Pisa da bemalol yashaysiz!")
else:
    print("Qimmatroq, stipendiya kerak bo'ladi!")

print("\nPisa seni kutmoqda! 🚀")
