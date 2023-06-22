# ---------------------------------------------------------------------------


import telebot

from telebot import types

# ---------------------------------------------------------------------------


bot = telebot.TeleBot(TOKEN = "YOUR_TELEGRAM_BOT_TOKEN")


@bot.message_handler(commands=['start'])
# ---------------------------------------------------------------------------

def welcome(message):


    # keyboard (Создание кнопок и приветствие)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Информация о боте 📄")
    item2 = types.KeyboardButton("Информация о учебном заведение 🏫")
    item3 = types.KeyboardButton("Настройки ⚙️")
    item4 = types.KeyboardButton("Расписание 📑")
    item5 = types.KeyboardButton("Преподаватели 🧑🏻‍🏫")
    item6 = types.KeyboardButton("Студент 🎓")
    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id,
                     f"Добро пожаловать😊! \nЯ буду твоим помощником в планировании расписания📄. С помощью меня ты сможешь быстро просматривать расписание на любой день 📑 недели - сегодня, завтра и так далее"
                     .format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
# ---------------------------------------------------------------------------

def choice(message):
    if message.chat.type == 'private':
        if message.text == 'Расписание 📑':

            # keyboard (Создание кнопок под текстом)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("101", callback_data='raspMon101')
            item2 = types.InlineKeyboardButton("102", callback_data='raspMon102')
            item3 = types.InlineKeyboardButton("103", callback_data='raspMon103')
            item4 = types.InlineKeyboardButton("201", callback_data='raspMon201')
            item5 = types.InlineKeyboardButton("202", callback_data='raspMon202')
            item6 = types.InlineKeyboardButton("203", callback_data='raspMon203')
            item7 = types.InlineKeyboardButton("301", callback_data='raspMon301')
            item8 = types.InlineKeyboardButton("302", callback_data='raspMon302')
            item9 = types.InlineKeyboardButton("303", callback_data='raspMon303')
            item10 = types.InlineKeyboardButton("401", callback_data='raspMon401')
            item11 = types.InlineKeyboardButton("402", callback_data='raspMon402')
            item12 = types.InlineKeyboardButton("403", callback_data='raspMon403')
            itemBACK = types.InlineKeyboardButton("Отмена", callback_data='Отмена')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, itemBACK)

            bot.send_message(message.chat.id, 'Расписание – Здесь будет твоё персональное расписание 📑, которые выложила твоя учебная часть!', reply_markup=markup)

        # elif message.text == ' '
        elif message.text == 'Информация о боте 📄':
            bot.send_message(message.chat.id, f"Этот бот представляет функционал расписание⏰, а также помогает в учебном процессе студентам👨‍🎓 и преподавателям🧑‍🏫. Основные особенности бота, которые могут выполнять следующие функции:" +
                             "\n 1. 📑Показывать расписание на сегодня, завтра и другие дни недели;" +
                             "\n 2. 🔨Предлагать изменения в расписании (например, переносить занятия на другое время);"+
                             "\n 3. 🧑‍🏫Отображать информацию о преподавателях и аудиториях;"+
                             "\n 4. ❔Отвечать на вопросы студентов о расписании, занятиях, и т.д.;", parse_mode='html')

        elif message.text == 'Информация о учебном заведение 🏫':
            bot.send_message(message.chat.id,
                             f'🏫Алматинский финансово-экономический колледж — это учебное заведение, расположенное в городе Алматы, Казахстан. Основные контакты для связи, с учебным заведением:'+
                             f'\n👨🏻‍🏫 Деканат: \n 1. +7 727 309 74 00 \n 2. +7 747 146 57 00 \n Приемная комиссия: 309 64 33 \n E-mail: kolledzh_fek@mail.ru \n Адрес: Рыскулбекова 39а, город Алматы, Республика Казахстан',
                             parse_mode='html')
        elif message.text == 'Настройки ⚙️':
            sett = types.InlineKeyboardMarkup(row_width=2)
            set1 = types.InlineKeyboardButton('Убрать эмодзи', callback_data='no_emodzi')
            set2 = types.InlineKeyboardButton('Жирный шрифт', callback_data='Zhirnii')
            sett.add(set1,set2)
            bot.send_message(message.chat.id, "Здравствуй🤓, здесь происходит моя основная настройка⚙️!", parse_mode='html', reply_markup=sett)

        elif message.text == 'Преподаватели 🧑🏻‍🏫':
            prep = types.InlineKeyboardMarkup(row_width=2)
            prep1= types.InlineKeyboardButton('Касенова Айжан', callback_data='210')
            prep2 = types.InlineKeyboardButton('Смирнов Сергей', callback_data='105')
            prep3 = types.InlineKeyboardButton ('Русланова Рамина', callback_data= '230')
            prep4 = types.InlineKeyboardButton ('Ильясова Мейрамгуль', callback_data='111')
            prep5 = types.InlineKeyboardButton ('Аятов Жандос', callback_data='132')
            prep6 = types.InlineKeyboardButton ('Крусп Едвард', callback_data='58')
            prep7 = types.InlineKeyboardButton ('Устинов Максим', callback_data='69')
            prep8 = types.InlineKeyboardButton ('Моисова Татьяна', callback_data='178')
            prep9 = types.InlineKeyboardButton ('Тихая Валентина', callback_data='51')
            prep10=types.InlineKeyboardButton ('Романов Илья', callback_data='21')
            prep11 = types.InlineKeyboardButton ('Воробьёв Иван', callback_data='11')
            prep12 = types.InlineKeyboardButton ('Пахтинова Варвара', callback_data='32')
            prep13 = types.InlineKeyboardButton ('Данияров Аскар', callback_data='271')
            prep14 = types.InlineKeyboardButton ('Болатов Елдос', callback_data='199')
            prep15 = types.InlineKeyboardButton ('Серикова Айнура', callback_data='205')
            prep16 = types.InlineKeyboardButton ('Фоменко Артур', callback_data='106')
            prep17 = types.InlineKeyboardButton ('Нурболатов Нурлан', callback_data='201')
            prep18 = types.InlineKeyboardButton ('Ахметжанова Абзал', callback_data='189')
            prep19 = types.InlineKeyboardButton ('Искандеров Асылхан', callback_data= '198')
            prep20 = types.InlineKeyboardButton ('Ходжанова Айгуль', callback_data= '207')
            prep.add(prep1, prep2, prep3, prep4, prep5, prep6, prep7, prep8, prep9, prep10, prep11, prep12, prep13, prep14, prep15, prep16, prep17, prep18, prep19, prep20)
            bot.send_message(message.chat.id, 'Здравствуйте🧑🏻‍🎓, здесь будет ваше расписание, для вашего учебного процесса👩🏻‍🏫. Здесь представлено: предмет, номер аудитории!', parse_mode='html', reply_markup=prep)
        elif message.text == 'Студент 🎓':
            #создадим направления
            pinup = types.InlineKeyboardMarkup(row_width=2)
            pin1 = types.InlineKeyboardButton("Маркетинг", callback_data='market')
            pin2 = types.InlineKeyboardButton("Туризм", callback_data='tourism')
            pin3 = types.InlineKeyboardButton("Информационные системы", callback_data='infosys')
            pinup.add(pin1, pin2, pin3)

            bot.send_message(message.chat.id, 'Привет🧑🏻‍💻, этот пункт для тебя, здесь будет информация об учебном заведение🏫, расписание лекций и событий📅, контактную информацию преподавателей и администрации🧑🏻‍🏫, а также контактные данные колледжа.', parse_mode='html')
            bot.send_message(message.chat.id, 'Выбери направление на котором ты учишься', reply_markup=pinup)



        elif message.text == 'Информация о боте':
            bot.send_message(message.chat.id,
                             f"Этот бот представляет функционал расписание, а также помогает в учебном процессе студентам и преподавателям. Основные особенности бота, которые могут выполнять следующие функции:" +
                             "\n 1. Показывать расписание на сегодня, завтра и другие дни недели;" +
                             "\n 2. Предлагать изменения в расписании (например, переносить занятия на другое время);" +
                             "\n 3. Отображать информацию о преподавателях и аудиториях;" +
                             "\n 4. Отвечать на вопросы студентов о расписании, занятиях, и т.д.;", parse_mode='html')
        elif message.text == 'Информация о учебном заведение':
            bot.send_message(message.chat.id, 'Здравствуйте, здесь будет ваше расписание, для вашего учебного процесса. Здесь представлено: номер группы, предмет, номер аудитория, время проводимого занятия.', parse_mode='html')

        elif message.text == 'Преподаватели':
            prep = types.InlineKeyboardMarkup(row_width=2)
            prep1 = types.InlineKeyboardButton('Касенова Айжан', callback_data='210*')
            prep2 = types.InlineKeyboardButton('Смирнов Сергей', callback_data='105*')
            prep3 = types.InlineKeyboardButton('Русланова Рамина', callback_data='230*')
            prep4 = types.InlineKeyboardButton('Ильясова Мейрамгуль', callback_data='111*')
            prep5 = types.InlineKeyboardButton('Аятов Жандос', callback_data='132*')
            prep6 = types.InlineKeyboardButton('Крусп Едвард', callback_data='58*')
            prep7 = types.InlineKeyboardButton('Устинов Максим', callback_data='69*')
            prep8 = types.InlineKeyboardButton('Моисова Татьяна', callback_data='178*')
            prep9 = types.InlineKeyboardButton('Тихая Валентина', callback_data='51*')
            prep10 = types.InlineKeyboardButton('Романов Илья', callback_data='21*')
            prep11 = types.InlineKeyboardButton('Воробьёв Иван', callback_data='11*')
            prep12 = types.InlineKeyboardButton('Пахтинова Варвара', callback_data='32*')
            prep13 = types.InlineKeyboardButton('Данияров Аскар', callback_data='271*')
            prep14 = types.InlineKeyboardButton('Болатов Елдос', callback_data='199*')
            prep15 = types.InlineKeyboardButton('Серикова Айнура', callback_data='205*')
            prep16 = types.InlineKeyboardButton('Фоменко Артур', callback_data='106*')
            prep17 = types.InlineKeyboardButton('Нурболатов Нурлан', callback_data='201*')
            prep18 = types.InlineKeyboardButton('Ахметжанова Абзал', callback_data='189*')
            prep19 = types.InlineKeyboardButton('Искандеров Асылхан', callback_data='198*')
            prep20 = types.InlineKeyboardButton('Ходжанова Айгуль', callback_data='207*')
            prep.add(prep1, prep2, prep3, prep4, prep5, prep6, prep7, prep8, prep9, prep10, prep11,
                     prep12, prep13, prep14, prep15, prep16, prep17, prep18, prep19, prep20)
            bot.send_message(message.chat.id, 'Здравствуйте, здесь будет ваше расписание, для вашего учебного процесса. Здесь представлено: предмет, номер аудитория!', parse_mode='html', reply_markup=prep)
        elif message.text == 'Студент':
            #создадим направления
            pinup = types.InlineKeyboardMarkup(row_width=2)
            pin1 = types.InlineKeyboardButton("Маркетинг", callback_data='market*')
            pin2 = types.InlineKeyboardButton("Туризм", callback_data='tourism*')
            pin3 = types.InlineKeyboardButton("Информационные системы", callback_data='infosys*')
            pinup.add(pin1, pin2, pin3)

            bot.send_message(message.chat.id, 'Привет, этот пункт для тебя, здесь будет информация об учебном заведение, расписание лекций и событий, контактную информацию преподавателей и администрации‍, а также контактные данные колледжа.', parse_mode='html')
            bot.send_message(message.chat.id, 'Выбери направление на котором ты учишься', reply_markup=pinup)
        elif message.text == 'Настройки':
            sett = types.InlineKeyboardMarkup(row_width=2)
            set1 = types.InlineKeyboardButton('Вернуть эмодзи', callback_data='emodzi')
            set2 = types.InlineKeyboardButton('Жирный шрифт', callback_data='Zhirnii')
            sett.add(set1,set2)
            bot.send_message(message.chat.id, "Здравствуй, здесь происходит моя основная настройка!", parse_mode='html', reply_markup=sett)
        if message.text == 'Расписание':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("101", callback_data='raspMon101*')
            item2 = types.InlineKeyboardButton("102", callback_data='raspMon102*')
            item3 = types.InlineKeyboardButton("103", callback_data='raspMon103*')
            item4 = types.InlineKeyboardButton("201", callback_data='raspMon201*')
            item5 = types.InlineKeyboardButton("202", callback_data='raspMon202*')
            item6 = types.InlineKeyboardButton("203", callback_data='raspMon203*')
            item7 = types.InlineKeyboardButton("301", callback_data='raspMon301*')
            item8 = types.InlineKeyboardButton("302", callback_data='raspMon302*')
            item9 = types.InlineKeyboardButton("303", callback_data='raspMon303*')
            item10 = types.InlineKeyboardButton("401", callback_data='raspMon401*')
            item11 = types.InlineKeyboardButton("402", callback_data='raspMon402*')
            item12 = types.InlineKeyboardButton("403", callback_data='raspMon403*')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)

            bot.send_message(message.chat.id, f'Расписание – Здесь будет твоё персональное расписание, которые выложила твоя учебная часть!', parse_mode='html',reply_markup=markup)


        if message.text == 'Рaсписание 📑':

            # keyboard (Создание кнопок под текстом)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("101", callback_data='raspMon101//')
            item2 = types.InlineKeyboardButton("102", callback_data='raspMon102//')
            item3 = types.InlineKeyboardButton("103", callback_data='raspMon103//')
            item4 = types.InlineKeyboardButton("201", callback_data='raspMon201//')
            item5 = types.InlineKeyboardButton("202", callback_data='raspMon202//')
            item6 = types.InlineKeyboardButton("203", callback_data='raspMon203//')
            item7 = types.InlineKeyboardButton("301", callback_data='raspMon301//')
            item8 = types.InlineKeyboardButton("302", callback_data='raspMon302//')
            item9 = types.InlineKeyboardButton("303", callback_data='raspMon303//')
            item10 = types.InlineKeyboardButton("401", callback_data='raspMon401//')
            item11 = types.InlineKeyboardButton("402", callback_data='raspMon402//')
            item12 = types.InlineKeyboardButton("403", callback_data='raspMon403//')
            itemBACK = types.InlineKeyboardButton("Отмена", callback_data='Отмена')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, itemBACK)

            bot.send_message(message.chat.id, f'<b>Расписание – Здесь будет твоё персональное расписание 📑, которые выложила твоя учебная часть!</b>', parse_mode='html',reply_markup=markup)

        # elif message.text == ' '
        elif message.text == 'Информация o боте 📄':
            bot.send_message(message.chat.id, f"<b>Этот бот представляет функционал расписание⏰, а также помогает в учебном процессе студентам👨‍🎓 и преподавателям🧑‍🏫. Основные особенности бота, которые могут выполнять следующие функции:</b>" +
                             f"<b>\n 1. 📑Показывать расписание на сегодня, завтра и другие дни недели;</b>" +
                             f"<b>\n 2. 🔨Предлагать изменения в расписании (например, переносить занятия на другое время);</b>"+
                             f"<b>\n 3. 🧑‍🏫Отображать информацию о преподавателях и аудиториях;</b>"+
                             f"<b>\n 4. ❔Отвечать на вопросы студентов о расписании, занятиях, и т.д.;</b>", parse_mode='html')

        elif message.text == 'Информация o учебном заведение 🏫':
            bot.send_message(message.chat.id,
                             f'<b>🏫Алматинский финансово-экономический колледж — это учебное заведение, расположенное в городе Алматы, Казахстан. Основные контакты для связи, с учебным заведением:</b>'+
                             f'<b>\n👨🏻‍🏫 Деканат: \n 1. +7 727 309 74 00 \n 2. +7 747 146 57 00 \n Приемная комиссия: 309 64 33 \n E-mail: kolledzh_fek@mail.ru \n Адрес: Рыскулбекова 39а, город Алматы, Республика Казахстан</b>',
                             parse_mode='html')
        elif message.text == 'Нaстройки ⚙️':
            sett = types.InlineKeyboardMarkup(row_width=2)
            set1 = types.InlineKeyboardButton('Убрать эмодзи', callback_data='no_emodzi')
            set2 = types.InlineKeyboardButton('Выключить жирный шрифт', callback_data='Zhirniioff')
            sett.add(set1,set2)
            bot.send_message(message.chat.id, f"<b>Здравствуй🤓, здесь происходит моя основная настройка⚙️!</b>", parse_mode='html', reply_markup=sett)

        elif message.text == 'Препoдаватели 🧑🏻‍🏫':
            prep = types.InlineKeyboardMarkup(row_width=2)
            prep1 = types.InlineKeyboardButton('Касенова Айжан', callback_data='210//')
            prep2 = types.InlineKeyboardButton('Смирнов Сергей', callback_data='105//')
            prep3 = types.InlineKeyboardButton('Русланова Рамина', callback_data='230//')
            prep4 = types.InlineKeyboardButton('Ильясова Мейрамгуль', callback_data='111//')
            prep5 = types.InlineKeyboardButton('Аятов Жандос', callback_data='132//')
            prep6 = types.InlineKeyboardButton('Крусп Едвард', callback_data='58//')
            prep7 = types.InlineKeyboardButton('Устинов Максим', callback_data='69//')
            prep8 = types.InlineKeyboardButton('Моисова Татьяна', callback_data='178//')
            prep9 = types.InlineKeyboardButton('Тихая Валентина', callback_data='51//')
            prep10 = types.InlineKeyboardButton('Романов Илья', callback_data='21//')
            prep11 = types.InlineKeyboardButton('Воробьёв Иван', callback_data='11//')
            prep12 = types.InlineKeyboardButton('Пахтинова Варвара', callback_data='32//')
            prep13 = types.InlineKeyboardButton('Данияров Аскар', callback_data='271//')
            prep14 = types.InlineKeyboardButton('Болатов Елдос', callback_data='199//')
            prep15 = types.InlineKeyboardButton('Серикова Айнура', callback_data='205//')
            prep16 = types.InlineKeyboardButton('Фоменко Артур', callback_data='106//')
            prep17 = types.InlineKeyboardButton('Нурболатов Нурлан', callback_data='201//')
            prep18 = types.InlineKeyboardButton('Ахметжанова Абзал', callback_data='189//')
            prep19 = types.InlineKeyboardButton('Искандеров Асылхан', callback_data='198//')
            prep20 = types.InlineKeyboardButton('Ходжанова Айгуль', callback_data='207//')
            prep.add(prep1, prep2, prep3, prep4, prep5, prep6, prep7, prep8, prep9, prep10, prep11,
                     prep12, prep13, prep14, prep15, prep16, prep17, prep18, prep19, prep20)

            bot.send_message(message.chat.id, f'<b>Здравствуйте🧑🏻‍🎓, здесь будет ваше расписание, для вашего учебного процесса👩🏻‍🏫. Здесь представлено: предмет, номер аудитория!</b>', parse_mode='html', reply_markup=prep)
        elif message.text == 'Студeнт 🎓':
            #создадим направления
            pinup = types.InlineKeyboardMarkup(row_width=2)
            pin1 = types.InlineKeyboardButton("Маркетинг", callback_data='market//')
            pin2 = types.InlineKeyboardButton("Туризм", callback_data='tourism//')
            pin3 = types.InlineKeyboardButton("Информационные системы", callback_data='infosys//')
            pinup.add(pin1, pin2, pin3)

            bot.send_message(message.chat.id, f'<b>Привет🧑🏻‍💻, этот пункт для тебя, здесь будет информация об учебном заведение🏫, расписание лекций и событий📅, контактную информацию преподавателей и администрации🧑🏻‍🏫, а также контактные данные колледжа.</b>', parse_mode='html')
            bot.send_message(message.chat.id, f'<b>Выбери направление на котором ты учишься</b>', parse_mode='html', reply_markup=pinup)


















