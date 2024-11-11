from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Configuración de la URL de la base de datos
DATABASE_URL = "sqlite:///./characters.db"

# Crea el motor de conexión a la base de datos
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Configura la sesión de la base de datos con parámetros personalizados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define una base para que todos los modelos puedan heredar de ella
Base = declarative_base()
