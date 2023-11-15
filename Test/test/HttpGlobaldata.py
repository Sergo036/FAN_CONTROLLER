__all__=['GlobalData']  


class HttpData:
    def __init__(self) -> None:
        self.POSTrequest_data = dict(req_flag=None,req_data=[None,None,None])
        self.POSTresponse_data = dict(status=None)
        self.GETresponse_data = dict(collant_temp=None,fan_speed=None,ac_state=None,error_code=None)
        
     

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





    

            
        

    












    