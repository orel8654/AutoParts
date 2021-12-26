import asyncio

async def re_write(num):
    import re

    with open(f'reports_rsa/{num.upper()}.txt', 'r') as file:
        line = file.readlines()
        lst = []
        lst_gen = []
        for i in line:
            lst.append(i.strip('\n'))
            if i == '\n':
                lst_gen.append(lst)
                lst = []
    sort_no_cost = []
    sort_lst = []
    for i in lst_gen:
        if re.search('Цена',i[-2]):
            sort_no_cost.append(i)
        else:
            sort_lst.append(i)
    sort_cost = []
    for i in sort_lst:
        try:
            cost = i[-2].split(':')[-1].replace('*', '').replace('.', '').strip()
            i.append(int(cost))
            sort_cost.append(i)
        except:
            continue
    fin_lst = sorted(sort_cost, key = lambda k : k[-1], reverse=True)
    fin_lst.extend(sort_no_cost)
    with open(f'reports_rsa/{num.upper()}.txt', 'w') as file:
        for i in fin_lst:
            file.write(f'{i[0]}\n{i[1]}\n{i[2]}\n{i[3]}\n\n')

if __name__ == '__main__':
    asyncio.run(re_write('ENY34250622'))