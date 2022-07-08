import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Tạo DataFrame
df = pd.read_csv("CSGO Player.csv")

#Bỏ%
df['Entry Attempt'] = df['Entry Attempt'].str.rstrip('%').astype('float') / 100.0
df['Entry Success'] = df['Entry Success'].str.rstrip('%').astype('float') / 100.0
df.dtypes

EA = df['Entry Attempt']
ES = df['Entry Success']
Name = df['Players']

#Chọn màu
colors = ['lightcoral', 'darkorange', 'olive', 'teal', 'violet',
         'skyblue','red','orange','yellow','blue','green','purple']
#Màu text
plt.rcParams['text.color'] = "Black"

#Ảnh background
img = plt.imread("Background.png")
fig, ax = plt.subplots()
ax.imshow(img,zorder=0, extent=[0.05, 0.3, 0.3, 0.7],aspect='auto', alpha = 0.3)

#Biểu đồ
ax.scatter(EA, ES, c=colors)

#Label
[plt.text(x=row['Entry Attempt'], y=row['Entry Success'], s=row['Players'],weight='bold') for k,row in df.iterrows()]
ax.set_xlabel('Entry Attempt/Round')
ax.set_ylabel('Entry Success/Round')
ax.set_title('Ai là King of Entry giữa Hyd và đồng bọn')
plt.text(0.265,0.495,'Avg Entry Attempt', size=10, color='Black')
plt.text(0.204,0.32,'Avg Entry Success', size=10, color='Black',rotation=270)

#Đường trung bình
ax.axvline(EA.mean(), color='gray', ls='--')
ax.axhline(ES.mean(), color='gray', ls='--')

##Comment
ax.text(0.06, 0.65, "Entry hiệu quà nhưng ít khi entry", size=10,
        bbox=dict(boxstyle="round,pad=0.3"))
ax.text(0.06, 0.33, "Entry ít mà đ hiệu quả", size=10,
        bbox=dict(boxstyle="round,pad=0.3"))
ax.text(0.265, 0.33, "Entry nhiều mà đ hiệu quả", size=10,
        bbox=dict(boxstyle="round,pad=0.3"))
ax.text(0.19, 0.65, "Entry lắm mà hiệu quả thì tốt", size=10,
        bbox=dict(boxstyle="round,pad=0.3"))

#Visualization
plt.tight_layout()
plt.show()
