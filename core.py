import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, delay=2):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise NetworkError(f'Failed to fetch {url} after {retries} attempts')

if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = retry_request(url)
        print(data)
    except NetworkError as e:
        print(e)