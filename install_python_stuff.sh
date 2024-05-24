# script om de meeste libs op de raspberry pi te installeren (maakt het makkelijker bij reïnstall)
#!/usr/bin/bash

sudo apt-get install python3-pip

sudo pip3 install sparkfun_qwiic

sudo apt-get install libatlas3-base
sudo apt-get install libffi-dev
sudo apt-get install at-spi2-core
sudo apt-get install python3-gi-cairo
pip3 install cairocffi
pip3 install matplotlib

# check als alle modules installed zijn
touch temp_programs.txt
apt list > temp_programs.txt
touch programs.txt
cat temp_programs.txt | grep libatlas3-base >> programs.txt
cat temp_programs.txt | grep  libffi-dev >> programs.txt
cat temp_programs.txt | grep  at-spi2-core >> programs.txt
cat temp_programs.txt | grep  python3-gi-cairo>> programs.txt
cat temp_programs.txt | grep cairocffi >> programs.txt
cat temp_programs.txt | grep mathplotlib >> programs.txt
rm temp_programs.txt

echo "\n \n installed programs:"
cat programs.txt
