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
