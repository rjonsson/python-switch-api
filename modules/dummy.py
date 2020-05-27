from random import randrange
import json

class DummySwitch():
    def __init__(
        self, 
        hostname, 
        domainname = None,
        ip = None,
        ):

        self.hostname = hostname.split('.', 1)[0] if '.' in hostname else hostname
        self.domainname = None
        self.fqdn = None
        self.ip = None


    def update_connection(self):
        self.domainname = 'domain.com'
        self.fqdn = f"{self.hostname}.{self.domainname}"
        self.ip = f"10.{randrange(90)}.{randrange(90)}.{randrange(11,254)}"
        self.reachable = True


class DummyConnect():
    def __init__(
        self,
        hostname
    ):

        self.hostname = hostname

    def send_command(self, hostname):
        return "hejsan"



if __name__ == '__main__':
    dummyswitch = DummySwitch('testswitch')
    dummyswitch.update_connection()
    print(json.dumps(dummyswitch.__dict__).encode('utf8'))