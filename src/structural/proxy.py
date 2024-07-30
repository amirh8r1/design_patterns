"""
    Proxy
        -a structural design pattern that lets you provide a substitute or
        placeholder for another object.
        -a proxy controls access to the original object, allowing you
        to perform something either before or after the request gets through
        to the original object.
"""
import abc
import time
import datetime


class AbstractServer(abc.ABC):
    @abc.abstractmethod
    def receive(self):
        pass


class Server(AbstractServer):
    def receive(self):
        print('Processing your request...')
        time.sleep(2)
        print('Done...')


class LogProxy(AbstractServer):
    def __init__(self, service) -> None:
        self._service = service

    def receive(self):
        self.logging()
        # ...
        self._service.receive()

    def logging(self):
        print(f'Request {datetime.datetime.now}')


def client_server(server, proxy):
    s = server()
    p = proxy(s)
    p.recive()
