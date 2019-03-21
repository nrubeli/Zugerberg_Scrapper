import requests


def get_trailstatus():
    url = 'https://zugerbergtrail.ch/'
    r = requests.get(url)
    if r.status_code == 200:
        print('Site was accessed')
        html = r.text
        start_index = html.find('var trailstatus')
        print(html[start_index:(start_index+19)])

        if html[start_index+19] == 1:
            print('Offen')
        elif html[start_index+19] == 2:
            print('Schonprogram')
        elif html[start_index+19] == 3:
            print('Winter')
        elif html[start_index+19] == 4:
            print('Gesperrt')
        else:
            print('Kein Biketransport')
    else:
        print('Site could not be reached')


def main():
    get_trailstatus()


main()
