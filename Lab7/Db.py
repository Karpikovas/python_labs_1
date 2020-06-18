from pymysql import *

class LibMedicaments(object):

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def connect(self):
        self.connection = connect(
            host='127.0.0.1',
            user='root',
            password='stivka1855275',
            db='medicaments',
            charset='utf8mb4',
            cursorclass=cursors.DictCursor
        )

    def close_connection(self):
        self.connection.close()

    def get_medicaments(self):
        sql = '''SELECT
                    vendore_code,
                    medicament.name,
                    cost,
                    description,
                    CONCAT(producer.name, ' / ', producer.country) as producer,
                    category.name as category
                FROM medicaments.medicament
                INNER JOIN medicamenthasproducer on medicament.vendore_code = medicamenthasproducer.id_medicament
                INNER JOIN producer on producer.id = medicamenthasproducer.id_producer
                INNER JOIN medicamenthascategory on medicament.vendore_code = medicamenthascategory.id_medicament
                INNER JOIN category on category.id = medicamenthascategory.id_category;'''

        cursor = self.connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def get_producers(self):
        sql = "SELECT id, CONCAT(producer.name, ' / ', producer.country) as producer FROM medicaments.producer;"

        cursor = self.connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def get_categories(self):
        sql = "SELECT id, name FROM medicaments.category;"

        cursor = self.connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    def delete_medicament(self, vendore_code):
        sql = 'DELETE FROM medicaments.medicament where vendore_code = %s'

        cursor = self.connection.cursor()
        cursor.execute(sql, int(vendore_code))
        self.connection.commit()
        return cursor

    def insert_medicament(self, vendore_code, name, description, cost, id_category, id_producer):
        sql = '''INSERT INTO medicament (
                    vendore_code,
                    name,
                    description,
                    cost
                )
                VALUES (%s, %s, %s, %s);'''

        cursor = self.connection.cursor()
        cursor.execute(sql, (vendore_code, name, description, cost))
        self.connection.commit()

        sql = '''INSERT INTO medicamenthascategory (
                    id_medicament,
                    id_category
                )
                VALUES (%s, %s);'''

        cursor = self.connection.cursor()
        cursor.execute(sql, (vendore_code, id_category))
        self.connection.commit()

        sql = '''INSERT INTO medicamenthasproducer (
                    id_medicament,
                    id_producer
                )
                VALUES (%s, %s);'''

        cursor = self.connection.cursor()
        cursor.execute(sql, (vendore_code, id_producer))
        self.connection.commit()

        return cursor