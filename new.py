from deeppavlov import build_model, train_model

# model = train_model('./tfidf_autofaq.json')

model = build_model('./tfidf_autofaq.json')



result = model(['Сколько раз в неделю нужно приезжать в университет студентам магистратуры?'])

if result[1][0] <= 0.1:
    print('Уточните вопрос')
else:
    print(result)
