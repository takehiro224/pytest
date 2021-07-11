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


msg = 'ABCDEABC'
# count
print(msg.count('ABC'))
# startswith
print(msg.startswith('ABCD'))
print(msg.startswith('ACD'))
# endswith
print(msg.endswith('C'))
# strip(両端), rstrip(右端), lstrip(左端)
msg = ' ABC '
print(msg)
print(msg.strip()) # 両端を削除
msg = 'ABCDEABC'
print(msg.strip('C')) # ABCDEAB
print(msg.strip('CBA')) # DE(ABC, ABCが削除される)
print(msg.lstrip('CBA'))
print(msg.rstrip('CBA'))
# upper, lower, swapcase, replace, capitalize
msg = 'abcABC'
msg_u = msg.upper() # 全てが大文字
msg_l = msg.lower() # 全てが小文字
msg_s = msg.swapcase() # 大文字と小文字を入れ替え
print(msg_u, msg_l, msg_s) # ABCABC abcabc ABCabc
msg = 'ABCDEABC'
msg_r = msg.replace('ABC', 'FFF')
print(msg_r) # FFFDEFFF
msg_r = msg.replace('ABC', 'FFF', 1)
print(msg_r) # FFFDEABC
msg_r = msg.replace('ABC', 'FFF', -1)
print(msg_r) # FFFDEFFF
msg = 'hello world'
print(msg.capitalize()) # Hello world 一番最初の文字が大文字になる
msg = 'hello World'
print(msg.capitalize()) # Hello world

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