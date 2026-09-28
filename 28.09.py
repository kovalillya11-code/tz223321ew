from flask import Flask

app = Flask(__name__)

STYLE = """
<style>
    body {
        background-color: black;
        color: white;
        font-family: Arial, sans-serif;
        padding: 20px;
    }
    a {
         color: #1e90ff; /* Світло-блакитний колір для посилань*/
     }
    a:hover {
        color: #00bfff;
    }
    /* Стилізація прокручування */
    ::-webkit-scrollbar {
        width: 12px;
    }
    ::-webkit-scrollbar-track {
        background: black;
    }
    ::-webkit-scrollbar-thumb {
        background-color: #333;
        border-radius: 6px;
        border: 3px solid black;
    }
    ::-webkit-scrollbar-button {
        display: none;
    }

    /* Стилізація */
    html {
        scrollbar-width: thin;
        scrollbar-color: #333 black; 
    }
</style>
"""


@app.route("/")
def home():
    return f"""
    {STYLE}
    <h1>Головне меню веб-додатка</h1>
    
    <h3>Міні-додаток «Моє місто / Хобі»</h3>
    <ul>
        <li><a href="/">Головна сторінка</a></li>
        <li><a href="/history">Історія міста</a></li>
        <li><a href="/gallery">Цікаві місця</a></li>
        <li><a href="/contact">Контакти</a></li>
    </ul>

    <h3>Вікова категорія</h3>
    <ul>
        <li><a href="/age/10">Дитина (/age/10)</a></li>
        <li><a href="/age/15">Підліток (/age/15)</a></li>
        <li><a href="/age/30">Дорослий (/age/30)</a></li>
        <li><a href="/age/65">Літня людина (/age/65)</a></li>
    </ul>

    <h3>Оцінка за бали</h3>
    <ul>
        <li><a href="/grade/95">Відмінно (/grade/95)</a></li>
        <li><a href="/grade/80">Добре (/grade/80)</a></li>
        <li><a href="/grade/65">Задовільно (/grade/65)</a></li>
        <li><a href="/grade/45">Незадовільно (/grade/45)</a></li>
        <li><a href="/grade/120">Помилка: >100 балів (/grade/120)</a></li>
    </ul>

    <h3>Конвертер одиниць</h3>
    <ul>
        <li><a href="/convert/km_to_m/3">Кілометри в метри (/convert/km_to_m/3)</a></li>
        <li><a href="/convert/kg_to_g/5">Кілограми в грами (/convert/kg_to_g/5)</a></li>
        <li><a href="/convert/c_to_f/25">Цельсій у... (/convert/c_to_f/25)</a></li>
        <li><a href="/convert/usd_to_uah/100">USD в UAH (/convert/usd_to_uah/100)</a></li>
        <li><a href="/convert/unknown/10">Помилка: невідома операція</a></li>
    </ul>

    <h3>Калькулятор покупки</h3>
    <ul>
        <li><a href="/shop/apple/3">Яблука 3 шт. (без знижки)</a></li>
        <li><a href="/shop/milk/6">Молоко 6 шт. (зі знижкою -10%)</a></li>
        <li><a href="/shop/bread/5">Хліб 5 шт. (зі знижкою -10%)</a></li>
        <li><a href="/shop/pizza/2">Помилка: невідомий товар</a></li>
    </ul>

    <h3>Погода</h3>
    <ul>
        <li><a href="/temperature/-5">Мороз (/temperature/-5)</a></li>
        <li><a href="/temperature/15">Прохолодно (/temperature/15)</a></li>
        <li><a href="/temperature/25">Тепло (/temperature/25)</a></li>
        <li><a href="/temperature/35">Спека (/temperature/35)</a></li>
    </ul>

    <h3>Математика</h3>
    <ul>
        <li><a href="/math/div/10/0">Ділення на нуль (/math/div/10/0)</a></li>
    </ul>
    """


@app.route("/history")
def history():
    return f"""
    {STYLE}
    <h1>Історія міста</h1>
    <p>Наше місто має багату багатовікову історію, засноване у глибоку давнину, воно розвивалося як важливий культурний та торговий центр.</p>
    <br><a href="/">[ Назад на головну ]</a>
    """


@app.route("/gallery")
def gallery():
    return f"""
    {STYLE}
    <h1>Цікаві місця (список)</h1>
    <ul>
        <li><b>Стара Ратуша</b> — архітектурна пам'ятка у центрі міста.</li>
        <li><b>Центральний парк</b> — чудове місце для відпочинку та прогулянок на свіжому повітрі.</li>
        <li><b>Міський замок</b> — середньовічна фортеця з величними краєвидами.</li>
    </ul>
    <br><a href="/">[ Назад на головну ]</a>
    """


