# CloudInf Restconf Lab
This Python script can be extended during the CloudInf Restconf Lab. 
It shows you how to do a basic Restconf request.
The task is specified in a separate document.

## Konfiguration
Um den Router zu konfigurieren werden folgende XML-Conf-Files mittels Restconf PUT-Operation geladen.
- Ospf Konfiguration
- BGP Konfiguration


## Device Config
interface loopback 0
    ip address 9.9.9.9 255.255.255.255
    
interface loopback 1
    ip address 192.168.9.1 255.255.255.0
    
router bgp 9
    neighbor 10.3.255.120 remote-as 20  
    network 192.168.9.0 mask 255.255.255.0
    
router ospf 1
    router-id 9.9.9.9 <br>
    network 10.3.255.0 0.0.0.255 area 0  
    network 192.168.9.0 0.0.0.255 area 0

int GigabitEthernet1
    ip ospf 1 area 0
    

## Device Infos
Die Device Informationen werden in device_infos.yaml festgelegt.

## Usage
Start the program:
`python restconf.py`