# CloudInf Restconf Lab 02

## Vorgehen
Device_infos.yaml wird als dictionary eingelesen. Damit wir mit jinja2 und dem config_template.xml
die XML Config erstellt. Die XML Config wird dann mittels restconf PUT Operation auf den Router geladen.


##device_infos.yaml
In der Datei device_infos.yaml werden alle Konfigurationsangaben getätigt. 
Der Benutzer kann diese Datei je nach Wunsch verändern.
Folgende Konfigurationsänderungen sind möglich:
*   hostname ändern
*   Restconf-Gigabit-Interface definieren
*   mehrere Loopback-Adressen erstellen
*   OSPF mit mehreren Netzen erstellen
*   BGP mit mehreren Neighbours und beliebig vielen Netzen erstellen


##config_template.xml
Dies ist das Template, aus dem das xml generiert wird, welches zum Router geschickt wird. 
Es wurde Jinja2 als Template-Engine genommen, um Logic und Variablen im xml zu verwenden.
Für das Erstellen von mehreren Loopback-Adressen, Netzwerke und Neighbours für BGP und OSPF wurden mithilfe von Listen realisiert.


## Device Config (Cisco CLI Befehle)
Nachfolgend sind die Cisco CLI Befehle aufgeführt, welche für das Lösen dieser Aufgabe verwendet wurden.

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

##restconf_helpers.py
In dieser Datei ist die PUT-Implementation für RESTCONF definiert, welche für die Konfigänderung des Routers benötigt wird.

## Benutzung
Zum Starten des Programms kann nachfolgende Zeile eingegeben werden:
`python restconf.py`