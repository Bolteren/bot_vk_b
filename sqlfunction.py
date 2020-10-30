import pymysql
import botConfiguration as bc


class msql:
    def __init__(self):
        self.db_config = bc.read_db_config()
        try:
            self.connection = pymysql.connect(**self.db_config)
            self.cursor = self.connection.cursor()
        except pymysql.Error as e:
            print('Error { ', e, ' }')

    def update(self, t_edit, id_user):
        query = "UPDATE users SET time_checks='%s:%s:00' WHERE user_id=%s;"
        try:
            self.cursor.execute(query, (t_edit.hour, t_edit.minute, id_user))
            self.connection.commit()
        except pymysql.Error as e:
            print('Error { ', e, ' }')

    def insert(self, id_user, first_name, last_name):
        query = "INSERT INTO `users` (`first_name`, `last_name`, `user_id`) VALUES(%s, %s, %s)"
        try:
            self.cursor.execute(query, (first_name, last_name, id_user))
            self.connection.commit()
        except pymysql.Error as e:
            print('Error { ', e, ' }')

    def select(self, t_edit, id_user):
        query = "SELECT time_checks FROM users WHERE user_id=%s;"
        result = ""
        try:
            self.cursor.execute(query, (id_user))
            result = self.cursor.fetchone()
            self.connection.commit()
        except pymysql.Error as e:
            print('Error { ', e, ' }')
        return result

    def __del__(self):
        self.cursor.close()
        self.connection.close()


def main():
    bd = msql()
    print(bd.select("asd", 3009235))


if __name__ == "__main__":
    main()