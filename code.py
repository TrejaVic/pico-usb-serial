import supervisor
import digitalio
import board

led = digitalio.DigitalInOut(board.LED)
led.switch_to_output()  # Set LED as output

variables = {}  # Dictionary to store registered variables

while True:
    if supervisor.runtime.serial_bytes_available:
        value = input().strip()
        print(f"Received: {value}\r")
        # -- OPEN BUILTIN LED --
        if value == "open":
            led.value = True
            print("success")
        # -- CLOSE BUILTIN LED --
        elif value == "close":
            led.value = False
            print("success")
        # -- PROCESS A SOFT REBOOT --
        elif value == "reboot":
            supervisor.reload()

