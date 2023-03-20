import docker
import sys

args = sys.argv

HOST_DOCKER = 'unix://var/run/docker.sock'

client = docker.DockerClient(base_url=HOST_DOCKER)

def remove_container(container_id):
    try:
        get = client.containers.get(container_id)
        container_name = get.name
        print('Container Encontrado')
        try:
            remove = get.remove(force=True)
            print(f'Container: {container_name} | Removido com sucesso')
        except Exception as err:
            print(f'Falha ao remover o container {container_name}')
    except Exception as err:
        print('Não encontrou o container')

if len(args) <= 1:
    print(f'Está faltando o container id')
    print(f'Ex.: python3 removendo_container.py 1234')
else:
    container_id = args[1]
    remove_container(container_id)
