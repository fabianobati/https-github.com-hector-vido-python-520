#!/usr/bin/python3

for n in map(lambda i : i * 2, [1, 2, 3, 4]):
    print(n)

duck_tails = ['Huguinho|1', 'Zezinho|2', 'Luizinho|3']

# ['Huguinho', 'Zezinho', 'Luizinho']
for d in [i.split('|')[0] for i in duck_tails]:
    print(d)
