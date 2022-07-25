import docker
import subprocess
import time
import warnings


class ContainerOrchestrator:
    def __init__(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', DeprecationWarning)
            self.client = docker.client.DockerClient()

    # TODO Create a separate API for launching an -inMemory dynamodb
    # instance in a container, so that we can use it for testing.

    # TODO This will need to change along with docker-compose.yml
    def start_containers(self):
        subprocess.Popen("docker compose up", shell=True)
        while len(self.client.containers.list()) == 0:
            time.sleep(0.1)
        container = self.client.containers.get("dynamodb-local")
        assert container.status == "running"

    def stop_containers(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', DeprecationWarning)
            container = self.client.containers.get("dynamodb-local")
            container.stop()
            self.client.containers.prune()
