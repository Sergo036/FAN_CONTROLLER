
def main():
    import network
    from time import sleep
    ssid='iPhone(Sergey)'
    pswd = 'Sergo036'

    def create_ap():
        try:
            ap = network.WLAN(network.AP_IF)
            ap.active(False)
            sleep(.1)
            ap.active(True)
            ap.config(essid = 'CNT_DSBD', password = '123456789')
            print('Ceated')
            return True, ap.ifconfig()[0]
    
        except:
            print('Error')
            return False, None


    def scan_networks(ssid):
        for i in range(0,5):
            sta = network.WLAN(network.STA_IF)
            sta.active(False)
            sleep(.1)
            sta.active(True)
            networks_array = sta.scan()
            for networks_info in networks_array:
                network_ssid = networks_info[0].decode('utf-8')
                if network_ssid == ssid:
                    sta.active(False)
                    return True
            print('Scan')
            sleep(.5)
        sta.active(False)
        return False


    def do_connect(ssid,pswd):
        conection_count = 0
        sta = network.WLAN(network.STA_IF)
        sta.active(False)
        sleep(.1)
        if not sta.isconnected():
            sta.active(True)
            sta.connect(ssid, pswd)
            sleep(.5)
            while not sta.isconnected() and conection_count<3:
                sleep(1)
                conection_count +=1
                pass
        if sta.isconnected():
            return True, sta.ifconfig()[0]
        else:
            return False, None


        
    
        

    return create_ap()
        
    
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
