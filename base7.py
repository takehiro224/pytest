fruit = "apple"
fruit * 10 # fruitが10回表示
fruit[2] # 3番目の文字が表示されるp

fruit = 'apple'
print(fruit)
print(type(fruit))

print(fruit*10)

new_fruit = fruit + ' banana'
print(new_fruit)

fruits = """apple
orange
grape
"""
print(fruits)

fruit = 'banana'
print(fruit[2]) # nが表示される
print(fruit[-1]) # aが表示される。後ろから数えて-1だと最後の文字

# bytes[]型に変換
byte_fruit = fruit.encode('utf-8')
print(byte_fruit)
print(type(byte_fruit))
str_fruit = byte_fruit.decode('utf-8')
print(str_fruit)
print(type(str_fruit))

test = 'テスト'
byte_test = test.encode('utf-8')
str_test = byte_test.decode('utf-8')
print(byte_test)
print(str_test)

# 文字列の一部取り出し、format, islower, isupper
msg = 'hello, my name is taro'
print(msg[:5]) # hello
print(msg[6:]) # my name is taro
print(msg[1:6]) #

print('hellow {}'.format('Taro'))
# Python3.6以上
name = 'Jiro'
print(f'hello {name}')
# Python3.8以上
print(f'{name=}')

# 小文字か大文字か判定
msg = 'apple'
print(msg.islower()) # true
msg = 'Apple'
print(msg.islower()) # false
msg = 'APPLE'
print(msg.isupper()) # true
msg = 'Apple'
print(msg.isupper()) # false

msg = 'ABCDEABC'
print(msg.find('ABC')) # 0
print(msg.rfind('ABC')) # 右端から検索 5
print(msg.index('ABC')) # 0
print(msg.rindex('ABC')) # 
print(msg.find('ABCE')) # 見つからなかったら-1になる
print(msg.index('ABC')) # 見つからなかったらエラーが表示される.エラー以降は実行されないのでエラーで終了させたい場合にしよう