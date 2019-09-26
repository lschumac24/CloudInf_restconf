# CloudInf Restconf Lab
This Python script can be extended during the CloudInf Restconf Lab. 
It shows you how to do a basic Restconf request.
The task is specified in a separate document.

## Konfiguration
Um den Router zu konfigurieren werden folgende XML-Conf-Files mittels Restconf PUT-Operation geladen.
- OSPF Konfiguration
- BGP Konfiguration


## Device Config
interface Loopback1
    description The first loopback
    ip address 9.9.9.9 255.255.255.255

interface Loopback2
    description The second Loopback
    ip address 192.168.9.1 255.255.255.0

router ospf 1
    router-id 9.9.9.9 
    network 9.9.9.9 0.0.0.0 area 0
    network 10.3.255.0 0.0.0.255 area 0
    
router bgp 9
    bgp log-neighbor-changes
    network 192.168.9.0
    neighbor 20.20.20.20 remote-as 20
    neighbor 20.20.20.20 ebgp-multihop 2
    neighbor 20.20.20.20 update-source Loopback1

## Device Infos
Die Device Informationen werden in device_infos.yaml festgelegt.

## Usage
Start the program:
`python restconf.py`