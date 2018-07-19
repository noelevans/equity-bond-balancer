import requests
import account_keys


def main():
    key = account_keys.tradier
    url = 'https://sandbox.tradier.com/v1/markets/quotes?symbols=spy'
    # connection = httplib.HTTPSConnection('sandbox.tradier.com', 443, timeout = 30)
    headers = {'Accept':'application/json',
               'Authorization':'Bearer ' + key}

    resp = requests.get(url, headers=headers)
    print(resp.json())


if __name__ == '__main__':
    main()
