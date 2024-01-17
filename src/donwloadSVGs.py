import requests
import os
import cairosvg

countries = ['no', 'se', 'fi', 'dk', 'is', 'de', 'nl', 'be', 'lu', 'fr', 'es', 'pt', 'it', 'ch', 'at', 'gb', 'ie', 'pl', 'cz', 'sk', 'hu', 'si', 'hr', 'ba', 'rs', 'me', 'al', 'mk', 'bg', 'ro', 'md', 'ua', 'by', 'lt', 'lv', 'ee', 'ru', 'tr', 'gr', 'cy', 'mt', 'il', 'us', 'ca', 'mx', 'br', 'ar', 'cl', 'uy', 'py', 'bo', 'pe', 'co', 've', 'ec', 'gy', 'sr', 'gf', 'pa', 'cr', 'ni', 'hn', 'sv', 'gt', 'bz', 'jm', 'cu', 'ht', 'do', 'bs', 'bb', 'tt', 'ag', 'dm', 'lc', 'vc', 'gd', 'kn', 'aw', 'ai', 'vg', 'vi', 'ms', 'gp', 'mq', 'tc', 'bm', 'ky', 'gd', 'gl', 'pm', 'wf', 'pf', 'nc', 'vu', 'sb', 'fj', 'to', 'ws', 'ki', 'tv', 'nr', 'pw', 'mh', 'fm', 'mp', 'gu', 'as', 'um', 'ck', 'nu', 'tk', 'ws', 'nf', 'cx', 'cc', 'hm', 'bv', 'tf', 'aq', 'gs', 'bv', 'io', 'ac', 'cp', 'dg', 'ea', 'ta', 'um', 'eu', 'un', 'va', 'xk', 'ps', 'eh', 'mf', 'sj', 'ax', 'gl', 'cw', 'bq', 'sx',]
def write_text(data: str, path: str):
    with open(path, 'w') as file:
        file.write(data)

for country in countries:
    url = 'https://hatscripts.github.io/circle-flags/flags/%s.svg' % country

    svg = requests.get(url).text

    write_text(svg, 'res/images/flags/%s.svg' % country)

    cairosvg.svg2png(url='res/images/flags/%s.svg' % country, write_to='res/images/flags/%s.png' % country)

    os.remove('res/images/flags/%s.svg' % country)
