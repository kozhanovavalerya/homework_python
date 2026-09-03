from sqlalchemy import create_engine
from sqlalchemy import text

db_connection_string = "postgresql://postgres:6745@localhost:5432/QA homework"
db = create_engine(db_connection_string)


def test_add_user():
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

    check_table = text("""
    SELECT user_id
    FROM users
    WHERE user_id = :new_user_id""")

    result = connection.execute(
        check_table, {"new_user_id": new_user_id})

    user = result.fetchone()
    assert user is not None

    delete_sql = text("""
    DELETE from users
    WHERE user_id = :new_user_id""")

    connection.execute(delete_sql, {"new_user_id": new_user_id})

    transaction.commit()
    connection.close()
