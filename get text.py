import requests
from bs4 import BeautifulSoup


def list_of_champs():
    url = 'http://ddragon.leagueoflegends.com/cdn/12.2.1/data/en_US/champion.json'
    r = requests.get(url)
    data = r.json()
    champ_list = []
    for champ in data['data']:
        champ_list.append(champ.lower())
    return champ_list


def main():
    l = list_of_champs()
    result = []
    for champ in l:
        url = f'https://universe.leagueoflegends.com/en_US/story/champion/{champ}/'
        r = requests.get(url)

        soup = BeautifulSoup(r.content, 'html.parser')
        meta_description = soup.find("meta", property="og:description")
        txt = meta_description['content']

        list = [x.strip() for x in txt.split('.')]

        x = 0
        description = ''
        while x < 5 and x < len(list):
            if list[x] == '':
                description += '.'
            else:
                description = f'{description} {list[x]}.'
            x += 1

        description = description.strip().replace(
            '’', "'").replace('—', '-').replace('–', '-').replace('…', '...').replace('“', '"').replace('”', '"').replace('ç', 'c').replace('\xa0', ' ').replace('ü', 'u')
        result.append(description)
    print(result)

    f = open('sentences.txt', 'a')
    for txt in result:
        f.write(txt + '\n')
    f.close


main()
