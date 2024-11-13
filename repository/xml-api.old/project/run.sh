gunicorn --bind 0.0.0.0:8000 --daemon app.app:app

ps aux | grep gunicorn
kill NumerodoProcesso

aliases

upgunicorn #exec in background
upgunicorndebug #exec debug
showgunicorn #show gunicorn proccess

#PRecisa dar permissões na pasta
sudo chmod 777 -R ~/portal-xml