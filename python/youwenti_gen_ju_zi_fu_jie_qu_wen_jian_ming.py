'''
根据字符截取文件名
@file：读取文件路径
@file2：写入文件路径
@key：字符
'''


def rename(file, key, file2):
    items = open(file, mode='r')

    for name in items:
        print(name)
        items2 = open(file2, mode='a')
        a = ''
        if name != '\n':
            new_name = name[name.index(key) + 1:]
            print(new_name)
        a = new_name
        if name == '\n':
            new_name = a
        items2.writelines(new_name)

    items.close()
    items2.close()


rename('/Users/liyan/Downloads/1', '_', '/Users/liyan/Downloads/2')
