kleding = ["Broek", "Shirt", "Jas", "Schoenen", "Pet"]
 
kleding.append("Trui")
kleding.append("Sokken")
 
kleding.remove("Pet")
 
print("Aantal producten:", len(kleding))
print("Mijn kledinglijst:")
print(kleding)
 
if "Jas" in kleding:
    print("Jas staat op de lijst!")
else:
    print("Jas staat niet op de lijst!")
