import docker

HOST_DOCKER = 'unix://var/run/docker.sock'

client = docker.DockerClient(base_url=HOST_DOCKER)

docker_info = client.version()

components = docker_info['Components']

for component in components:
    if component['Name'] == 'Engine':
        version = component['Version']
        print(f'A versão do Docker é: {version}')
