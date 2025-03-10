import tldextract
import Levenshtein as lv

legitimate_domains = ['example.com', 'google.com', 'facebook.com']

test_urls = [
    'http://example.co',
    'http://example.com',
    'https://www.google.security-update.com',
    'http://faceb00k.com/login',
    'https://google.com',
]

def extract_domain_parts(url):
    extracted = tldextract.extract(url)
    return extracted.subdomain, extracted.domain, extracted.suffix

def is_misspelled_domain(domain, legitimate_domains, threshold=0.9):
    for legit_domain in legitimate_domains:
        similarity = lv.ratio(domain, legit_domain)
        if similarity >= threshold:
            return False # It's a legitimate domain
        return True # No close match found, possibly misspelled

def is_phishing_url(url, legitimate_domains):
    subdomain, domain, suffix = extract_domain_parts(url)

    # Check if it's a known legitimate domain
    if f"{domain}.{suffix}" in legitimate_domains:
         return False

    # Check for misspelled domain names
    if is_misspelled_domain(domain, legitimate_domains):
        print(f"Potential phishing detected: {url}")
        return True

    # You can add more checks here, like suspicious subdomains


    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for url in test_urls:
        is_phishing_url(url, legitimate_domains)
 
        
    
