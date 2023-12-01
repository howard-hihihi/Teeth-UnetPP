import cv2
import numpy as np

# 創建一個範例影像數據
image_data = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

# 設定保存的文件路徑
file_path = 'output_image.jpg'

# 使用 cv2.imwrite() 保存影像
cv2.imwrite(file_path, image_data)