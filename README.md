# Automatic_Fish_Feeder
This is a project on creating an automatic fish feeder that will disperse fish food into a tank once every 12 hours. 

Components:
- ESP32-C3 Supermini, ([See Notes](https://github.com/bcollins131004/ESP32-C3-SuperMini_Notes/blob/main))
- TX DC Motor with Plastic Gearbox

![](https://github.com/bcollins131004/Automatic_Fish_Feeder/blob/main/TT_DC_Motor.jpg)
- IRFZ44N Mosfet
- 1x 220Ω Resistor
- 1x 10KΩ Resistor
- 5x 100μF Capacitors (Just becuase I didnt have a 470μF I had to wire them in parralell)

The ESP32 has to be [flashed](https://github.com/bcollins131004/ESP32-C3-SuperMini_Notes/blob/main/README.md) originally to be able to write code to it. The code I added is [here]((https://github.com/bcollins131004/Automatic_Fish_Feeder/blob/main/Fish_Feeder_Code.py)).
The general wiring idea is the motor is powered from the 5v output from the ESP32 and the negative is controlled by the mosfet with the GPIO0 pin on the ESP32 being used. I chose this one as it allowed me to connect the mosfet from that pin to the GND with ease. Between the motor pins and the mosfet/5v were the 5 Capacitors in series. I am not sure if these were necessary in the end, but they were needed when I was troubleshooting the circuit so they were left in. 
I also designed a [housing](https://github.com/bcollins131004/Automatic_Fish_Feeder/blob/main/Fish_Feeder.stl) and 3d printed it to hold the device and tub.
### Issues
I was encountering issues with the circuit where I was running it off an external power supply (an old phone charger) which provided 5v and 600mA which was just borderline enough to run the motor, but anytime I tried to run the system, it would brownout, and restart the circuit, meaning the motor never moved. I added the capacitors then to try and mitigate some of the current loss but it was no use. I then switched power supplies to try and run directly from the ESP32 USB-C port and that seemed to be working perfectly so I continued from there.
