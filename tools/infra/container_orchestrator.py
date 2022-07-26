import subprocess


class ContainerOrchestrator:
    def __init__(self):
        pass

    def start_containers(self):
        docker_compose_up = subprocess.Popen("docker compose up -d", shell=True, stdout=subprocess.PIPE)
        docker_compose_up.wait()

    def stop_containers(self):
        docker_compose_down = subprocess.Popen("docker compose down", shell=True, stdout=subprocess.PIPE)
        docker_compose_down.wait()




