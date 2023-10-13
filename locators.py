from selenium.webdriver.common.by import By


class Locators:

    # Шапка страницы
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]')  # Кнопка перехода к конструктору в шапке
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//a[@href=\"/account\"]//p')  # Кнопка перехода в личный кабинет

    # Личный кабинет
    LOGOUT_PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//button[text()="Выход"]')  # Кнопка "Выход"

    # Конструктор
    BUN_CHAPTER_BUTTON = (By.XPATH, '//span[text()="Булки"]/parent::div')  # Кнопка переключения раздела конструктора "Булки"
    SAUCE_CHAPTER_BUTTON = (By.XPATH, '//span[text()="Соусы"]/parent::div')  # Кнопка переключения раздела конструктора "Соусы"
    FILLING_CHAPTER_BUTTON = (By.XPATH, '//span[text()="Начинки"]/parent::div')  # Кнопка переключения раздела конструктора "Начинки"

    # Главная страница
    LOGIN_MAIN_PAGE_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # Кнопка "Войти в аккаунт"
    MAKE_ORDER_MAIN_PAGE_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')  # Кнопка "Оформить заказ"

    # Страница регистрации
    REGISTRATION_BUTTON = (By.XPATH, '//form//button')  # Кнопка регистрации
    LOGIN_LINK_REGISTRATION_PAGE = (By.XPATH, '//a[@href="/login"]')  # Ссылка перехода на страницу логина
    REGISTRATION_TITLE = (By.XPATH, '//h2[text()="Регистрация"]')  # Заголовок формы регистрации
    USER_ALREADY_EXIST_VALIDATION_ERROR = (By.XPATH, '//p[text()="Такой пользователь уже существует"]')  # Ошибка валидации "Такой пользователь уже существует"

    # Страница логина
    REGISTRATION_LINK_LOGIN_PAGE = (By.XPATH, '//a[@href="/register"]')  # Ссылка перехода на страницу регистрации
    ENTER_BUTTON = (By.XPATH, '//button[text()="Войти"]')  # Кнопка логина
    RESTORE_PASSWORD_LOGIN_PAGE = (By.XPATH, '//a[@href="/forgot-password"]')  # Ссылка перехода на страницу восстановления пароля

    # Страница восстановления пароля
    LOGIN_LINK_RESTORE_PASSWORD_PAGE = (By.XPATH, '//a[@href="/login"]')  # Ссылка перехода на страницу логина

    # Поля ввода логин \ регистрация
    INPUT_NAME = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')  # Поле ввода имени
    INPUT_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # Поле ввода email
    INPUT_PASSWORD = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')  # Поле ввода пароля
