start:
	poetry run python manage.py runserver

migrations:
	poetry run python manage.py makemigrations

aply_migrations:
	poetry run python manage.py migrate

translation_messages:
	django-admin makemessages -l ru

copile_messages:
	django-admin compilemessages
