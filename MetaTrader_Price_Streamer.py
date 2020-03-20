#needs to use metatrader5 for chart data and datetime for the current time
from datetime import datetime
import MetaTrader5 as mt5
 

# Initializing MT5 connection 
if not mt5.initialize():
    print("initialize() failed")
    mt5.shutdown()

print(mt5.terminal_info())
print(mt5.version())

gbpusd_ticks = mt5.copy_ticks_from("GBPUSD", datetime.now(), 1, mt5.COPY_TICKS_ALL)

now = datetime.now()

print('gbpusd_ticks(', len(gbpusd_ticks), ')')
for val in gbpusd_ticks[:5000]: print(val)

start = input("Would you now like to stream the price of GBPUSD? (y/n): ")
if start == "y":
    count = 0
    while (count < 1):   
      print(gbpusd_ticks, now)
      
