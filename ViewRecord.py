from AutoClockIn import AutoClockIn
import time

auto = AutoClockIn()
time.sleep(1)
auto.keyIn()
time.sleep(1)
auto.viewRecord()
# auto.close()