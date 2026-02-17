from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Veritabanı Dosyasının Adı
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# 2. Motoru (Engine) Başlatıyoruz
# check_same_thread=False ayarı sadece SQLite için gereklidir.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. Oturum (Session) Oluşturucu
# Her veritabanı işlemi için bir oturum açıp kapatacağız.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Taban Sınıfı (Base)
# Modellerimizi (Tabloları) bu sınıftan türeteceğiz.
Base = declarative_base()