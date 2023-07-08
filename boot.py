import network

# Connect to Wi-Fi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Muttur', 'Chandu@1')

# Wait for connection
while not sta_if.isconnected():
    pass

# Print connection details
print('Network connected:', sta_if.ifconfig())


