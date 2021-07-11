# int str 変換
int_num = 12
str_num = str(int_num)
print(str_num)
print(type(str_num)) # <class 'str'>
#print('num = ' + int_num) 
# Traceback (most recent call last):
#  File "/Users/takehiro/play/python/base8.py", line 6, in <module>
#    print('num = ' + int_num)
#TypeError: can only concatenate str (not "int") to str
print('num = ' + str(int_num)) # num = 12
float_num = -20.5
str_float = str(float_num)
print(str_float) # -20.5
print(type(str_float)) # <class 'str'>

# 文字列からint, float
msg = '12'
int_msg = int(msg)
float_msg = float(msg)
print('value = {}, type = {}'.format(int_msg, type(int_msg))) # value = 12, type = <class 'int'>
print('value = {}, type = {}'.format(float_msg, type(float_msg))) # value = 12.0, type = <class 'float'>