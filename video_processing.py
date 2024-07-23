import os
import cv2
import numpy as np
import tkinter as tk

def run(config, video_location, text_widget):
    # 读取视频
    video_path = video_location.get()
    cap = cv2.VideoCapture(video_path)

    def log_message(message):
        text_widget.insert(tk.END, message + "\n")
        text_widget.see(tk.END)

    # 提取视频文件名，不包括扩展名
    video_filename = os.path.splitext(os.path.basename(video_path))[0]

    # 检查视频是否打开
    if not cap.isOpened():
        log_message("Error opening video file")
        return

    # 获取视频的总帧数
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # 计算间隔，确保平均分配帧
    num_frames_to_capture = config['frames_per_row'] * config['frames_per_col']
    frame_interval = (frame_count - config['back_frame'] - config['start_frame']) // num_frames_to_capture

    # 获取视频帧的宽度和高度
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 设置每个帧之间的间距
    margin = config['frame_margin']

    # 创建空白图像用于存储帧，加上边距
    grid_image = np.zeros((frame_height * config['frames_per_col'] + margin * (config['frames_per_col'] + 1),
                           frame_width * config['frames_per_row'] + margin * (config['frames_per_row'] + 1), 3), dtype=np.uint8)

    # 设置文本参数
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_color = (255, 255, 255)

    # 逐帧读取视频并截取指定帧
    captured_frames = 0
    for i in range(config['start_frame'], frame_count - config['back_frame'], frame_interval):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        if not ret:
            log_message(f"Failed to read frame at position {i}")
            continue

        # 计算当前帧在网格中的位置
        row = captured_frames // config['frames_per_row']
        col = captured_frames % config['frames_per_row']

        # 计算当前帧在大图像中的起始位置
        start_y = row * (frame_height + margin) + margin
        start_x = col * (frame_width + margin) + margin

        # 将当前帧放置到网格中对应的位置
        grid_image[start_y:start_y + frame_height, start_x:start_x + frame_width] = frame

        # 获取文本尺寸
        text_size = cv2.getTextSize(str(captured_frames + 1), font, config['font_scale'], config['font_thickness'])[0]

        # 在帧上添加编号，根据用户选择的位置进行调整
        if config['number_position'] == '左上角':
            text_x = start_x + 15
            text_y = start_y + 15 + text_size[1]
        elif config['number_position'] == '右上角':
            text_x = start_x + frame_width - 15 - text_size[0]
            text_y = start_y + 15 + text_size[1]
        elif config['number_position'] == '左下角':
            text_x = start_x + 15
            text_y = start_y + frame_height - 15
        elif config['number_position'] == '右下角':
            text_x = start_x + frame_width - 15 - text_size[0]
            text_y = start_y + frame_height - 15

        cv2.putText(grid_image, str(captured_frames + 1), (text_x, text_y),
                    font, config['font_scale'], font_color, config['font_thickness'], cv2.LINE_AA)

        captured_frames += 1
        if captured_frames >= num_frames_to_capture:
            break

    # 释放视频对象
    cap.release()

    # 检查生成的网格图像是否有效
    if grid_image.size == 0:
        log_message("Error: Grid image is empty")
    else:
        # 保存结果图像
        output_filename = os.path.join(config['picture_location'], f'{video_filename}_grid_image.png')
        cv2.imwrite(output_filename, grid_image)
        log_message(f"图像已保存为 {output_filename}")
