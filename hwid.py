from wmi import WMI  
a = WMI().Win32_ComputerSystemProduct()[0].UUID
print(a)