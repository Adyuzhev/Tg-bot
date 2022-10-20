from deeppavlov import build_model, train_model

model = train_model('./fasttext_tfidf_autofaq.json')

model = build_model('./fasttext_tfidf_autofaq.json')


result = model(['Можно ли сомещать обучение в магистратуре с работой?'])

print(result)
