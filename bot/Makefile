db_migrate:
	orator migrate -c app/db/connect.py -p app/db/migrations -f

db_rollback:
	orator migrate:rollback -c app/db/connect.py -p app/db/migrations -f

bot_setup:
	pip install -r requirements.txt

db_seed:
	orator db:seed --config app/db/connect.py -p app/db/seeds -f