#---------------------------------------------------------------------------


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:

            # keyboard (Работа с кнопками под текстом)
#-----------------------------------------------------------
            if call.data =='tourism':
                        tour = types.InlineKeyboardMarkup(row_width=2)
                        tour1 = types.InlineKeyboardButton("1 курс", callback_data='T1')
                        tour2 = types.InlineKeyboardButton("2 курс", callback_data='T2')
                        tour3 = types.InlineKeyboardButton("3 курс", callback_data='T3')
                        tour4 = types.InlineKeyboardButton("4 курс", callback_data='T4')

                        tour.add(tour1, tour2, tour3, tour4)
                        bot.send_message(call.message.chat.id,"На каком курсе вы учитесь?",parse_mode='html', reply_markup=tour)

#-----------------------------------------------------------
            if call.data == 'T1':
                rasp102 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник",callback_data='raspMon102')
                raspTue = types.InlineKeyboardButton("Вторник",callback_data='raspTue102')
                raspWed = types.InlineKeyboardButton("Среда",callback_data='raspWed102')
                raspThu = types.InlineKeyboardButton("Четверг",callback_data='raspThu102')
                raspFri = types.InlineKeyboardButton("Пятница",callback_data='raspFri102')
                rasp102.add(raspMon, raspTue, raspWed, raspThu,raspFri)
                bot.send_message(call.message.chat.id,"Выбирай день недели и я отправлю тебе расписание!", parse_mode='html', reply_markup= rasp102)
            if call.data == 'raspMon102':
                rasp102 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon102')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue102')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed102')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu102')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri102')
                rasp102.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,f"📅Понедельник: \n🕒8:00 - 9:30 – Программирования операционных систем \n🕒9:40 - 11:10 - Немецкий язык \n🕒11:30 - 13:00 - Английский язык", parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp102)
            if call.data == 'raspTue102':
                rasp102 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon102')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue102')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed102')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu102')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri102')
                rasp102.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Вторник: \n🕒 8:00 - 9:30 - Программирования операционных систем \n🕒 9:40 - 11:10 - Администрирование информационных систем \n🕒 11:30 - 13:00 - Дизайн для крупного бизнеса",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp102)
            if call.data == 'raspWed102':
                rasp102 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon102')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue102')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed102')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu102')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri102')
                rasp102.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,f"📅Среда: \n🕒 8:00 - 9:30 - Высшая математика \n🕒 9:40 - 11:10 - Основы алгоритмов и программирования \n🕒 11:30 - 13:00 - Бухгалтерский учёт",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp102)
            if call.data == 'raspThu102':
                rasp102 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon102')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue102')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed102')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu102')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri102')
                rasp102.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,f"📅Четверг: \n🕒 8:00 - 9:30 – Микроэкономика \n🕒 9:40 - 11:10 – Макроэкономика \n🕒 11:30 - 13:00 - Логистика и построение маршрутов",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp102)
            if call.data == 'raspFri102':
                rasp102 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon102')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue102')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed102')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu102')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri102')
                rasp102.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,"📅Пятница: \n🕒 8:00 - 9:30 - Профессиональный казахский язык \n🕒 9:40 - 11:10 - Казахский язык \n🕒 11:30 - 13:00 - Профессиональный английский язык",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp102)

#----------------------------------------------------------
            if call.data == 'T2':
                rasp202 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon202')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue202')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed202')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu202')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri202')
                rasp202.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp202)
            if call.data == 'raspMon202':
                rasp202 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon202')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue202')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed202')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu202')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri202')
                rasp202.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Понедельник: \n🕒 8:00-9:30 – Казахский язык \n🕒 9:40-11:10 - Администрирование информационных систем \n🕒 11:30-13:00 - Менеджмент в маркетинге",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp202)
            if call.data == 'raspTue202':
                rasp202 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon202')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue202')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed202')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu202')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri202')
                rasp202.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Вторник: \n🕒 8:00-9:30 - Логистика и построение маршрутов \n🕒 9:40-11:10 - Дизайн для крупного бизнеса \n🕒 11:30-13:00 - Основы алгоритмов и программирования",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp202)
            if call.data == 'raspWed202':
                    rasp202 = types.InlineKeyboardMarkup(row_width=2)
                    raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon202')
                    raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue202')
                    raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed202')
                    raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu202')
                    raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri202')
                    rasp202.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                    bot.send_message(call.message.chat.id,
                                     f"📅Среда: \n🕒 8:00-9:30 - Макроэкономика \n🕒 9:40-11:10 - Программирования операционных систем \n🕒 11:30-13:00 - Философия древнего Рима",
                                     parse_mode='html')
                    bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                     parse_mode='html', reply_markup=rasp202)
            if call.data == 'raspThu202':
                    rasp202 = types.InlineKeyboardMarkup(row_width=2)
                    raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon202')
                    raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue202')
                    raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed202')
                    raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu202')
                    raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri202')
                    rasp202.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                    bot.send_message(call.message.chat.id,
                                     f"📅Четверг: \n🕒 8:00-9:30 - Профессиональный английский язык \n🕒 9:40-11:10 – Микроэкономика \n🕒 11:30-13:00 - Дизайн логотипов в крупных компаниях",
                                     parse_mode='html')
                    bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                     parse_mode='html', reply_markup=rasp202)
            if call.data == 'raspFri202':
                    rasp202 = types.InlineKeyboardMarkup(row_width=2)
                    raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon202')
                    raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue202')
                    raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed202')
                    raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu202')
                    raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri202')
                    rasp202.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                    bot.send_message(call.message.chat.id,
                                     f"📅Пятница: \n🕒 8:00-9:30 - Высшая математика \n🕒 9:40-11:10 - Немецкий язык \🕒 11:30-13:00 - Бухгалтерский учет",
                                     parse_mode='html')
                    bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                     parse_mode='html', reply_markup=rasp202)

#-------------------------------------------------------------
            if call.data == 'T3':
                rasp302 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon302')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue302')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed302')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu302')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri302')
                rasp302.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp302)
            if call.data == 'raspMon302':
                rasp302 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon302')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue302')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed302')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu302')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri302')
                rasp302.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Понедельник: \n🕒 8:00-9:30 - Профессиональный казахский язык \n🕒 9:40-11:10 – Макроэкономика \n🕒 11:30-13:00 - Программирования микроконтроллеров",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp302)
            if call.data == 'raspTue302':
                rasp302 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon302')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue302')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed302')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu302')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri302')
                rasp302.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Вторник: \n🕒 8:00-9:30 - Английский язык \n🕒 9:40-11:10 - Дизайн логотипов в крупных компаниях \n🕒 11:30-13:00 - Логистика в сфере туризма",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp302)
            if call.data == 'raspWed302':
                rasp302 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon302')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue302')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed302')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu302')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri302')
                rasp302.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Среда: \n🕒 8:00-9:30 - Менеджмент в маркетинге \n🕒 9:40-11:10 - Основы алгоритмов и программирования \n🕒 11:30-13:00 - Профессиональный английский язык",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp302)
            if call.data == 'raspThu302':
                rasp302 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon302')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue302')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed302')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu302')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri302')
                rasp302.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Четверг: \n🕒 8:00-9:30 - Немецкий язык \n🕒 9:40-11:10 - Дизайн для крупного бизнеса \n🕒 11:30-13:00 - Администрирование информационных систем",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе Трасписание!",
                                 parse_mode='html', reply_markup=rasp302)
            if call.data == 'raspFri302':
                rasp302 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon302')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue302')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed302')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu302')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri302')
                rasp302.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Пятница: \n🕒 8:00-9:30 - Французский язык \n🕒 9:40-11:10 - Высшая математика \n🕒 11:30-13:00 - Бухгалтерский учёт",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp302)

