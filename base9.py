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