import usb.core
import usb.util


# Scan for all USB devices
def find_usb_devices():
    # Find all devices
    devices = usb.core.find(find_all=True)
    return devices


# Display information about each device
def display_device_info(devices):
    for i, dev in enumerate(devices):
        try:
            print(f"Device {i}:")
            print(f"  Device Address: {dev.address}")
            print(f"  Device Bus: {dev.bus}")
            print(f"  idVendor: {hex(dev.idVendor)}")
            print(f"  idProduct: {hex(dev.idProduct)}")
            manufacturer = (
                usb.util.get_string(dev, dev.iManufacturer)
                if dev.iManufacturer
                else "Unknown"
            )
            product = (
                usb.util.get_string(dev, dev.iProduct) if dev.iProduct else "Unknown"
            )
            try:
                serial_number = usb.util.get_string(dev, dev.iSerialNumber)
            except usb.core.USBError:
                serial_number = "Unknown"
            print(f"  Manufacturer: {manufacturer}")
            print(f"  Product: {product}")
            print(f"  Serial Number: {serial_number}")
            print(f"  Device Class: {dev.bDeviceClass}")
            print(f"  Device SubClass: {dev.bDeviceSubClass}")
            print(f"  Device Protocol: {dev.bDeviceProtocol}")
            print(f"  Max Packet Size: {dev.bMaxPacketSize0}")
            print(f"  Num Configurations: {dev.bNumConfigurations}")
            for cfg in dev:
                print(f"    Configuration Value: {cfg.bConfigurationValue}")
                for intf in cfg:
                    print(
                        f"      Interface Number: {intf.bInterfaceNumber}, Alternate Setting: {intf.bAlternateSetting}"
                    )
                    for ep in intf:
                        print(f"        Endpoint Address: {ep.bEndpointAddress}")
        except usb.core.USBError as e:
            print(f"  Could not retrieve all information for device {i}: {e}")


# Find and display USB devices
devices = find_usb_devices()
if not devices:
    print("No USB devices found")
else:
    display_device_info(devices)