#-------------------------------------------------------------
            if call.data == 'T4':
                rasp402 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon402')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue402')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed402')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu402')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri402')
                rasp402.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp402)
            if call.data == 'raspMon402':
                rasp402 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon402')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue402')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed402')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu402')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri402')
                rasp402.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Понедельник: \n🕒 8:00 - 9:30: Философия древнего Рима \n🕒 9:40 - 11:10: Основы алгоритмов и программирования \n🕒 11:30 - 13:00: Профессиональный английский язык",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp402)
            if call.data == 'raspTue402':
                rasp402 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon402')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue402')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed402')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu402')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri402')
                rasp402.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Вторник: \n🕒 8:00 - 9:30: Микроэкономика \n🕒 9:40 - 11:10: Английский язык \n🕒 11:30 - 13:00: Логистика и построение маршрутов",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp402)
            if call.data == 'raspWed402':
                rasp402 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon402')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue402')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed402')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu402')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri402')
                rasp402.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Среда: \n🕒 8:00 - 9:30: Высшая математика \n🕒 9:40 - 11:10: Немецкий язык \n🕒 11:30 - 13:00: Бухгалтерский учёт",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp402)
            if call.data == 'raspThu402':
                rasp402 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon402')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue402')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed402')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu402')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri402')
                rasp402.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Четверг: \n🕒 8:00 - 9:30: Программирование микроконтроллеров \n🕒 9:40 - 11:10: Профессиональный казахский язык \n🕒 11:30 - 13:00: Менеджмент в маркетинге",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp402)
            if call.data == 'raspFri402':
                rasp402 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon402')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue402')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed402')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu402')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri402')
                rasp402.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Пятница: \n🕒 8:00 - 9:30: Макроэкономика \n🕒 9:40 - 11:10: Французский язык \n🕒 11:30 - 13:00: Дизайн логотипов в крупных компаниях",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp402)

#-------------------------------------------------------------
            if call.data == 'market':
                market = types.InlineKeyboardMarkup(row_width=2)
                market1 = types.InlineKeyboardButton("1 курс", callback_data='M1')
                market2 = types.InlineKeyboardButton("2 курс", callback_data='M2')
                market3 = types.InlineKeyboardButton("3 курс", callback_data='M3')
                market4 = types.InlineKeyboardButton("4 курс", callback_data='M4')

                market.add(market1, market2, market3, market4)
                bot.send_message(call.message.chat.id, "На каком курсе вы учитесь?", parse_mode='html',
                                     reply_markup=market)

#-------------------------------------------------------------
            if call.data == 'M1':
                rasp101 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon101')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue101')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed101')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu101')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri101')
                rasp101.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp101)
            if call.data == 'raspMon101':
                rasp101 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon101')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue101')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed101')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu101')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri101')
                rasp101.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Понедельник: \n🕒 8:00 - 9:30 - Высшая математика \n🕒 9:40 - 11:10 - Основы алгоритмов и программирования \n🕒 11:30 - 13:00 - Микроэкономика",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                     parse_mode='html', reply_markup=rasp101)
            if call.data == 'raspTue101':
                rasp101 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon101')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue101')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed101')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu101')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri101')
                rasp101.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Вторник: \n🕒 8:00- 9:30 - Логистика в сфере туризма \n🕒 9:40- 11:10 – Макроэкономика \n🕒 11:30 - 13:00 - Философия древнего Рима",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp101)
            if call.data == 'raspWed101':
                rasp101 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon101')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue101')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed101')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu101')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri101')
                rasp101.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Среда: \n🕒 9:00-11:00 - Французский язык \n🕒 9:40 - 11:10 - Немецкий язык \n🕒 11:30 - 13:00 - Английский язык",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp101)
            if call.data == 'raspThu101':
                rasp101 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon101')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue101')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed101')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu101')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri101')
                rasp101.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Четверг: \n🕒 8:00 - 9:30 - Профессиональный казахский язык \n🕒 9:40 - 11:10 - Казахский язык \n🕒 11:30 - 13:00 - Профессиональный английский язык",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp101)
            if call.data == 'raspFri101':
                rasp101 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon101')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue101')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed101')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu101')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri101')
                rasp101.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Пятница: \n🕒 8:00 - 9:30 - Программирования микроконтроллеров \n🕒 9:40 - 11:10 - Менеджмент в маркетинге \n🕒 11:30 - 13:00 - Дизайн логотипов в крупных компаниях",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp101)

#--------------------------------------------------------------
            if call.data == 'M2':
                rasp201 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon201')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue201')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed201')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu201')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri201')
                rasp201.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp201)

            if call.data == 'raspMon201':
                rasp201 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon201')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue201')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed201')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu201')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri201')
                rasp201.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Понедельник: \n🕒 8:00-9:30 - Основы алгоритмов и программирования \n🕒 9:40-11:10 - Логистика в сфере туризма \n🕒 11:30-13:00 - Философия древнего Рима",
                               parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp201)
            if call.data == 'raspTue201':
                rasp201 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon201')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue201')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed201')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu201')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri201')
                rasp201.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Вторник: \n🕒 8:00-9:30 - Профессиональный казахский язык \n🕒 9:40-11:10 – Макроэкономика \n🕒 11:30-13:00 - Программирования операционных систем",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp201)
            if call.data == 'raspWed201':
                rasp201 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon201')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue201')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed201')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu201')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri201')
                rasp201.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                f"📅Среда: \n🕒 8:00-9:30 - Менеджмент в маркетинге \n🕒 9:40-11:10 - Дизайн логотипов в крупных компаниях \n🕒 11:30-13:00 - Логистика и построение маршрутов",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp201)
            if call.data == 'raspThu201':
                rasp201 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon201')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue201')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed201')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu201')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri201')
                rasp201.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Четверг: \n🕒 8:00-9:30 - Высшая математика \n🕒 9:40-11:10 - Французский язык \n🕒 11:30-13:00 - Администрирование информационных систем",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp201)
            if call.data == 'raspFri201':
                rasp201 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon201')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue201')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed201')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu201')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri201')
                rasp201.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Пятница: \n🕒 8:00-9:30 – Микроэкономика \n🕒 9:40-11:10 - Бухгалтерский учет \n🕒 11:30-13:00 - Дизайн для крупного бизнеса",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp201)

#---------------------------------------------------------------
            if call.data == 'M3':
                rasp301 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon301')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue301')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed301')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu301')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri301')
                rasp301.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp301)

            if call.data == 'raspMon301':
                rasp301 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon301')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue301')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed301')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu301')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri301')
                rasp301.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                    f"📅Понедельник: \n🕒 8:00-9:30 - Французский язык \n🕒 9:40-11:10 - Администрирование информационных систем \n🕒 11:30-13:00 - Менеджмент в маркетинге",
                                    parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                     parse_mode='html', reply_markup=rasp301)
            if call.data == 'raspTue301':
                rasp301 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon301')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue301')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed301')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu301')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri301')
                rasp301.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Вторник: \n🕒 8:00-9:30 - Логистика и построение маршрутов \n🕒 9:40-11:10 - Дизайн для крупного бизнеса \n🕒 11:30-13:00 - Основы алгоритмов и программирования",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp301)
            if call.data == 'raspWed301':
                rasp301 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon301')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue301')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed301')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu301')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri301')
                rasp301.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Среда: \n🕒 8:00-9:30 – Макроэкономика \n🕒 9:40-11:10 - Программирования операционных систем \n🕒 11:30-13:00 - Микроэкономика",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                     parse_mode='html', reply_markup=rasp301)
            if call.data == 'raspThu301':
                rasp301 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon301')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue301')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed301')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu301')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri301')
                rasp301.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Четверг: \n🕒 8:00-9:30 - Профессиональный английский язык \n🕒 9:40-11:10 – Микроэкономика \n🕒 11:30-13:00 - Дизайн логотипов в крупных компаниях",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp301)
            if call.data == 'raspFri301':
                rasp301 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon301')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue301')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed301')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu301')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri301')
                rasp301.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Пятница: \n🕒 8:00-9:30 - Высшая математика \n🕒 9:40-11:10 - Немецкий язык \n🕒11:30-13:00 - Бухгалтерский учет",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp301)

#---------------------------------------------------------------
            if call.data == 'M4':
                    rasp401 = types.InlineKeyboardMarkup(row_width=2)
                    raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon401')
                    raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue401')
                    raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed401')
                    raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu401')
                    raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri401')
                    rasp401.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                    bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                     parse_mode='html', reply_markup=rasp401)

            if call.data == 'raspMon401':
                rasp401 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon401')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue401')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed401')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu401')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri401')
                rasp401.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Понедельник: \n🕒 8:00 - 9:30: Английский язык \n🕒 9:40 - 11:10: Макроэкономика \n🕒 11:30 - 13:00: Логистика в сфере туризма",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp401)
            if call.data == 'raspTue401':
                rasp401 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon401')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue401')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed401')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu401')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri401')
                rasp401.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Вторник: \n🕒 8:00 - 9:30: Основы алгоритмов и программирования \n🕒 9:40 - 11:10: Французский язык \n🕒 11:30 - 13:00: Профессиональный казахский язык",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp401)
            if call.data == 'raspWed401':
                rasp401 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon401')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue401')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed401')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu401')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri401')
                rasp401.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Среда: \n🕒 8:00 - 9:30: Высшая математика \n🕒 9:40 - 11:10: Немецкий язык \n🕒 11:30 - 13:00: Дизайн для крупного бизнеса",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp401)
            if call.data == 'raspThu401':
                rasp401 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon401')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue401')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed401')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu401')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri401')
                rasp401.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Четверг: \n🕒 8:00 - 9:30: Микроэкономика \n🕒 9:40 - 11:10: Программирование микроконтроллеров \n🕒 11:30 - 13:00: Бухгалтерский учёт",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp401)
            if call.data == 'raspFri401':
                rasp401 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon401')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue401')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed401')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu401')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri401')
                rasp401.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Пятница: \n🕒 8:00 - 9:30: Казахский язык \n🕒 9:40 - 11:10: Бухгалтерский учёт \n🕒 11:30 - 13:00: Немецкий язык",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp401)

#----------------------------------------------------------------
            if call.data == 'infosys':
                info = types.InlineKeyboardMarkup(row_width=2)
                info1 = types.InlineKeyboardButton("1 курс", callback_data='I1')
                info2 = types.InlineKeyboardButton("2 курс", callback_data='I2')
                info3 = types.InlineKeyboardButton("3 курс", callback_data='I3')
                info4 = types.InlineKeyboardButton("4 курс", callback_data='I4')

                info.add(info1, info2, info3, info4)
                bot.send_message(call.message.chat.id, "На каком курсе вы учитесь?", parse_mode='html',
                                 reply_markup=info)

#----------------------------------------------------------------
            if call.data == 'I1':
                rasp103 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon103')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue103')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed103')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu103')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri103')
                rasp103.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp103)

            if call.data == 'raspMon103':
                rasp103 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon103')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue103')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed103')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu103')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri103')
                rasp103.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Понедельник: \n🕒 8:00-9:30 - Основы алгоритмов и программирования \n🕒 9:40-11:10 - Программирования микроконтроллеров \n🕒 11:30-13:00 - Дизайн логотипов в крупных компаниях",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp103)
            if call.data == 'raspTue103':
                rasp103 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon103')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue103')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed103')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu103')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri103')
                rasp103.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Вторник: \n🕒 8:00-9:30 – Макроэкономика \n🕒 9:40-11:10 - Менеджмент в маркетинге \n🕒 11:30-13:00 - Логистика и построение маршрутов",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp103)
            if call.data == 'raspWed103':
                rasp103 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon103')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue103')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed103')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu103')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri103')
                rasp103.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Среда: \n🕒 8:00-9:30 - Высшая математика \n🕒 9:40-11:10 - Профессиональный английский язык \n🕒 11:30-13:00 - Администрирование информационных систем",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp103)
            if call.data == 'raspThu103':
                rasp103 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon103')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue103')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed103')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu103')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri103')
                rasp103.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Четверг: \n🕒 8:00-9:30 - Философия древнего Рима \n🕒 9:40-11:10 - Французский язык \n🕒 11:30-13:00 - Немецкий язык",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp103)
            if call.data == 'raspFri103':
                rasp103 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon103')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue103')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed103')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu103')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri103')
                rasp103.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Пятница: \n🕒 8:00-9:30 – Микроэкономика \n🕒 9:40-11:10 - Бухгалтерский учет \n🕒 11:30-13:00 - Логистика в сфере туризма",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp103)

#------------------------------------------------------------------
            if call.data == 'I2':
                rasp203 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon203')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue203')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed203')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu203')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri203')
                rasp203.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp203)

            if call.data == 'raspMon203':
                rasp203 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon203')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue203')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed203')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu203')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri203')
                rasp203.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Понедельник: \n🕒 8:00-9:30 - Программирования микроконтроллеров \n🕒 9:40-11:10 – Немецкий язык \n🕒 11:30-13:00 - Профессиональный казахский язык",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp203)
            if call.data == 'raspTue203':
                rasp203 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon203')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue203')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed203')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu203')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri203')
                rasp203.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Вторник: \n🕒 8:00-9:30 - Дизайн логотипов в крупных компаниях \n🕒 9:40-11:10 - Логистика в сфере туризма \n🕒 11:30-13:00 - Администрирование информационных систем",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp203)
            if call.data == 'raspWed203':
                rasp203 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon203')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue203')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed203')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu203')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri203')
                rasp203.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Среда: \n🕒 8:00-9:30 - Философия древнего Рима \n🕒 9:40-11:10 – Макроэкономика \n🕒 11:30-13:00 - Программирования операционных систем",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp203)
            if call.data == 'raspThu203':
                rasp203 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon203')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue203')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed203')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu203')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri203')
                rasp203.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Четверг: \n🕒 8:00-9:30 - Менеджмент в маркетинге \n🕒 9:40-11:10 - Немецкий язык \n🕒 11:30-13:00 - Основы алгоритмов и программирования",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp203)
            if call.data == 'raspFri203':
                rasp203 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon203')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue203')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed203')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu203')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri203')
                rasp203.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Пятница: \n🕒 8:00-9:30 - Логистика и построение маршрутов \n🕒 9:40-11:10 - Бухгалтерский учет \n🕒 11:30-13:00 - Микроэкономика",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp203)

