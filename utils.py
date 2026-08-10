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
        except requests.HTTPError as e:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise NetworkError(f"Failed to fetch {url} after {retries} attempts") from e
        except requests.RequestException as e:
            raise NetworkError(f"Request failed: {e}")

