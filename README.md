# TimelyTweet

Basics 
=====
1. On mac, install homebrew (http://brew.sh/)
 ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)" 

2. Install pip 
sudo easy_install pip
3. Install Virtual Environment 
sudo pip install virtualenv

Getting Started
===============

1. Clone the repo

    git clone http://github.com/shoyebi/TimelyTweet.git

2. create a new virtualenv (named 'hs' in the example)

    virtualenv hs --no-site-packages

3. enter your virtualenv

    source hs/bin/activate
4. bootstrap your installation (this installs some requirements via pip)

    TimelyTweet/bin/bootstrap.py
5. RUN
    python timetwitter/server.py
    Application will start running on http://127.0.0.1:5000/
