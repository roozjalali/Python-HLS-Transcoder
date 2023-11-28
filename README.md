# python-hls-transcoder
A simple HLS transcoder using AES encryption. This is


## Requirements
- Linux OS, recommend Ubunutu latest TLS
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
