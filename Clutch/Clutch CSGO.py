import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Tạo DataFrame
df = pd.read_csv("CSGO Player 2.csv")

#Bỏ%
df['1v1 Success'] = df['1v1 Success'].str.rstrip('%').astype('float') / 100.0
df.dtypes

EA = df['Clutch Attempts 1v1']
ES = df['1v1 Success']
Name = df['Players']

#Chọn màu
colors = ['lightcoral', 'darkorange', 'olive', 'teal', 'violet',
         'skyblue','red','orange','yellow','blue','green','purple']
#Màu text
plt.rcParams['text.color'] = "Black"

#Ảnh backgorund
img = plt.imread("Background2.png")
fig, ax = plt.subplots()
ax.imshow(img,zorder=0, extent=[0, 190, 0, 0.8],aspect='auto', alpha = 0.3)

#Biểu đồ
ax.scatter(EA, ES, c=colors)

#Label
[plt.text(x=row['Clutch Attempts 1v1'], y=row['1v1 Success'], s=row['Players'],weight='bold') for k,row in df.iterrows()]
ax.set_xlabel('Clutch Attempts 1v1')
ax.set_ylabel('1v1 Success')
ax.set_title('Tin đứa nào khi cần clutch 1v1')
plt.text(157,0.62,'Avg Clutch Attempts 1v1', size=10, color='Black')
plt.text(76,0.1,'Avg 1v1 Success', size=10, color='Black',rotation=270)

#Đường trung bình
ax.axvline(EA.mean(), color='gray', ls='--')
ax.axhline(ES.mean(), color='gray', ls='--')

##Comment
ax.text(5, 0.75, "Quái vật đang ngủ", size=10,
        bbox=dict(boxstyle="round,pad=0.3"))
ax.text(162, 0.1, "Baiter chúa", size=10,
        bbox=dict(boxstyle="round,pad=0.3"))
ax.text(5, 0.1, "Đừng tin đám này", size=10,
        bbox=dict(boxstyle="round,pad=0.3"))
ax.text(162, 0.75, "Những đứa đáng tin", size=10,
        bbox=dict(boxstyle="round,pad=0.3"))

#Visualization
plt.tight_layout()
plt.show()