try:
    import uasyncio as asyncio
except:
    import asyncio


from .HttpGlobaldata import GlobalData
from .utils import parese_url_data,logg
from .settings_file_actions import get_settings_param




__all__=['handle_echo','POSTresponse']


async def POSTresponse(writer):
    await writer.awrite(b'HTTP/1.0 200 OK\n')
    await writer.awrite(b'Content-type: text/plain\n')
    await writer.awrite(b'Connection: close\n\n')
    await writer.awrite(bytes(GlobalData.POSTresponse_data['status'],'utf-8'))
    await writer.wait_closed()
    await writer.drain()
    await writer.wait_closed()
    
     
        

async def GETresponse(writer,msg):
    await writer.awrite(b'HTTP/1.0 200 OK\n')
    await writer.awrite(b'Content-type: text/plain\n')
    await writer.awrite(b'Connection: close\n\n')
    await writer.awrite(bytes(msg,'utf-8'))
    await writer.wait_closed()
    await writer.drain()
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
        
        await writer.awrite(b'HTTP/1.0 404 Not found\n')
        await writer.awrite(b'Content-type: text/html\n')
        await writer.awrite(b'Connection: close\n\n')
        await writer.awrite(bytes(not_found_page,'utf-8'))
        await writer.wait_closed()
        await writer.drain()
        await writer.wait_closed()
        


async def render_template(writer,msg):
        if msg =='':
            msg = 'index.html'
        content_types = {'html':'Content-Type: text/html\n','css':'Content-Type: text/css\n','js':'Content-Type: application/javascript\n','log':'Content-type: text/plain\n'}
        shar_index = msg.find('.')
        try:
            with open (msg,'rb')as f:
                __data = f.read()
                f.flush()
                f.close()
            content_type = content_types[msg[shar_index+1:]]
            await writer.awrite(b'HTTP/1.0 200 OK\n')
            await writer.awrite(bytes(content_type,'utf-8'))
            await writer.awrite(b'Connection: close\n\n')
            await writer.awrite(__data)
            await writer.wait_closed()
            await writer.drain()
            await writer.wait_closed()
            
        except OSError:
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
                
                
            
            
            
            
                
                    

            




