import os
import random
import re
import sys
import time

sys.setrecursionlimit(1000000)  # 设置递归函数次数上限为一百万
# 引入时间，系统，正则表达式，随机模块
# 游戏退出
Esc = False
# 游戏重新加载
Continue = False
# 检验esc的正则表达式
esc = re.compile("^esc{0,3}")
# 检验reset的正则表达式
reset = re.compile("^reset{0,5}")
# 检验数字的正则表达式
number = re.compile("[1-6]{0,2}")
# 检验标记的正则表达式
mark = re.compile("b[1-6]{0,2}")
# 记录序号
Number = 0
Ray_number = 5  # 雷数显示
Random = []  # 随机从中选取五个字符串
for i in range(1, 6):
    for j in range(1, 6):
        Random.append(str(i) + str(j))


# 游戏运行中，判断玩家是否输入合法
def check(Str):
    global Number, Esc, d, Ray_number
    # 检查是否输入esc，并转换成字符串型
    Break = "".join(esc.findall(Str))
    # print(Break)
    # 检查是否输入reset，并转换成字符串型
    Reset = "".join(reset.findall(Str))
    # print(Reset)
    # 检查是否输入的为数字且为两位，并转换成字符串型
    Number = "".join(number.findall(Str))
    # 检查是否输入的标记，并转换成字符串型
    Mark = "".join(mark.findall(Str))
    # print(Number)
    if Break == 'esc':
        # 退出游戏
        Esc = True
        return 1
    elif Reset == 'reset':
        # 重新开始游戏
        print('下一场游戏正在加载中')
        print('waiting....')
        time.sleep(2)
        return 1
    elif len(Mark) == 3 and len(Str) == 3 and Mark == Str:
        list_Mark = list(Mark)  # 字符串转换成列表
        if int(list_Mark[1]) > 5 or int(list_Mark[2]) - 1 > 4 or int(list_Mark[1]) < 1 or int(list_Mark[2]) - 1 < 0:
            # 检验输入的序号是否有效
            print('请输入有效标记序号！')
            print('waiting....')
            time.sleep(2)
            return 2
        else:
            if d[int(list_Mark[1])][int(list_Mark[2]) - 1] == '⊙':
                d[int(list_Mark[1])][int(list_Mark[2]) - 1] = ''
                Ray_number = Ray_number + 1
                return 2
            elif d[int(list_Mark[1])][int(list_Mark[2]) - 1] == '':
                if Ray_number <= 0:
                    print('标记符号达到上限，无法继续标记！')
                    print('waiting....')
                    time.sleep(2)
                    return 2
                else:
                    d[int(list_Mark[1])][int(list_Mark[2]) - 1] = '⊙'
                    Ray_number = Ray_number - 1
                    return 2
            else:
                print('此位以显示，无法标记！')
                print('waiting....')
                time.sleep(2)
                return 2
    elif (Number == '' and Mark == '') or (len(Number) != 0 and Mark != ''):
        # 经过正则表达式检测后，值都为空不合格，值都不空不合格，输入的字符串与检测出的数值字符串不符
        print('请按照正确要求输入！')
        print('waiting....')
        time.sleep(2)
        return 2
    elif Number == Str:
        return 3


# 游戏已结束时，判断玩家是否重开游戏或退出
def check_over(Str):
    global Continue, Esc
    # 检查是否输入esc，并转换成字符串型
    Break = "".join(esc.findall(Str))
    # print(Break)
    # 检查是否输入reset，并转换成字符串型
    Reset = "".join(reset.findall(Str))
    # print(Reset)
    if Break == 'esc':
        # 退出游戏
        Esc = True
        Continue = True
        return True
    elif Reset == 'reset':
        # 重新开始游戏
        print('下一场游戏正在加载中')
        print('waiting....')
        Continue = True
        time.sleep(2)
        return True
    elif (len(Break) == 0 and len(Reset) != 0) or (len(Break) != 0 and len(Reset) != 0) or Reset != Str:
        # 经过正则表达式检测后，值都为空不合格，值都不空不合格，输入的字符串与检测出的数值字符串不符
        print('请按照正确要求输入！')
        print('waiting....')
        time.sleep(2)
        return False


