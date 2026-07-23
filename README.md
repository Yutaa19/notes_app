# 📝 Notes App RESTful API

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)

Sebuah *backend service* yang tangguh dan terukur untuk aplikasi manajemen catatan (Notes App). Dibangun menggunakan **FastAPI** dengan menerapkan arsitektur **Model-View-Controller (MVC)** yang dimodifikasi menjadi sistem modular. API ini dirancang dengan fokus pada keamanan (*Security*), efisiensi performa, dan kemudahan skalabilitas.

## ✨ Fitur Utama (Key Features)

- **Authentication & Authorization:** Sistem registrasi dan login yang aman menggunakan **JWT (JSON Web Tokens)** dan enkripsi *password* menggunakan `pwdlib`.
- **Modular Architecture:** Struktur *codebase* berbasis modul (Auth, User, Note, Like) yang memudahkan *maintenance* dan pengembangan fitur berkelanjutan.
- **Advanced Notes Management:** - Catatan dilengkapi dengan status privasi (`Public`, `Private`, `Protected`).
  - Fitur keamanan ekstra berupa *password* khusus dan *hint* untuk catatan berstatus `Protected`.
- **Media Handling:** Dukungan unggah *file* secara lokal untuk foto profil dan *thumbnail* pengguna.
- **Relational Database Design:** Desain skema *database* relasional yang optimal menggunakan **PostgreSQL** dan **SQLAlchemy (ORM)** (mencakup relasi antar entitas User, Note, dan Likes).
- **Containerized Database:** Lingkungan *database* terisolasi menggunakan **Docker Compose** lengkap dengan pgAdmin untuk manajemen data visual.

## 🛠️ Teknologi yang Digunakan (Tech Stack)

* **Framework:** FastAPI
* **Bahasa Pemrograman:** Python 3.x
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy (Async/Sync Compatible Structure)
* **Validasi & Konfigurasi:** Pydantic & Pydantic Settings
* **Authentication:** PyJWT
* **Server:** Uvicorn
* **DevOps / Container:** Docker & Docker Compose

## 🗂️ Struktur Proyek (Architecture Overview)

Proyek ini menggunakan pola arsitektur yang memisahkan *Routing* (Controller), *Business Logic* (Service), dan *Data Access* (Model) untuk menjaga kode tetap *Clean* dan *DRY (Don't Repeat Yourself)*.

    ```text
    ├── app/
    │   ├── config/          # Manajemen environment variables & logger
    │   ├── db/              # Konfigurasi koneksi SQLAlchemy & PostgreSQL
    │   ├── modules/         # Domain-Driven Modules
    │   │   ├── auth/        # Controller & Service untuk Autentikasi
    │   │   ├── like/        # Model relasi Likes
    │   │   ├── note/        # Logika manajemen catatan
    │   │   └── user/        # Profiling dan manajemen gambar pengguna
    │   └── __init__.py      # FastAPI App Factory & Lifespan handler
    ├── docker-compose.yml   # Konfigurasi service PostgreSQL & pgAdmin
    ├── main.py              # Entry point aplikasi (Uvicorn)
    └── requirements.txt

🚀 Panduan Instalasi (Getting Started)
1. Prasyarat (Prerequisites)
Pastikan sistem Anda sudah terinstal:
Python 3.10+
Docker & Docker Compose

2. Clone Repositori
   ```
    git clone [https://github.com/username-anda/notes-app-backend.git](https://github.com/username-anda/notes-app-backend.git)
    cd notes-app-backend

3. Konfigurasi Environment (Variabel Lingkungan)
Buat file .env pada root directory dan sesuaikan dengan kredensial Anda
    ```
    # Database Config
    POSTGRES_USER=xxx xxx
    POSTGRES_PASSWORD=xxx xxx
    POSTGRES_DB=xxx xxx
    POSTGRES_HOST=xxx xxx
    POSTGRES_PORT=xxx xxx
    
    # pgAdmin Config (Opsional)
    PGADMIN_DEFAULT_EMAIL=xxx xxx
    PGADMIN_DEFAULT_PASSWORD=xxx xxx
    
    # JWT Token Config
    SECRECT_KEY=xxx xxx
    ALGORITHM=xxx xxx
    ACCESS_TOKEN_EXPIRE_HOURS=xx

4. Menjalankan Database dengan Docker
Jalankan PostgreSQL dan pgAdmin menggunakan Docker Compose:
    ```
    docker-compose up -d

6. Instalasi Dependensi Python
Sangat disarankan menggunakan Virtual Environment (venv):
   ```
    python -m venv venv
    source venv/bin/activate  # (Untuk Linux/Mac)
    venv\Scripts\activate     # (Untuk Windows)

    pip install -r requirements.txt

6. Menjalankan Aplikasi
Mulai server FastAPI menggunakan Uvicorn:
    ```
    python main.py

📡 Daftar Endpoint API (API Endpoints)
Secara garis besar, berikut adalah resource yang tersedia:

* **Authentication:** POST /auth/register - Pendaftaran pengguna baru.
* **POST /auth/login** - Autentikasi dan pengeluaran token JWT (OAuth2 Flow).
* **Users: * GET /users/** - Mengambil data profil pengguna berdasarkan ID.
* **PUT /users/** - Memperbarui data pengguna, termasuk unggah profile_img & thumbnail.
(Catatan: Endpoint untuk Notes dan Likes dirancang mengikuti pola yang sama pada tahap pengembangan selanjutnya).

Dibuat dengan ❤️ oleh [Nama Anda/Mohamad Rafly Andreanto] - Terbuka untuk diskusi kolaborasi dan peluang pengembangan karir.

