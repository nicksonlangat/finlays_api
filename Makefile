run:
	python manage.py runserver
migrate:
	python manage.py makemigrations && python manage.py migrate
su:
	python manage.py createsuperuser
pull:
	git pull origin master
spin:
	sudo systemctl restart finlay && sudo systemctl restart nginx