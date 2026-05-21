from random import sample

dic = {"a": {"Charizard" : 1, "Blastoise" : 2, "Venusaur" : 3},
       "b": {}}

dic["b"] = dict(sample(list(dic["a"].items()), 2))

print(dic["b"].values())

print(len(dic["b"]))