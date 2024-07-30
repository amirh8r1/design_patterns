"""
    Decorator
        -a structural pattern that allows adding new behaviors
        to objects dynamically by placing them inside special wrapper objects,
        called decorators.
"""
import abc


class Page(abc.ABC):  # Abstract Component
    @abc.abstractmethod
    def show(self):
        pass


class AuthPage(Page):  # Concrete Component 1
    def show(self):
        print('Welcome to authenticated page')


class AnonPage(Page):  # Concrete Component 2
    def show(self):
        print('Welcome to anonymous page')


class PageDecorator(Page, abc.ABC):  # Abstract Decorator
    def __init__(self, component) -> None:
        self._component = component

    @abc.abstractmethod
    def show(self):
        pass


class PageAuthDecorator(PageDecorator):
    def show(self):
        user = input('username: ')
        password = input('password: ')
        if user == 'admin' and password == 'secret':
            self._component.show()
        else:
            print('you are not authenticated')


def client_decorator():
    page = AnonPage()
    authenticated = PageAuthDecorator(page)
    authenticated.show()