#------------------------------------------------------------------
            if call.data == 'I3':
                rasp303 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon303')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue303')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed303')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu303')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri303')
                rasp303.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp303)

            if call.data == 'raspMon303':
                rasp303 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon303')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue303')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed303')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu303')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri303')
                rasp303.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Понедельник: \n🕒 8:00 - 9:30: Микроэкономика \n🕒 9:40 - 11:10: Основы алгоритмов и программирования \n🕒 11:30 - 13:00: Профессиональный казахский язык",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp303)
            if call.data == 'raspTue303':
                rasp303 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon303')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue303')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed303')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu303')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri303')
                rasp303.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Вторник: \n🕒 8:00 - 9:30: Высшая математика \n🕒9:40 - 11:10: Английский язык \n🕒 11:30 - 13:00: Программирование микроконтроллеров",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp303)
            if call.data == 'raspWed303':
                rasp303 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon303')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue303')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed303')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu303')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri303')
                rasp303.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Среда: \n🕒 8:00 - 9:30: Макроэкономика \n🕒 9:40 - 11:10: Немецкий язык \n🕒11:30 - 13:00: Бухгалтерский учёт",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp303)
            if call.data == 'raspThu303':
                rasp303 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon303')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue303')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed303')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu303')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri303')
                rasp303.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Четверг: \n🕒 8:00 - 9:30: Философия древнего Рима \n🕒 9:40 - 11:10: Профессиональный английский язык \n🕒 11:30 - 13:00: Администрирование информационных систем",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp303)
            if call.data == 'raspFri303':
                rasp303 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon303')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue303')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed303')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu303')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri303')
                rasp303.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Пятница: \n🕒 8:00 - 9:30: Логистика в сфере туризма \n🕒 9:40 - 11:10: Французский язык \n🕒 11:30 - 13:00: Дизайн для крупного бизнеса",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp303)