# 玩家选择一个位置点后，判断周围位置点的雷数，并作出相应的响应
def Around(Number):
    global d
    # 将字符串数值分离开
    a = int(Number) // 10  # 十位
    b = int(Number) % 10 - 1  # 个位
    # 统计周围雷数，并返回值
    ray_number = 0
    top = int(Number) - 10  # 上方
    bottom = int(Number) + 10  # 下方
    left = int(Number) - 1  # 左方
    right = int(Number) + 1  # 右方
    top_l = int(Number) - 11  # 上左方
    top_r = int(Number) - 9  # 上右方
    bottom_l = int(Number) + 9  # 下左方
    bottom_r = int(Number) + 11  # 下右方
    around = [top, bottom, left, right, top_l, top_r, bottom_l, bottom_r]  # 存储输入的序号周围序号数
    around_t = []  # 存储输入的序号周围合法序号数
    # print(around)
    for i in range(len(around)):
        # 判断次序号数是否属于雷区中的
        if str(around[i]) in Random:
            e = around[i] // 10  # 十位
            f = around[i] % 10 - 1  # 个位
            if len(str(d[e][f])) == 0:
                around_t.append(str(around[i]))  # 将周围合法序号数存储进去
            if str(around[i]) in ray:
                # 判断次序号数是否属于雷码中
                ray_number = ray_number + 1
    # 玩家输入的序号位置显示周围雷数
    if ray_number == 0:
        d[a][b] = '◎'
    elif ray_number == 1:
        d[a][b] = '①'
    elif ray_number == 2:
        d[a][b] = '②'
    elif ray_number == 3:
        d[a][b] = '③'
    elif ray_number == 4:
        d[a][b] = '④'
    elif ray_number == 5:
        d[a][b] = '⑤'
    elif ray_number == 6:
        d[a][b] = '⑥'
    elif ray_number == 7:
        d[a][b] = '⑦'
    # print(around_t)
    if ray_number == 0:
        for i in range(len(around_t)):
            Around(str(around_t[i]))


