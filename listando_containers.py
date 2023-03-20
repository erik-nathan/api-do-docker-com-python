import docker

HOST_DOCKER = 'unix://var/run/docker.sock'

client = docker.DockerClient(base_url=HOST_DOCKER)

container_list = client.containers.list()

for container in container_list:
    container_short_id = container.short_id
    container_name = container.name
    container_attrs = container.attrs
    container_status = container_attrs['State']['Status']
    print(f'{container_short_id} - {container_name} - {container_status}')
    