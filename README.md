# IoT2-Software-Development-Project 

Projektwr fokuserer på at integrere Azure med Flask-frameworket - Projektet omfatter forskellige komponenter, herunder Espressif og en Raspberry Pi-baseret gateway.

**Kommunikationsmetoder:**
- **MQTT fra Hub til Azure:**
    Data fra gatewayen sendes til Azure ved hjælp af MQTT-protokollen.
- **LoRa fra Espressif til Hub:**
    Espressif-sensorerne bruger LoRa-teknologi til at sende data til gatewayen.

## Mapper

Projektet indeholder følgende mapper:

1. **Azure-Flask:**
   Denne mappe indeholder koden til Flask-applikationen, der viser data fra Espressif-sensorerne i Azure.

2. **Espressif-Sensor:**
   Denne mappe indeholder koden til Espressif. Sensorerne opsamler data og sender dem til gatewayen.

3. **RaspHub-Gateway:**
   I denne mappe findes koden til Raspberry Pi-baserede gatewayen. Gatewayen modtager data fra sensorerne og sender dem videre til Azure.

## Licens

Dette projekt er licenseret under [MIT licensen](LICENSE). Se LICENSE-filen for flere detaljer.

(project-picture.png)
