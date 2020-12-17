'''
PPT中文名 批量 改成 英文名 并输出csv文件
tsv文件格式： PPT所在目录名，中文名，英文名
@in_path:中文名ppt所在路径、英文名ppt所在路径
@file:输出文件路径
'''

import os
import os.path


def set_in_path():
    in_path = '/Volumes/李岩硬盘/27/'
    print('当前文件夹路径：'+ in_path + '\n')
    while_flag = 0
    while while_flag == 0:
        tag = input('是否修改路径？y/n'+ '\n')
        if tag == 'y':
            while_flag = 1
            in_path = input("请输入文件夹路径"+ '\n')
            return in_path
        elif tag == 'n':
            while_flag = 1
            return in_path
        else:
            print('输入有误！')


def set_out_path():
    out_path = in_path + dname
#
# out_path = '/Users/liyan/Documents/文本/'
#
# flag = 27    #文件夹序号
# flag2 = 2786 #文件夹内容序号
#
# file = out_path + str(flag) +'.tsc'
#
# def rename(path, file, f, f2):
#     # os.chdir() 方法用于改变当前工作目录到指定的路径。
#     os.chdir(path)
#     # 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。
#     items = os.listdir(path)
#     items.sort() # 内容排序
#     items2 = open(file, mode='a')
#
#
#
#     for name in items:
#         if name[0] != '.':  #排除'.'开头的隐藏文件
#
#             num0 = '%02d' % f    # 格式化序号  2 --> 02
#             num = '%07d' %  f2    #   866 --->  0000866
#             kuo_zhan_ming = name.split('.')[-1]   # 提取扩展名
#             new_name = 'PPT' + '_' + num0 + '_' + num + '.' + kuo_zhan_ming    #组合新文件名
#             # 遍历所有文件
#             os.renames(name, new_name)  # 改名
#             items2.writelines(name + '\t' + new_name + '\n')  #写入文件
#             f2 += 1  # 文件序号自增
#
#
#     items.clear()
#     items2.close()

in_path = set_in_path()
dname = in_path.split('/')[-1]
if dname == '':
    dname = in_path.split('/')[-2]
print(in_path , dname)
# rename(in_path, file, flag, flag2)
