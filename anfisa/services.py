import requests


def what_weather(city):
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 2,
        'M': ''
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text.strip()
    else:
        return '<ошибка на сервере погоды. попробуйте позже>'

def what_temperature(weather):    
    if (weather == '<сетевая ошибка>' or
        weather == '<ошибка на сервере погоды. попробуйте позже>'):
        return weather
    temperature = weather.split()[1]
    parsed_temperature = ''
    for char in temperature:
        if char == '-':
            parsed_temperature += char
        try:
            num = int(char)
            parsed_temperature += char
        except ValueError:
            continue
    return parsed_temperature


def what_conclusion(parsed_temperature):
    try:
        temperature = int(parsed_temperature)

        # Теперь можно сравнивать temperature с заданными пределами 18°С и 27°С
        # и возвращать нужные фразы в зависимости от результатов сравнения.
        
        if temperature < 18:
                return ('Бррррр&#129398&#129398&#129398 холллодддднооо! ' 
                        'Как же холодно!!!&#129482&#129398&#128534&#128565<br>' 
                        'В такую погоду я бы не ела мороженое, а то ещё ' 
                        'заболеееешь&#129319&#129298&#129301<br>' 
                        'Может лучше глинтвейн&#129396&#128540&#129323 ' 
                        'нуууу, или горячий какао, чтобы согреться&#128523' 
                        '&#129392&#128524')
         # Если температура в диапазоне от 18 до 27 включительно
        elif temperature in range(18, 28):
            return ('Iiiiiiiitssss icecreeeeeaaaam tiiiiiiime!!!<br>' 
                    'Идеальная погода для мороженого! В самый раз!' 
                    '&#9728&#9728&#9728&#128526&#128526&#128526<br>'
                    'Сейчас лягу под зонтик и буду с мороженым представлять ' 
                    'Geminoid DK или Джулса&#128525&#129392&#128514 ' 
                    'кстати Pepper такооой милааашкаа, ну просто заглядение' 
                    '&#128514&#128514&#128514<br>А ты чего сидишь?!<br>' 
                    'Скорее хватай своё любимое мороженное и присоединяйся!')
        else:
            return ('Уффф, ну и жараааа&#129397&#129397 ' 
                    'Жарко! Здесь не обойтись без мороженого&#128523&#128523&#129316<br>' 
                    'Кстати какое твоё любимое?<br>' 
                    'Я вот люблю кибернетическое))<br>' 
                    'Мммм, програмный код с кусочками единиц и нолей, ' 
                    'покрытый соусом из данных&#129316&#129316<br>' 
                    'Теперь ты расскажи про своё любимое))')
            
    except ValueError:
        return ("Не могу узнать погоду(( вечно эти проблемы с инетом " 
                "в неподходящее время&#128530&#128548&#129324<br>Мдааааааа...<br>" 
                "А что насчёт твоего мороженого, решение за тобой " 
                "всё-таки тебе его есть))")
