'''
序号排序

@split_key :序号分割标识符，用于对应删除'P'后面的序号
@path1 : Volumes目录下一级   '新工科学科体系'
@path2 : Volumes目录下两级   'ywm'
@path3 : Volumes目录下三级   '15 哈尔滨工业大学-单片机原理（国家级精品课）'
@path : 合并后的路径          '/Volumes/'+path1+'/'+path2+'/'+path3+'/'

@rename(split_key, path, key_rename) : 去掉的带有规律的字段


'''
import os
import os.path

split_key = '.'

path1 = '李岩硬盘' \
        '/大数据' \
        '/2020版大数据教程_完全入门_学完达到大数据工程师水平【千锋】~持续更新中'
path2 = '32 【好程序员】最新大数据_400集_Flink教程（精心录制）'
path3 = '【好程序员】最新大数据_400集_Flink教程（精华版）视频-1'
path = '/Volumes/' + path1 + '/' + path2 + '/' + path3 + '/'


def rename(file, keyword):
    os.chdir(file)
    items = os.listdir(file)
    items.sort()
    # print(items)
    flag = 1
    for name in items:

        if not os.path.isdir(name):
            if keyword in name:
                new_name = str(flag) + "." + name
                os.renames(name, new_name)
                print(name, new_name)
                flag += 1
        else:
            rename(file + '\\' + name, keyword)
            os.chdir('...')
    print("-------------------")


def rename2(file, keyword):
    os.chdir(file)
    items2 = os.listdir(file)
    items2.sort()
    # print(items2)
    flag2 = 840
    flag3 = 2
    for name in items2:

        if not os.path.isdir(name):
            if keyword in name:
                num = '%06d' % flag2
                kuo_zhan_ming = name.split('.')[-1]
                new_name = 'ShiPin' + '_' + str(flag3) + '_' + num + '.' + kuo_zhan_ming
                os.renames(name, new_name)
                print(name, new_name)
                flag2 += 1
        else:
            rename(file + '\\' + name, keyword)
            os.chdir('...')


rename(path, split_key)
# rename2(path, split_key)
