# IoT2-Software-Development-Project 
## Beskrivelse

Dette projekt fokuserer på at integrere Azure-tjenester med Flask-frameworket til IoT-applikationer. Projektet omfatter forskellige komponenter, herunder Espressif og en Raspberry Pi-baseret gateway.

**Azure Flask:**
Azure Flask bruges til at vise data fra Espressif-sensorerne. Flask håndterer webserveren, der præsenterer sensordataene for brugerne.

**Kommunikationsmetoder:**
- **MQTT fra Hub til Azure:**
    Data fra gatewayen sendes til Azure ved hjælp af MQTT-protokollen.
- **LoRa fra Espressif til Hub:**
    Espressif-sensorerne bruger LoRa-teknologi til at sende data til gatewayen.

## Mapper

Projektet indeholder følgende mapper:

1. **Azure-Flask:**
   Denne mappe indeholder koden til Flask-applikationen, der viser data fra Espressif-sensorerne i Azure-miljøet.

2. **Espressif-Sensor:**
   Denne mappe indeholder koden til Espressif ESP8266/ESP32-baserede sensorer. Sensorerne opsamler data og sender dem til gatewayen til yderligere behandling.

3. **RaspHub-Gateway:**
   I denne mappe findes koden til Raspberry Pi-baserede gatewayen. Gatewayen modtager data fra sensorerne, behandler dem og sender dem videre til Azure-tjenesterne til lagring og analyse.

## Licens

Dette projekt er licenseret under [MIT licensen](LICENSE). Se LICENSE-filen for flere detaljer.
