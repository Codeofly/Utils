'''
重命名文件
掐头去尾，去掉文件名前非汉子英文部分，去掉扩展名
例：
    (1.2.10)--嵌入式系统应用领域B1.2.ppt   -------> 嵌入式系统应用领域B1.2

'''

import re


def rename(file, file2):
    items = open(file, mode='r')
    items2 = open(file2, mode='a')
    fil = re.compile(u'[^a-zA-Z\u4e00-\u9fa5]+', re.UNICODE)
    for name in items:
        d = fil.search(name).span()[1]

        new_name = '.'.join(name[d:].split('.')[:-1])+'\n'

        print(name, new_name)
        items2.writelines(new_name)

    items.close()
    items2.close()


rename('/Users/liyan/Documents/文本/1.txt', '/Users/liyan/Documents/文本/2.txt')
