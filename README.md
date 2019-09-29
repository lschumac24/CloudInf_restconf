# CloudInf Restconf Lab

## Vorgehen
Device_infos.yaml wird als dictionary eingelesen. Damit wir mit jinja2 und dem config_template.xml
die XML Config erstellt. Die XML Config wird dann mittels restconf PUT Operation auf den Router geladen.

##device_infos.yaml
In der Datei device_infos.yaml werden alle Konfigurationsangaben getätigt. Folgende Angaben sind möglich:
*   hostname
*   Restconf-Gigabit-Interface
*   mehrere Loopback-Adressen mithilfe einer Liste
*   OSPF mit mehreren Netzen (Liste) 
*   BGP mit mehreren Neighbours und Netzen (Listen)


## Device Config
* interface GigabitEthernet1
    *   description RESTful API Interface
    *   ip address 10.3.255.109 255.255.255.0

* interface Loopback1
    *   description The first loopback
    *   ip address 9.9.9.9 255.255.255.255

*   interface Loopback2
    *   description The second Loopback
    *   ip address 192.168.9.1 255.255.255.0
    
*   router ospf 1
    *   router-id 9.9.9.9
    *   network 9.9.9.9 0.0.0.0 area 0
    *   network 10.3.255.0 0.0.0.255 area 0
    
*   router bgp 9
    *   bgp log-neighbor-changes
    *   network 192.168.9.0
    *   neighbor 20.20.20.20 remote-as 20
    *   neighbor 20.20.20.20 ebgp-multihop 2
    *   neighbor 20.20.20.20 update-source Loopback1

## Usage
Start the program:
`python restconf.py`