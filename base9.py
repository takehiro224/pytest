# リスト
list_a = [1,2,3,4]
list_b = []

print(list_a)
print(list_a[0]) # 1
print(list_a[1]) # 2
print(list_a[-2]) # 3

list_a = [1, [1, 2, 'apple'], 3, 'banana']
print(list_a[1][2]) # apple
print(list_a)
list_a[1][2] = 'lemon'
print(list_a) # [1, [1, 2, 'lemon'], 3, 'banana']

# リストのメソッド
list_a = [1, 2, 3, 4, 5]
list_b = list_a[:3]
print(list_b) # [1, 2, 3]
list_b = list_a[3:]
print(list_b) # [4, 5]
list_b = list_a[1:4]
print(list_b) # [2, 3, 4]
list_b = list_a[1:4:2] # 一つ飛ばし
print(list_b) # [2, 4]

# append, extend, insert, clear
list_a.append('apple') # appendは一番使う
print(list_a) # [1, 2, 3, 4, 5, 'apple']
list_a.append(['banana', 'melon'])
print(list_a) # [1, 2, 3, 4, 5, 'apple', ['banana', 'melon']]
list_a = [1, 2, 3, 4, 5]
list_a.extend(['banana', 'melon'])
print(list_a) # [1, 2, 3, 4, 5, 'banana', 'melon']
list_a.insert(1, 'grape')
print(list_a) # [1, 'grape', 2, 3, 4, 5, 'banana', 'melon']
#list_a.clear()
#print(list_a) # []　中身を空にする

# remove, pop, count, index
list_a = [0, 1, 1, 2, 2, 3, 3, 3, 4] 
list_a.remove(3) # 左から一番最初に出てくる「3」を削除する
print(list_a) # [0, 1, 1, 2, 2, 3, 3, 4]
value = list_a.pop() # 一番最後の要素を取り出す
print(list_a, value) # [0, 1, 1, 2, 2, 3, 3] 4
print(list_a.count(1)) # 2 # 1が何個あるか
print(list_a.index(1)) # 1 # 1が最初に出てくるインデックスを表示
# copy
print(list_a)
list_b = list_a
#list_b[0] = 'AAAAA'
print(list_a) # ['AAAAA', 1, 1, 2, 2, 3, 3] # list_aの値が書き変わってしまう。 
# list_b = list_aは参照渡し
list_c = list_a.copy()
list_c[0] = 'BBBBB'
print(list_c) # ['BBBBB', 1, 1, 2, 2, 3, 3]
print(list_a) # [0, 1, 1, 2, 2, 3, 3]
# copy()は値渡し

# sort, reverse
list_a = ['banana', 'apple', 'lemon', 'grape']
print(list_a)
list_a.sort() # 昇順に並び替える
print(list_a) # ['apple', 'banana', 'grape', 'lemon']
list_a = ['banana', 'apple', 'lemon', 'grape']
list_a = sorted(list_a)
print(list_a) # ['apple', 'banana', 'grape', 'lemon']
list_a.reverse()
print(list_a) # ['lemon', 'grape', 'banana', 'apple']