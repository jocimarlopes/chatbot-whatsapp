import datetime

months = {
    '01' : "Janeiro",
    '02' : "Fevereiro",
    '03' : "Março",
    '04' : "Abril",
    '05' : "Maio",
    '06' : "Junho",
    '07' : "Julho",
    '08' : "Agosto",
    '09' : "Setembro",
    '10' : "Outubro",
    '11' : "Novembro",
    '12' : "Dezembro",
}
frases = {
    'hour': [
        'que horas são',
        'que hora é',
        'horas por favor',
        'que hora são',
        'horas',
    ],
    'date': [
        'que dia é',
        'que dia é hoje',
        'qual a data',
        'qual dia é'
    ]
}

def get_hour():
    x = str(datetime.datetime.now())
    y = x.split(' ')
    d = y[1].split('.')
    hora = d[0].split(':')

    if '00' in hora[0]:
        print(hora)
        return "Agora são 00:{}, senhor.".format(int(hora[1]))
        
    if '01' in hora[0]:
        return "Agora são {}:{}, senhor.".format(int(hora[0]), int(hora[1]))
    else:
        return "Agora são {}:{}, senhor.".format(int(hora[0]), int(hora[1]))


def get_date():
    x = str(datetime.datetime.now())
    y = x.split(' ')
    d = y[0].split('-')
    for month in months:
        if d[1] == month:
            d[1] = months[d[1]]
    return "Hoje é dia {} de {} de {}".format(int(d[2]), d[1], int(d[0]))


def dates(text):
    for item in frases['hour']:
        if item in text:
            return get_hour()
    for item in frases['date']:
        if item in text:
            print(text)
            return get_date()
