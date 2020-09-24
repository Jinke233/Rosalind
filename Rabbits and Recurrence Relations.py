# 题目是 Rabbits and Recurrence Relations
# 这道题起源于 菲波那妾数列
# 1 1 2 3 5 8
# 通用 斐波那契数列公式
# Fn = F(n-1) + k*F(n-2)

# # 起始都是 1
# F1 = 1
# F2 = 1

# # 第n 个月份是 第 n-1个月份的兔子数目与 第n-2个月份的兔子数目与每次兔子产生数量k
# # 的乘积
# k = 3
# n = 5

# F3 = F2 + k *F1

# F4 = F3 + k * F2

# F5 = F4 + k*F3

# # 首先肯定需要迭代

# # 如果 n= 3
# for i in range(3,n+1):
#     b = F2 + k* F1

# # 如果 n = 4
# for i in range(3,5):
#     b = F2 + k* F1
#     c = b + k* F2

# # 如果 n = 5
# for i in range(3,6):
#     b = F2 + k* F1
#     c = b + k* F2
#     d = c + k*b

n = 29
k = 4
a = 1
b = 1
c = 0

for i in range(3, n+1):
    c = b
    # 首先需要 b(F2) + a(F1)*K
    # 每次 b的结果 会自动提升为一代，但是 a 也需要提升一代，这样就需要一个中间变量替换，因为必须在 a 用完之后
    # 在提升
    b = b + a * k
    a = c
    print(b)
