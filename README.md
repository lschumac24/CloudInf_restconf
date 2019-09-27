# CloudInf Restconf Lab

## Vorgehen
Device_infos.yaml wird als dictionary eingelesen. Damit wir mit jinja2 und dem config_template.xml
das XML Config File erstellt. Dieses wird dann mittels restconf PUT Operation auf den Router geladen.


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

## Usage
Start the program:
`python restconf.py`