#------------------------------------------------------------------
            if call.data == 'I4':
                rasp403 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon403')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue403')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed403')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu403')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri403')
                rasp403.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp403)

            if call.data == 'raspMon403':
                rasp403 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon403')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue403')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed403')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu403')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri403')
                rasp403.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Понедельник: \n🕒 8:00 - 9:30: Высшая математика \n🕒 9:40 - 11:10: Профессиональный английский язык \n🕒 11:30 - 13:00: Программирование операционных систем",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp403)
            if call.data == 'raspTue403':
                rasp403 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon403')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue403')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed403')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu403')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri403')
                rasp403.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Вторник: \n🕒 8:00 - 9:30: Микроэкономика \n🕒 9:40 - 11:10: Английский язык \n🕒 11:30 - 13:00: Дизайн логотипов в крупных компаниях",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp403)
            if call.data == 'raspWed403':
                rasp403 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon403')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue403')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed403')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu403')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri403')
                rasp403.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Среда: \n🕒 8:00 - 9:30: Логистика в сфере туризма \n🕒 9:40 - 11:10: Основы алгоритмов и программирования \n🕒 11:30 - 13:00: Менеджмент в маркетинге",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp403)
            if call.data == 'raspThu403':
                rasp403 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon403')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue403')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed403')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu403')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri403')
                rasp403.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Четверг: \n🕒 8:00 - 9:30: Высшая математика \n🕒 9:40 - 11:10: Профессиональный казахский язык \n🕒 11:30 - 13:00: Казахский язык",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp403)
            if call.data == 'raspFri403':
                rasp403 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon403')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue403')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed403')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu403')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri403')
                rasp403.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"📅Пятница: \n🕒8:00 - 9:30: Макроэкономика \n🕒9:40 - 11:10: Немецкий язык \n🕒11:30 - 13:00: Логистика и построение маршрутов",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp403)


                # show alert
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                          text="Пишите, всегда поможем!")
#------------------------------------------------------------------меню без эмодзи
            if call.data == 'no_emodzi':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Информация о боте")
                item2 = types.KeyboardButton("Информация о учебном заведение")
                item3 = types.KeyboardButton("Настройки")
                item4 = types.KeyboardButton("Расписание")
                item5 = types.KeyboardButton("Преподаватели")
                item6 = types.KeyboardButton("Студент")
                markup.add(item1, item2, item3, item4, item5, item6)

                bot.send_message(call.message.chat.id,
                                 f"Настройки успешно сохранены"
                                 ,
                                 parse_mode='html', reply_markup=markup)

            if call.data == 'tourism*':
                tour = types.InlineKeyboardMarkup(row_width=2)
                tour1 = types.InlineKeyboardButton("1 курс", callback_data='T1*')
                tour2 = types.InlineKeyboardButton("2 курс", callback_data='T2*')
                tour3 = types.InlineKeyboardButton("3 курс", callback_data='T3*')
                tour4 = types.InlineKeyboardButton("4 курс", callback_data='T4*')

                tour.add(tour1, tour2, tour3, tour4)
                bot.send_message(call.message.chat.id, "На каком курсе вы учитесь?", parse_mode='html',
                                 reply_markup=tour)

            # -----------------------------------------------------------
            if call.data == 'T1*':
                rasp102 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon102*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue102*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed102*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu102*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri102*')
                rasp102.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp102)
            if call.data == 'raspMon102*':
                rasp102 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon102*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue102*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed102*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu102*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri102*')
                rasp102.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Понедельник: \n8:00 - 9:30 – Программирования операционных систем \n9:40 - 11:10 - Немецкий язык \n11:30 - 13:00 - Английский язык",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp102)
            if call.data == 'raspTue102*':
                rasp102 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon102*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue102*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed102*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu102*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri102*')
                rasp102.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Вторник: \n8:00 - 9:30 - Программирования операционных систем \n9:40 - 11:10 - Администрирование информационных систем \n11:30 - 13:00 - Дизайн для крупного бизнеса",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp102)
            if call.data == 'raspWed102*':
                rasp102 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon102*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue102*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed102*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu102*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri102*')
                rasp102.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Среда: \n8:00 - 9:30 - Высшая математика \n9:40 - 11:10 - Основы алгоритмов и программирования \n11:30 - 13:00 - Бухгалтерский учёт",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp102)
            if call.data == 'raspThu102*':
                rasp102 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon102*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue102*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed102*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu102*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri102*')
                rasp102.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Четверг: \n8:00 - 9:30 – Микроэкономика \n9:40 - 11:10 – Макроэкономика \n11:30 - 13:00 - Логистика и построение маршрутов",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp102)
            if call.data == 'raspFri102*':
                rasp102 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon102*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue102*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed102*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu102*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri102*')
                rasp102.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Пятница: \n8:00 - 9:30 - Профессиональный казахский язык \n9:40 - 11:10 - Казахский язык \n11:30 - 13:00 - Профессиональный английский язык",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp102)

            # ----------------------------------------------------------
            if call.data == 'T2*':
                rasp202 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon202*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue202*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed202*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu202*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri202*')
                rasp202.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp202)
            if call.data == 'raspMon202*':
                rasp202 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon202*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue202*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed202*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu202*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri202*')
                rasp202.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Понедельник: \n8:00-9:30 – Казахский язык \n9:40-11:10 - Администрирование информационных систем \n11:30-13:00 - Менеджмент в маркетинге",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp202)
            if call.data == 'raspTue202*':
                rasp202 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon202*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue202*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed202*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu202*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri202*')
                rasp202.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Вторник: \n8:00-9:30 - Логистика и построение маршрутов \n9:40-11:10 - Дизайн для крупного бизнеса \n11:30-13:00 - Основы алгоритмов и программирования",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp202)
            if call.data == 'raspWed202*':
                rasp202 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon202*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue202*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed202*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu202*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri202*')
                rasp202.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Среда: \n8:00-9:30 - Макроэкономика \n9:40-11:10 - Программирования операционных систем \n11:30-13:00 - Философия древнего Рима",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp202)
            if call.data == 'raspThu202*':
                rasp202 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon202*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue202*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed202*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu202*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri202*')
                rasp202.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Четверг: \n8:00-9:30 - Профессиональный английский язык \n9:40-11:10 – Микроэкономика \n11:30-13:00 - Дизайн логотипов в крупных компаниях",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp202)
            if call.data == 'raspFri202*':
                rasp202 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon202*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue202*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed202*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu202*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri202*')
                rasp202.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Пятница: \n8:00-9:30 - Высшая математика \n9:40-11:10 - Немецкий язык \n11:30-13:00 - Бухгалтерский учет",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp202)

            # -------------------------------------------------------------
            if call.data == 'T3*':
                rasp302 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon302*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue302*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed302*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu302*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri302*')
                rasp302.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp302)
            if call.data == 'raspMon302*':
                rasp302 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon302*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue302*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed302*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu302*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri302*')
                rasp302.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Понедельник: \n8:00-9:30 - Профессиональный казахский язык \n9:40-11:10 – Макроэкономика \n11:30-13:00 - Программирования микроконтроллеров",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp302)
            if call.data == 'raspTue302*':
                rasp302 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon302*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue302*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed302*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu302*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri302*')
                rasp302.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Вторник: \n8:00-9:30 - Английский язык \n9:40-11:10 - Дизайн логотипов в крупных компаниях \n11:30-13:00 - Логистика в сфере туризма",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp302)
            if call.data == 'raspWed302*':
                rasp302 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon302*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue302*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed302*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu302*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri302*')
                rasp302.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Среда: \n8:00-9:30 - Менеджмент в маркетинге \n9:40-11:10 - Основы алгоритмов и программирования \n11:30-13:00 - Профессиональный английский язык",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp302)
            if call.data == 'raspThu302*':
                rasp302 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon302*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue302*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed302*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu302*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri302*')
                rasp302.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Четверг: \n8:00-9:30 - Немецкий язык \n9:40-11:10 - Дизайн для крупного бизнеса \n11:30-13:00 - Администрирование информационных систем",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp302)
            if call.data == 'raspFri302*':
                rasp302 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon302*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue302*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed302*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu302*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri302*')
                rasp302.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Пятница: \n8:00-9:30 - Французский язык \n9:40-11:10 - Высшая математика \n11:30-13:00 - Бухгалтерский учёт",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp302)

            # -------------------------------------------------------------
            if call.data == 'T4*':
                rasp402 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon402*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue402*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed402*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu402*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri402*')
                rasp402.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp402)
            if call.data == 'raspMon402*':
                rasp402 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon402*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue402*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed402*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu402*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri402*')
                rasp402.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Понедельник: \n8:00 - 9:30: Философия древнего Рима \n9:40 - 11:10: Основы алгоритмов и программирования \n11:30 - 13:00: Профессиональный английский язык",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp402)
            if call.data == 'raspTue402*':
                rasp402 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon402*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue402*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed402*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu402*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri402*')
                rasp402.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Вторник: \n8:00 - 9:30: Микроэкономика \n9:40 - 11:10: Английский язык \n11:30 - 13:00: Логистика и построение маршрутов",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp402)
            if call.data == 'raspWed402*':
                rasp402 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon402*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue402*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed402*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu402*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri402*')
                rasp402.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Среда: \n8:00 - 9:30: Высшая математика \n9:40 - 11:10: Немецкий язык \n11:30 - 13:00: Бухгалтерский учёт",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp402)
            if call.data == 'raspThu402*':
                rasp402 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon402*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue402*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed402*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu402*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri402*')
                rasp402.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Четверг: \n8:00 - 9:30: Программирование микроконтроллеров \n9:40 - 11:10: Профессиональный казахский язык \n11:30 - 13:00: Менеджмент в маркетинге",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp402)
            if call.data == 'raspFri402*':
                rasp402 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon402*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue402*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed402*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu402*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri402*')
                rasp402.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Пятница: \n8:00 - 9:30: Макроэкономика \n9:40 - 11:10: Французский язык \n11:30 - 13:00: Дизайн логотипов в крупных компаниях",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp402)

            # -------------------------------------------------------------
            if call.data == 'market*':
                market = types.InlineKeyboardMarkup(row_width=2)
                market1 = types.InlineKeyboardButton("1 курс", callback_data='M1*')
                market2 = types.InlineKeyboardButton("2 курс", callback_data='M2*')
                market3 = types.InlineKeyboardButton("3 курс", callback_data='M3*')
                market4 = types.InlineKeyboardButton("4 курс", callback_data='M4*')

                market.add(market1, market2, market3, market4)
                bot.send_message(call.message.chat.id, "На каком курсе вы учитесь?", parse_mode='html',
                                 reply_markup=market)

            # -------------------------------------------------------------
            if call.data == 'M1*':
                rasp101 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon101*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue101*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed101*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu101*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri101*')
                rasp101.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp101)
            if call.data == 'raspMon101*':
                rasp101 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon101*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue101*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed101*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu101*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri101*')
                rasp101.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Понедельник: \n8:00 - 9:30 - Высшая математика \n9:40 - 11:10 - Основы алгоритмов и программирования \n11:30 - 13:00 - Микроэкономика",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp101)
            if call.data == 'raspTue101':
                rasp101 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon101*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue101*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed101*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu101*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri101*')
                rasp101.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 "Вторник: \n8:00- 9:30 - Логистика в сфере туризма \n9:40- 11:10 – Макроэкономика \n11:30 - 13:00 - Философия древнего Рима",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp101)
            if call.data == 'raspWed101*':
                rasp101 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon101*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue101*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed101*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu101*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri101*')
                rasp101.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Среда: \n9:00-11:00 - Французский язык \n9:40 - 11:10 - Немецкий язык \n11:30 - 13:00 - Английский язык",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp101)
            if call.data == 'raspThu101*':
                rasp101 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon101*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue101*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed101*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu101*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri101*')
                rasp101.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Четверг: \n8:00 - 9:30 - Профессиональный казахский язык \n9:40 - 11:10 - Казахский язык \n11:30 - 13:00 - Профессиональный английский язык",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp101)
            if call.data == 'raspFri101*':
                rasp101 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon101*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue101*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed101*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu101*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri101*')
                rasp101.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Пятница: \n8:00 - 9:30 - Программирования микроконтроллеров \n9:40 - 11:10 - Менеджмент в маркетинге \n11:30 - 13:00 - Дизайн логотипов в крупных компаниях",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp101)

            # --------------------------------------------------------------
            if call.data == 'M2*':
                rasp201 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon201*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue201*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed201*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu201*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri201*')
                rasp201.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp201)

            if call.data == 'raspMon201*':
                rasp201 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon201*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue201*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed201*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu201*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri201*')
                rasp201.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 "Понедельник: \n8:00-9:30 - Основы алгоритмов и программирования \n9:40-11:10 - Логистика в сфере туризма \n11:30-13:00 - Философия древнего Рима",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp201)
            if call.data == 'raspTue201*':
                rasp201 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon201*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue201*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed201*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu201*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri201*')
                rasp201.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Вторник: \n8:00-9:30 - Профессиональный казахский язык \n9:40-11:10 – Макроэкономика \n11:30-13:00 - Программирования операционных систем",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp201)
            if call.data == 'raspWed201*':
                rasp201 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon201*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue201*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed201*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu201*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri201*')
                rasp201.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Среда: \n8:00-9:30 - Менеджмент в маркетинге \n9:40-11:10 - Дизайн логотипов в крупных компаниях \n11:30-13:00 - Логистика и построение маршрутов",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp201)
            if call.data == 'raspThu201*':
                rasp201 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon201*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue201*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed201*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu201*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri201*')
                rasp201.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Четверг: \n8:00-9:30 - Высшая математика \n9:40-11:10 - Французский язык \n11:30-13:00 - Администрирование информационных систем",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp201)
            if call.data == 'raspFri201*':
                rasp201 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon201*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue201*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed201*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu201*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri201*')
                rasp201.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Пятница: \n8:00-9:30 – Микроэкономика \n9:40-11:10 - Бухгалтерский учет \n11:30-13:00 - Дизайн для крупного бизнеса",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp201)

            # ---------------------------------------------------------------
            if call.data == 'M3*':
                rasp301 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon301*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue301*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed301*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu301*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri301*')
                rasp301.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp301)

            if call.data == 'raspMon301*':
                rasp301 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon301*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue301*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed301*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu301*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri301*')
                rasp301.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Понедельник: \n8:00-9:30 - Французский язык \n9:40-11:10 - Администрирование информационных систем \n11:30-13:00 - Менеджмент в маркетинге",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp301)
            if call.data == 'raspTue301*':
                rasp301 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon301*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue301*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed301*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu301*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri301*')
                rasp301.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Вторник: \n8:00-9:30 - Логистика и построение маршрутов \n9:40-11:10 - Дизайн для крупного бизнеса \n11:30-13:00 - Основы алгоритмов и программирования",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp301)
            if call.data == 'raspWed301*':
                rasp301 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon301*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue301*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed301*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu301*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri301*')
                rasp301.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Среда: \n8:00-9:30 – Макроэкономика \n9:40-11:10 - Программирования операционных систем \n11:30-13:00 - Микроэкономика",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp301)
            if call.data == 'raspThu301*':
                rasp301 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon301*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue301*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed301*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu301*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri301*')
                rasp301.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Четверг: \n8:00-9:30 - Профессиональный английский язык \n9:40-11:10 – Микроэкономика \n11:30-13:00 - Дизайн логотипов в крупных компаниях",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp301)
            if call.data == 'raspFri301*':
                rasp301 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon301*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue301*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed301*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu301*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri301*')
                rasp301.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Пятница: \n8:00-9:30 - Высшая математика \n9:40-11:10 - Немецкий язык \n11:30-13:00 - Бухгалтерский учет",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp301)

            # ---------------------------------------------------------------
            if call.data == 'M4*':
                rasp401 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon401*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue401*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed401*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu401*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri401*')
                rasp401.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp401)

            if call.data == 'raspMon401*':
                rasp401 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon401*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue401*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed401*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu401*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri401*')
                rasp401.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Понедельник: \n8:00 - 9:30: Английский язык \n9:40 - 11:10: Макроэкономика \n11:30 - 13:00: Логистика в сфере туризма",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp401)
            if call.data == 'raspTue401*':
                rasp401 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon401*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue401*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed401*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu401*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri401*')
                rasp401.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Вторник: \n8:00 - 9:30: Основы алгоритмов и программирования \n9:40 - 11:10: Французский язык \n11:30 - 13:00: Профессиональный казахский язык",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp401)
            if call.data == 'raspWed401*':
                rasp401 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon401*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue401*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed401*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu401*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri401*')
                rasp401.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Среда: \n8:00 - 9:30: Высшая математика \n9:40 - 11:10: Немецкий язык \n11:30 - 13:00: Дизайн для крупного бизнеса",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp401)
            if call.data == 'raspThu401*':
                rasp401 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon401*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue401*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed401*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu401*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri401*')
                rasp401.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Четверг: \n8:00 - 9:30: Микроэкономика \n9:40 - 11:10: Программирование микроконтроллеров \n11:30 - 13:00: Бухгалтерский учёт",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp401)
            if call.data == 'raspFri401*':
                rasp401 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon401*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue401*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed401*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu401*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri401*')
                rasp401.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Пятница: \n8:00 - 9:30: Казахский язык \n9:40 - 11:10: Бухгалтерский учёт \n11:30 - 13:00: Немецкий язык",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp401)

            if call.data == 'infosys*':
                info = types.InlineKeyboardMarkup(row_width=2)
                info1 = types.InlineKeyboardButton("1 курс", callback_data='I1*')
                info2 = types.InlineKeyboardButton("2 курс", callback_data='I2*')
                info3 = types.InlineKeyboardButton("3 курс", callback_data='I3*')
                info4 = types.InlineKeyboardButton("4 курс", callback_data='I4*')

                info.add(info1, info2, info3, info4)
                bot.send_message(call.message.chat.id, "На каком курсе вы учитесь?", parse_mode='html',
                                 reply_markup=info)

            # ----------------------------------------------------------------
            if call.data == 'I1*':
                rasp103 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon103*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue103*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed103*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu103*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri103*')
                rasp103.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp103)

            if call.data == 'raspMon103*':
                rasp103 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon103*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue103*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed103*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu103*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri103*')
                rasp103.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Понедельник: \n8:00-9:30 - Основы алгоритмов и программирования \n9:40-11:10 - Программирования микроконтроллеров \n🕒 11:30-13:00 - Дизайн логотипов в крупных компаниях",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp103)
            if call.data == 'raspTue103*':
                rasp103 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon103*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue103*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed103*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu103*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri103*')
                rasp103.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Вторник: \n8:00-9:30 – Макроэкономика \n9:40-11:10 - Менеджмент в маркетинге \n11:30-13:00 - Логистика и построение маршрутов",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp103)
            if call.data == 'raspWed103*':
                rasp103 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon103*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue103*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed103*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu103*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri103*')
                rasp103.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Среда: \n8:00-9:30 - Высшая математика \n9:40-11:10 - Профессиональный английский язык \n11:30-13:00 - Администрирование информационных систем",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp103)
            if call.data == 'raspThu103':
                rasp103 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon103*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue103*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed103*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu103*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri103*')
                rasp103.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Четверг: \n8:00-9:30 - Философия древнего Рима \n9:40-11:10 - Французский язык \n11:30-13:00 - Немецкий язык",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp103)
            if call.data == 'raspFri103*':
                rasp103 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon103*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue103*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed103*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu103*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri103*')
                rasp103.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Пятница: \n8:00-9:30 – Микроэкономика \n9:40-11:10 - Бухгалтерский учет \n11:30-13:00 - Логистика в сфере туризма",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp103)

            # ------------------------------------------------------------------
            if call.data == 'I2*':
                rasp203 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon203*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue203*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed203*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu203*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri203*')
                rasp203.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp203)

            if call.data == 'raspMon203*':
                rasp203 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon203*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue203*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed203*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu203*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri203*')
                rasp203.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Понедельник: \n8:00-9:30 - Программирования микроконтроллеров \n9:40-11:10 – Немецкий язык \n11:30-13:00 - Профессиональный казахский язык",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp203)
            if call.data == 'raspTue203*':
                rasp203 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon203*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue203*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed203*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu203*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri203*')
                rasp203.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Вторник: \n8:00-9:30 - Дизайн логотипов в крупных компаниях \n9:40-11:10 - Логистика в сфере туризма \n11:30-13:00 - Администрирование информационных систем",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp203)
            if call.data == 'raspWed203*':
                rasp203 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon203*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue203*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed203*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu203*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri203*')
                rasp203.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Среда: \n8:00-9:30 - Философия древнего Рима \n9:30-11:10 – Макроэкономика \n11:30-13:00 - Программирования операционных систем",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp203)
            if call.data == 'raspThu203*':
                rasp203 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon203*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue203*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed203*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu203*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri203*')
                rasp203.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Четверг: \n8:00-9:30 - Менеджмент в маркетинге \n9:40-11:10 - Немецкий язык \n11:30-13:00 - Основы алгоритмов и программирования",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp203)
            if call.data == 'raspFri203*':
                rasp203 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon203*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue203*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed203*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu203*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri203*')
                rasp203.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Пятница: \n8:00-9:30 - Логистика и построение маршрутов \n9:40-11:10 - Бухгалтерский учет \n11:30-13:00 - Микроэкономика",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp203)

            # ------------------------------------------------------------------
            if call.data == 'I3*':
                rasp303 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon303*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue303*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed303*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu303*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri303*')
                rasp303.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp303)

            if call.data == 'raspMon303*':
                rasp303 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon303*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue303*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed303*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu303*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri303*')
                rasp303.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Понедельник: \n8:00 - 9:30: Микроэкономика \n9:40 - 11:10: Основы алгоритмов и программирования \n11:30 - 13:00: Профессиональный казахский язык",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp303)
            if call.data == 'raspTue303*':
                rasp303 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon303*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue303*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed303*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu303*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri303*')
                rasp303.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Вторник: \n8:00 - 9:30: Высшая математика \n9:40 - 11:10: Английский язык \n11:30 - 13:00: Программирование микроконтроллеров",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp303)
            if call.data == 'raspWed303*':
                rasp303 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon303*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue303*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed303*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu303*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri303*')
                rasp303.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Среда: \n8:00 - 9:30: Макроэкономика \n9:40 - 11:10: Немецкий язык \n11:30 - 13:00: Бухгалтерский учёт",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp303)
            if call.data == 'raspThu303*':
                rasp303 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon303*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue303*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed303*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu303*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri303*')
                rasp303.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Четверг: \n8:00 - 9:30: Философия древнего Рима \n9:40 - 11:10: Профессиональный английский язык \n11:30 - 13:00: Администрирование информационных систем",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp303)
            if call.data == 'raspFri303*':
                rasp303 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon303*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue303*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed303*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu303*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri303*')
                rasp303.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Пятница: \n8:00 - 9:30: Логистика в сфере туризма \n9:40 - 11:10: Французский язык \n11:30 - 13:00: Дизайн для крупного бизнеса",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp303)

            # ------------------------------------------------------------------
            if call.data == 'I4*':
                rasp403 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon403*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue403*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed403*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu403*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri403*')
                rasp403.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp403)

            if call.data == 'raspMon403*':
                rasp403 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon403*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue403*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed403*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu403*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri403*')
                rasp403.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Понедельник: \n8:00 - 9:30: Высшая математика \n9:40 - 11:10: Профессиональный английский язык \n11:30 - 13:00: Программирование операционных систем",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp403)
            if call.data == 'raspTue403*':
                rasp403 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon403*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue403*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed403*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu403*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri403*')
                rasp403.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Вторник: \n8:00 - 9:30: Микроэкономика \n9:40 - 11:10: Английский язык \n11:30 - 13:00: Дизайн логотипов в крупных компаниях",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp403)
            if call.data == 'raspWed403*':
                rasp403 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon403*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue403*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed403*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu403*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri403*')
                rasp403.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Среда: \n8:00 - 9:30: Логистика в сфере туризма \n9:40 - 11:10: Основы алгоритмов и программирования \n11:30 - 13:00: Менеджмент в маркетинге",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp403)
            if call.data == 'raspThu403*':
                rasp403 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon403*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue403*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed403*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu403*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri403*')
                rasp403.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Четверг: \n8:00 - 9:30: Высшая математика \n9:40 - 11:10: Профессиональный казахский язык \n11:30 - 13:00: Казахский язык",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp403)
            if call.data == 'raspFri403*':
                rasp403 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon403*')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue403*')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed403*')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu403*')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri403*')
                rasp403.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"Пятница: \n8:00 - 9:30: Макроэкономика \n9:40 - 11:10: Немецкий язык \n11:30 - 13:00: Логистика и построение маршрутов",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "Выбирай день недели и я отправлю тебе расписание!",
                                 parse_mode='html', reply_markup=rasp403)
#-------------------------------------------------------------------

#-------------------------------------------------------------------
            if call.data == 'Zhirnii':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Информация o боте 📄")
                item2 = types.KeyboardButton("Информация o учебном заведение 🏫")
                item3 = types.KeyboardButton("Нaстройки ⚙️")
                item4 = types.KeyboardButton("Рaсписание 📑")
                item5 = types.KeyboardButton("Препoдаватели 🧑🏻‍🏫")
                item6 = types.KeyboardButton("Студeнт 🎓")
                markup.add(item1, item2, item3, item4, item5, item6)

                bot.send_message(call.message.chat.id,
                                 f"<b>Настройки успешно сохранены</b>",
                                 parse_mode='html', reply_markup=markup)
