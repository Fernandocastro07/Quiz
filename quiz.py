print("Welcome my quiz")
answer_user = input ("quer comecar? (S/N) ")

if answer_user != "S": 
    quit()

print("começando...")
print("Quem construiu o templo de jerusalem (AT)? \n (A) Davi \n (B) Pedro \n (C) Moises \n (D)salomao \n")
answer_1 = input("Resposta: ")

if answer_1 == "D":
    print("correct!")
else:
    print("incorreto") 
