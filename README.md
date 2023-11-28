# Important
A simple HLS transcoder using AES encryption. This is is just a handy repo for beginners, ideally you need to add source of your original video and don't forget to provide a URL where key is stored. I'll try my best to update this repo frequently however if you have any questions, raise an issue


## Requirements
- Linux OS, recommend Ubunutu latest LTS
- Python 3.6+
- FFMPEG
- Virtualenv


## Features

This code encrypts HLS segments with an AES key. To generate a key make sure you have 

## Installation

```sh
Clone this repo
# echo -e "${keyinfo}" > ${target}.keyinfo
sudo apt update
sudo apt install ffmpeg && sudo apt install vierualenv
cd to "repo folder"
virtualenv env && source env/bin/activate
python app.py
