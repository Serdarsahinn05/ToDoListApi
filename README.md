# To-Do List REST API (FastAPI) ⚡🚀

Python'un modern ve hızlı web çatısı **FastAPI** ve **SQLAlchemy** kullanılarak geliştirilmiş, yüksek performanslı bir To-Do List API projesi. Bu proje, CRUD işlemlerini, ORM yapısını ve Pydantic veri doğrulama sistemini göstermektedir.

## 🌟 Özellikler

* **⚡ FastAPI:** Çok hızlı ve modern asenkron altyapı.
* **🗄️ SQLAlchemy & SQLite:** İlişkisel veritabanı yönetimi (ORM) ve yerel depolama.
* **📑 Otomatik Dokümantasyon:** Swagger UI (`/docs`) ve ReDoc (`/redoc`) desteği.
* **✅ Pydantic:** Veri doğrulama ve tip güvenliği.

## 🛠️ Proje Yapısı

Proje modüler bir yapıda tasarlanmıştır:

* `main.py`: Uygulamanın giriş noktası ve API endpoint'leri.
* `models.py`: Veritabanı tablolarının (SQLAlchemy) tanımları.
* `database.py`: Veritabanı bağlantısı ve oturum yönetimi.
* `todos.db`: Verilerin tutulduğu SQLite dosyası (Otomatik oluşur).

## 💻 Kurulum ve Çalıştırma

Projeyi yerel makinenizde çalıştırmak için adımları izleyin:

### 1. Projeyi Klonlayın
```bash
git clone [https://github.com/Serdarsahinn05/ToDoListApi.git](https://github.com/Serdarsahinn05/ToDoListApi.git)
cd ToDoListApi
```

### 2. Gerekli Kütüphaneleri Yükleyin
```bash
pip install -r requirements.txt
```

### 3. Sunucuyu Başlatın
FastAPI projelerini çalıştırmak için `uvicorn` kullanılır.
```bash
uvicorn main:app --reload
```
* --reload: Kodda değişiklik yaptığınızda sunucuyu otomatik yeniler.

### 📡 API Kullanımı ve Dokümantasyon

Sunucu çalıştıktan sonra tarayıcınızdan aşağıdaki adreslere giderek API'yi test edebilirsiniz:
* Swagger UI (İnteraktif Test): http://127.0.0.1:8000/docs
* Alternatif Dokümantasyon: http://127.0.0.1:8000/redoc


| Metot  | URL         | Açıklama                        |
|--------|-------------|---------------------------------|
| GET    | /todos      | Kayıtlı tüm görevleri listeler. |
| POST   | /todos      | Yeni bir görev ekler.           |
| DELETE | /todos/{id} | ID'si verilen görevi siler.     |

### 📌 Örnek JSON İsteği (POST)
`/todos` adresine gönderilecek örnek veri:
```json
{
  "title": "FastAPI öğren",
  "completed": false
}
```

### 📝 Lisans
Bu proje açık kaynaklıdır ve eğitim amaçlı geliştirilmiştir.

Geliştirici: [Serdarsahinn05](https://github.com/Serdarsahinn05)
