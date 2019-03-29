lines = int(input('请输入行数:'))
lines_nei = int(input('请输入掏空行数:'))
tao = 1
for top_line in range(1, lines + 1):
    # print(type(line),line)
    numbers = 2 * top_line - 1
    lastNumbers = 2 * lines - 1
    spaces = lastNumbers // 2 - (numbers // 2)
    for space in range(spaces):
        print(' ', end='')
    
    a = lines - lines_nei
    for number in range(1, numbers + 1):
        if top_line > a:
            #print(tao,((a + 1) * 2 - 1) // 2 + (2 * tao - 1),end='')
            if ((a + 1) * 2 - 1) // 2 < number <= ((a + 1) * 2 - 1) // 2 + (2 * tao - 1):
                print(' ', end='')
            else:
                print('*', end='')
        else:
            print('*', end='')
    if top_line > a and tao < lines_nei:
        # print('ok')
        tao += 1
    print('')
    if number == lastNumbers:
        underNumbers = lastNumbers - 2
        underLinesNei = tao-1
        #print(underLinesNei)
        for under_line in range(1, lines):
            spaces = lastNumbers // 2 - (underNumbers // 2)
            for space in range(spaces):
                print(' ', end='')
            #print(underNumbers // 2)
            for number in range(underNumbers):
                if underLinesNei > 0:
                    if (underNumbers // 2)-(underLinesNei*2-1)//2-1 < number < (underNumbers // 2)+(underLinesNei*2-1)//2+1:
                        print(' ', end='')
                    else:
                        print('*', end='')
                else:
                    print('*', end='')
            print('')
            underNumbers -= 2
            underLinesNei -= 1
