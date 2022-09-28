dict = {'Александр' : 34510,
        'Екатерин'  : 46910,
        'Елен'      : 34610,
        'Кирил'     : 45710
}
print('min val :', min(dict, key=dict.get))
print('max val :', max(dict, key=dict.get))