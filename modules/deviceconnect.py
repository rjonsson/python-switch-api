from netmiko import ConnectHandler
# export NET_TEXTFSM=~/python/python-cdp-desc/venv/lib/python3.7/site-packages/ntc_templates/templates

class DeviceConnect:
    def __init__(
        self,
        hostname
    ):
        self.username, self.password = self.__get_credentials()
        self.hostname = hostname
        self.options = {
            'device_type': 'cisco_ios',
            #'ssh_config_file': '~/.ssh/config',
            'username': self.username,
            'password': self.password
        }

    def __get_credentials(self):
        with open('credentials.conf', 'r') as readfile:
            for line in readfile:
                username, password = line.strip().split(':')
        return (username, password)

    # connects to the host and sends the command(s), depending on if input is string or list
    def send_command(self, command):
        # returns output if informational command, returns commands given if execution command
        with ConnectHandler(host=self.hostname, **self.options) as session:
            if 'show ' in command:
                return session.send_command(command, use_textfsm=True)
            else:
                return "Only show-commands supported"

# Testing
if __name__ == '__main__':
    device_session = DeviceConnect('10.37.94.114')
    print(device_session.send_command('show interfaces status'))

        
        

