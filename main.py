import os
import tkinter as tk
from tkinter import scrolledtext
from tkinterdnd2 import TkinterDnD, DND_FILES
from settings import show_settings
from video_processing import run

# 默认变量设置
config = {
    'frames_per_row': 1,
    'frames_per_col': 1,
    'start_frame': 0,
    'back_frame': 0,
    'frame_margin': 10,
    'font_scale': 10,
    'font_thickness': 10,
    'number_position': '左上角',
    'picture_location': '.',
    'video_location': '.'
}

def log_message(message):
    text_widget.insert(tk.END, message + "\n")
    text_widget.see(tk.END)

def drop(event):
    video_location.delete(0, tk.END)
    video_location.insert(0, event.data)
    log_message(f"视频文件已加载: {event.data}")

def update_config(new_config):
    global config
    config.update(new_config)

# 创建主窗口
root = TkinterDnD.Tk()
root.title("视频导出网格截图")

# 创建标签和输入框
tk.Label(root, text="请输入视频位置（绝对位置或者和该程序同一文件夹）: ").grid(row=0)
tk.Label(root, text="照片输出位置与程序同一文件夹 ").grid(row=1)
video_location = tk.Entry(root)
video_location.grid(row=0, column=1)

# 创建按钮
tk.Button(root, text="运行", command=lambda: run(config, video_location, text_widget)).grid(row=2, column=1)
tk.Button(root, text="设置", command=lambda: show_settings(root, config, update_config)).grid(row=2, column=0)

# 创建文本框以显示日志信息
text_widget = scrolledtext.ScrolledText(root, width=50, height=10)
text_widget.grid(row=3, column=0, columnspan=2)

# 绑定拖放事件
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

# 运行主循环
root.mainloop()
