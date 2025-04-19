import requests

url = "https://eddykamwi.github.io/wdd231/dogs/"  # Replace with the target URL

def get_webpage_html(url):
    """Fetch the HTML content of a webpage."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
    
def get_webpage_css(html):
    """Fetch the CSS content of a webpage."""
    if html is not None:
        css_files = []
        css_links = [link.strip() for link in html.split("\n") if ".css" in link and "href" in link]
        for css_link in css_links:
            css_files.append(css_link.split('"'))
        #     try:
        #         response = requests.get(css_link.strip("href=\""))
        #         response.raise_for_status()  # Raise an error for bad responses
        #         css_files[css_link] = response.text
        #     except requests.RequestException as e:
        #         print(f"Error fetching {css_link}: {e}")
        return css_files
    else:
        print("No HTML content to parse for CSS.")
        return None

def get_webpage_javascript(url):
    """Fetch the JavaScript content of a webpage."""
    try:
        response = requests.get(url + "/scripts.js")
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def check_js():
    """Check if JavaScript requirements are met."""
    if "import" in js:
        print("✅ Modules imported in JavaScript.")
    else:
        print("❌ No modules imported in JavaScript.")

    if "document." in js:
        print("✅ DOM manipulation detected in JavaScript.")
    else:
        print("❌ No DOM manipulation detected in JavaScript.")

    if "`" in js:
        print("✅ Template literals detected in JavaScript.")
    else:
        print("❌ No template literals detected in JavaScript.")

    if "fetch(" in js:
        print("✅ Fetch API detected in JavaScript.")
    else:
        print("❌ No Fetch API detected in JavaScript.")

    if "async" in js:
        print("✅ Async functions detected in JavaScript.")
    else:
        print("❌ No async functions detected in JavaScript.")

    if "modal" in html:
        print("✅ Modal detected in HTML.")
    else:
        print("❌ No modal detected in HTML.")

    if "localStorage" in js:
        print("✅ Local Storage detected in JavaScript.")
    else:
        print("❌ No Local Storage detected in JavaScript.")

# check_js()

print(get_webpage_css(get_webpage_html(url)))