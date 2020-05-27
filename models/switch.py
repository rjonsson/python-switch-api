import socket
import subprocess
import platform 

class Switch():
    def __init__(
        self, 
        hostname, 
        domainname = None,
        ip = None,
        ):

        self.hostname = hostname.split('.', 1)[0] if '.' in hostname else hostname
        self.domainname = domainname if domainname else None
        self.ip = ip if ip else None
        self.reachable = None


    def update_connection(self):
        self.domainname = self._check_domain()
        self.fqdn = f"{self.hostname}.{self.domainname}" if self.domainname else None
        self.ip = self._resolve_ip() if self.fqdn else None
        self.reachable = self._test_reachability() if self.ip else None


    def update_neighbors(self):
        return None


    def _check_domain(self):
        potential_suffixes = ['skanska.org','skanska.net','neteq.skanska.net','clients.skanska.se']
        for suffix in potential_suffixes:
            try:
                socket.getaddrinfo(f"{self.hostname}.{suffix}",0,0,0,0)
                return suffix
            except socket.gaierror:
                if suffix == potential_suffixes[-1]:
                    print(f"{self.hostname}: no matching domains")
                    return None


    def _resolve_ip(self):
        try:
            return socket.gethostbyname(self.fqdn)
        except socket.gaierror:
            print(f"{self.fqdn}: error resolving ip")
            return None


    def _test_reachability(self):
        # format command depending on OS
        param = '-n' if platform.system().lower()=='windows' else '-c'
        command = ['ping', param, '1', '-w', '1000', self.ip]
        process = subprocess.call(command, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        return True if not process else False

# testing
if __name__ == '__main__':
    switch = Switch(hostname='se2169sw05')
    print(f"{switch.ip}, {switch.reachable}") if switch.domainname else print(f"{switch.hostname} fail")