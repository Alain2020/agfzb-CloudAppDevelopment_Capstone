import requests
from .models import CarDealer, DealerReview
from requests.auth import HTTPBasicAuth

def post_request(url, json_payload, api_key=None, **kwargs):
    try:
        if api_key:
            response = requests.post(url, json=json_payload, params=kwargs,
                                     auth=HTTPBasicAuth('apikey', api_key))
        else:
            response = requests.post(url, json=json_payload, params=kwargs)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return None
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = response.json()
    return json_data

def get_request(url, api_key=None, **kwargs):
    try:
        if api_key:
            response = requests.get(url, headers={'Content-Type': 'application/json'}, params=kwargs,
                                    auth=HTTPBasicAuth('apikey', api_key))
        else:
            response = requests.get(url, headers={'Content-Type': 'application/json'}, params=kwargs)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return None
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = response.json()
    return json_data

def analyze_review_sentiments(dealerreview, api_key=None):
    url = "https://api.eu-de.natural-language-understanding.watson.cloud.ibm.com/instances/b545aead-a3dc-4b6b-8c62-2a46e8c62980/v1/analyze"
    params = {
        "text": dealerreview,
        "version": "2022-01-01",
        "features": "emotion,sentiment",
        "return_analyzed_text": True
    }
    response = get_request(url, api_key, **params)
    if response:
        return response

def get_dealers_from_cf(url, api_key=None, **kwargs):
    results = []
    json_result = get_request(url, api_key, **kwargs)
    if json_result:
        if isinstance(json_result, list):
            for dealer_doc in json_result:
                dealer = dealer_doc  # Add this line
                dealer_obj = CarDealer(
                    address=dealer.get("address", ""),
                    city=dealer.get("city", ""),
                    full_name=dealer.get("full_name", ""),
                    id=dealer.get("id", ""),
                    lat=dealer.get("lat", 0),
                    long=dealer.get("long", 0),
                    short_name=dealer.get("short_name", ""),
                    st=dealer.get("st", ""),
                    zip=dealer.get("zip", "")
                )
                results.append(dealer_obj)
        else:
            print("Error: Invalid JSON format for dealers data")
    return results


def get_dealer_by_id_from_cf(url, id, api_key=None):
    results = get_request(url, api_key, id=id)
    if results:
        return results[0]
    else:
        return None

def get_dealers_from_cf(url, api_key=None, **kwargs):
    results = []
    json_result = get_request(url, api_key, **kwargs)
    if json_result:
        if isinstance(json_result, list):
            for dealer_doc in json_result:
                dealer_obj = CarDealer(
                    address=dealer_doc.get("address", ""),
                    city=dealer_doc.get("city", ""),
                    full_name=dealer_doc.get("full_name", ""),
                    id=dealer_doc.get("id", ""),
                    lat=dealer_doc.get("lat", 0),
                    long=dealer_doc.get("long", 0),
                    short_name=dealer_doc.get("short_name", ""),
                    st=dealer_doc.get("st", ""),
                    zip=dealer_doc.get("zip", "")
                )
                results.append(dealer_obj)
        else:
            print("Error: Invalid JSON format for dealers data")
    return results
