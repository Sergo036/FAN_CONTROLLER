__all__ = ['parese_url_data','logg']


from time import sleep,time
import datetime



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
    def __init__(self,f_name,size = 2000):
        self.f_size = size/10000
        self.file = f_name

    def __check_size(self):
        import os
        try:
            self.f_stat = os.stat(self.file)
            self.a = self.f_size-self.f_stat.st_size/1e+6
            if (self.a<0.005):
                return True
        except:
            return False
    
        
        


    def __writer(self,message): 
        with open (self.file,'a',encoding='utf-8') as f:
            while not isinstance(message,list):
                f.writelines(f"{message}\n")
                f.close()
                break
            else:
                for line in message:
                    f.writelines(line)
                f.close()
            
            
    
    def __re_writer(self):
        self.re_write_data = []
        with open (self.file,'r') as f:
            self.read_data = f.readlines()
            f.close()
        self.read_data_size = len(self.read_data)
        with open (self.file,'w') as f:
            f.seek(0)
            f.close()
        for i in range((int(self.read_data_size/2)),self.read_data_size):
            self.re_write_data.append(self.read_data[i])
        logging.__writer(self,self.re_write_data)
        
        

        
        

        
    def info(self,message):
        if not logging.__check_size(self):
            logging.__writer(self,message = f"[INFO] : {message}")
        elif logging.__check_size(self):
            #return
            logging.__re_writer(self)
    def debug(self,message):
        logging.__writer(self,level='INFO',message = message)
    def error(self,message):
        logging.__writer(self,level='INFO',message = message)
        
            
            

logg = logging('logfile.log')



#print(logg.f_size_info()/1000)
st = time()
for i in range(0,100000):
    
    current_time = datetime.datetime.now()
    logg.info(f'Test Message Test Message Test Message Test Message Test Message. Time: {current_time.second}:{current_time.microsecond}') 

print(time()-st)
#print(logg.f_size_info()/1e+6)
"""
with open ('logfile.log','r') as f:
    a = f.readlines()
    lines_len = len(a)
    b = []
    for i in range(int(lines_len/2),lines_len):
        b.append(a[i])
    f.close()
    print(lines_len)
with open ('logfile.log','w') as f:
    f.seek(0)
    f.writelines(b)
    f.close()
print('Done')

def __check_size (self):
        self.a = 0.2005-self.f_size_info()/1e+6
        if (self.a<0.0001):
            return logging.__reader(self)
        else:
            return False


    def f_size_info(self):
        import os
        self.f_stat = os.stat(self.file)
        return (self.f_stat.st_size)

def __reader (self):
        with open (self.file,'r') as f:
            self.file_lines_data = f.readlines()
            self.lines_size = len(self.file_lines_data)
            f.close()
        with open (self.file, 'w') as f:
            f.close()
        self.new_data_lines = []
        for i in range(int(self.lines_size/2),self.lines_size):
            self.new_data_lines.append(self.file_lines_data[i])
        print(f'Done. Size: {self.f_stat.st_size}')
        
        
        return True

"""

    
    




