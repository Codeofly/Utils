'''
去掉的带有规律的字段、去掉的重复字段

@split_key :序号分割标识符，用于对应删除'P'后面的序号
@path1 : Volumes目录下一级   '新工科学科体系'
@path2 : Volumes目录下两级   'ywm'
@path3 : Volumes目录下三级   '15 哈尔滨工业大学-单片机原理（国家级精品课）'
@path : 合并后的路径          '/Volumes/'+path1+'/'+path2+'/'+path3+'/'
@key_rename : 需要去掉的，带有规律的字段         'Av76587547'
@key_shanchuxiangtong : 需要去掉的，重复字段      '千锋Python教程:'

@rename(split_key, path, key_rename) : 去掉的带有规律的字段
@shanchuxiangtong(path, key_shanchuxiangtong): 去掉的重复字段


'''
import os
import os.path

split_key = '.'
path1 = 'E'
path2 = '大数据/2020版大数据教程_完全入门_学完达到大数据工程师水平【千锋】~持续更新中'
path3 = '32 【好程序员】最新大数据_400集_Flink教程（精心录制）/【好程序员】最新大数据_400集_Flink教程（精华版）视频-1'
path = '/Volumes/' + path1 + '/' + path2 + '/' + path3 + '/'

key_rename = 'Av285925486'

key_Text = '好程序员大数据教程：'
# key_Text = '千锋大数据教程：'


def rename(flag, file, keyword):
    os.chdir(file)
    items = os.listdir(file)

    for name in items:
        # print(name)
        a = name.split(flag)[0]
        if not os.path.isdir(name):
            if keyword in name:
                # new_name = name.replace(keyword+',P'+a+')', '')
                new_name = name.replace('(' + keyword + ',P' + a + ')', '')
                os.renames(name, new_name)
        else:
            rename(file + '\\' + name, keyword)
            os.chdir('...')

    print('-----------------------分界线------------------------')
    items = os.listdir(file)
    for name in items:
        print(name)


def delete_the_same_string(file, keyword):
    os.chdir(file)
    items = os.listdir(file)
    print(os.getcwd())
    for name in items:
        print(name)
        # 遍历所有文件
        if not os.path.isdir(name):
            if keyword in name:
                new_name = name.replace(keyword, '')
                os.renames(name, new_name)
        else:
            rename(file + '\\' + name, keyword)
            os.chdir('...')
    print('-----------------------分界线------------------------')
    items = os.listdir(file)
    for name in items:
        print(name)


rename(split_key, path, key_rename)
delete_the_same_string(path, key_Text)
