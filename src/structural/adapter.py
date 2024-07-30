"""
    Adapter
    -a structural design pattern that allows objects
    with incompatible interfaces to collaborate.
"""
import xmltodict


class Application:
    def send_request(self):
        return 'data.xml'


class Analytic:
    def receve_request(self, json):
        return json


class Adapter:
    def convert_xml2json(self, file):
        with open(file, 'r') as myfile:
            obj = xmltodict.parse(myfile.read())
            return obj


def client_adapter():
    sender = Application().send_request()
    converted_data = Adapter().convert_xml2json(sender)
    receiver = Analytic().receve_request(converted_data)
    return receiver
