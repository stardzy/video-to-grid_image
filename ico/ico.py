from PIL import Image

# 打开 PNG 文件
png_image_path = 'ico.png'  # 替换为实际路径
img = Image.open(png_image_path)

# 保存为 ICO 文件
ico_image_path = 'output_icon.ico'
img.save(ico_image_path, format='ICO', sizes=[(256, 256)])
