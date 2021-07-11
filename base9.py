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
list_a.clear()
print(list_a)