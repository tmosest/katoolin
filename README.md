![katoolin](https://cloud.githubusercontent.com/assets/8742190/9415562/83397aae-4840-11e5-8f72-28dfffcc70a9.png)
# katoolin
Automatically install all Kali linux tools

# Features
- Add Kali linux repositories
- Remove kali linux repositories
- Install Kali linux tools

# Requirements
- Python 3.12
- An operating system (tested on Ubuntu)

# Installation
- sudo su
- git clone https://github.com/LionSec/katoolin.git && cp katoolin/katoolin.py /usr/bin/katoolin
- chmod +x /usr/bin/katoolin
- sudo katoolin 

# Video
https://www.youtube.com/watch?v=8VxCWVoZEEE

# Usage
- Typing the number of a tool will install it
- Typing 0 will install all Kali Linux tools
- back : Go back
- gohome : Go to the main menu
- By installing armitage , you will install metasploit

# Warning
Before updating your system , please remove all Kali-linux repositories to avoid any kind of problem .

Might need this is update command wont work.

```
# download
wget http://http.kali.org/kali/pool/main/k/kali-archive-keyring/kali-archive-keyring_2024.1_all.deb
# install
sudo dpkg -i kali-archive-keyring_2024.1_all.deb
# remove downloaded file again
rm kali-archive-keyring_2024.1_all.deb
# update
sudo apt-get update
```
