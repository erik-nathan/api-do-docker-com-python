import docker

HOST_DOCKER = 'unix://var/run/docker.sock'

client = docker.DockerClient(base_url=HOST_DOCKER)
container_id = '2a9ff9b439d5'
get = client.containers.get(container_id)

for line in get.logs(stream=True):
    print(line.strip())
