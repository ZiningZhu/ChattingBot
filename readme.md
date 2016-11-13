ChattingBot
===

A web server to experiment on my NLP stuffs.

### Adding a virtual server to port X:
Let X=81 as example
1. Add `Listen 81` to the file `/etc/apache2/ports.conf`  
2. `sudo cp config/ChattingBot.conf /etc/apache2/sites-available/`  
3. `sudo cp -r ChattingBot /var/www/`  
4. `sudo a2ensite ChattingBot`  
5. `sudo service apache2 reload`
