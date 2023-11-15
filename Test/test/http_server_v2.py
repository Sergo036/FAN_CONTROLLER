#HDR_200 = b'HTTP/1.1 200 OK\n'
    #HDR_404 = b'HTTP/1.1 404 OK\n'
    #HDR_404_MSG = b'Page non found'
    #PATH_LIST = []
    #CONTENT = render_page('index.html')

def start_server(ip):
    import socket


    print('Server starting...')
    low_speed_val = 30
    hight_speed_val = 60
    setpoint_val = 90
    ERRORS = 0

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((ip,8080))
    server.listen(1)


    def file_data(f_name):
        with open(f_name, 'r') as f:
            data = f.read()
            f.close()
        return data
    
    def get_switch_status(status):return int((int(status[0])*80)+(int(status[1])*80))

    def get_temp(t):return int((t*.78431373)+50)

    def get_speed(s):return s

    def create_response_msg():return f'{hex(get_temp(35.5))},{hex(get_speed(60))},{hex(get_switch_status([True,False]))},{hex(low_speed_val)},{hex(hight_speed_val)},{hex(setpoint_val)},{hex(ERRORS)}'

    def send_response_only(code):
        HDR_STATUS = {200:b'HTTP/1.1 200 OK\n',404:b'HTTP/1.1 404 OK\n'}
        conn.send(HDR_STATUS[code])
        conn.send(b'Connection: close\n\n')
        conn.close()

    def render_page(msg):
        if msg == '':
            msg = 'index.html'
        content_types = {'html':'Content-Type: text/html\n','css':'Content-Type: text/css\n','js':'Content-Type: application/javascript\n'}
        shar_index = msg.find('.')
        try:
            content_type = content_types[msg[shar_index+1:]]
            conn.send(b'HTTP/1.1 200 OK\n')
            conn.send(bytes(content_type,'utf-8'))
            conn.send(b'Connection: close\n\n')
            conn.sendall(bytes(file_data(msg),'utf-8'))
            conn.close()
        except KeyError:
            send_response_only(200)

    def send_response():
        conn.send(b'HTTP/1.1 200 OK\n')
        conn.send(b'Content-Type: text/plain\n')
        conn.send(b'Connection: close\n\n')
        conn.sendall(bytes(create_response_msg(),'utf-8'))
        conn.close()
    
    
    while True:
        conn, addr = server.accept()
        request = b''
        request = conn.recv(512)
        print(len(request.decode('utf-8')))
        if len(request.decode('utf-8'))>0:
            request_list = []
            request_list.append(request.decode('utf-8'))
            path_first_index = request_list[0].find(' ')
            path_last_index = request_list[0].find('HTTP')
            path = request_list[0][path_first_index+1:path_last_index-1]
            print(path)
            if not '?' in path: 
                render_page(path[1:])
            elif '?client_data=' in path:
                client_msg=path.split('=')
                client_data = client_msg[1]
                send_response()
                print(client_data)
                conn.close()
        else:
            conn.close()
       
if __name__ == '__main__':
    try:
        start_server()
    except KeyboardInterrupt:
        pass