@app.route("/contact")
def contact():
    return f"""
    {STYLE}
    <h1>Контакти</h1>
    <p> Вулиця kj[jd 2 будинок 47</p>
    <br><a href="/">[ Назад на головну ]</a>
    """


@app.route("/age/<int:age>")
def check_age(age):
    if age < 0:
        return f"{STYLE}<h1>Помилка</h1><p>Вік не може бути меншим за 0!</p>", 400

    if age < 13:
        status = "Дитина"
    elif 13 <= age <= 17:
        status = "Підліток"
    elif 18 <= age <= 59:
        status = "Дорослий"
    else:
        status = "Літня людина"

    return f"""
    {STYLE}
    <h1>Визначення вікової категорії</h1>
    <p>Вік: {age} -> Категорія: <b>{status}</b></p>
    <br><a href="/">[ Назад на головну ]</a>
    """


@app.route("/grade/<int:score>")
def get_grade(score):
    if score > 100:
        return (
            f"{STYLE}<h1>Помилка</h1><p>Помилка: максимум 100 балів</p>",
            400,
        )
    if score < 0:
        return (
            f"{STYLE}<h1>Помилка</h1><p>Бал не може бути меншим за 0</p>",
            400,
        )

    if 90 <= score <= 100:
        grade = "Відмінно"
    elif 75 <= score <= 89:
        grade = "Добре"
    elif 60 <= score <= 74:
        grade = "Задовільно"
    else:
        grade = "Незадовільно"

    return f"""
    {STYLE}
    <h1>Оцінка за бали</h1>
    <p>Бал: {score} -> Результат: <b>{grade}</b></p>
    <br><a href="/">[ Назад на головну ]</a>
    """


@app.route("/convert/<unit>/<int:value>")
def convert(unit, value):
    if unit == "km_to_m":
        result = f"{value * 1000} м"
    elif unit == "kg_to_g":
        result = f"{value * 1000} г"
    elif unit == "c_to_f":
        result = f"{value * 9 / 5 + 32} °F"
    elif unit == "usd_to_uah":
        result = f"{value * 40} грн"
    else:
        return (
            f"{STYLE}<h1>Помилка</h1><p>Помилка: невідома операція конвертації '{unit}'</p>",
            400,
        )

    return f"""
    {STYLE}
    <h1>Конвертер одиниць</h1>
    <p>Конвертація [{unit}] для значення {value}: <b>{result}</b></p>
    <br><a href="/">[ Назад на головну ]</a>
    """


@app.route("/shop/<item>/<int:qty>")
def shop(item, qty):
    prices = {"apple": 20, "bread": 30, "milk": 45}

    if item not in prices:
        return (
            f"{STYLE}<h1>Помилка</h1><p>Помилка: невідомий товар '{item}'</p>",
            404,
        )
    if qty <= 0:
        return (
            f"{STYLE}<h1>Помилка</h1><p>Кількість товару повинна бути більшою за 0</p>",
            400,
        )

    total_price = prices[item] * qty

    if qty >= 5:
        total_price = total_price * 0.9
        discount_text = " (Враховано знижку 10% за опт від 5 шт.)"
    else:
        discount_text = ""

    return f"""
    {STYLE}
    <h1>Калькулятор покупки</h1>
    <p>Товар: {item} | Кількість: {qty} шт.</p>
    <p><b>Разом: {total_price:.2f} грн</b>{discount_text}</p>
    <br><a href="/">[ Назад на головну ]</a>
    """


@app.route("/temperature/<t>")
def weather(t):
    try:
        t = int(t)
    except ValueError:
        return "Будь ласка, вкажіть коректне числове значення температури", 400
    if t < 0:
        status = "Мороз"
    elif t <= 20:
        status = "Прохолодно"
    elif t <= 30:
        status = "Тепло"
    else:
        status = "Спека"
    return f'''
    {STYLE}
    <h1>Стан погоди</h1>
    <p>Температура: {t}°C -> На вулиці <b>{status}</b>.</p>
    <br><br><a href="/">[ Назад на головну ]</a>
    '''


@app.route("/math/<operation>/<int:a>/<int:b>")
def advanced_calc(operation, a, b):
    if operation == "add":
        res = str(a + b)
    elif operation == "sub":
        res = str(a - b)
    elif operation == "mul":
        res = str(a * b)
    elif operation == "div":
        if b == 0:
            return (
                f"{STYLE}<h1>Помилка</h1><p>Помилка: Ділення на нуль!</p>",
                400,
            )
        else:
            res = str(a / b)
    else:
        return (
            f"{STYLE}<h1>Помилка</h1><p>Помилка: Невідома операція '{operation}'!</p>",
            400,
        )

    return f"""
    {STYLE}
    <h1>Калькулятор</h1>
    <p>Результат: <b>{res}</b></p>
    <br><a href="/">[ Назад на головну ]</a>
    """


if __name__ == "__main__":
    app.run(debug=True)
