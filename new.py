from deeppavlov import build_model, train_model

model = train_model('./copy.json')

model = build_model('./copy.json')


result = model(['Можно ли сомещать обучение в магистратуре с работой?'])

print(result)
