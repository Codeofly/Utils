'''
视频中文名 批量 改成 英文名 并输tsv文件
双层文件夹
tsv文件格式： 视频所在目录名 \t 中文名 \t 英文名
@path:中文名视频所在路径、英文名视频所在路径
@file:输出文件路径
'''
import os
import os.path

use_path = '/Volumes/李岩硬盘/ywm/'
use_file = '/Users/liyan/Downloads/文本/ShiPin_YWMDYB.tsv'

def rename(path, file2):
    # os.chdir() 方法用于改变当前工作目录到指定的路径。
    os.chdir(path)
    # 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。
    items = os.listdir(path)
    items.sort()

    items2 = open(file2, mode='a')

    flag = 0
    flag2 = 1
    for directory_name in items:
        if directory_name[0] == '.':
            continue
        else:
            file = path + directory_name + '/'
            os.chdir(file)
            itemss = os.listdir(file)

            for name in itemss:
                if name[0] == '.':
                    continue
                else:
                    num0 = '%02d' % flag
                    num = '%06d' % flag2
                    kuo_zhan_ming = name.split('.')[-1]
                    new_name = 'ShiPin' + '_' + str(num0) + '_' + str(num) + '.' + kuo_zhan_ming
                    # 遍历所有文件
                    os.renames(name, new_name)
                    items2.writelines(directory_name + '\t' + name + '\t' + new_name + '\n')
                    flag2 += 1

            flag += 1
            itemss.clear()

    items.clear()
    items2.close()


rename(use_path,use_file )