#------------------------------------------------расписание студентов с жирным шрифтом
            if call.data == 'tourism//':
                tour = types.InlineKeyboardMarkup(row_width=2)
                tour1 = types.InlineKeyboardButton("1 курс", callback_data='T1//')
                tour2 = types.InlineKeyboardButton("2 курс", callback_data='T2//')
                tour3 = types.InlineKeyboardButton("3 курс", callback_data='T3//')
                tour4 = types.InlineKeyboardButton("4 курс", callback_data='T4//')

                tour.add(tour1, tour2, tour3, tour4)
                bot.send_message(call.message.chat.id, "<b>На каком курсе вы учитесь?</b>", parse_mode='html',
                                 reply_markup=tour)

            # -----------------------------------------------------------
            if call.data == 'T1//':
                rasp102 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon102//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue102//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed102//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu102//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri102//')
                rasp102.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp102)
            if call.data == 'raspMon102//':
                rasp102 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon102//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue102//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed102//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu102//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri102//')
                rasp102.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Понедельник: \n🕒8:00 - 9:30 – Программирования операционных систем \n🕒9:40 - 11:10 - Немецкий язык \n🕒11:30 - 13:00 - Английский язык</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp102)
            if call.data == 'raspTue102//':
                rasp102 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon102//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue102//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed102//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu102//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri102//')
                rasp102.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Вторник: \n🕒 8:00 - 9:30 - Программирования операционных систем \n🕒 9:40 - 11:10 - Администрирование информационных систем \n🕒 11:30 - 13:00 - Дизайн для крупного бизнеса</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp102)
            if call.data == 'raspWed102//':
                rasp102 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon102//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue102//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed102//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu102//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri102//')
                rasp102.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Среда: \n🕒 8:00 - 9:30 - Высшая математика \n🕒 9:40 - 11:10 - Основы алгоритмов и программирования \n🕒 11:30 - 13:00 - Бухгалтерский учёт</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp102)
            if call.data == 'raspThu102//':
                rasp102 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon102//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue102//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed102//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu102//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri102//')
                rasp102.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Четверг: \n🕒 8:00 - 9:30 – Микроэкономика \n🕒 9:40 - 11:10 – Макроэкономика \n🕒 11:30 - 13:00 - Логистика и построение маршрутов</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp102)
            if call.data == 'raspFri102//':
                rasp102 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon102//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue102//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed102//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu102//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri102//')
                rasp102.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 "<b>📅Пятница: \n🕒 8:00 - 9:30 - Профессиональный казахский язык \n🕒 9:40 - 11:10 - Казахский язык \n🕒 11:30 - 13:00 - Профессиональный английский язык</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp102)

            # ----------------------------------------------------------
            if call.data == 'T2//':
                rasp202 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon202//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue202//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed202//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu202//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri202//')
                rasp202.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp202)
            if call.data == 'raspMon202//':
                rasp202 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon202//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue202//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed202//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu202//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri202//')
                rasp202.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Понедельник: \n🕒 8:00-9:30 – Казахский язык \n🕒 9:40-11:10 - Администрирование информационных систем \n🕒 11:30-13:00 - Менеджмент в маркетинге</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp202)
            if call.data == 'raspTue202//':
                rasp202 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon202//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue202//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed202//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu202//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri202//')
                rasp202.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Вторник: \n🕒 8:00-9:30 - Логистика и построение маршрутов \n🕒 9:40-11:10 - Дизайн для крупного бизнеса \n🕒 11:30-13:00 - Основы алгоритмов и программирования</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp202)
            if call.data == 'raspWed202//':
                rasp202 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon202//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue202//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed202//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu202//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri202//')
                rasp202.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Среда: \n🕒 8:00-9:30 - Макроэкономика \n🕒 9:40-11:10 - Программирования операционных систем \n🕒 11:30-13:00 - Философия древнего Рима</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp202)
            if call.data == 'raspThu202//':
                rasp202 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon202//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue202//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed202//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu202//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri202//')
                rasp202.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Четверг: \n🕒 8:00-9:30 - Профессиональный английский язык \n🕒 9:40-11:10 – Микроэкономика \n🕒 11:30-13:00 - Дизайн логотипов в крупных компаниях</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp202)
            if call.data == 'raspFri202//':
                rasp202 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon202//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue202//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed202//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu202//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri202//')
                rasp202.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Пятница: \n🕒 8:00-9:30 - Высшая математика \n🕒 9:40-11:10 - Немецкий язык \🕒 11:30-13:00 - Бухгалтерский учет</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp202)

            # -------------------------------------------------------------
            if call.data == 'T3//':
                rasp302 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon302//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue302//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed302//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu302//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri302//')
                rasp302.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp302)
            if call.data == 'raspMon302//':
                rasp302 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon302//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue302//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed302//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu302//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri302//')
                rasp302.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Понедельник: \n🕒 8:00-9:30 - Профессиональный казахский язык \n🕒 9:40-11:10 – Макроэкономика \n🕒 11:30-13:00 - Программирования микроконтроллеров</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp302)
            if call.data == 'raspTue302//':
                rasp302 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon302//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue302//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed302//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu302//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri302//')
                rasp302.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Вторник: \n🕒 8:00-9:30 - Английский язык \n🕒 9:40-11:10 - Дизайн логотипов в крупных компаниях \n🕒 11:30-13:00 - Логистика в сфере туризма</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp302)
            if call.data == 'raspWed302//':
                rasp302 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon302//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue302//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed302//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu302//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri302//')
                rasp302.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Среда: \n🕒 8:00-9:30 - Менеджмент в маркетинге \n🕒 9:40-11:10 - Основы алгоритмов и программирования \n🕒 11:30-13:00 - Профессиональный английский язык</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp302)
            if call.data == 'raspThu302//':
                rasp302 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon302//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue302//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed302//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu302//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri302//')
                rasp302.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Четверг: \n🕒 8:00-9:30 - Немецкий язык \n🕒 9:40-11:10 - Дизайн для крупного бизнеса \n🕒 11:30-13:00 - Администрирование информационных систем</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp302)
            if call.data == 'raspFri302//':
                rasp302 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon302//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue302//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed302//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu302//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri302//')
                rasp302.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Пятница: \n🕒 8:00-9:30 - Французский язык \n🕒 9:40-11:10 - Высшая математика \n🕒 11:30-13:00 - Бухгалтерский учёт</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp302)

            # -------------------------------------------------------------
            if call.data == 'T4//':
                rasp402 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon402//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue402//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed402//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu402//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri402//')
                rasp402.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp402)
            if call.data == 'raspMon402//':
                rasp402 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon402//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue402//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed402//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu402//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri402//')
                rasp402.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Понедельник: \n🕒 8:00 - 9:30: Философия древнего Рима \n🕒 9:40 - 11:10: Основы алгоритмов и программирования \n🕒 11:30 - 13:00: Профессиональный английский язык</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp402)
            if call.data == 'raspTue402//':
                rasp402 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon402//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue402//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed402//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu402//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri402//')
                rasp402.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Вторник: \n🕒 8:00 - 9:30: Микроэкономика \n🕒 9:40 - 11:10: Английский язык \n🕒 11:30 - 13:00: Логистика и построение маршрутов</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp402)
            if call.data == 'raspWed402//':
                rasp402 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon402//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue402//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed402//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu402//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri402//')
                rasp402.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Среда: \n🕒 8:00 - 9:30: Высшая математика \n🕒 9:40 - 11:10: Немецкий язык \n🕒 11:30 - 13:00: Бухгалтерский учёт</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp402)
            if call.data == 'raspThu402//':
                rasp402 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon402//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue402//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed402//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu402//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri402//')
                rasp402.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Четверг: \n🕒 8:00 - 9:30: Программирование микроконтроллеров \n🕒 9:40 - 11:10: Профессиональный казахский язык \n🕒 11:30 - 13:00: Менеджмент в маркетинге</b",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp402)
            if call.data == 'raspFri402//':
                rasp402 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon402//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue402//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed402//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu402//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri402//')
                rasp402.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Пятница: \n🕒 8:00 - 9:30: Макроэкономика \n🕒 9:40 - 11:10: Французский язык \n🕒 11:30 - 13:00: Дизайн логотипов в крупных компаниях</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp402)

            if call.data == 'market//':
                market = types.InlineKeyboardMarkup(row_width=2)
                market1 = types.InlineKeyboardButton("1 курс", callback_data='M1//')
                market2 = types.InlineKeyboardButton("2 курс", callback_data='M2//')
                market3 = types.InlineKeyboardButton("3 курс", callback_data='M3//')
                market4 = types.InlineKeyboardButton("4 курс", callback_data='M4//')

                market.add(market1, market2, market3, market4)
                bot.send_message(call.message.chat.id, "<b>На каком курсе вы учитесь?</b>", parse_mode='html',
                                 reply_markup=market)

            # -------------------------------------------------------------
            if call.data == 'M1//':
                rasp101 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon101//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue101//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed101//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu101//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri101//')
                rasp101.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp101)
            if call.data == 'raspMon101':
                rasp101 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon101//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue101//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed101//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu101//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri101//')
                rasp101.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Понедельник: \n🕒 8:00 - 9:30 - Высшая математика \n🕒 9:40 - 11:10 - Основы алгоритмов и программирования \n🕒 11:30 - 13:00 - Микроэкономика</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp101)
            if call.data == 'raspTue101//':
                rasp101 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon101//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue101//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed101//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu101//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri101//')
                rasp101.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Вторник: \n🕒 8:00- 9:30 - Логистика в сфере туризма \n🕒 9:40- 11:10 – Макроэкономика \n🕒 11:30 - 13:00 - Философия древнего Рима</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp101)
            if call.data == 'raspWed101//':
                rasp101 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon101//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue101//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed101//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu101//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri101//')
                rasp101.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Среда: \n🕒 9:00-11:00 - Французский язык \n🕒 9:40 - 11:10 - Немецкий язык \n🕒 11:30 - 13:00 - Английский язык</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp101)
            if call.data == 'raspThu101//':
                rasp101 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon101//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue101//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed101//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu101//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri101//')
                rasp101.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Четверг: \n🕒 8:00 - 9:30 - Профессиональный казахский язык \n🕒 9:40 - 11:10 - Казахский язык \n🕒 11:30 - 13:00 - Профессиональный английский язык</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp101)
            if call.data == 'raspFri101//':
                rasp101 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon101//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue101//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed101//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu101//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri101//')
                rasp101.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Пятница: \n🕒 8:00 - 9:30 - Программирования микроконтроллеров \n🕒 9:40 - 11:10 - Менеджмент в маркетинге \n🕒 11:30 - 13:00 - Дизайн логотипов в крупных компаниях</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp101)

            # --------------------------------------------------------------
            if call.data == 'M2//':
                rasp201 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon201//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue201//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed201//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu201//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri201//')
                rasp201.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp201)

            if call.data == 'raspMon201//':
                rasp201 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon201//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue201//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed201//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu201//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri201//')
                rasp201.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Понедельник: \n🕒 8:00-9:30 - Основы алгоритмов и программирования \n🕒 9:40-11:10 - Логистика в сфере туризма \n🕒 11:30-13:00 - Философия древнего Рима</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp201)
            if call.data == 'raspTue201//':
                rasp201 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon201//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue201//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed201//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu201//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri201//')
                rasp201.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Вторник: \n🕒 8:00-9:30 - Профессиональный казахский язык \n🕒 9:40-11:10 – Макроэкономика \n🕒 11:30-13:00 - Программирования операционных систем</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp201)
            if call.data == 'raspWed201//':
                rasp201 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon201//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue201//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed201//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu201//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri201//')
                rasp201.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Среда: \n🕒 8:00-9:30 - Менеджмент в маркетинге \n🕒 9:40-11:10 - Дизайн логотипов в крупных компаниях \n🕒 11:30-13:00 - Логистика и построение маршрутов</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp201)
            if call.data == 'raspThu201//':
                rasp201 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon201//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue201//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed201//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu201//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri201//')
                rasp201.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Четверг: \n🕒 8:00-9:30 - Высшая математика \n🕒 9:40-11:10 - Французский язык \n🕒 11:30-13:00 - Администрирование информационных систем</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp201)
            if call.data == 'raspFri201//':
                rasp201 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon201//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue201//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed201//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu201//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri201//')
                rasp201.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Пятница: \n🕒 8:00-9:30 – Микроэкономика \n🕒 9:40-11:10 - Бухгалтерский учет \n🕒 11:30-13:00 - Дизайн для крупного бизнеса</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp201)

            # ---------------------------------------------------------------
            if call.data == 'M3//':
                rasp301 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon301//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue301//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed301//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu301//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri301//')
                rasp301.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp301)

            if call.data == 'raspMon301//':
                rasp301 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon301//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue301//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed301//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu301//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri301//')
                rasp301.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Понедельник: \n🕒 8:00-9:30 - Французский язык \n🕒 9:40-11:10 - Администрирование информационных систем \n🕒 11:30-13:00 - Менеджмент в маркетинге</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp301)
            if call.data == 'raspTue301//':
                rasp301 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon301//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue301//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed301//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu301//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri301//')
                rasp301.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Вторник: \n🕒 8:00-9:30 - Логистика и построение маршрутов \n🕒 9:40-11:10 - Дизайн для крупного бизнеса \n🕒 11:30-13:00 - Основы алгоритмов и программирования</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp301)
            if call.data == 'raspWed301//':
                rasp301 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon301//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue301//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed301//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu301//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri301//')
                rasp301.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Среда: \n🕒 8:00-9:30 – Макроэкономика \n🕒 9:40-11:10 - Программирования операционных систем \n🕒 11:30-13:00 - Микроэкономика</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp301)
            if call.data == 'raspThu301//':
                rasp301 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon301//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue301//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed301//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu301//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri301//')
                rasp301.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Четверг: \n🕒 8:00-9:30 - Профессиональный английский язык \n🕒 9:40-11:10 – Микроэкономика \n🕒 11:30-13:00 - Дизайн логотипов в крупных компаниях</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp301)
            if call.data == 'raspFri301//':
                rasp301 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon301//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue301//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed301//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu301//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri301//')
                rasp301.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Пятница: \n🕒 8:00-9:30 - Высшая математика \n🕒 9:40-11:10 - Немецкий язык \n🕒11:30-13:00 - Бухгалтерский учет</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp301)

            # ---------------------------------------------------------------
            if call.data == 'M4//':
                rasp401 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon401//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue401//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed401//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu401//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri401//')
                rasp401.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp401)

            if call.data == 'raspMon401//':
                rasp401 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon401//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue401//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed401//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu401//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri401//')
                rasp401.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Понедельник: \n🕒 8:00 - 9:30: Английский язык \n🕒 9:40 - 11:10: Макроэкономика \n🕒 11:30 - 13:00: Логистика в сфере туризма</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp401)
            if call.data == 'raspTue401//':
                rasp401 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon401//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue401//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed401//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu401//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri401//')
                rasp401.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Вторник: \n🕒 8:00 - 9:30: Основы алгоритмов и программирования \n🕒 9:40 - 11:10: Французский язык \n🕒 11:30 - 13:00: Профессиональный казахский язык</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp401)
            if call.data == 'raspWed401//':
                rasp401 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon401//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue401//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed401//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu401//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri401//')
                rasp401.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Среда: \n🕒 8:00 - 9:30: Высшая математика \n🕒 9:40 - 11:10: Немецкий язык \n🕒 11:30 - 13:00: Дизайн для крупного бизнеса</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp401)
            if call.data == 'raspThu401//':
                rasp401 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon401//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue401//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed401//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu401//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri401//')
                rasp401.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Четверг: \n🕒 8:00 - 9:30: Микроэкономика \n🕒 9:40 - 11:10: Программирование микроконтроллеров \n🕒 11:30 - 13:00: Бухгалтерский учёт</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp401)
            if call.data == 'raspFri401//':
                rasp401 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon401//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue401//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed401//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu401//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri401//')
                rasp401.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Пятница: \n🕒 8:00 - 9:30: Казахский язык \n🕒 9:40 - 11:10: Бухгалтерский учёт \n🕒 11:30 - 13:00: Немецкий язык</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp401)

            if call.data == 'infosys':
                info = types.InlineKeyboardMarkup(row_width=2)
                info1 = types.InlineKeyboardButton("1 курс", callback_data='I1//')
                info2 = types.InlineKeyboardButton("2 курс", callback_data='I2//')
                info3 = types.InlineKeyboardButton("3 курс", callback_data='I3//')
                info4 = types.InlineKeyboardButton("4 курс", callback_data='I4//')

                info.add(info1, info2, info3, info4)
                bot.send_message(call.message.chat.id, "<b>На каком курсе вы учитесь?</b>", parse_mode='html',
                                 reply_markup=info)

            # ----------------------------------------------------------------
            if call.data == 'I1//':
                rasp103 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon103//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue103//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed103//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu103//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri103//')
                rasp103.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp103)

            if call.data == 'raspMon103//':
                rasp103 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon103//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue103//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed103//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu103//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri103//')
                rasp103.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Понедельник: \n🕒 8:00-9:30 - Основы алгоритмов и программирования \n🕒 9:40-11:10 - Программирования микроконтроллеров \n🕒 11:30-13:00 - Дизайн логотипов в крупных компаниях</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp103)
            if call.data == 'raspTue103//':
                rasp103 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon103//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue103//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed103//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu103//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri103//')
                rasp103.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Вторник: \n🕒 8:00-9:30 – Макроэкономика \n🕒 9:40-11:10 - Менеджмент в маркетинге \n🕒 11:30-13:00 - Логистика и построение маршрутов</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp103)
            if call.data == 'raspWed103//':
                rasp103 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon103//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue103//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed103//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu103//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri103//')
                rasp103.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Среда: \n🕒 8:00-9:30 - Высшая математика \n🕒 9:40-11:10 - Профессиональный английский язык \n🕒 11:30-13:00 - Администрирование информационных систем</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp103)
            if call.data == 'raspThu103//':
                rasp103 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon103//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue103//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed103//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu103//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri103//')
                rasp103.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Четверг: \n🕒 8:00-9:30 - Философия древнего Рима \n🕒 9:40-11:10 - Французский язык \n🕒 11:30-13:00 - Немецкий язык</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp103)
            if call.data == 'raspFri103//':
                rasp103 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon103//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue103//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed103//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu103//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri103//')
                rasp103.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Пятница: \n🕒 8:00-9:30 – Микроэкономика \n🕒 9:40-11:10 - Бухгалтерский учет \n🕒 11:30-13:00 - Логистика в сфере туризма</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp103)

            # ------------------------------------------------------------------
            if call.data == 'I2//':
                rasp203 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon203//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue203//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed203//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu203//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri203//')
                rasp203.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp203)

            if call.data == 'raspMon203//':
                rasp203 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon203//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue203//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed203//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu203//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri203//')
                rasp203.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Понедельник: \n🕒 8:00-9:30 - Программирования микроконтроллеров \n🕒 9:40-11:10 – Немецкий язык \n🕒 11:30-13:00 - Профессиональный казахский язык</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp203)
            if call.data == 'raspTue203//':
                rasp203 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon203//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue203//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed203//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu203//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri203//')
                rasp203.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Вторник: \n🕒 8:00-9:30 - Дизайн логотипов в крупных компаниях \n🕒 9:40-11:10 - Логистика в сфере туризма \n🕒 11:30-13:00 - Администрирование информационных систем</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp203)
            if call.data == 'raspWed203//':
                rasp203 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon203//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue203//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed203//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu203//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri203//')
                rasp203.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Среда: \n🕒 8:00-9:30 - Философия древнего Рима \n🕒 9:40-11:10 – Макроэкономика \n🕒 11:30-13:00 - Программирования операционных систем</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp203)
            if call.data == 'raspThu203//':
                rasp203 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon203//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue203//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed203//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu203//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri203//')
                rasp203.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Четверг: \n🕒 8:00-9:30 - Менеджмент в маркетинге \n🕒 9:40-11:10 - Немецкий язык \n🕒 11:30-13:00 - Основы алгоритмов и программирования</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp203)
            if call.data == 'raspFri203//':
                rasp203 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon203//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue203//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed203//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu203//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri203//')
                rasp203.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Пятница: \n🕒 8:00-9:30 - Логистика и построение маршрутов \n🕒 9:40-11:10 - Бухгалтерский учет \n🕒 11:30-13:00 - Микроэкономика</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp203)

            # ------------------------------------------------------------------
            if call.data == 'I3//':
                rasp303 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon303//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue303//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed303//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu303//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri303//')
                rasp303.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp303)

            if call.data == 'raspMon303//':
                rasp303 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon303//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue303//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed303//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu303//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri303//')
                rasp303.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Понедельник: \n🕒 8:00 - 9:30: Микроэкономика \n🕒 9:40 - 11:10: Основы алгоритмов и программирования \n🕒 11:30 - 13:00: Профессиональный казахский язык</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp303)
            if call.data == 'raspTue303//':
                rasp303 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon303//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue303//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed303//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu303//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri303//')
                rasp303.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Вторник: \n🕒 8:00 - 9:30: Высшая математика \n🕒9:40 - 11:10: Английский язык \n🕒 11:30 - 13:00: Программирование микроконтроллеров</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp303)
            if call.data == 'raspWed303//':
                rasp303 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon303//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue303//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed303//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu303//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri303//')
                rasp303.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Среда: \n🕒 8:00 - 9:30: Макроэкономика \n🕒 9:40 - 11:10: Немецкий язык \n🕒11:30 - 13:00: Бухгалтерский учёт</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp303)
            if call.data == 'raspThu303//':
                rasp303 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon303//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue303//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed303//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu303//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri303//')
                rasp303.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Четверг: \n🕒 8:00 - 9:30: Философия древнего Рима \n🕒 9:40 - 11:10: Профессиональный английский язык \n🕒 11:30 - 13:00: Администрирование информационных систем</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp303)
            if call.data == 'raspFri303//':
                rasp303 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon303//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue303//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed303//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu303//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri303//')
                rasp303.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Пятница: \n🕒 8:00 - 9:30: Логистика в сфере туризма \n🕒 9:40 - 11:10: Французский язык \n🕒 11:30 - 13:00: Дизайн для крупного бизнеса</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp303)

            # ------------------------------------------------------------------
            if call.data == 'I4//':
                rasp403 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon403//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue403//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed403//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu403//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri403//')
                rasp403.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp403)

            if call.data == 'raspMon403//':
                rasp403 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon403//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue403//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed403//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu403//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri403//')
                rasp403.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Понедельник: \n🕒 8:00 - 9:30: Высшая математика \n🕒 9:40 - 11:10: Профессиональный английский язык \n🕒 11:30 - 13:00: Программирование операционных систем</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp403)
            if call.data == 'raspTue403//':
                rasp403 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon403//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue403//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed403//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu403//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri403//')
                rasp403.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Вторник: \n🕒 8:00 - 9:30: Микроэкономика \n🕒 9:40 - 11:10: Английский язык \n🕒 11:30 - 13:00: Дизайн логотипов в крупных компаниях</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp403)
            if call.data == 'raspWed403//':
                rasp403 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon403//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue403//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed403//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu403//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri403//')
                rasp403.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Среда: \n🕒 8:00 - 9:30: Логистика в сфере туризма \n🕒 9:40 - 11:10: Основы алгоритмов и программирования \n🕒 11:30 - 13:00: Менеджмент в маркетинге</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp403)
            if call.data == 'raspThu403//':
                rasp403 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon403//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue403//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed403//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu403//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri403//')
                rasp403.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Четверг: \n🕒 8:00 - 9:30: Высшая математика \n🕒 9:40 - 11:10: Профессиональный казахский язык \n🕒 11:30 - 13:00: Казахский язык</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp403)
            if call.data == 'raspFri403//':
                rasp403 = types.InlineKeyboardMarkup(row_width=2)
                raspMon = types.InlineKeyboardButton("Понедельник", callback_data='raspMon403//')
                raspTue = types.InlineKeyboardButton("Вторник", callback_data='raspTue403//')
                raspWed = types.InlineKeyboardButton("Среда", callback_data='raspWed403//')
                raspThu = types.InlineKeyboardButton("Четверг", callback_data='raspThu403//')
                raspFri = types.InlineKeyboardButton("Пятница", callback_data='raspFri403//')
                rasp403.add(raspMon, raspTue, raspWed, raspThu, raspFri)
                bot.send_message(call.message.chat.id,
                                 f"<b>📅Пятница: \n🕒8:00 - 9:30: Макроэкономика \n🕒9:40 - 11:10: Немецкий язык \n🕒11:30 - 13:00: Логистика и построение маршрутов</b>",
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, "<b>Выбирай день недели и я отправлю тебе расписание!</b>",
                                 parse_mode='html', reply_markup=rasp403)

            if call.data=='emodzi':
                emodzi = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Информация о ботe 📄")
                item2 = types.KeyboardButton("Информация о учебном заведение 🏫")
                item3 = types.KeyboardButton("Настройки ⚙️")
                item4 = types.KeyboardButton("Расписание 📑")
                item5 = types.KeyboardButton("Преподаватели 🧑🏻‍🏫")
                item6 = types.KeyboardButton("Студент 🎓")
                emodzi.add(item1, item2, item3, item4, item5, item6)

                bot.send_message(call.message.chat.id,
                                 f"Ваши настройки сохранены",
                                 parse_mode='html', reply_markup=emodzi)
            if call.data=='Zhirniioff':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Информация о боте 📄")
                item2 = types.KeyboardButton("Информация о учебном заведение 🏫")
                item3 = types.KeyboardButton("Настройки ⚙️")
                item4 = types.KeyboardButton("Расписание 📑")
                item5 = types.KeyboardButton("Преподаватели 🧑🏻‍🏫")
                item6 = types.KeyboardButton("Студент 🎓")
                markup.add(item1, item2, item3, item4, item5, item6)

                bot.send_message(call.message.chat.id,
                                 f"Ваши настройки сохранены",
                                 parse_mode='html', reply_markup=markup)







