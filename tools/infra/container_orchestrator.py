from typing import List
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
    def start_containers(self, containers: List[str] = ["dynamodb-local", 
                                                        "reviewers-like-you-ingestion-1", 
                                                        "reviewers-like-you-projection-1",
                                                        "reviewers-like-you-recommendation-1", 
                                                        "reviewers-like-you-scraper-1"]):
        subprocess.Popen("docker compose up", shell=True)
        while len(self.client.containers.list()) != 5:
            time.sleep(1)

        for container_name in containers:
            container = self.client.containers.get(container_name)
            assert container.status == "running"

    def stop_containers(self):
        subprocess.Popen("docker compose down", shell=True)

        while len(self.client.containers.list()) != 0:
            time.sleep(1)

