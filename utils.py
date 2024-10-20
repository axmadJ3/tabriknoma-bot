
words = {
    'lang-uz': "Assalomu alaykum, tilni tanlang 👇",
    'welcome-uz': "Assalomu alaykum, xush kelibsiz!",
    'welcome-ru': "Здравствуйте, добро пожаловать!",
    'name-uz': "Ismingizni kiriting: ",
    'name-ru': "Введите свое имя: ",
    'phone-uz': "Telefon raqamingizni kiriting: ",
    'phone-ru': "Введите свой номер телефона: ",
    'company-uz': "Siz ishlayotgan kompaniya yoki tashkilot nomi: ",
    'company-ru': "Название компании или организации, в которой вы работаете: ",
    'skip-uz': "O'tkazib yuborish",
    'skip-ru': "Пропустить",
    'registered-uz': "Siz muvaffaqiyatli ro'yxatdan o'tdingiz",
    'registered-ru': "Вы успешно зарегистрировались",
    "tabriknomalar-uz": "Tabriknomalar",
    "tabriknomalar-ru": "Открытки",
    "devor-uz": "Devor uchun",
    "devor-ru": "Для стены",
    "bayram-uz": "Bayramlar",
    "bayram-ru": "Праздники",
    "toy-uz": "To'y",
    "toy-ru": "Свадьба",
    "yubiley-uz": "Yubiley",
    "yubiley-ru": "Юбилейный",
    "tugilgan-uz": "Tug'ilgan kun",
    "tugilgan-ru": "День рождения",
    "choose-event-uz": "Qanday tadbir uchun?",
    "choose-event-ru": "На какое мероприятие?",
}


async def get_word(key, lang = 'uz'):
    word = words.get(key+ '-' + lang)
    return word
