import machine
import utime


# 温度センサが接続されている、
# 4つ目の ADC(アナログデジタルコンバータ) を取得します
sensor_temp = machine.ADC(4)

# ADCの最大電圧3.3Vを16bit(65535)で割って、
# 16bitの 1 目盛りのあたりの電圧(変換係数)を計算します( 約 0.00005V)
conversion_factor = 3.3 / (65535)

led = machine.Pin(25, machine.Pin.OUT)
led.value(True)
utime.sleep(5)

while True:

    # センサから取得した値(0~65535) を電圧に変換します。
    reading = sensor_temp.read_u16() * conversion_factor
   
    # 温度を計算します。センサは27度を基準にしているため、
    # 温度センサの数値を27度から引いて計算します。
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)

    for i in range(int(temperature % 10)):
        led.value(1)
        utime.sleep(0.5)
        led.value(0)
        utime.sleep(0.5)

    led.value(0)
    utime.sleep(2)
    

