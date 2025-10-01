#Subir proyecto a GitHub: Incluye README.md.

from github import Github, Auth
import os 
#Configuracion 
TOKEN = "TU_TOKEN_PERSONAL"
REPO_NAME = "NOMBRE PARA TU REPOSITORIO"
CARPETA = r"DIRECCIÓN DE CARPETA QUE DESEAS SUBIR"

#Conectar con GITHUB
g = Github(auth=Auth.Token(TOKEN))
user = g.get_user()

#Creamos o usamos un repositorio
repo = None

repos = [r.name for r in user.get_repos()]

if(REPO_NAME in repos):
    repo = user.get_repo(REPO_NAME)
    print(f"Repositorio {REPO_NAME} ya existe, usando repositorio")
else:
    repo = user.create_repo(REPO_NAME)
    print(f"Repositorio {REPO_NAME} Creado correctamente")

#Crear README.md
readme_content = """
50 días aprendiendo Python -
XTheUchyX
Encuéntrame en:
Youtube
Tiktok
Facebook
"""
try:
    repo.create_file("README.md","Creando README.md",readme_content)
    print(f"README.md creado con exito")
except:
    archivo = repo.get_contents("README.md")
    repo.update_file("README.md","Actualizando README.md",readme_content,archivo.sha)
    print("README.md actualizado")

#Subir todos los archivos de la carpeta
for root, dirs, files in os.walk(CARPETA):
    for file in files:
        ruta_local = os.path.join(root,file)
        ruta_repo = os.path.relpath(ruta_local,CARPETA)
        with open(ruta_local,"r",encoding="utf-8") as f:
            contenido = f.read()
        try:
            repo.create_file(ruta_repo,f"Agregando {ruta_repo}", contenido)
            print(f"{ruta_repo} subido correctamente")
        except:
            archivo = repo.get_contents(ruta_repo)
            repo.update_file(ruta_repo,f"Actualizando {ruta_repo}", contenido, archivo.sha)
            print(f"{ruta_repo},Actualizado correctamente")