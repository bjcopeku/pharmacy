# import kivy


def get_corrected_weight(h, w, g):
    if g == 'M':
        ideal = 50 + (2.3 * (h - 60))
    else:
        ideal = 45.5 + (2.3 * (h - 60))

    print('Weight range that does not require adjustment: ', round((0.8 * ideal), 1), "-", round((1.2 * ideal), 1))

    if (w < 0.8 * ideal) or (w > 1.2 * ideal):
        print('Applying adjustment for weight outside IBW range')
        w = (0.4 * (w - ideal)) + ideal

    return w


Age = int(input('Age? '))
height = int(input('Height in inches? '))
weight = float(input('Weight in kilos? '))
SCr = float(input('Serum Creatinine? '))
gender = input('M or F? ')

if height >= 60:
    weight = get_corrected_weight(height, weight, gender)
else:
    print('Cannot use IBW for patients under 60 inches')


if gender == 'F':
    print('Applying adjustment for female gender')
    weight = 0.85 * weight

print('CrCl is:', round((((140 - Age) * weight) / (72 * SCr))))