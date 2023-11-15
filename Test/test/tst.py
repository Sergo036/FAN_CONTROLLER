

from time import sleep
"""
a = ['0x0','0x1','0x2']



def main(e):
    
    def func_1():
        print('Func 1')
    def func_2():
        print('Func 2')
    def func_3():
        print('Func 3')
    func_dict = {'0x0':func_1,'0x1':func_2,'0x2':func_3}
    func_dict[e]()


for i in a:
    main(i)
    sleep(1)

"""

data_str = 'req_flag:0x16;req_data:0x00,0x11,0x22'


def parese_url_data(e):
    data_list = e.split(';')
    parse_data_list = []
    for data in data_list:
        data = data.split(':')
        for el in data:
            parse_data_list.append(el)
    it = iter(parse_data_list)
    data_dict = dict(zip(it,it))
    data_dict['req_data'] = data_dict['req_data'].split(',')
    return data_dict


d = parese_url_data(data_str)
print(d['req_flag'])
    

    


