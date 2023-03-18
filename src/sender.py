import serial
from multiprocessing import Process, Queue

class SerialSender:
    def __init__(self, port, baudrate):
        self.ser = serial.Serial(port, baudrate)
        self.q = Queue()

    def start(self):
        p = Process(target=self.send_data, args=(self.q,))
        p.start()

        while True:
            data = self.q.get()
            self.ser.write(data.encode())

    def send_data(self, q):
        while True:
            data = self.ser.readline().decode().strip()
            if data:
                q.put(data)

if __name__ == '__main__':
    PORT = 'COM6'
    BAUDRATE = 9600
    sender = SerialSender(PORT, BAUDRATE)
    sender.start()
