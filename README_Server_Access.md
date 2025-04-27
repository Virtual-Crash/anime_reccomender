In order to access the server

1. CMD / Ubuntu

    #Lets say you lost the IP address or it changed! If on windows run:

    cd .. (until you are in the C drive)
    cd Program Files (x86)
    nmap 192.168.0.1-255 -p 22
    
    #You are looking for one wheere state is open and name matches. luckily the server is names battle-cruiser

    PORT   STATE SERVICE
    22/tcp open  ssh
    MAC Address: F6:09:0D:50:2B:93 (Unknown)

    Nmap scan report for battle-cruiser (192.168.0.101)
    Host is up (0.071s latency).
    

2. ssh server address

    ssh kayla@192.168.0.101

3. log in with my credentials 

    You took a screenshot you big dummy 