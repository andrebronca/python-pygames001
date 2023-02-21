score = 100
health = 60
damage = 50
fugu = "tasty"
price = 50.
print(score != 100)
print(health - damage > 0)
print(fugu == "tasty")

if fugu == "tasty":
    print("Eat the fugu!")

if (fugu == "tasty" and price < 100.):
    print("Eat the fugu cheap!")

if fugu == "tasty" or price < 20.:
    print("Fugu está bem barato ou é tasty")

if not(fugu == "tasty" and price < 100.):
    print("Don't eat the fugu!")

if fugu == "tasty":
    print("Eath the fugu!")
else:
    print("Don't eat the fugu!")

if price < 20:
    print("Cheap fugu!")
elif price < 100:
    print("Reasonably priced Fugu.")
else:
    print("Expensive fugu!")

def fugu_tip(price, num_plates, tip):
    total = price * num_plates
    tip = total * (tip / 100)
    return tip

#definindo valores padrões
def fugu_tip2(price, num_plates = 2, tip = 15.):
    return (price * num_plates) * (tip / 100)

print(fugu_tip(100., 2, 15.))
print(fugu_tip(50., 1, 5.))
print(fugu_tip2(100.))
print(fugu_tip2(50., 1, 5.))
print(fugu_tip2(50., tip=10.))