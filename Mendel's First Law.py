###
Qustion: Mendel's First Law
date: 2020/5/30/9: 47
####
k = 16
m = 22
n = 19

probility = 1 - (m * n + m * (m-1)/4 + n * (n - 1))/((m + n + k)*(m + n + k-1))
probility = round(probility, 5)
# 或者
# 字符串格式化输出字符串类型
probility = '%.5f' % probility
# 或者
print("{:.5f}".format(float(probility)))
