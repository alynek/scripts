import os
import sys
import subprocess

def main():

    validate_required_fields()

    branch = sys.argv[1]
    workspace = sys.argv[2]

    validate_path(workspace)

    #TODO: 
    #validate branch exists
    #get data from branch
    #create zip file
    #validate bucket name
    #send to bucket

    print('✅ Build finalizado com sucesso!')
    sys.exit(0)


def validate_required_fields():
    if len(sys.argv) < 3:
        print('❌ A branch e o workspace são obrigatórios')
        sys.exit(1)

def validate_path(path):
    if not os.path.exists(path):
        print(f"❌ O diretório {path} não existe!")
        sys.exit(1)

if __name__ == '__main__':
    main()
