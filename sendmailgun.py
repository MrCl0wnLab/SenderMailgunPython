import time
import requests
import threading


# Set url api Mailgun.
API_URL = "https://api.mailgun.net/v3/"
# Set api key Mailgun.
API_KEY = None
# Result request api.
RESULT_SEND = []
# Option request verbose.
VERBOSE = False
# Option request timeout.
TIMEOUT = 5
# Option max value threads.
MAX_CONECTION_THREAD = 1


def send_request(api_url_domain: str, post_data: dict):

    try:
        response = requests.post(
            url=f"{api_url_domain}/messages",
            data=post_data,
            timeout=TIMEOUT,
            auth=('api', API_KEY),

        )
        # Result request body / string.
        RESULT_SEND.append(response.text)
        # Result request header.
        RESULT_SEND.extend(response.headers)

    except Exception as e:
        print(e)


def send_mail_thread(domain: str, post_data: dict):

    api_url_domain = API_URL + domain
    send_request(api_url_domain, post_data)


def send_mail(domains: str, post_data: dict):

    try:
        list_threads = []
        RESULT_SEND.clear()
        while threading.active_count() > MAX_CONECTION_THREAD:
            time.sleep(0.1)
        thread = threading.Thread(target=send_mail_thread,
                                args=(domains, post_data))
        list_threads.append(thread)
        thread.start()

        for thread in list_threads:
            thread.join()

    except Exception as e:
        print(e)
        return False
