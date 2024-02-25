import time
import serial

# Open the serial port with appropriate parameters
# (adjust COM port based on your system)
ser = serial.Serial('COM3', 115200, timeout=0.25)  # Adjust timeout as needed

while True:
    command2 = input("Enter command: ")
    command = b'' + command2.encode() + b'\r\n'

    print(f"Sending Command: [{command}]")
    ser.write(command)  # Write the command string

    # Read the response with timeout handling and buffer clearing
    reply = b''
    start_time = time.time()  # Track start time for timeout
    while time.time() - start_time < ser.timeout:
        try:
            a = ser.read(1)  # Read one byte at a time
            if not a:  # Check for timeout or no data
                break
            reply += a
        except serial.SerialTimeoutException:
            print("Timeout while reading response")
            break

    # Print the received response
    print(f"Reply was: [{reply}]")
    print(" ")
    print("Decoded Version: ")
    print(" ")
    print(reply.decode('utf-8'))

# Close the serial port
ser.close()
