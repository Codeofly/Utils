'''

获取 路径

'''

import os


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
