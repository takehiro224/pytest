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
print(msg.capitalize()) # 