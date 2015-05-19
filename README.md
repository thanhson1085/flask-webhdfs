PREREQUISITE:
- python3
- virtualenv
- pip


INSTALLATION:
```
git clone git@git.sigma-solutions.eu:web-team/clotify-framework.git
cd clotify-framework
virtualenv -p /usr/bin/python3 env
source env/bin/activate
cp config/config.tpl config/config.py
pip install -r requirements.txt  
python run.py  
```
