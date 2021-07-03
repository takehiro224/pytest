age = 25
age += 1
height = 175.5
print(age + 1)
print(height + 1)
value = -1

print(5//2) # 小数点以下切り下げ

# >>, << シフト演算
# &, | ビット演算
value = 1
# print(value)
# value = -2
# print(value)
# value = value + 4
# print(value)
# print(value * 4) # 8
# print(value / 3) # 0.66...
# value = 10
# print(value // 3) # 3
# print(value % 3) # 1


value += 3
# value -= 2

# print(value)
# print(value ** 3) # 4の3乗

# 浮動小数点数
height = 175.5
print(height)
print(type(height))
print(height + 10) # 175.5 + 10.0

value = 8 
print(value >> 2)# 2進数だと1000 => 0010
print(value << 3)# 8は2進数だと1000で1を右に3つずらすので1000000
print(12 & 21) # 01100 and 10101 => (論理積) 00100 => 4
print(12| 21) # 01100 and 10101 => (論理和) 11101 => 29
value = 12
value &= 21 # value = value & 21
print(value)