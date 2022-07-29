import subprocess
import time


class ContainerOrchestrator:
    def __init__(self):
        pass

    def start_containers(self):
        docker_compose_up = subprocess.Popen("docker compose up -d", shell=True)
        docker_compose_up.wait()
        time.sleep(5)

    def stop_containers(self):
        docker_compose_down = subprocess.Popen("docker compose down", shell=True)
        docker_compose_down.wait()

