#!/usr/bin/python
import sys
import logging

activate_this = '/var/www/ChattingBot/ChattingBot/venv/bin/activate_this.py'
execfile (activate_this, dict(__file__ = activate_this))


logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/ChattingBot")

from ChattingBot import app as application
