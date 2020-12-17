'''
PPT中文名 批量 改成 英文名 并输出csv文件
tsv文件格式： PPT所在目录名，中文名，英文名
@in_path:中文名ppt所在路径、英文名ppt所在路径
@file:输出文件路径
'''

import os
import os.path


in_path = '/Volumes/李岩硬盘/27/'

out_path = '/Users/liyan/Documents/文本/'

flag = 27    #文件夹序号
flag2 = 2786 #文件夹内容序号

file = out_path + str(flag) +'.tsc'

def rename(path, file, f, f2):
    # os.chdir() 方法用于改变当前工作目录到指定的路径。
    os.chdir(path)
    # 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。
    items = os.listdir(path)
    items.sort() # 内容排序
    items2 = open(file, mode='a')



    for name in items:
        if name[0] != '.':  #排除'.'开头的隐藏文件

            num0 = '%02d' % f    # 格式化序号  2 --> 02
            num = '%07d' %  f2    #   866 --->  0000866
            kuo_zhan_ming = name.split('.')[-1]   # 提取扩展名
            new_name = 'PPT' + '_' + num0 + '_' + num + '.' + kuo_zhan_ming    #组合新文件名
            # 遍历所有文件
            os.renames(name, new_name)  # 改名
            items2.writelines(name + '\t' + new_name + '\n')  #写入文件
            f2 += 1  # 文件序号自增


    items.clear()
    items2.close()

rename(in_path, file, flag, flag2)
