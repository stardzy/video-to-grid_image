import tkinter as tk

def show_settings(root, config, update_config):
    def assign():
        new_config = {
            'frames_per_row': int(entry_frames_row.get()),
            'frames_per_col': int(entry_frames_col.get()),
            'start_frame': int(entry_start_frame.get()),
            'back_frame': int(entry_back_frame.get()),
            'frame_margin': int(entry_frame_margin.get()),
            'font_scale': int(entry_font_scale.get()),
            'font_thickness': int(entry_font_thickness.get()),
            'number_position': position_var.get()
        }
        update_config(new_config)
        settings_window.destroy()

    settings_window = tk.Toplevel(root)
    settings_window.title("设置")

    tk.Label(settings_window, text="请输入行数（默认为1）: ").grid(row=0)
    entry_frames_row = tk.Entry(settings_window)
    entry_frames_row.insert(0, str(config['frames_per_row']))
    entry_frames_row.grid(row=0, column=1)

    tk.Label(settings_window, text="请输入列数（默认为1）: ").grid(row=1)
    entry_frames_col = tk.Entry(settings_window)
    entry_frames_col.insert(0, str(config['frames_per_col']))
    entry_frames_col.grid(row=1, column=1)

    tk.Label(settings_window, text="请输入前截去帧（默认为0）: ").grid(row=2)
    entry_start_frame = tk.Entry(settings_window)
    entry_start_frame.insert(0, str(config['start_frame']))
    entry_start_frame.grid(row=2, column=1)

    tk.Label(settings_window, text="请输入后截去帧（默认为0）: ").grid(row=3)
    entry_back_frame = tk.Entry(settings_window)
    entry_back_frame.insert(0, str(config['back_frame']))
    entry_back_frame.grid(row=3, column=1)

    tk.Label(settings_window, text="请输入图片间距（默认为10）: ").grid(row=4)
    entry_frame_margin = tk.Entry(settings_window)
    entry_frame_margin.insert(0, str(config['frame_margin']))
    entry_frame_margin.grid(row=4, column=1)

    tk.Label(settings_window, text="请输入序号大小（默认为10）: ").grid(row=5)
    entry_font_scale = tk.Entry(settings_window)
    entry_font_scale.insert(0, str(config['font_scale']))
    entry_font_scale.grid(row=5, column=1)

    tk.Label(settings_window, text="请输入序号厚度（默认为10）: ").grid(row=6)
    entry_font_thickness = tk.Entry(settings_window)
    entry_font_thickness.insert(0, str(config['font_thickness']))
    entry_font_thickness.grid(row=6, column=1)

    tk.Label(settings_window, text="请选择序号位置（默认为左上角）: ").grid(row=7)
    position_var = tk.StringVar(value=config['number_position'])
    position_menu = tk.OptionMenu(settings_window, position_var, '左上角', '右上角', '左下角', '右下角')
    position_menu.grid(row=7, column=1)

    tk.Button(settings_window, text="确定", command=assign).grid(row=8, column=1)
    tk.Button(settings_window, text="关闭", command=settings_window.destroy).grid(row=8, column=2)
