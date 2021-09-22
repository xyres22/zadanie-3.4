zakupy = {
    'Piekarnia': ['Chleb', 'Bułka', 'Pączek'],
    'Warzywniak': ['Marchew', 'Seler', 'Rukola']
}
print('Lista zakupów')
g = sum(len(val) for val in zakupy.values())
for i,v in zakupy.items():
    print(f'Idę do {i}, kupuję tu następujące rzeczy: {v}.')

print(f'W sumie kupuję {g} produktów.')
