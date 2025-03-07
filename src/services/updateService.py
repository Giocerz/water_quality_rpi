import os
import shutil
import subprocess

# Configuración
REPO_URL = "https://github.com/tu_usuario/water_rpi.git"
LOCAL_DIR = "/home/pi/water_rpi"
VERSION_FILE = "version.txt"

# Obtener la versión actual
def get_local_version():
    version_path = os.path.join(LOCAL_DIR, VERSION_FILE)
    if os.path.exists(version_path):
        with open(version_path, "r") as f:
            return f.read().strip()
    return "0.0.0"

# Obtener la versión remota usando Git
def get_remote_version():
    temp_dir = "/tmp/water_rpi_temp"

    # Clonar solo el archivo version.txt sin descargar todo el repo
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    
    subprocess.run(["git", "clone", "--depth", "1", "--filter=blob:none", "--sparse", REPO_URL, temp_dir], check=True)
    subprocess.run(["git", "-C", temp_dir, "sparse-checkout", "set", VERSION_FILE], check=True)

    version_path = os.path.join(temp_dir, VERSION_FILE)
    if os.path.exists(version_path):
        with open(version_path, "r") as f:
            version = f.read().strip()
        shutil.rmtree(temp_dir)  # Eliminar la carpeta temporal
        return version
    return None

# Clonar el repositorio en una carpeta temporal
def clone_repo():
    temp_dir = "/home/pi/water_rpi_temp"
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)  # Borrar si existe
    subprocess.run(["git", "clone", REPO_URL, temp_dir], check=True)
    return temp_dir

# Reemplazar archivos sin sobrescribir `config` y `database.db`
def update_project(temp_dir):
    for item in os.listdir(temp_dir):
        src_path = os.path.join(temp_dir, item)
        dest_path = os.path.join(LOCAL_DIR, item)

        if os.path.isdir(src_path):
            if item == "config":
                continue  # No reemplazar config
            if os.path.exists(dest_path):
                shutil.rmtree(dest_path)  # Eliminar carpeta vieja
            shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
        else:
            if item == "database.db":
                continue  # No reemplazar database.db
            shutil.copy2(src_path, dest_path)

    shutil.rmtree(temp_dir)  # Limpiar la carpeta temporal

# Verificar y actualizar si es necesario
def check_and_update():
    local_version = get_local_version()
    remote_version = get_remote_version()

    if remote_version and remote_version > local_version:
        print(f"Actualización disponible: {local_version} → {remote_version}")
        temp_dir = clone_repo()
        update_project(temp_dir)
        print("Actualización completada.")
    else:
        print("No hay actualizaciones disponibles.")

