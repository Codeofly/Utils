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
import re

def get(p='/'):
    path = p  # 目录路径
    flag = 1  # 循环判断
    while flag == 1:
        print('请选择下一目录\n--|-----------')
        index = 0  # 目录列表 索引
        dir_list = os.listdir(path)  # 获取指定目录下的所有子目录的列表
        dir_list = [x for x in dir_list if x[0] != '.']  # 去除隐藏文件
        dir_list.sort()
        # 输出选项列表
        print('0', '|', '上一级')
        for i in dir_list:
            index += 1
            print(index, '|', i)
        print('---------------\n直接回车确定路径\n---------------')
        # 获取选项序号
        int_index = input('当前路径：' + path + '\n请输入对应目录序号：')
        # 直接回车结束循环
        if int_index == '':
            break
        # 判断是否合法
        try:
            d_index = int(int_index)
        except:
            print('输入错误，请输入数字!!!')
            continue
        # 判断序号
        if d_index == 0:
            if path != '/':
                if path[-1] != '/':
                    path = '/'.join(path.split('/')[:-1]) + '/'
                else:
                    path = '/'.join(path.split('/')[:-2]) + '/'
            else:
                print('当前为根目录无法返回上一级，请重新选择！')
                continue
        elif 0 < d_index <= len(dir_list):
            path = path + str(dir_list[d_index - 1]) + '/'
        else:
            print('输入错误，请输入0~' + str(len(dir_list)) + '整数')

    return path

split_key = '.'
print('选择输入路径')
path = get()
print('path ：' + path)


key_rename = input('请输入AV编号（回车确定）：')

key_Text = input('请输入想删除的相同字段（回车确定）：')


def rename(flag, file, keyword):
    os.chdir(file)
    items = os.listdir(file)
    fil = re.compile(u'[^a-zA-Z\u4e00-\u9fa5]+', re.UNICODE)
    for name in items:
        # print(name)
        a = name.split(flag)[0]
        if not os.path.isdir(name):
            if keyword in name:

                # new_name = name.replace(keyword+',P'+a+')', '')
                name2 = name.replace('(' + keyword + ',P' + a + ')', '')

                d = fil.search(name2).span()[1]

                new_name = name2.split('.')[0]+'.'+ name2[d:]

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



delete_the_same_string(path, key_Text)
rename(split_key, path, key_rename)