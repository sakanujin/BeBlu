from bluepy import btle

BLE_ADD = "74:90:50:40:BB:5C"

peri = btle.Peripheral()
peri.connect(BLE_ADD)

for sevice in peri.getServices():
    print(f'Service UUID : {service.uuid}')
