1 REST API должна предоставить возможность ведения блога.
2 Сущности
    1 пользователь  - User
    2 пост - Msg
        2.1 комментарий к посту - comMsg
Пользователь должен иметь возможность:
а - создать ('POST')' -ok,
    прочитать ('GET') - ok,
    изменить ('PUT') -
    удалить пост ('DELETE') - .

б - получить список всех постов  - ok
в - Добавить и удалить комментарий к посту