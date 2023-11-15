__all__ = ['parese_url_data','logg']



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






class logging:
    def __init__(self,f_name):
        self.file = f_name
        from machine import RTC
        self.rtc = RTC()
        self.rtc.datetime((2023, 10, 5, 1, 22, 00, 42, 0))
        
    def __writer(self,level,message):
        self.date_time = self.rtc.datetime()
        self.datetime_format = f"{self.date_time[2]}.{self.date_time[1]}.{self.date_time[0]} {self.date_time[4]}:{self.date_time[5]}:{self.date_time[6]}"
        with open (self.file,'a',encoding='utf-8') as f:
            f.write(f"{self.datetime_format} [{level}]:{message}\n")
            f.close()
        
    def info(self,message):
        logging.__writer(self,'INFO',message)
    def debug(self,message):
        logging.__writer(self,'DEBUG',message)
    def error(self,message):
        logging.__writer(self,'ERROR',message)
        
            
            

logg = logging('logfile.log')





