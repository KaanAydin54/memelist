meme_dict = { 
      "Cringe": "Garip yada utandırıcı durumlar",
        "LOL": "Komik durumlara verilen tepki",
            "Sus": "Şüpheli",
        "troll": "Alay durumlarında kullanılır"
        }
word = input("Anlamını öğrenmek istediğiniz kelimeyi girin:")

if word in meme_dict.keys():
    print("Aradığınız kelimenin anlamı", meme_dict[word])

else: 
    print("Maalesef aradığınız kelimeyi bilmiyorum...")
