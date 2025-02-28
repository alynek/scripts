import os
import sys
import subprocess

def main():
    branch = sys.argv[1]
    workspace = sys.argv[2]

    validate_fields(branch, workspace)

    validate_path(workspace)

    print('Chegou até aqui!')
    sys.exit(0)


def validate_fields(branch, workspace):

    if not branch:
        print('O campo da branch é obrigatório')
        sys.exit(-1)

    if not workspace:
        print('O workspace é obrigatório')
        sys.exit(-1)

def validate_path(path):
    if not os.path.exists(path):
        print("O diretório do workkdpace não existe!")
        sys.exit(-1)

if __name__ == '__main__':
    main()
