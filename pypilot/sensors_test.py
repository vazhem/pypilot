import time

from client import pypilotClient
from values import *


def main():
    print('pypilot Servo')
    from server import pypilotServer
    server = pypilotServer()
    client = pypilotClient(server)

    from sensors import Sensors # for rudder feedback
    sensors = Sensors(client)

    period = .1
    start = lastt = time.monotonic()
    while True:

        sensors.poll()

        dt = period - time.monotonic() + lastt
        if dt > 0 and dt < period:
            time.sleep(dt)
            lastt += period
        else:
            lastt = time.monotonic()


if __name__ == '__main__':
    main()
