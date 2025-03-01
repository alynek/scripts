import os
import sys
import subprocess

jobName = 'myJobProject'

def main():

    validate_required_fields()

    branch = sys.argv[1]
    workspace = sys.argv[2]
    repository = sys.argv[3]

    validate_path(workspace)

    setup_repository(workspace, repository, branch)

    #TODO: 
    #create zip file
    #validate bucket name
    #send to bucket

    print('\n✅ Build finalizado com sucesso!')
    sys.exit(0)

def setup_repository(workspace, repo_url, branch):

    validateBranch(repo_url, branch)
    
    print(f"🚀 Iniciando clone da branch: {branch}")

    repo_path = os.path.join(workspace, jobName) 

    if not os.path.exists(repo_path) or not os.path.exists(os.path.join(repo_path, ".git")):

        run_command(f"git clone --branch {branch} {repo_url} {repo_path}")

    else:
        print(f"\n🔄 Repositório já existe, indo para a branch '{branch}'...")
    
        os.chdir(repo_path)

        run_command("git fetch origin")
        run_command(f"git checkout {branch}")
        run_command(f"git pull origin {branch}")

        print(f"\n✅  Branch '{branch}' pronta para o build!")

def run_command(command):
    print(f"\n🔹 Executando: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"❌ Erro ao executar '{command}': {result.stderr}")
        sys.exit(1)
    
    print(f"✅ Sucesso: {result.stdout.strip()}")
    return result.stdout.strip()


def validate_required_fields():
    if len(sys.argv) < 4:
        print('❌ A branch, workspace e repositório são obrigatórios')
        sys.exit(1)

def validate_path(path):
    if not os.path.exists(path):
        print(f"❌ O diretório {path} não existe!")
        sys.exit(1)

def validateBranch(repo_url, branch):
    check_branch = subprocess.run(f"git ls-remote --heads {repo_url} {branch}", shell=True, capture_output=True, text=True)

    if not check_branch:
        print(f"❌ Erro: A branch '{branch}' não existe no repositório remoto!")
        exit(1)

if __name__ == '__main__':
    main()
