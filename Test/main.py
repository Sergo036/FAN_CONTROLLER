import sys
from machine import Pin

try:
    import uasyncio as asyncio
except:
    import asyncio

from modules import handle_echo,create_AP,GlobalData,set_user_settings,get_settings_param,get_default_settings,logg

if sys.platform == 'esp8266':
    IP_ADDR = create_AP()
else:
    IP_ADDR = '172.20.10.7'
    





settings_value = [get_settings_param('Low speed val'),get_settings_param('Hight speed val'),get_settings_param('Setpoint val')]
out = Pin(14,Pin.OUT)

def remote_controll(e):
    def __reset():
        print('Reset')
        GlobalData.POSTresponse_data['status'] = '0x0'
        
        return True
    def __low_speed_on():
        print('Low speed on')
        GlobalData.POSTresponse_data['status'] = '0x11'
        logg.info('Remote low speed activite')
        out.value(True)
        return True
    def __low_speed_off():
        print('Low speed off')
        GlobalData.POSTresponse_data['status'] = '0x10'
        logg.info('Remote low speed deactivite')
        out.value(False)
        return True
    def __hight_speed_on():
        print('Hight speed on')
        GlobalData.POSTresponse_data['status'] = '0x21'
        logg.info('Remote hight speed activite')
        return True
    def __hight_speed_off():
        print('Hight speed off')
        GlobalData.POSTresponse_data['status'] = '0x20'
        logg.info('Remote hight speed deactivite')
        return True
    def __save_new_settings():
        global settings_value
        print('Save new settings')
        GlobalData.POSTresponse_data['status'] = '0xFF'
        
        if set_user_settings(GlobalData.POSTrequest_data['req_data']):
            
            settings_value = GlobalData.POSTrequest_data['req_data']
            logg.info('Save new settings')
        return True
    def __get_default_settings():
        global settings_value
        GlobalData.settings['low_speed'],GlobalData.settings['hight_speed'],GlobalData.settings['setpoint'] = get_default_settings()
        settings_value = get_default_settings()
        GlobalData.POSTresponse_data['status'] = '0x85'
        set_user_settings(settings_value)
        logg.info('Get default settings')
        return True
    func_dict = {'0x16':__reset,'0x4':__low_speed_on,'0x28':__low_speed_off,
                 '0x8':__hight_speed_on,'0x50':__hight_speed_off,'0xC0':__save_new_settings,
                 '0x32':__get_default_settings}
    func_dict[e]()



async def main():
    
    while True:
        for i in range(-50,151):
            GlobalData.GETresponse_data['collant_temp'] = hex(int(i*.78431373)+50)
            await asyncio.sleep(1)
        await asyncio.sleep(1)
        


async def web():
    oldPOSTRequestData = {}
    if sys.platform == 'esp8266':
        IP_ADDR = create_AP()
        asyncio.create_task(asyncio.start_server(handle_echo, IP_ADDR, 8080))
    else:
        IP_ADDR = '172.20.10.7'
        asyncio.create_task(asyncio.start_server(handle_echo, IP_ADDR, 8080))
    
    
    while True:
        while (oldPOSTRequestData!=GlobalData.POSTrequest_data): 
            oldPOSTRequestData = GlobalData.POSTrequest_data
            if (oldPOSTRequestData['req_flag']!='0x0'):
                remote_controll(GlobalData.POSTrequest_data['req_flag'])
                oldPOSTRequestData['req_flag'] = GlobalData.POSTrequest_data['req_flag']='0x0'
            break
        await asyncio.sleep(.2)


def start():
    loop = asyncio.new_event_loop()
    loop.create_task(web())
    loop.create_task(main())
    loop.run_forever()


if __name__ == '__main__':
    start()







        
















