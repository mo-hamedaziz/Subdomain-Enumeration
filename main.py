import argparse
import requests
import json

def get_subdomains(domain):
    """
    Retrieve subdomains for a given domain from the specified URL.
    
    Args:
    domain (str): The domain to lookup subdomains for.
    
    Returns:
    list: A list of subdomains.
    """
    url = f"https://columbus.elmasy.com/lookup/{domain}"
    response = requests.get(url, headers={"Accept": "text/plain"})
    
    if response.status_code == 200:
        return response.text.splitlines()
    else:
        print(f"Failed to retrieve subdomains, status code: {response.status_code}")
        return []

def print_subdomains(domain, subdomains):
    """
    Print the count and list of subdomains for a given domain.
    
    Args:
    domain (str): The main domain.
    subdomains (list): A list of subdomains.
    """
    print(f"Total subdomains found: {len(subdomains)}\n")
    for sub in subdomains:
        if sub == "":
            host = domain
        else:
            host = f"{sub}.{domain}"
        print(host)

def save_subdomains_to_json(domain, subdomains, filename="subdomains.json"):
    """
    Save the subdomains to a JSON file.
    
    Args:
    domain (str): The main domain.
    subdomains (list): A list of subdomains.
    filename (str): The name of the JSON file to save the subdomains.
    """
    data = [{"subdomain": sub, "host": domain if sub == "" else f"{sub}.{domain}"} for sub in subdomains]
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"\nSubdomains saved to {filename}")

def main():
    """
    Main function to parse arguments and lookup subdomains.
    """
    # Set up argument parser to accept domain input and optional JSON flag
    parser = argparse.ArgumentParser(description="Lookup subdomains for a given domain.")
    parser.add_argument("-d", "--domain", required=True, help="The domain to lookup subdomains for")
    parser.add_argument("-j", "--json", action="store_true", help="Save the output to a JSON file")
    args = parser.parse_args()

    # Retrieve the domain from the arguments
    domain = args.domain
    
    # Get subdomains for the domain
    subdomains = get_subdomains(domain)
    
    # Print the subdomains
    print_subdomains(domain, subdomains)
    
    # Save to JSON if the flag is set
    if args.json:
        save_subdomains_to_json(domain, subdomains)

if __name__ == "__main__":
    main()
