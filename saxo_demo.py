import requests


def account(filename='account.txt'):
    with open(filename) as file:
        return file.read()


ROOT = 'https://gateway.saxobank.com/sim/openapi/'
ACCOUNT = account()


def main():
    # Log on to get session id
    pass

    # Who am i
    requests.get('{0}port/v1/users/me'.format(ROOT))

    # View ClientKey
    requests.get('{0}port/v1/clients/me'.format(ROOT))

    # Get AccountKey
    # By default, it is the same as the ClientKey but there may be multiple

    # See my account balances
    requests.get('{0}port/v1/balances?AccountKey={1}&ClientKey={1}'.format(
        ROOT, ACCOUNT))

    # Instruments
    # You can fetch summary information about all instruments and option ROOTs
    # fromthe /ref/instruments endpoint. If you need more detailed information
    # about a particular instrument or option ROOT, you must make a secondary
    # call to /instruments/details for instruments and
    # /instruments/contractoptionspaces for options.

    # Instruments containing DKK in lookup
    requests.get(
        '{0}ref/v1/instruments?KeyWords=DKK&AssetTypes=FxSpot'.format(ROOT))
    # This will give UICs to be used in the next query

    # Instrument prices
    url = ('{0}trade/v1/infoprices/list?AccountKey={1}&' +
           'Uics=2047,1311,2046,17749,16&AssetType=FxSpot&Amount=100000&' +
           'FieldGroups=DisplayAndFormat,Quote').format(ROOT, ACCOUNT)
    requests.get(url)


    # Order (post request)
    requests.post(
        '{0}trade/v1/orders'.format(ROOT),
        data={
            'Uic': 16,
            'BuySell': 'Buy',
            'AssetType': 'FxSpot',
            'Amount': 100000,
            'OrderPrice': 7,
            'OrderType': 'Market',
            'OrderRelation': 'StandAlone',
            'OrderDuration': {
                'DurationType': 'GoodTillCancel'
            },
            'AccountKey': ACCOUNT
        })


    # A target price can be set rather than at market price by setting
    # OrderType to "Limit". You can then see while your off market price waits
    # for the right price using this:
    # See my outstanding orders
    requests.get(
        '{0}port/v1/orders/me?fieldGroups=DisplayAndFormat'.format(ROOT))

    # View position
    raw_url = ('{0}port/v1/positions?ClientKey={1}&' +
               'FieldGroups=DisplayAndFormat,PositionBase,PositionView')
    requests.get(raw_url.format(ROOT, ACCOUNT))


if __name__ == '__main__':
    main()
