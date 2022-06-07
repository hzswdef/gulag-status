## What is gulag-status?

**gulag-status** is the webpage for check up [bancho.py]( https://github.com/osuAkatsuki/bancho.py ) & [guweb]( https://github.com/Varkaria/guweb ) servers status.

## Requirements
- <sup>Some know-how with Linux (tested on Ubuntu 18.04), Python, and general-programming knowledge.</sup>
- NGINX

## Setup
Setup is relatively simple - these commands should set you right up.

```bash
# Update apt & add repo.
sudo apt update
sudo add-apt-repository ppa:deadsnakes/ppa

# Install Python >=3.9 and NGINX.
sudo apt install python3.9 python3.9-dev python3.9-distutils build-essential nginx

# Install Python PIP
wget https://bootstrap.pypa.io/get-pip.py
python3.9 get-pip.py && rm get-pip.py

# Clone gulag-status from GitHub.
git clone https://github.com/hzswdef/gulag-status.git
cd gulag-status/

# Install all requirements from pip.
python3.9 -m pip install -r ext/requirements.txt

# Add and configure gulag-status NGINX config to your nginx/sites-enabled.
sudo ln -r -s ext/nginx.conf /etc/nginx/sites-enabled/gulag-status.conf
sudo nano ext/nginx.conf
sudo nginx -s reload

# Configure gulag-status.
cp ext/.env.example .env
nano .env

# Run gulag-status (on port 8000).
python3.9 app.py # Run directly to access debug features for development!
hypercorn app.py # Please run guweb with hypercorn when in production! It will improve performance drastically by disabling all of the debug features a developer would need!
```

## Directory structure

```
.
├── ext          # External files from guweb's primary operation.
├── objects      # Code for global objects and more.
├── static       # Code or content that is not modified or processed by guweb itself.
└── templates    # HTML that contains content that is rendered after the page has loaded.
    └── status   # Templated content for the status page (/).
```
