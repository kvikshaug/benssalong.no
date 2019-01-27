import html
import json


with open("database.json") as file_:
    data = json.load(file_)


def data_unescaped():
    data_unescaped = data.copy()
    data_unescaped['åpningstider'] = html.unescape(data_unescaped['åpningstider'])
    data_unescaped['priser'] = html.unescape(data_unescaped['priser'])
    data_unescaped['timebestilling'] = html.unescape(data_unescaped['timebestilling'])
    data_unescaped['nyheter'] = html.unescape(data_unescaped['nyheter'])
    data_unescaped['varetilbud'] = html.unescape(data_unescaped['varetilbud'])
    return data_unescaped


def save(åpningstider, priser, timebestilling, nyheter, varetilbud):
    data['åpningstider'] = html.escape(åpningstider)
    data['priser'] = html.escape(priser)
    data['timebestilling'] = html.escape(timebestilling)
    data['nyheter'] = html.escape(nyheter)
    data['varetilbud'] = html.escape(varetilbud)
    with open("database.json", "w") as file_:
        json.dump(data, file_)
