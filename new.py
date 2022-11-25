from deeppavlov import build_model, train_model

model = train_model('./tfidf_autofaq.json')

model = build_model('./tfidf_autofaq.json')
sum = 0
with open('FAQ.csv') as f:
    f.readline()
    for line in f:
        a = line.split(',')[0]
        result = model([a])
        if result[1][0] <= 0.04:
            print(a, result)
            sum += 1
    print(sum)

result1 = model(['Могу ли я поступить на направление магистратуры, которое никак не связано с образованием, полученным на бакалавриате?'])

if result[1][0] <= 0.04:
    print('Уточните вопрос')
else:
    print(result1)
