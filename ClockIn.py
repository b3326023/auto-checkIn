from AutoClockIn import AutoClockIn
import time
auto = AutoClockIn()
time.sleep(1)
auto.keyIn()
time.sleep(1)
auto.signIn()
time.sleep(1)
auto.close()
time.sleep(1)
exit()