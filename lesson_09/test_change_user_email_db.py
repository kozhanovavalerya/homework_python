from sqlalchemy import create_engine
from sqlalchemy import text

# Перед запуском подставить значения:
# myuser - имя пользователя
# mypassword - пароль
# mydatabase - название БД
db_connection_string = (
    "postgresql://myuser:mrpassword@localhost:5432/mydatabase")
db = create_engine(db_connection_string)


def test_update_email():
    new_user_id = '999999'
    new_user_email = 'test090@mail.ru'
    new_subject_id = 1

    connection = db.connect()
    transaction = connection.begin()

    sql = text("""INSERT INTO users(
        user_id, user_email, subject_id)
    VALUES (:new_user_id, :new_user_email, :new_subject_id)""")
    connection.execute(
        sql,
        {
           "new_user_id": new_user_id,
           "new_user_email": new_user_email,
           "new_subject_id": new_subject_id})

    new_email = 'test0100@mail.ru'

    change_email = text("UPDATE users SET user_email = :new_email \
        WHERE user_id = :new_user_id")
    connection.execute(change_email,
                       {"new_email": new_email, "new_user_id": new_user_id})

    check_new_email = text("""
    SELECT user_id
    FROM users
    WHERE user_id = :new_user_id
    AND user_email = :new_email""")

    result = connection.execute(
        check_new_email, {"new_user_id": new_user_id,
                          "new_email": new_email})

    user = result.fetchone()
    assert user is not None

    delete_sql = text("""
    DELETE from users
    WHERE user_id = :new_user_id""")

    connection.execute(delete_sql, {"new_user_id": new_user_id})

    transaction.commit()
    connection.close()
