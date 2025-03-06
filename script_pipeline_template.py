import os
import sys
import subprocess
import shutil
import glob

#Existing variables in jenkins with valid path in machine
jobName = 'myJobProject'
deploy_path = '../deploy'

def main():

    validate_required_fields()

    branch = sys.argv[1]
    workspace = sys.argv[2]
    repository = sys.argv[3]

    validate_path(workspace)

    setup_repository(workspace, repository, branch)

    build_project(workspace)

    create_package(workspace)

    #TODO: 
    #validate bucket name 
    #send to bucket

    print(' Build finalizado com sucesso!')
    sys.exit(0)

def setup_repository(workspace, repo_url, branch):

    validateBranch(repo_url, branch)
    
    print(f"\n Iniciando clone da branch: {branch}")

    repo_path = os.path.join(workspace, jobName) 

    if not os.path.exists(repo_path) or not os.path.exists(os.path.join(repo_path, ".git")):

        run_command(f"git clone --branch {branch} {repo_url} {repo_path}")
        os.chdir(repo_path)

    else:
        print(f" Repositório já existe, indo para a branch '{branch}'...")
    
        os.chdir(repo_path)

        run_command("git fetch origin")
        run_command(f"git checkout {branch}")
        run_command(f"git pull origin {branch}")

        print(f"  Branch '{branch}' pronta para o build!")

def build_project(workspace):

    print(f"\n Verificando a sintaxe do código")

    python_files = glob.glob(f"{workspace}/*.py")

    for file in python_files:
        print(f"Compilando {file}...")
        subprocess.run(["python", "-m", "py_compile", file])

def create_package(workspace):

    print(f"\n Iniciando criação do pacote em: {workspace}")

    print(f" Voltando um nível para: {workspace}")
    os.chdir('..')

    repo_path = os.path.join(workspace, jobName) 
    print(f" Caminho de origem: {repo_path}")

    zip_file = os.path.join(deploy_path, jobName)
    print(f" Caminho de destino: {zip_file}")

    shutil.make_archive(zip_file, 'zip', repo_path)
    
    print(f" ZIP criado e movido para: {deploy_path}/{jobName}.zip")

def run_command(command):
    print(f" Executando: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        print(f" Erro ao executar '{command}': {result.stderr}")
        sys.exit(1)
    
    print(f" Sucesso: {result.stdout.strip()}")
    return result.stdout.strip()


def validate_required_fields():
    if len(sys.argv) < 4:
        print(' A branch, diretório de trabalho e url do repositório são obrigatórios')
        sys.exit(1)

    if not sys.argv[1].strip():
        print(" A branch não pode estar vazia.")
        sys.exit(1)

    if not sys.argv[2].strip():
        print(" O diretório de trabalho não pode estar vazio.")
        sys.exit(1)

    if not sys.argv[3].strip():
        print(" A url do repositório não pode estar vazio.")
        sys.exit(1)

def validate_path(path):
    if not os.path.exists(path):
        print(f" O diretório {path} não existe!")
        sys.exit(1)

def validateBranch(repo_url, branch):
    check_branch = subprocess.run(f"git ls-remote --heads {repo_url} {branch}", shell=True, capture_output=True, text=True)

    if not check_branch:
        print(f" Erro: A branch '{branch}' não existe no repositório remoto!")
        exit(1)

if __name__ == '__main__':
    main() 
