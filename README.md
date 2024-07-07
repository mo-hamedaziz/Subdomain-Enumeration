# Subdomain Lookup Tool

This Python script retrieves subdomains for a given domain using the **Columbus Elmasy API**. It optionally saves the output to a JSON file.

## Requirements

- Python 3.6+
- Install required packages using `pip install -r requirements.txt`

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/subdomain-lookup-tool.git
   cd subdomain-lookup-tool
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
3. Run the script to lookup subdomains:
    ```bash
    python script.py -d example.com
4. Optionally, save the output to a JSON file:
    ```bash
    python script.py -d example.com -j
## Command-line Arguments
- -d, --domain: Required. The domain to lookup subdomains for.
- -j, --json: Optional flag. Save the output to a JSON file (subdomains.json).

You can find the github repo for the columbus project [here](https://github.com/elmasy-com/columbus).
