echo "Welcome"
echo "This setup will install the following packages and utilities"
echo "**** NodeJS ****"
echo "**** Angular CLI ****"
echo "**** MySQL database ****"
echo "**** Python 2.7**** "
echo "**** Flask server ****"
echo "**** Github ****"
echo "Starting setp for web application"
cd
echo "Installing NodeJS"
sudo apt-get install python-software-properties
$curl -sL https://deb.ondesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs
if [ $? -ne 0 ]; then
echo "CRITICAL: Failed to install NodeJS"
exit 1
fi 
exit 0
node -v
if [ $1 -gt 100 ]; then
  echo "that's a large number"
fi
echo "Installing Angular CLI"
sudo npm install -g @angular/cli
if [ $? -ne 0 ]; then
echo "CRITICAL: Failed to install Angular CLI"
exit 1
fi
exit 0
ng -v
echo "Installing MySQL Database"
sudo apt-get update
sudo apt-get install mysql-server-5.5
sudo mysql_secure_installation
mysql --version
sudo mysql_install_db
sudo service mysql status
echo "Installing Python"
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
cd /usr/src
sudo wget https://www.python.org/ftp/python/2.7.6/Python-2.7.6.tgz
sudo tar xzf Python-2.7.6.tgz
cd Python-2.7.6
sudo ./configure --enable-optimizations
sudo make altinstall
if [ $? -ne 0 ]; then
  echo "There was a problem installing Python"
exit 1
fi
exit 0
python2.7 -V
echo "Installing Flask"
sudo apt-get install python2.7-flask
if [ $? -ne 0 ]; then
   echo "There was a problem installing flask"
exit 1
fi
exit 0
echo "Installing Github"
sudo apt-get install git
if [ $? -ne 0 ]; then
  echo "CRITICAL: There was an error installing Github. Aborting"
exit 1
fi
exit 0
echo "Installation completed. You may proceed with application installation next"

