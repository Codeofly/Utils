# PPT中文名 批量 改成 英文名 并输出csv文件
# tsv文件格式： PPT所在目录名，中文名，英文名
# @in_path:中文名ppt所在路径、英文名ppt所在路径
# @file:输出文件路径


import os
import os.path
import time
import py.get_path

print('选择输入路径')
in_path = py.get_path.get()
print('in_path ：' + in_path)
# print('选择输出路径（默认为输入路径）')
# out_path = py.get_path.get(in_path)
# print('out_path ：' + out_path)
# dname = in_path.split('/')[-2]  # 获取文件夹名，作为输出文件名
# flag = int(input('输出文件夹序号（整数）：'))  # 文件夹序号1
# flag2 = int(input('输入文件序号（整数）：'))  # 文件夹内容序号

# file = out_path + dname + '_' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '.tsc'


def rename(path):
    # os.chdir() 方法用于改变当前工作目录到指定的路径。
    os.chdir(path)
    # 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。
    items = os.listdir(path)
    items.sort()  # 内容排序
    # items2 = open(myfile, mode='a')

    for name in items:
        if name[0] != '.':  # 排除'.'开头的隐藏文件

            # num0 = '%02d' % f  # 格式化序号  2 --> 02
            # num = '%07d' % f2  # 866 --->  0000866
            kuo_zhan_ming = name.split('.')[-1]  # 提取扩展名

            # new_name = 'PPT' + '_' + num0 + '_' + num + '.' + kuo_zhan_ming  # 组合新文件名
            new_name = name.split('_')[0]+ '.'+name.split('.')[-1]  # 组合新文件名
            # 遍历所有文件
            os.renames(name, new_name)  # 改名
            # items2.writelines(name + '\t' + new_name + '\n')  # 写入文件
            # f2 += 1  # 文件序号自增

    items.clear()
    # items2.close()


rename(in_path)

# 4、将路径分解为目录名和文件名——os.path.split()
# 5、分解文件名的扩展名——os.path.splitext()
