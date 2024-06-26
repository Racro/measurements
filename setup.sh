sudo apt-get update

# Setup venv
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.10 python3.10-venv python3.10-dev
sudo apt-get install python3-pip
python3.10 -m venv crawl

# Install packages
pip install -r requirements.txt

# Install Xvfb
sudo apt-get install xvfb xserver-xephyr tigervnc-standalone-server x11-utils gnumeric

# Install Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
rm google-chrome-stable_current_amd64.deb

# Netstat
sudo apt-get install net-tools

# Catapult
pushd "~" > /dev/null

pip install gdown
gdown --id 1Kd4YiEj3TeZ0lJrYwPju1dz0uFQK59Zr # Drive link - https://drive.google.com/file/d/1Kd4YiEj3TeZ0lJrYwPju1dz0uFQK59Zr/view?usp=drive_link
tar -xvzf catapult.tar.gz
rm catapult.tar.gz

wget https://go.dev/dl/go1.22.4.linux-amd64.tar.gz
rm -rf /usr/local/go && tar -C /usr/local -xzf go1.22.4.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin
rm go1.22.4.linux-amd64.tar.gz

popd > /dev/null

