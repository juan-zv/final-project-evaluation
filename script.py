import requests

url = "https://juanzurita.dev/"  # Replace with the target URL

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
        css_links = [link.split('"')[3] for link in css_links ]

        for css_link in css_links:
            try:
                response = requests.get(url + css_link)
                response.raise_for_status()  # Raise an error for bad responses
                css_files.append(response.text)
            except requests.RequestException as e:
                print(f"Error fetching {css_link}: {e}")
        return css_files
    else:
        print("No HTML content to parse for CSS.")
        return None

def get_webpage_js(html):
    """Fetch the JavaScript content of a webpage."""
    if html is not None:
        js_files = []
        js_links = [link.strip() for link in html.split("\n") if ".js" in link and "src" in link]
        js_links = [link.split('"')[1] for link in js_links]

        for js_link in js_links:
            try:
                response = requests.get(url + js_link)
                response.raise_for_status()  # Raise an error for bad responses
                js_files.append(response.text)
            except requests.RequestException as e:
                print(f"Error fetching {js_link}: {e}")
        return js_files
    else:
        print("No HTML content to parse for JS.")
        return None

def check_js(js):
    """Check if JavaScript requirements are met."""
    for js_file in js:
        if "import" in js_file:
            print("✅ Modules imported in JavaScript.")
        else:
            print("❌ No modules imported in JavaScript.")

        if "document." in js_file:
            print("✅ DOM manipulation detected in JavaScript.")
        else:
            print("❌ No DOM manipulation detected in JavaScript.")

        if "`" in js_file:
            print("✅ Template literals detected in JavaScript.")
        else:
            print("❌ No template literals detected in JavaScript.")

        if "fetch(" in js_file:
            print("✅ Fetch API detected in JavaScript.")
        else:
            print("❌ No Fetch API detected in JavaScript.")

        if "async" in js_file:
            print("✅ Async functions detected in JavaScript.")
        else:
            print("❌ No async functions detected in JavaScript.")

        # if "modal" in html:
        #     print("✅ Modal detected in HTML.")
        # else:
        #     print("❌ No modal detected in HTML.")

        if "localStorage" in js_file:
            print("✅ Local Storage detected in JavaScript.")
        else:
            print("❌ No Local Storage detected in JavaScript.")

# check_js()

check_js(get_webpage_js(get_webpage_html(url)))