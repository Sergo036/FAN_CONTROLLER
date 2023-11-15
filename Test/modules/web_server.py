try:
    import uasyncio as asyncio
except:
    import asyncio


from .HttpGlobaldata import GlobalData
from .utils import parese_url_data,logg
from .settings_file_actions import get_settings_param




__all__=['handle_echo','POSTresponse']


async def POSTresponse(writer):
    writer.write(b'HTTP/1.0 200 OK\n')
    writer.write(b'Content-type: text/plain\n')
    writer.write(b'Connection: close\n\n')
    writer.write(bytes(GlobalData.POSTresponse_data['status'],'utf-8'))
    await writer.drain()
    writer.close()
    await writer.wait_closed()
     
        

async def GETresponse(writer,msg):
    writer.write(b'HTTP/1.0 200 OK\n')
    writer.write(b'Content-type: text/plain\n')
    writer.write(b'Connection: close\n\n')
    writer.write(bytes(msg,'utf-8'))
    await writer.drain()
    writer.close()
    await writer.wait_closed()
    
    
async def not_found(writer):
        not_found_page = """

        <!DOCTYPE html>
        <html lang="ru">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="shortcut icon" href="#" type="image/x-icon">
                <title>Document</title>
            </head>
            <body style="background: #161616">
                <center>
                    <h1 style="color:gray;font-size:40px">404 Code</h1>
                    <h2 style="color:gray"> This page doesn't exist </h2>
                    <h3 style="color:gray">Return to <a href="/" style="color:rgba(77, 231, 141, 0.363)">main</a> page</h3>

                    
                </center>
                
                
            </body>
        </html>

        """
        
        writer.write(b'HTTP/1.0 404 Not found\n')
        writer.write(b'Content-type: text/html\n')
        writer.write(b'Connection: close\n\n')
        writer.write(bytes(not_found_page,'utf-8'))
        await writer.drain()
        writer.close()
        await writer.wait_closed()
        


async def render_template(writer,msg):
        if msg =='':
            msg = 'index.html'
        content_types = {'html':'Content-Type: text/html\n','css':'Content-Type: text/css\n','js':'Content-Type: application/javascript\n','log':'Content-type: text/plain\n'}
        shar_index = msg.find('.')
        try:
            with open (msg,'r')as f:
                __data = f.read()
                f.close()
            content_type = content_types[msg[shar_index+1:]]
            writer.write(b'HTTP/1.0 200 OK\n')
            writer.write(bytes(content_type,'utf-8'))
            writer.write(b'Connection: close\n\n')
            writer.write(bytes(__data,'utf-8'))
            await writer.drain()
            writer.close()
            await writer.wait_closed()
        except:
             logg.error(f"Page '{msg}' not found")
             await not_found(writer)


async def handle_echo(reader, writer):
        data = await reader.readline()
        while await reader.readline() != b"\r\n":
            pass
        message = data.decode()
        path_first_index = message.find(' ')
        path_last_index = message.find('HTTP')
        method = message[0:path_first_index]
        request_url = message[(path_first_index+1):(path_last_index-1)]
        if method == 'GET':
            if not '?' in request_url:
                await render_template(writer,request_url[1:])  
            elif 'get_data' in request_url:
                await GETresponse(writer,str(GlobalData.GETresponse_data))
            elif 'settings' in request_url:
                 GlobalData.settings['low_speed'] = get_settings_param('Low speed val')
                 GlobalData.settings['hight_speed'] = get_settings_param('Hight speed val')
                 GlobalData.settings['setpoint'] = get_settings_param('Setpoint val')
                 print('get settings')
                 await GETresponse(writer,str(GlobalData.settings))
        elif method == 'POST':
            request_url_data = request_url[2:]
            parse_url_data = parese_url_data(request_url_data)
            GlobalData.POSTrequest_data = parse_url_data
            await asyncio.sleep(.2)
            await POSTresponse(writer)
                
                
            
            
            
            
                
                    
                
""""            
writer.write(b'Content-Type: text/plain')
writer.write(bytes(f"/?data={online_data[0]},{online_data[1]},{online_data[2]},{online_data[3]},{online_data[4]},{online_data[5]},{online_data[6]}",'utf-8'))
print(response_data)

global REQUEST_SWITCHES

print(request_path)
REQUEST_SWITCHES = 0

if len(response_data[1])>0:
                if not set_param(response_data[1].split(',')):
                    writer.write(b'HTTP/1.0 200 OK\n')
                    writer.write(b'Connection: close\n\n')
                    await writer.drain()
                    writer.close()
                    await writer.wait_closed()
                    
                elif set_param(response_data[1].split(',')):
                    #print('save new data')
                    writer.write(b'HTTP/1.0 200 OK\n')
                    writer.write(b'Content-Type: text/plain')
                    writer.write(b'Connection: close\n\n')
                    writer.write(bytes(f"/?new_data_saved","utf-8"))
                    await writer.drain()
                    writer.close()
                    await writer.wait_closed()

changeData.REQUEST_SWITCHES = 0
online_data = []
REQUEST_SWITCHES = 0
NEW_SETTINGS_DATA = [0,0,0]
def set_online_data (e):
    global online_data
    online_data=e

def get_response_data():
    return REQUEST_SWITCHES,NEW_SETTINGS_DATA

def set_param(*args):
        args_list = []
        global REQUEST_SWITCHES,NEW_SETTINGS_DATA
        for arg in args[0]:
            args_list.append(arg)
        if len(args_list)>1:
            REQUEST_SWITCHES = int(args_list[0],16)
            NEW_SETTINGS_DATA[0]=(int(args_list[1],16))
            NEW_SETTINGS_DATA[1]=(int(args_list[2],16))
            NEW_SETTINGS_DATA[2]=(int(args_list[3],16))
            return True
        elif len(args_list) ==1:
            REQUEST_SWITCHES = int(args_list[0],16)
            return False

"""
            




