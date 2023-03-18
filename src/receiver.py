import serial

class SerialReceiver:
    def __init__(self, port, baudrate):
        self.ser = serial.Serial(port, baudrate)

    def start(self):
        while True:
            data = self.ser.readline().decode().strip()

            if data:
                self.send_response(data)

    def send_response(self, data):
        response = f'Received: {data}\n'
        self.ser.write(response.encode())

if __name__ == '__main__':
    PORT = 'COM3'
    BAUDRATE = 9600
    receiver = SerialReceiver(PORT, BAUDRATE)
    receiver.start()
