capitals = {'VA': 'Richmond', 'DE': 'Dover'}
capitals['NC'] = "Raleigh"
capitals['MD'] = "Annapolis"
capitals['CA'] = "Sacramento"
print(f"{capitals = }")
print(f"{capitals['MD'] = }")
capitals['MD'] = "Baltimore"
print(f"{capitals = }")
print(f"{capitals['VA'] = }")
if 'ND' in capitals:
    value1 = capitals['ND']
else:
    value1 = "NOT FOUND"

print(f"{value1 = }")

value2 = capitals.get('ND', 'NOT FOUND')
print(f"{value2 = }")

value3 = capitals.setdefault('ND', 'Bismarck')
print(f"{value3 = }")
print(f"{capitals = }")

for capital, state in capitals.items():
    print(capital, state)
print(f"{capitals.items() = }")
print()
for capital in capitals.values():
    print(capital)
for state in capitals:
    print(state)
