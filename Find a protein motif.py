
# 载入模块
import re
import requests

# 读取id 名字
with open("rosalind_mprt.txt") as origin:
    id = origin.read().strip().split("\n")

# 正则化motif名称, 并且是重叠匹配
# ？= 是一个知识点
# 下次可以直接使用 新的模块 regex
N_gly = re.compile(r'(?=(N[^P][ST][^P]))')
# 网址的前缀
html = "http://www.uniprot.org/uniprot/"

# 获取网站
for element in id:
    response = requests.get(html + element + ".fasta")
    response_text = response.text
    response_text = response_text.split("\n")[1:]
    response_text = "".join(response_text)
    sign_0 = N_gly.search(response_text)
    if sign_0 != None:
        print("\n" + element)
    sign = N_gly.finditer(response_text)
    for i in sign:
        if i.start():
            print( i.start() + 1, end = " " )

