from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import MetaTrader5 as mt5
 

# Initializing MT5 connection 
if not mt5.initialize():
    print("initialize() failed")
    mt5.shutdown()

print(mt5.terminal_info())
print(mt5.version())

gbpusd_ticks = mt5.copy_ticks_from("GBPUSD", datetime.now(), 5000, mt5.COPY_TICKS_ALL)

print('gbpusd_ticks(', len(gbpusd_ticks), ')')
for val in gbpusd_ticks[:5000]: print(val)

