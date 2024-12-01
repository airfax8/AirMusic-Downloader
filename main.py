import tkinter as tk
import sys
import os
from tkinter import ttk
from yt_helper import search_and_display_info, download_audio
from update_checker import check_for_updates  # Güncelleme kontrolü

# Güncelleme kontrolü
check_for_updates()

def on_search_click(entry, info_text, download_button):
    url_or_query = entry.get()
    if url_or_query:
        search_and_display_info(url_or_query, info_text, download_button)

def resource_path(relative_path):
    """PyInstaller'ın oluşturduğu EXE'de dosya yollarını düzeltir."""
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Ana pencere
root = tk.Tk()
root.title("AirMusic Downloader")
root.geometry("600x400")
root.config(bg="#282C34")
root.iconbitmap(resource_path("airmic1.ico"))

# Başlık
title_label = tk.Label(root, text="AirMusic Downloader", font=("Arial", 20, "bold"), fg="white", bg="#282C34")
title_label.pack(pady=10)

# Giriş kutusu
entry = tk.Entry(root, font=("Arial", 14), width=40)
entry.pack(pady=10)

# Ara butonu
search_button = tk.Button(
    root,
    text="Ara",
    font=("Arial", 12),
    bg="#007BFF",
    fg="white",
    width=15,
    height=2,
    relief="raised",
    command=lambda: on_search_click(entry, info_text, download_button)
)
search_button.pack(pady=10)

# Bilgi metni
info_text = tk.Text(root, height=8, width=70, state=tk.DISABLED, bg="#1E1E1E", fg="white", font=("Arial", 10))
info_text.pack(pady=10)

# İndir butonu
download_button = tk.Button(
    root,
    text="İndir",
    font=("Arial", 12),
    bg="#28A745",
    fg="white",
    width=15,
    height=2,
    relief="raised",
    state=tk.DISABLED,
    command=lambda: download_audio(entry.get())
)
download_button.pack(pady=10)

# İlerleme çubuğu
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100, length=400)
progress_bar.pack(pady=10)

# Ana döngü
root.mainloop()
