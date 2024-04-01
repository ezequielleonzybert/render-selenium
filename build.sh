echo 'export PATH=$PATH:/opt/render/project/src' >> ~/.bash_profile
source ~/.bash_profile

pip install -r requirements.txt

mkdir -p /chrome
cd /chrome
wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -x ./google-chrome-stable_current_amd64.deb /chrome