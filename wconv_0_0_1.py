#імпортуємо модуль import PySimpleGUI as sg для роботи графіки.
#Встановлення:
#apt install python3-pip python3-tk
#pip3 install PySimpleGUI
#Виникли трабли з залежностями, рішення:
#apt update
#apt --fix-broken install
#Ще потрібна mac_vendor_lookup для коректної роботи визначення вендора.
#Встановлення mac_vendor_lookup: pip install mac-vendor-lookup
#Прога бере мак в довільному форматі та конвертує в інші, + визначає вендор.
#Підтримує формати:
#{B0,05,94,F7,D1,61}
#B00594F7D161
#0xB00594F7D161
#B005.94F7.D161
#B005-94F7-D161
#B0:05:94:F7:D1:61
#B0-05-94-F7-D1-61
import PySimpleGUI as sg
layout = [
    [sg.Text('Введіть mac'), sg.InputText(key='-IN-'), sg.Submit('Конвертувати'), sg.Cancel('Очистити')
     ],
    [sg.Output(size=(88, 20), key='-OUT-')],
]
window = sg.Window('Конвертер mac-адрес', layout)
while True:                             # The Event Loop
    event, values = window.read()
    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break
    if event == 'Конвертувати':
        # print ('Хелло ворлд') - вивід для дебагу
        a = values['-IN-']
        # print (a) - вивід для дебагу
        val = 0 #змінна для перевірки
        dopusk = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', '{', '}', 'x', '-', ',', '.', ':', 'A', 'B', 'C', 'D', 'E', 'F']
        zbig = 0
        if len(a) != 19 and len(a) != 12 and len(a) != 14 and len(a) != 17:
            val = 1
        else:
            for m in a:
                for n in dopusk:
                    if m == n:
                        zbig = zbig + 1
            if zbig != len(a):
                val = 1
        if val == 1:
            print ('некоректно введені дані')
        elif val == 0:
            #перевірка формату
            #1 - {B0,05,94,F7,D1,61}
            #2 - B00594F7D161
            #3 - 0xB00594F7D161
            #4 - B005.94F7.D161
            #5 - B005-94F7-D161
            #6 - B0:05:94:F7:D1:61
            #7 - B0-05-94-F7-D1-61
            ap = 0 #сюди будемо записувати формат
            if len(a) == 19: #формат {B0,05,94,F7,D1,61}
                ap = 1
            elif len(a) == 12: #формат B00594F7D161
                ap = 2
            elif len(a) == 14: #формати B005.94F7.D161 0xB00594F7D161 B005-94F7-D161
                if a[0] == '0' and a[1] ==  'x': #формат 0xB00594F7D161
                    ap = 3
                elif a[4] == '.' and a[9] == '.': #формат B005.94F7.D161
                    ap = 4
                elif a[4] == '-' and a[9] == '-': #формат B005-94F7-D161
                    ap = 5
            elif len(a) == 17: #формати B0-05-94-F7-D1-61 B0:05:94:F7:D1:61
                if a[2] == ':' and a[5] ==  ':' and a[8] ==  ':' and a[11] ==  ':' and a[14] ==  ':': #формат B0:05:94:F7:D1:61
                    ap = 6
                elif a[2] == '-' and a[5] ==  '-' and a[8] ==  '-' and a[11] ==  '-' and a[14] ==  '-': #формат B0-05-94-F7-D1-61
                    ap = 7
            #задаємо змінні для виводу
            mac_1 = '' #формат {B0,05,94,F7,D1,61}
            mac_2 = '' #формат B00594F7D161
            mac_3 = '' #формат 0xB00594F7D161
            mac_4 = '' #B005.94F7.D161
            mac_5 = '' #B005-94F7-D161
            mac_6 = '' #B0:05:94:F7:D1:61
            mac_7 = '' #B0-05-94-F7-D1-61
            mac = '' #формат B00594F7D161; дубль для покращення розуміння коду
            #переводимо формат в B00594F7D161
            if ap != 2: #перевіряємо, чи зараз формат не B00594F7D161
                if ap == 7:
                    for y in a:
                        if y!='-':
                            mac=mac+y
                elif ap == 6:
                    for y in a:
                        if y!=':':
                            mac=mac+y
                elif ap == 5:
                    for y in a:
                        if y!='-':
                            mac=mac+y
                elif ap == 4:
                    for y in a:
                        if y!='.':
                            mac=mac+y
                elif ap == 3:
                    mac=mac + a[2:13]
                elif ap == 1:
                    for y in a:
                        if y!=',' and y!='{' and y != '}':
                            mac=mac+y
            elif ap == 2:
                mac=a
            mac_2 = mac #готові до виводу одного з форматів
            #Розбиваємо мак на фрагменти по 2 елементи
            #Вводимо допоміжні змінні для розбивки маку на фрагменти по 2 елементи
            dop_1 = ''
            dop_2 = ''
            dop_3 = ''
            dop_4 = ''
            dop_5 = ''
            dop_6 = ''
            dop_i = 0
            #Розбиваємо мак на допоміжні фрагменти:
            for x in mac:
                dop_i = dop_i + 1
                if dop_i < 3:
                    dop_1 = dop_1 + x
                elif dop_i >= 3 and dop_i < 5:
                   dop_2 = dop_2 + x
                elif dop_i >= 5 and dop_i < 7:
                   dop_3 = dop_3 + x
                elif dop_i >= 7 and dop_i < 9:
                   dop_4 = dop_4 + x
                elif dop_i >= 9 and dop_i < 11:
                   dop_5 = dop_5 + x
                else:
                    dop_6 = dop_6 + x
            #знаходимо формат {B0,05,94,F7,D1,61} з розбитих елементів
            mac_1 = '{'+dop_1+'.'+dop_2+'.'+dop_3+'.'+dop_4+'.'+dop_5+'.'+dop_6+'}'
            #знаходимо формат  0xB00594F7D161 з простого формату
            mac_3 = '0x'+mac
            #знаходимо формат  B005.94F7.D161 з розбитих елементів
            mac_4 = dop_1+dop_2+'.'+dop_3+dop_4+'.'+dop_5+dop_6
            #знаходимо формат  B005-94F7-D161 з розбитих елементів
            mac_5 = dop_1+dop_2+'-'+dop_3+dop_4+'-'+dop_5+dop_6
            #знаходимо формат  B0:05:94:F7:D1:61 з розбитих елементів
            mac_6 = dop_1+':'+dop_2+':'+dop_3+':'+dop_4+':'+dop_5+':'+dop_6
            #знаходимо формат  B0-05-94-F7-D1-61 з розбитих елементів
            mac_7 = dop_1+'-'+dop_2+'-'+dop_3+'-'+dop_4+'-'+dop_5+'-'+dop_6
            #виводимо результати
            vyv = [mac_1, mac_2, mac_3, mac_4, mac_5, mac_6, mac_7]
            for y in vyv:
                print (y)
            #вендор
            from mac_vendor_lookup import MacLookup
            print('Вендор: ' + MacLookup().lookup(mac_2))
    if event == 'Очистити':
        window['-OUT-'].update('')

