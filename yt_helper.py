import yt_dlp
import os

def search_and_display_info(query, info_text, download_button):
    try:
        # YouTube bilgilerini al
        with yt_dlp.YoutubeDL({"quiet": True}) as ydl:
            if not query.startswith("http"):
                query = f"ytsearch:{query}"
            info = ydl.extract_info(query, download=False)['entries'][0]
            title = info['title']
            uploader = info.get('uploader', 'Bilinmiyor')
            duration = info.get('duration', 0)

        # Bilgileri göster
        info_text.config(state="normal")
        info_text.delete(1.0, "end")
        info_text.insert("end", f"Başlık: {title}\n")
        info_text.insert("end", f"Sanatçı: {uploader}\n")
        info_text.insert("end", f"Süre: {duration // 60} dakika {duration % 60} saniye\n")
        info_text.config(state="disabled")

        # İndir butonunu etkinleştir
        download_button.config(state="normal", command=lambda: download_audio(info['webpage_url']))
    except Exception as e:
        info_text.config(state="normal")
        info_text.delete(1.0, "end")
        info_text.insert("end", f"Arama sırasında hata oluştu: {e}\n")
        info_text.config(state="disabled")

def download_audio(query_or_url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join("downloads", "%(uploader)s - %(title)s.%(ext)s"),
            'progress_hooks': [progress_hook],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            if not query_or_url.startswith("http"):
                query_or_url = f"ytsearch:{query_or_url}"
            ydl.download([query_or_url])
    except Exception as e:
        print(f"İndirme sırasında hata oluştu: {e}")

def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '0%').strip('%')
        print(f"İlerleme: {percent}%")
    elif d['status'] == 'finished':
        print("İndirme tamamlandı!")
