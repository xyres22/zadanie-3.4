zakupy = {
    'Piekarnia': ['Chleb', 'Bułka', 'Pączek'],
    'Warzywniak': ['Marchew', 'Seler', 'Rukola']
}
zakupy_upper = {str(k).upper():str(v).upper()   for k,v in zakupy.items()}
print('Lista zakupów')
g = sum(len(val) for val in zakupy.values())
for i,v in zakupy.items():
    print(f'Idę do {i}, kupuję tu następujące rzeczy: {v}.')

print(f'W sumie kupuję {g} produktów.')
print('zmiana do zadania')