# 游戏开始运行
while True:
    # 输入esc退出游戏
    if Esc:
        break
    # 游戏开始循环
    # 游戏重新加载关闭
    Continue = False
    # 创建一个空容器
    d = []
    # 为容器里添加初始值
    for i in range(6):
        d.append([])
        for j in range(1, 6):
            if i == 0:
                d[i].append(j)
            else:
                d[i].append('')
        # end
    # end
    random.shuffle(Random)  # 打乱无返回值
    ray = random.sample(Random, 5)  # 随机返回五个字符串，代表着五颗雷
    Ray_number = 5  # 重置雷数
    # print(ray)#显示雷码
    # 游戏开始下一局
    while True:
        Win = 0
        Other = 0
        for i in range(len(d)):  # 每次循环判断是否到达游戏胜利条件
            for j in range(len(d[i])):
                if d[i][j] == '⊙':
                    if str(i) + str(int(j + 1)) in ray:
                        Win = Win + 1
                if d[i][j] == '':
                    if str(i) + str(int(j + 1)) in ray:
                        Win = Win + 1
                elif d[i][j] != '⊙' and d[i][j] != '':
                    Other = Other + 1

        if Win == 5 and Other == 25:  # 胜利条件达到后，则显示结果
            while True:
                p_ray = 0
                os.system('cls')  # 界面清空
                print('\t\t代码扫雷')
                for i in range(len(d)):  # 绘制答案
                    if i > 0:
                        print(i, end='')
                    else:
                        print('※', end='')
                    for j in range(len(d[i])):
                        if str(i) + str(int(j + 1)) in ray:
                            if d[i][j] == '⊙':
                                d[i][j] = '¤'
                                print('\t' + str(d[i][j]), end='')
                                p_ray = p_ray + 1
                            else:
                                d[i][j] = '●'
                                print('\t' + str(d[i][j]), end='')
                        else:
                            print('\t' + str(d[i][j]), end='')
                    # end
                    print('\n\n')
                # end
                print('\tYOU WIN!Happy every day!')
                print('注:行数是十位,列数是个位,标记雷的符号样式为⊙,成功排除雷的符号标记样式为¤。')
                print('\t你成功排除' + str(p_ray) + '个')
                WIN = input('请输入reset重新开始游戏\n或输入esc退出游戏:')
                gg = check_over(WIN)  # 调用check函数检查输入值内容
                if gg:
                    break

        if Continue:
            break
        os.system('cls')  # 界面清空
        print('\t\t代码扫雷')
        for i in range(len(d)):  # 绘制雷区
            if i > 0:
                print(str(i), end='')
            else:
                print('※', end='')
            for j in range(len(d[i])):
                print('\t' + str(d[i][j]), end='')
            # end
            print('\n\n')
        # end
        # 接受用户输入信息
        print('当前剩余雷数：' + str(Ray_number))
        print('注:行数是十位,列数是个位,标记雷的符号样式为⊙,成功排除雷的符号标记样式为¤。')
        Str = input('请输入有效序号例如:12\n或输入标记序号例如:b12即可标记雷\n或重复输入标记序号如:b12即可清除标记\n或输入reset重新开始游戏\n或输入esc退出游戏\n请输入:')
        B = check(Str)  # 调用check函数检查输入值内容
        if B == 1:
            break
        if B == 2:
            continue
        if B == 3:
            # print(str(Number))
            # 将字符串数值分离开
            a = int(Number) // 10  # 十位
            b = int(Number) % 10 - 1  # 个位
            if a > 5 or b > 4 or a < 1 or b < 0:
                # 检验输入的序号是否有效
                print('请输入有效序号！')
                print('waiting....')
                time.sleep(2)
            else:
                # 当输入的序号是雷码时，则游戏结束，显示所有的答案
                if Number in ray:
                    while True:
                        p_ray = 0
                        os.system('cls')  # 界面清空
                        print('\t\t代码扫雷')
                        for i in range(len(d)):  # 绘制答案
                            if i > 0:
                                print(i, end='')
                            else:
                                print('※', end='')
                            for j in range(len(d[i])):
                                if str(i) + str(int(j + 1)) in ray:
                                    if d[i][j] == '⊙':
                                        d[i][j] = '¤'
                                        print('\t' + str(d[i][j]), end='')
                                        p_ray = p_ray + 1
                                    else:
                                        d[i][j] = '●'
                                        print('\t' + str(d[i][j]), end='')
                                else:
                                    print('\t' + str(d[i][j]), end='')
                            # end
                            print('\n\n')
                        # end
                        print('\tYOU LOSE!GAME OVER!')
                        print('注:行数是十位,列数是个位,标记雷的符号样式为⊙,成功排除雷的符号标记样式为¤。')
                        print('\t你成功排除' + str(p_ray) + '个')
                        OVER = input('请输入reset重新开始游戏\n或输入esc退出游戏:')
                        gg = check_over(OVER)  # 调用check函数检查输入值内容
                        if gg:
                            break
                        # print('下一场游戏正在加载中')
                        # print('\twaiting....5s')
                        # time.sleep(5)
                # 当输入的序号不是雷码，则显示周围雷数
                else:
                    if d[a][b] != '⊙' and d[a][b] != '':
                        print('此位以显示，请勿重复输入!')
                        print('waiting....')
                        time.sleep(2)
                        continue
                    if d[a][b] == '⊙':
                        Ray_number = Ray_number + 1
                    Around(Number)  # 调用函数统计周围雷数
