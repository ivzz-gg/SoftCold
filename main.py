import config
import server.threads
from db import Person

if __name__ == '__main__':
    Person.create_table()
    Person.create(name='Daniil', telegram_id='411243851', rooms_access='room1,room2,room3')
    Person.create(name='Dmitrii', telegram_id='330410183', rooms_access='room1,room2')
    print("Start bot...")
    print("Serving at port", config.HTTP_PORT)
    server.threads.threads_start()
