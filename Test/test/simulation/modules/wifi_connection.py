__all__ = ['create_AP']


def create_AP():
    import network,time
    ap = network.WLAN(network.AP_IF)
    ap.active(False)
    time.sleep(.2)
    ap.active(True)
    ap.config(essid='Fan Dashboard')
    return ap.ifconfig()[0]
