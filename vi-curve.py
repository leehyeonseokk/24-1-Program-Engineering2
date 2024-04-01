import xml.etree.ElementTree as elemTree
import matplotlib.pyplot as plt
import numpy as np
tree = elemTree.parse('./HY202103_D07_(0,0)_LION1_DCM_LMZC.xml')
root = tree.getroot()


iv_measurement = root.find('.//IVMeasurement')

# Voltage와 Current 요소의 값을 가져옵니다.
voltage_text = iv_measurement.find('Voltage').text
current_text = iv_measurement.find('Current').text

voltages = [float(v) for v in voltage_text.split(',')]

currents = [abs(float(c)) for c in current_text.split(',')]  # 전류 값을 절댓값으로 변환합니다.

print("Voltages:", voltages)
print("Currents:", currents)

plt.plot(voltages, currents)
  # x축을 로그 스케일로 설정
plt.yscale('log')  # y축을 로그 스케일로 설정
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.title('IV Curve (Log Scale)')
plt.grid(True)
plt.show()