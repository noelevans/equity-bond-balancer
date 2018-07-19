import quandl
import account_keys

def main():
    quandl.ApiConfig.api_key = account_keys.quandl
    res = quandl.get('BP/WIND_CAP_URY',
                     start_date='2016-12-31',
                     end_date='2016-12-31')
    print(res)


if __name__ == '__main__':
    main()
