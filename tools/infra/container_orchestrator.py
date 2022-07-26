import os


class ContainerOrchestrator:
    def __init__(self):
        pass

    def start_containers(self):
        os.popen("docker compose up -d").read()

    def stop_containers(self):
        os.popen("docker compose down").read()


