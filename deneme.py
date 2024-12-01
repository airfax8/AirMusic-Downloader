import tkinter as tk

def on_enter(e):
    e.widget.config(bg="#00FF00", fg="black", relief="flat", font=("Arial", 12, 'bold'))
    e.widget.config(highlightbackground="cyan", highlightthickness=3)

def on_leave(e):
    e.widget.config(bg="#007BFF", fg="white", relief="raised", font=("Arial", 10))
    e.widget.config(highlightbackground="", highlightthickness=0)

def search():
    # Arama butonuna tıklandığında yapılacak işlemler
    search_term = entry.get()
    result_label.config(text=f"Arama Sonucu: {search_term}")

# Ana pencere oluştur
root = tk.Tk()
root.title("Şık Tasarım Uygulaması")
root.geometry("600x400")
root.configure(bg="#2e3b4e")

# Canvas kullanarak arka plan ekle
canvas = tk.Canvas(root, width=600, height=400, bg="#2e3b4e", bd=0, highlightthickness=0)
canvas.pack()

# Başlık
canvas.create_text(300, 50, text="Arama ve İndirme Uygulaması", fill="white", font=("Arial", 18, "bold"))

# Arama çubuğu
entry = tk.Entry(root, font=("Arial", 14), width=20, bd=2, relief="solid")
canvas.create_window(300, 150, window=entry)

# Arama butonu
search_button = tk.Button(root, text="Ara", bg="#007BFF", fg="white", font=("Arial", 12), width=15, height=2)
canvas.create_window(300, 200, window=search_button)

# Arama sonucu etiket
result_label = tk.Label(root, text="Arama Sonucu: ", fg="white", bg="#2e3b4e", font=("Arial", 12))
canvas.create_window(300, 250, window=result_label)

# Butonların üzerine gelindiğinde efekt oluştur
search_button.bind("<Enter>", on_enter)
search_button.bind("<Leave>", on_leave)

# Arama butonuna tıklanınca search fonksiyonu çalışacak
search_button.config(command=search)

# Uygulamayı çalıştır
root.mainloop()
