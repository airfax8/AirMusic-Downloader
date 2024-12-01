import requests

VERSION = "1.0.0"  # Mevcut sürümünüz

def check_for_updates():
    try:
        response = requests.get("https://example.com/version.json")  # JSON dosyanızın URL'si
        data = response.json()
        latest_version = data["latest_version"]
        if VERSION != latest_version:
            print("Güncelleme mevcut! İndiriliyor...")
            download_update(data["download_url"])
        else:
            print("Uygulamanız güncel!")
    except Exception as e:
        print("Güncelleme kontrolü sırasında hata oluştu:", e)

def download_update(url):
    try:
        response = requests.get(url, stream=True)
        with open("updated_app.exe", "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        print("Güncelleme başarıyla indirildi. Lütfen uygulamayı yeniden başlatın.")
    except Exception as e:
        print("Güncelleme indirilemedi:", e)

if __name__ == "__main__":
    check_for_updates()
