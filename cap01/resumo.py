shopping = ['fugu', 'ramen', 'sake', 'shiitake mushrooms', 'soy sauce', 'wasabi']
prices = {'fugu': 100., 'ramen': 5., 'sake': 45., 'shiitake mushrooms': 3.5, 'soy sauce': 7.5, 'wasabi': 10}
total = 0.

for item in shopping:
    total += prices[item]

print(total)