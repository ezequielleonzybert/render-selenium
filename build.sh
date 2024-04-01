echo 'export PATH=$PATH:/opt/render/project/src' >> ~/.bash_profile
source ~/.bash_profile

pip install -r requirements.txt

apt-get install google-chrome-stable -y