'''
PPT中文名 批量 改成 英文名 并输出csv文件
双层文件夹
csv文件格式： PPT所在目录名，中文名，英文名
@path:中文名ppt所在路径、英文名ppt所在路径
@file:输出文件路径
'''
import os
import os.path

use_path = '/Volumes/李岩硬盘/ywm/'
use_file = '/Users/liyan/Downloads/PPT_YWMDYB.tsv'


def rename(path, file):
    # os.chdir() 方法用于改变当前工作目录到指定的路径。
    os.chdir(path)
    # 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。
    items = os.listdir(path)
    items.sort()
    items2 = open(file, mode='a')

    flag = 7
    flag2 = 143

    for directory_name in items:
        if directory_name[0] != '.':
            file = path + directory_name + '/'
            os.chdir(file)
            itemss = os.listdir(file)
            itemss.sort()
            for name in itemss:
                if name[0] != '.':

                    num0 = '%02d' % flag
                    num = '%06d' % flag2

                    kuo_zhan_ming = name.split('.')[-1]
                    new_name = 'PPT' + '_' + str(num0) + '_' + num + '.' + kuo_zhan_ming
                    # 遍历所有文件
                    os.renames(name, new_name)
                    items2.writelines(directory_name + '\t' + name + '\t' + new_name + '\n')
                    flag2 += 1
            itemss.clear()
            flag += 1


    items.clear()
    items2.close()


rename(use_path, use_file)
