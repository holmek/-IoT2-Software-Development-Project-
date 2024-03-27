# IoT2-Software-Development-Project 

Projektwr fokuserer på at integrere Azure med Flask-frameworket - Projektet omfatter forskellige komponenter, herunder Espressif og en Raspberry Pi-baseret gateway.

**Kommunikationsmetoder:**
- **MQTT -> Azure:**
    Data fra gatewayen sendes til Azure ved hjælp af MQTT.
- **LoRa -> Hub:**
    Espressif-sensorerne bruger LoRa til at sende data til gatewayen.

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

![Projekt Billede](res/project-picture.png)
