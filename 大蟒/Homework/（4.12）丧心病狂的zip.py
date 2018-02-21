#用zip迭代可以将多个列表合成字典（前者为键，后者为值）
title = ['Creature of Habit','Crewel Fate']
plots = ['A nun turns into a monster','A hunted yarn shop']

dict = dict(zip(title,plots))
print(dict)
