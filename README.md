# python-switch-api
Using netmiko and flask to push commands to switches

Installation:
```
# Windows Subsystem for Linux (Ubuntu)
git clone https://github.com/rjonsson/python-switch-api.git && cd python-switch-api

sudo apt-get install -y python curl virtualenv
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py --user
export $PATH="$HOME/.local/bin:$PATH"
virtualenv --python=python3 venv
echo "export NET_TEXTFSM=$HOME/venv/lib/python3.7/site-packages/ntc_templates/templates" | tee -a $HOME/venv/bin/activate > /dev/null
source $HOME/venv/bin/activate
pip install -r requirements.txt

```

#### Starting the API
```
echo username:hostname > credentials.conf
python app.py

```

#### Testing
http://<api-hostname>:5000/api/dummy/command/show_interfaces_status/<imaginary switch hostname>  
http://<api-hostname>:5000/api/dummy/gather/<imaginary switch hostname>

#### Real endpoints
http://<api-hostname>/api/command/show_interfaces_status/<switch hostname>  
http://<api-hostname>/api/gather/<switch hostname>