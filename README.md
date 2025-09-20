# Autonomes Parken mit LEGO MINDSTORMS EV3  

## 📖 Projektbeschreibung  
Dieses Projekt wurde im Rahmen des TEKO-Moduls **Robotik** umgesetzt. Ziel war es, ein EV3-Fahrzeug zu entwickeln, das einer Linie folgt, an einer Markierung stoppt und mit Hilfe von Sensoren autonom einen Parkplatz erkennt und einparkt.  

Das Fahrzeug nutzt einen **Farbsensor**, um Linien und Markierungen am Boden zu erkennen, sowie einen **Ultraschallsensor**, der über einen zusätzlichen Motor bewegt wird, um die Umgebung nach freien Parkplätzen abzusuchen. Zwei grosse Motoren sorgen für den Antrieb des Fahrzeugs.  

---

## ⚙️ Funktionen  
- Linienverfolgung mit PID-Regler (Farbsensor)  
- Stoppen an roten Markierungen  
- Drehen des Ultraschallsensors nach links und rechts (180°)  
- Erkennen von freien oder belegten Parkplätzen  
- Autonomes Einparken auf der rechten oder linken Seite  
- Sicherheitsfunktion: Fahrzeug bleibt stehen, wenn beide Parkplätze belegt sind  

---

## 🔩 Verwendete Komponenten  
- EV3-Stein (Microcontroller)  
- 2× Grosse Motoren (Antrieb)  
- 1× Mittlerer Motor (Drehung Ultraschallsensor)  
- 1× Farbsensor  
- 1× Ultraschallsensor  

---

## 💻 Programmierung  
Das Programm wurde in **MicroPython (Pybricks)** geschrieben.  

Wichtige Punkte:  
- PID-Regler zur Linienverfolgung  
- Nutzung von Distanzmessungen in Zentimetern  
- Steuerung über Motorpositionen und Sensordaten  

👉 Der vollständige Quellcode befindet sich in der Datei **`main.py`**.  

---

## 🧪 Tests  
- Mehrere Testläufe bestätigt: Fahrzeug folgt zuverlässig der Linie und parkt korrekt ein.  
- Sowohl Parken rechts als auch links erfolgreich getestet.  
- Bekannte Einschränkung: Fahrzeug bleibt stehen, wenn beide Parkplätze belegt sind.  
- Mögliche Erweiterung: Nach definierter Zeit erneut prüfen oder zur nächsten Station weiterfahren.  

---

## 🚀 Installation & Nutzung  
1. Pybricks auf den EV3 installieren  
2. Repository klonen oder `main.py` herunterladen  
3. Programm auf den EV3 hochladen  
4. Fahrzeug auf die vorbereitete Teststrecke stellen (gelbe Linie mit roten Markierungen)  
5. Programm starten – das Fahrzeug übernimmt die Steuerung autonom  

---

## 📜 Lizenz  
Dieses Projekt wurde im Rahmen einer Schularbeit erstellt und dient ausschliesslich zu Lern- und Demonstrationszwecken.  
