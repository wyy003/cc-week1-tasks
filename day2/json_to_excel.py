import json
import openpyxl

with open('sample.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

wb = openpyxl.Workbook()
ws = wb.active

headers = list(data[0].keys())
ws.append(headers)

for item in data:
    ws.append(list(item.values()))

wb.save('sample.xlsx')
print("已生成 sample.xlsx")
