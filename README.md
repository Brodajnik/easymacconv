easymacconv - перша версія
Версії після першої переробки - в архівах macc_x_x_x
---
easymacconv
Конвертер мак-адрес.

Прога бере мак в довільному форматі та конвертує в інші.

Підтримує формати:

{B0,05,94,F7,D1,61}

B00594F7D161

0xB00594F7D161

B005.94F7.D161

B005-94F7-D161

B0:05:94:F7:D1:61

B0-05-94-F7-D1-61

Історія змін:
macc_0_0_1 - відключено прохання 'Введіть мак' для того, щоб прискорити роботу.
macc_0_0_2 - додано визначення вендору за допомогою mac_vendor_lookup; для коректної роботи потребує цю бібліотеку.
  Встановлення mac_vendor_lookup: pip install mac-vendor-lookup
macc_0_0_3 - виправлено проблему з валідацією формату B0:05:94:F7:D1:61
macc_0_0_3 - програма реалізована через безкінений цикл, внаслідок чого після спрацювання одразу вибиває поле для вводу нового маку
