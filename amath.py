import math


def declination(c, m, s):
    out = ["", "", ""]
    if c == 1:
        out[0] = " час : "
    elif 1 < c < 5:
        out[0] = " часа : "
    elif c >= 5 or c == 0:
        out[0] = " часов : "
    if m == 1:
        out[1] = " минута : "
    elif 1 < m < 5:
        out[1] = " минуты : "
    elif m >= 5 or m == 0:
        out[1] = " минут : "
    if s == 1:
        out[2] = " секунда."
    elif 1 < s < 5:
        out[2] = " секунды."
    elif s >= 5 or s == 0:
        out[2] = " секунд."
    return out


def correction(lit, grad):
    lit = float(lit)
    grad = float(grad)
    if lit > 0 and (1 < grad < 97):
        x = lit * grad
        y = (x / 100 * 1) / 0.96
        z = y * 3
        c = y * 6
        d = y * 85
        e = z // 180
        f = c / 60
        out_text = "ЭАФ " + str(round(z, 2)) + "\nПодголовья " + \
                   str(round(c, 2)) + "\nТоварный спирт " + \
                   str(round(d, 2)) + "\nСкорость отбора голов мл. в 1 мин. " + \
                   str(round(e, 2)) + "\nСкорость отбора подголовников мл. в мин. " + \
                   str(round(f, 2))
    elif lit <= 0:
        out_text = "Лиров не может быть меньше или равно нулю."
    else:
        out_text = "Градусы должны быть в пределе от 1 до 97"
    return out_text


def rate_harting(V, T, P):
    V = float(V)
    T = float(T)
    P = float(P)
    if P > 0 and V > 0:
        y = 88 - T
        x = (V * 4.2 * y / P)
        s = math.floor(x // 60)
        m = math.floor(x // 120)
        c = math.floor(x // 120)
        time_prefix = declination(c, m, s)
        outText = "Примерное время закипания составит:\n" + \
                  str(c) + time_prefix[0] + \
                  str(m) + time_prefix[1] + \
                  str(s) + time_prefix[2]
    elif (P <= 0):
        outText = "Мощность не иожет быть меньше или равная нулю"
    elif (V <= 0):
        outText = "Объем жидкости не может быть нулевым или меньше нуля."
    return outText
