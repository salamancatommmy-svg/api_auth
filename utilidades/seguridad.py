"""Utilidades de seguridad: hash y verificación de contraseñas con bcrypt."""
import bcrypt

def generar_hash(clave: str) -> str:
    """Devuelve el hash bcrypt de la contraseña (incluye sal aleatoria)."""
    return bcrypt.hashpw(clave.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def verificar_clave(clave: str, clave_hash: str) -> bool:
    """Compara una contraseña en texto plano contra el hash almacenado."""
    try:
        return bcrypt.checkpw(clave.encode("utf-8"), clave_hash.encode("utf-8"))
    except ValueError:
        return False
