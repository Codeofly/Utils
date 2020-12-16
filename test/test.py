# asdf = 'asdfas.ewfasf.wefasf.aewfad'
# #
# # print(asdf.split('.')[-1])
# #
# # print(asdf.split('.')[1:])
# #
# # print(".".join(asdf.split('.')[1:]))

import os
import os.path

path1 = '李岩硬盘' \
        '/大数据' \
        '/2020版大数据教程_完全入门_学完达到大数据工程师水平【千锋】~持续更新中'
path2 = '32 【好程序员】最新大数据_400集_Flink教程（精心录制）'
path3 = '【好程序员】最新大数据_400集_Flink教程（精华版）视频-1'
path = '/Volumes/' + path1 + '/' + path2 + '/' + path3 + '/'
keyword = '.'


def rename(file, key):
    os.chdir(file)
    items = os.listdir(file)

    for name in items:

        if not os.path.isdir(name):
            if keyword in name:
                new_name2 = name.split(key)[1:]
                new_name = '.'.join(new_name2)
                os.renames(name, new_name)
                print(name, new_name)
        else:
            rename(file + '\\' + name, keyword)
            os.chdir('...')

    # print('-----------------------分界线------------------------')
    # items = os.listdir(file)
    # for name in items:
    #     print(name)


# Download/新建文件夹
# rename('/Volumes/Download/新建文件夹/西北大学 - 数据结构 （国家级精品课）', 'Av38920216')

# /Volumes/新工科学科体系/
rename(path, keyword)
