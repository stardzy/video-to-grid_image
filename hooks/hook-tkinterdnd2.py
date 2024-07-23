from PyInstaller.utils.hooks import collect_data_files

# Collect the tkdnd2.8 directory
datas = collect_data_files('tkinterdnd2', includes=['tkdnd2.8/**/*'])
