
class ConstantsAuth:
    # Стандартный логин*пароль для большинства тестов
    EMAIL = 'boris_bulgakov_1@gmail.com'
    PASSWORD = 'password'

    # Комбанации валидных данных для регистрации
    NAME_VAL_1 = 'борис'
    NAME_VAL_2 = 'BORIS'
    NAME_VAL_3 = 'Имя1'
    NAME_VAL_4 = 'Name1'
    NAME_VAL_5 = 'Борис Borisov#$% Borisovich11'

    EMAIL_VAL_1 = 'тест@ътест.som'
    EMAIL_VAL_2 = 'TEST@XTEST.som'
    EMAIL_VAL_3 = 'тестов@ътест.som'
    EMAIL_VAL_4 = 'login@XDOMEN.som'
    EMAIL_VAL_5 = 'грязнаяDUCK@ъсидойRICK.som'
    EMAIL_VAL_NOT_USED = 'notUsedEmail6667771111@notUsed.som'

    PASSWORD_VAL_1 = 'пароль'
    PASSWORD_VAL_2 = 'PASSWORD'
    PASSWORD_VAL_3 = '1234567890'
    PASSWORD_VAL_4 = '!@#$%^&*()_+'
    PASSWORD_VAL_5 = 'Пароль Password 123456 !@#$%^&*()'

    # Комбинации не валидных данных для регистрации
    NAME_NOT_VAL_1 = ''

    EMAIL_NOT_VAL_1 = ''
    EMAIL_NOT_VAL_2 = 'notFormatEmail.slon'

    PASSWORD_NOT_VAL_1 = ''
    PASSWORD_NOT_VAL_2 = '5symb'

class ConstantsLinks:
    REGISTER_PAGE_LINK = 'https://stellarburgers.nomoreparties.site/register'
    LOGIN_PAGE_LINK = 'https://stellarburgers.nomoreparties.site/login'
    MAIN_PAGE_LINK = 'https://stellarburgers.nomoreparties.site'


