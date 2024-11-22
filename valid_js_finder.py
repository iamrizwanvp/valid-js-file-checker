import requests  # Make sure to import the requests library

valid_js_urls = []

def fetch_js_content(url):
    try:
        response = requests.get(url, allow_redirects=True)
        
        if response.status_code == 200:
            content_type = response.headers.get('Content-Type')
            if 'application/javascript' in content_type or 'text/javascript' in content_type:
                valid_js_urls.append(url)  # Store valid URLs
                print(f"Content fetched from: {url}")
                print(response.text[:500])  # Print the first 500 characters of the content
            else:
                print(f"URL does not serve JavaScript content: {url}")
                print(f"Content-Type: {content_type}")
        else:
            print(f"Failed to fetch content from {url} with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

# Load URLs from your text file
with open('yourjsfile.txt', 'r') as file:
    urls = file.readlines()

# Fetch content for each URL
for url in urls:
    url = url.strip()
    if url:
        fetch_js_content(url)

# Save valid JavaScript URLs to a new file
with open('valid_js.txt', 'w') as output_file:
    for valid_url in valid_js_urls:
        output_file.write(valid_url + '\n')

print("Valid JavaScript URLs saved to valid_js_urls.txt")
