__all__=['GlobalData']  


class HttpData:
    def __init__(self) -> None:
        self.POSTrequest_data = dict(req_flag='0x0',req_data=['0x0','0x0','0x0'])
        self.POSTresponse_data = dict(status='0x0')
        self.GETresponse_data = dict(collant_temp='0xC0',fan_speed=0,ac_state='0x4',error_code='0x65')
        self.settings = dict(low_speed = 0,hight_speed=0,setpoint=0)
        
     

    def parse_request_data(self,client_request):
        while len(client_request)!=1:
            self.POSTrequest_data['req_flag'] = client_request[0]
            if (len(client_request)-1)==(len(self.POSTrequest_data['req_data'])):
                for i in range(len(self.POSTrequest_data['req_data'])):
                    self.POSTrequest_data['req_data'][i]=client_request[i+1]
                break
            else:
                return
        else:
            self.POSTrequest_data['req_flag'] = client_request[0]
        return 
    
    def create_response_data(self,method: str,server_response: list)->None:
        
        def __get_method():
            self.GETresponse_data = dict(collant_temp=server_response[0],fan_speed=str(server_response[1]),ac_state=server_response[2],error_code=server_response[3])
            return
        
        def __post_method():
            self.POSTresponse_data = server_response[0]
            return

        if method == 'GET' and len(server_response)>1:
            __get_method()
        else:
            __post_method()
        


GlobalData = HttpData()






    

            
        

    












    