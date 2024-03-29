import json
import os
import requests
import asyncio
import time

working_cookies_path = "working_cookies"
exceptions = 0
working_cookies = 0
expired_cookies = 0

MAX_CONCURRENT_REQUESTS = 8
BATCH_SIZE = 28

def maximum():
    count = sum(len(files) for _, _, files in os.walk(r"json_cookies"))
    return count

def load_cookies_from_json(json_cookies_path):
    with open(json_cookies_path, "r", encoding="utf-8") as cookie_file:
        cookies_list = json.load(cookie_file)

    try:
        cookies = {cookie['name']: cookie['value'] for cookie in cookies_list}
    except (KeyError, TypeError):
        raise ValueError("Invalid cookie format. Cookies must be a dictionary with 'name' and 'value' fields.")

    return cookies

def send_request_with_cookies(url, cookies):
    try:
        response = requests.get(url, cookies=cookies)
        return "netflix.com/browse" in response.url

    except Exception as e:
        print(f"Error occurred during the request: {str(e)}")
        return False

def process_cookie(filename):
    filepath = os.path.join("json_cookies", filename)

    if os.path.isfile(filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
            url = "https://netflix.com/browse"

            try:
                cookies = load_cookies_from_json(filepath)
                is_valid_cookie = send_request_with_cookies(url, cookies)

                if is_valid_cookie:
                    print(f"Working cookie found! - {filename}")
                    os.makedirs(working_cookies_path, exist_ok=True)
                    with open(os.path.join(working_cookies_path, filename), "w", encoding="utf-8") as a:
                        a.write(content)
                    global working_cookies
                    working_cookies += 1
                elif is_valid_cookie is False:
                    print(f"Invalid cookie - {filename}")
                    global expired_cookies
                    expired_cookies += 1
                else:
                    print(f"Invalid cookies - {filename}")
                    global exceptions
                    exceptions += 1

            except json.decoder.JSONDecodeError:
                print(f"Please use cookie_converter.py to convert your cookies to json format! (File: {filename})\n")
                exceptions += 1

async def process_batch_async(filenames):
    tasks = [asyncio.to_thread(process_cookie, filename) for filename in filenames]
    await asyncio.gather(*tasks)

async def process_cookies_concurrently(filenames):
    for i in range(0, len(filenames), BATCH_SIZE):
        batch = filenames[i : i + BATCH_SIZE]
        await process_batch_async(batch)

async def main():
    global working_cookies
    global expired_cookies
    global exceptions

    start_time = time.time()

    filenames = os.listdir("json_cookies")
    await process_cookies_concurrently(filenames)

    elapsed_time = time.time() - start_time
    print(
        f"\nSummary:\nTotal cookies: {maximum()}\nWorking cookies: {working_cookies}\nExpired cookies: {expired_cookies}\nInvalid cookies: {exceptions}"
    )
    print(f"Time taken: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
