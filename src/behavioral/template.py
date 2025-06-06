"""
    Template Method
        -a behavioral design pattern that defines the skeleton of an algorithm
        in the superclass but lets subclasses override specific steps of the
        algorithm without changing its structure.
"""
import abc


class Top(abc.ABC):
    def template_method(self):
        self.first_common()
        self.second_common()
        self.third_require()
        self.fourth_require()

    def first_common(self):
        print('This is first common...')

    def second_common(self):
        print('This is second common...')

    @abc.abstractmethod
    def third_require(self):
        pass

    @abc.abstractmethod
    def fourth_require(self):
        pass


class One(Top):
    def third_require(self):
        print('third...(one)')

    def fourth_require(self):
        print('fourth...(one)')


class Two(Top):
    def third_require(self):
        print('third...(two)')

    def fourth_require(self):
        print('fourth...(two)')


def client(klass):
    klass.template_method()
