import json,os

__all__=['get_settings_param','get_default_settings','set_user_settings']



def __check_file_name(f_name):
    for f in os.listdir():
        if f == f_name:
            
            return True
        
    
    return False

def read_file(f_name):
    with open (f_name,'r') as f:
        json_obj = json.loads(f.read())
        f.close()
    return json_obj


def get_settings_param(param):
    file_available = __check_file_name('user_settings.json')
    
    if file_available:
        json_obj = read_file('user_settings.json')
        return json_obj[param]
    elif not file_available:
        json_obj = read_file('default.json')
        return json_obj[param]
    else:
        
        return None
    

def get_default_settings():
    json_obj = read_file('default.json')
    return [json_obj['Low speed val'],json_obj['Hight speed val'],json_obj['Setpoint val']]

def set_user_settings(settings_data=[30,60,90]):
    data = {'Low speed val':int(settings_data[0]),'Hight speed val':int(settings_data[1]),'Setpoint val':int(settings_data[2])}
    with open ('user_settings.json','w') as f:
        f.write(json.dumps(data))
        f.close()
        return True



        