#--------------------------------------------------------------Расписание преподавателей
            if call.data=='210':
                bot.send_message(call.message.chat.id,"🧑🏻‍🎓Преподаватель: Касенова Айжан \n👩🏻‍🏫Предмет: Высшая математика \n🎓Аудитория: 210", parse_mode='html' )
#------------------------------------------------------------------------
            if call.data=='105':
                bot.send_message(call.message.chat.id, "🧑🏻‍🎓Преподаватель: Смирнов Сергей \n👩🏻‍🏫Предмет: Основы алгоритмов и программирования \n🎓Аудитория: 105",
                                 parse_mode='html')
#------------------------------------------------------------------------
            if call.data=='230':
                bot.send_message(call.message.chat.id, "🧑🏻‍🎓Преподаватель: Русланова Рамина \n👩🏻‍🏫Предмет: Микроэкономика \n🎓Аудитория: 230",
                                 parse_mode='html')
#======================================================
            if call.data=='111':
                bot.send_message(call.message.chat.id, "🧑🏻‍🎓Преподаватель: Ильясова Мейрамгуль \n👩🏻‍🏫Предмет: Логистика в сфере туризма \n🎓Аудитория: 111",
                                 parse_mode='html')

            if call.data=='132':
                bot.send_message(call.message.chat.id, "🧑🏻‍🎓Преподаватель: Аятов Жандос\n👩🏻‍🏫Предмет: Макроэкономика \n🎓Аудитория: 132",
                                 parse_mode='html')

            if call.data=='58':
                bot.send_message(call.message.chat.id, "🧑🏻‍🎓Преподаватель: Крусп Едвард\n👩🏻‍🏫Предмет:Философия древнего Рима \n🎓Аудитория: 58",
                                 parse_mode='html')
            if call.data=='69':
                bot.send_message(call.message.chat.id, "🧑🏻‍🎓Преподаватель: Устинов Максим \n👩🏻‍🏫Предмет: Французкий язык \n🎓Аудитория: 69",
                                 parse_mode='html')
            if call.data=='178':
                bot.send_message(call.message.chat.id, "🧑🏻‍🎓Преподаватель: Моисова Татьяна \n👩🏻‍🏫Предмет: Немецкий язык \n🎓Аудитория: 178",
                                 parse_mode='html')
            if call.data=='51':
                bot.send_message(call.message.chat.id, "🧑🏻‍🎓Преподаватель: Тихая Валентина \n👩🏻‍🏫Предмет: Английский язык \n🎓Аудитория:51",
                                 parse_mode='html')
            if call.data=='21':
                bot.send_message(call.message.chat.id, "🧑🏻‍🎓Преподаватель: Романов Илья \n👩🏻‍🏫Предмет: Профессиональный казахский язык\n🎓Аудитория:21",
                                 parse_mode='html')
            if call.data=='11':
                bot.send_message(call.message.chat.id, "🧑🏻‍🎓Преподаватель: Воробьёв Иван \n👩🏻‍🏫Предмет: Казахский язык \n🎓Аудитория: 11",
                                 parse_mode='html')
            if call.data=='32':
                bot.send_message(call.message.chat.id, "🧑🏻‍🎓Преподаватель:Пахтинова Варвара \n👩🏻‍🏫Предмет: Профессиональный английский язык \n🎓Аудитория: 32",
                                 parse_mode='html')

            if call.data=='271':
                bot.send_message(call.message.chat.id, "🧑🏻‍🎓Преподаватель: Данияров Аскар \n👩🏻‍🏫Предмет: Программирования микроконтроллеров \n🎓Аудитория: 271",
                                 parse_mode='html')
            if call.data=='199':
                bot.send_message(call.message.chat.id, "🧑🏻‍🎓Преподаватель: Болатов Елдос \n👩🏻‍🏫Предмет: Менеджмент в маркетинге \n🎓Аудитория: 199",
                                 parse_mode='html')
            if call.data=='205':
                bot.send_message(call.message.chat.id, "🧑🏻‍🎓Преподаватель: Серикова Айнура \n👩🏻‍🏫Предмет: Дизайн логотипов в крупных компаниях \n🎓Аудитория: 205",
                                 parse_mode='html')
            if call.data=='106':
                bot.send_message(call.message.chat.id, "🧑🏻‍🎓Преподаватель: Фоменко Артур \n👩🏻‍🏫Предмет: Бухгалтерский учёт  \n🎓Аудитория: 106",
                                 parse_mode='html')
            if call.data=='201':
                bot.send_message(call.message.chat.id, "🧑🏻‍🎓Преподаватель: Нурболатов Нурлан \n👩🏻‍🏫Предмет: Программирования операционных систем \n🎓Аудитория: 201",
                                 parse_mode='html')
            if call.data=='189':
                bot.send_message(call.message.chat.id, "🧑🏻‍🎓Преподаватель: Ахметжанова Абзал \n👩🏻‍🏫Предмет: Администирование информационных систем \n🎓Аудитория: 189",
                                 parse_mode='html')
            if call.data=='198':
                bot.send_message(call.message.chat.id, "🧑🏻‍🎓Преподаватель: Искандеров Асылхан \n👩🏻‍🏫Предмет: Дизайн для крупного бизнеса  \n🎓Аудитория: 198",
                                 parse_mode='html')
            if call.data=='207':
                bot.send_message(call.message.chat.id, "🧑🏻‍🎓Преподаватель: Ходжанова Айгуль \n👩🏻‍🏫Предмет: Логистика и построение маршрутов \n🎓Аудитория: 207",
                                 parse_mode='html')


            #--------------------------------------------------------------Расписание преподавателей без смайликов
            if call.data=='210*':
                bot.send_message(call.message.chat.id, "Преподаватель: Касенова Айжан\nПредмет: Высшая математика \nАудитория: 210",
                                 parse_mode='html')
            if call.data=='105*':
                bot.send_message(call.message.chat.id, "Преподаватель: Смирнов Сергей \nПредмет: Основы алгоритмов и программирования \nАудитория: 105",
                                 parse_mode='html')

            if call.data=='230*':
                bot.send_message(call.message.chat.id, "Преподаватель: Русланова Рамина \nПредмет: Микроэкономика \nАудитория: 230",
                                 parse_mode='html')

            if call.data=='111*':
                bot.send_message(call.message.chat.id, "Преподаватель: Ильясова Мейрамгуль \nПредмет: Логистика в сфере туризма \nАудитория: 111",
                                 parse_mode='html')
            if call.data=='132*':
                bot.send_message(call.message.chat.id, "Преподаватель: Аятов Жандос \nПредмет: Макроэкономика  \nАудитория: 132",
                                 parse_mode='html')
            if call.data=='58*':
                bot.send_message(call.message.chat.id, "Преподаватель: Крусп Едвард \nПредмет: Философия древнего Рима \nАудитория: 58",
                                 parse_mode='html')
            if call.data=='69*':
                bot.send_message(call.message.chat.id, "Преподаватель: Устинов Максим \nПредмет: Французкий язык \nАудитория: 69",
                                 parse_mode='html')
            if call.data=='178*':
                bot.send_message(call.message.chat.id, "Преподаватель: Моисова Татьяна \nПредмет: Немецкий язык \nАудитория: 178",
                                 parse_mode='html')
            if call.data=='51*':
                bot.send_message(call.message.chat.id, "Преподаватель: Тихая Валентина \nПредмет: Английский язык \nАудитория: 51",
                                 parse_mode='html')
            if call.data=='21*':
                bot.send_message(call.message.chat.id, "Преподаватель: Романов Илья \nПредмет: Профессиональный казахский язык \nАудитория: 21",
                                 parse_mode='html')
            if call.data=='11*':
                bot.send_message(call.message.chat.id, "Преподаватель: Воробьёв Иван \nПредмет: Казахский язык \nАудитория: 11",
                                 parse_mode='html')
            if call.data=='32*':
                bot.send_message(call.message.chat.id, "Преподаватель: Пахтинова Варвара \nПредмет: Профессиональный английский язык \nАудитория: 32",
                                 parse_mode='html')
            if call.data=='271*':
                bot.send_message(call.message.chat.id, "Преподаватель: Данияров Аскар \nПредмет: Программирования микроконтроллеров \nАудитория: 271",
                                 parse_mode='html')
            if call.data=='199*':
                bot.send_message(call.message.chat.id, "Преподаватель: Болатов Елдос \nПредмет: Менеджмент в маркетинге \nАудитория: 199",
                                 parse_mode='html')
            if call.data=='205*':
                bot.send_message(call.message.chat.id, "Преподаватель: Серикова Айнура \nПредмет: Дизайн логотипов в крупных компаниях \nАудитория: 205",
                                 parse_mode='html')
            if call.data=='106*':
                bot.send_message(call.message.chat.id, "Преподаватель: Фоменко Артур \nПредмет: Бухгалтерский учёт  \nАудитория: 106",
                                 parse_mode='html')
            if call.data=='201*':
                bot.send_message(call.message.chat.id, "Преподаватель: Нурболатов Нурлан \nПредмет: Программирования операционных систем \nАудитория: 201",
                                 parse_mode='html')
            if call.data=='189*':
                bot.send_message(call.message.chat.id, "Преподаватель: Ахметжанова Абзал \nПредмет: Администирование информационных систем \nАудитория: 189",
                                 parse_mode='html')
            if call.data=='198*':
                bot.send_message(call.message.chat.id, "Преподаватель: Искандеров Асылхан\nПредмет: Дизайн для крупного бизнеса  \nАудитория: 198",
                                 parse_mode='html')
            if call.data=='207*':
                bot.send_message(call.message.chat.id, "Преподаватель: Ходжанова Айгуль \nПредмет: Логистика и построение маршрутов \nАудитория: 207",
                                 parse_mode='html')

            #--------------------------------------------------------------Расписание преподавателей жирным шрифтом
            if call.data=='210//':
                bot.send_message(call.message.chat.id, "<b>🧑🏻‍🎓Преподаватель: Касенова Айжан \n👩🏻‍🏫Предмет: Высшая математика \n🎓Аудитория: 210</b>",
                                 parse_mode='html')
            if call.data=='105//':
                bot.send_message(call.message.chat.id, "<b>🧑🏻‍🎓Преподаватель: Смирнов Сергей \n👩🏻‍🏫Предмет: Основы алгоритмов и программирования \n🎓Аудитория: 105</b>",
                                 parse_mode='html')

            if call.data=='230//':
                bot.send_message(call.message.chat.id, "<b>🧑🏻‍🎓Преподаватель: Русланова Рамина \n👩🏻‍🏫Предмет: Микроэкономика \n🎓Аудитория: 230</b>",
                                 parse_mode='html')
            if call.data=='111//':
                bot.send_message(call.message.chat.id, "<b>🧑🏻‍🎓Преподаватель: Ильясова Мейрамгуль \n👩🏻‍🏫Предмет: Логистика и построение маршрутов \n🎓Аудитория: 111</b>",
                                 parse_mode='html')
            if call.data=='132//':
                bot.send_message(call.message.chat.id, "<b>🧑🏻‍🎓Преподаватель: Аятов Жандос \n👩🏻‍🏫Предмет: Макроэкономика  \n🎓Аудитория: 132</b>",
                                 parse_mode='html')
            if call.data=='58//':
                bot.send_message(call.message.chat.id, "<b>🧑🏻‍🎓Преподаватель: Крусп Едвард \n👩🏻‍🏫Предмет: Философия древнего Рима \n🎓Аудитория: 58</b>",
                                 parse_mode='html')
            if call.data=='69//':
                bot.send_message(call.message.chat.id, "<b>🧑🏻‍🎓Преподаватель: Устинов Максим \n👩🏻‍🏫Предмет: Французкий язык \n🎓Аудитория: 69</b>",
                                 parse_mode='html')
            if call.data=='178//':
                bot.send_message(call.message.chat.id, "<b>🧑🏻‍🎓Преподаватель: Моисова Татьяна \n👩🏻‍🏫Предмет: Немецкий язык \n🎓Аудитория: 178</b>",
                                 parse_mode='html')
            if call.data=='51//':
                bot.send_message(call.message.chat.id, "<b>🧑🏻‍🎓Преподаватель: Тихая Валентина \n👩🏻‍🏫Предмет: Английский язык \n🎓Аудитория: 51</b>",
                                 parse_mode='html')
            if call.data=='21//':
                bot.send_message(call.message.chat.id, "<b>🧑🏻‍🎓Преподаватель: Романов Илья \n👩🏻‍🏫Предмет: Профессиональный казахский язык \n🎓Аудитория: 21</b>",
                                 parse_mode='html')
            if call.data=='11//':
                bot.send_message(call.message.chat.id, "<b>🧑🏻‍🎓Преподаватель: Воробьёв Иван \n👩🏻‍🏫Предмет: Казахский язык \n🎓Аудитория: 11</b>",
                                 parse_mode='html')
            if call.data=='32//':
                bot.send_message(call.message.chat.id, "<b>🧑🏻‍🎓Преподаватель: Пахтинова Варвара \n👩🏻‍🏫Предмет: Профессиональный английский язык \n🎓Аудитория: 32</b>",
                                 parse_mode='html')
            if call.data=='271//':
                bot.send_message(call.message.chat.id, "<b>🧑🏻‍🎓Преподаватель: Данияров Аскар \n👩🏻‍🏫Предмет: Программирования микроконтроллеров \n🎓Аудитория: 271</b>",
                                 parse_mode='html')
            if call.data=='199//':
                bot.send_message(call.message.chat.id, "<b>🧑🏻‍🎓Преподаватель: Болатов Елдос \n👩🏻‍🏫Предмет: Менеджмент в маркетинге \n🎓Аудитория: 199</b>",
                                 parse_mode='html')
            if call.data=='205//':
                bot.send_message(call.message.chat.id, "<b>🧑🏻‍🎓Преподаватель: Серикова Айнура \n👩🏻‍🏫Предмет: Дизайн логотипов в крупных компаниях \n🎓Аудитория: 205</b>",
                                 parse_mode='html')
            if call.data=='106//':
                bot.send_message(call.message.chat.id, "<b>🧑🏻‍🎓Преподаватель: Фоменко Артур \n👩🏻‍🏫Предмет: Бухгалтерский учёт  \n🎓Аудитория: 106</b>",
                                 parse_mode='html')
            if call.data=='201//':
                bot.send_message(call.message.chat.id, "<b>🧑🏻‍🎓Преподаватель: Нурболатов Нурлан \n👩🏻‍🏫Предмет: Программирования операционных систем \n🎓Аудитория: 201</b>",
                                 parse_mode='html')
            if call.data=='189//':
                bot.send_message(call.message.chat.id, "<b>🧑🏻‍🎓Преподаватель: Ахметжанова Абзал \n👩🏻‍🏫Предмет: Администирование информационных систем\n🎓Аудитория: 189</b>",
                                 parse_mode='html')
            if call.data=='198//':
                bot.send_message(call.message.chat.id, "<b>🧑🏻‍🎓Преподаватель: Искандеров Асылхан\n👩🏻‍🏫Предмет: Дизайн для крупного бизнеса \n🎓Аудитория: 198</b>",
                                 parse_mode='html')
            if call.data=='207//':
                bot.send_message(call.message.chat.id, "<b>🧑🏻‍🎓Преподаватель: Ходжанова Айгуль \n👩🏻‍🏫Предмет: Логистика и построение маршрутов \n🎓Аудитория: 207</b>",
                                 parse_mode='html')
    except Exception as e:
        print(repr(e))


# -----------------------------------------------------------------


# Старт
bot.polling(none_stop=True)