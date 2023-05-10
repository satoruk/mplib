from machine import Pin

from HX711 import HX711

def main():
  pin_OUT = Pin(15, Pin.IN, pull=Pin.PULL_DOWN)
  pin_SCK = Pin(14, Pin.OUT)

  hx711 = HX711(pin_SCK, pin_OUT)

  print("tare")
  hx711.tare()
  print("tare ... done")
  while True:
    value = hx711.read()
    # value = hx711.get_value()

    print(f"value: {value}")

if __name__ == '__main__':
  print("Starting")

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    print("Goodbye!")
        
