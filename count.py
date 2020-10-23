"""
en: this python file is to count the lines of a data file
cn: 计算数据文件总行数
"""

with open("data/dbpedia_entity.csv", "r") as f:
    data = f.readlines()
    print(data.__len__())
    f.close()





