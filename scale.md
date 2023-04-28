# Scale


## Raspberry Pi Pico Pin layout

|              | Left Name | Hole    | Right Name |                 |
| ------------ | --------- | ------- | ---------- | --------------- |
|              | GP0       | 01 (40) | VBUS       | HX711 VDD(1)    |
|              | GP1       | 02 (39) | VSYS       |                 |
| HX711 GND(6) | GND       | 03 (38) | GND        |                 |
|              | GP2       | 04 (37) | 3V3_EN     |                 |
|              | GP3       | 05 (36) | 3V3(OUT)   | HD44780 VDD(1)  |
|              | GP4       | 06 (35) |            |                 |
|              | GP5       | 07 (34) | GP28       |                 |
|              | GND       | 08 (33) | GND        | HD44780 VSS(2)  |
|              | GP6       | 09 (32) | GP27       |                 |
|              | GP7       | 10 (31) | GP26       |                 |
|              | GP8       | 11 (30) | RUN        |                 |
|              | GP9       | 12 (29) | GP22       |                 |
|              | GND       | 13 (28) | GND        |                 |
|              | GP10      | 14 (27) | GP21       | HD44780 RS(4)   |
|              | GP11      | 15 (26) | GP20       | HD44780 E(6)    |
|              | GP12      | 16 (25) | GP19       | HD44780 DB4(11) |
|              | GP13      | 17 (24) | GP18       | HD44780 DB5(12) |
|              | GND       | 18 (23) | GND        |                 |
| HX711 CLK(3) | GP14      | 19 (22) | GP17       | HD44780 DB6(13) |
| HX711 DAT(2) | GP15      | 20 (21) | GP16       | HD44780 DB7(14) |
|              |           |         |            |                 |
|              |           |         |            | HD44780 Vo(3)   |

## HD44780 Pin layout

| Hole    | Pin | Name | Description                  |
| ------- | --- | ---- | ---------------------------- |
| 05 (36) | 1   | VDD  | Power supply for logic (+5V) |
| 08 (33) | 2   | VSS  | Ground                       |
|         | 3   | V0   | Contrast adjustment          |
| 14 (27) | 4   | RS   | Register select              |
| NONE    | 5   | R/W  | Read/Write                   |
| 15 (26) | 6   | E    | Enable signal                |
| NONE    | 7   | DB0  | Data bus line 0              |
| NONE    | 8   | DB1  | Data bus line 1              |
| NONE    | 9   | DB2  | Data bus line 2              |
| NONE    | 10  | DB3  | Data bus line 3              |
| 16 (25) | 11  | DB4  | Data bus line 4              |
| 17 (24) | 12  | DB5  | Data bus line 5              |
| 19 (22) | 13  | DB6  | Data bus line 6              |
| 20 (21) | 14  | DB7  | Data bus line 7              |

