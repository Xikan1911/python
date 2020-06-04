number ={
    'andrey': 2,
    'jura': 6,
    'victor': 4,
    'sveta': 9,
    'alex':10,
}
print(*[ [k, v] for k, v in {'andrey': 2, 'jura': 6, 'victor': 4, 'sveta': 9, 'alex': 10}.items() ], sep='\n')