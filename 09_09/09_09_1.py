# list

twice = ['momo', 'sana', 'zwi', 'nayun', 'dayun']  # 리스트 생성

print(type(twice))  # list
print(len(twice))  # 5

twice.append('jihyo')  # 리스트 마지막에 추가

twice.sort()  # 이름 기준 정렬

print(twice[0])
print(twice[-1])  # 마지막

black_pink = ['jisu', 'jeni', 'rose']
unite = twice + black_pink  # list + list
print(unite)

unite.sort()
print(unite)

unite.remove('momo')  # momo delete
print(unite)
print(len(unite))

best = unite[0:3]
print(best)  # sort => 0~2 to best

poor = unite[-3:]
print(poor)

# dictionary
score = {'momo': 80, 'zwi': 85, 'sana': 98}
print(type(score)) #dict
print(score['momo'])
print(score['zwi'])
score['jihyo'] = 99
print(score)
del score['jihyo']
print(score)
print(score.values())
print(sum(score.values()))

print(score.keys())
print('zwi' in score)
print('jiyho' in score)

#set

