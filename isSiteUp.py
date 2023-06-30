import requests

websites = [
    "https://www.example.com",
    "https://www.google.com",
    "https://www.github.com",
    "https://www.openai.com"
]

def check_website_status(website):
    try:
        response = requests.get(website)
        if response.status_code == 200:
            return "Website is up and running."
        else:
            return "Website is experiencing issues. Status code: " + str(response.status_code)
    except requests.exceptions.RequestException as e:
        return "An error occurred: " + str(e)

if __name__ == '__main__':
    for website in websites:
        status = check_website_status(website)
        print(website + ": " + status)
