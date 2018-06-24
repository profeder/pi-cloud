import docker
import threading
import configparser

config = configparser.ConfigParser()
config.read('etc/agent.cnf')