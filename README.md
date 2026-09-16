# phone-osint-lookup
## Phone Number OSINT & Recon Tool

A Python-based Open Source Intelligence (OSINT) tool that extracts telecom metadata and generates web footprint reconnaissance queries (Google Dorks) for any international phone number.

## Features

- **Telecom Metadata Extraction:** Identifies country, region, service provider (carrier), and timezones using Google's `phonenumbers` library.
- **Number Validation:** Verifies whether a given input is a valid international phone number format.
- **OSINT Recon Links:** Automatically generates targeted Google search queries to look for public footprints across social media and paste sites.

## Project Structure

```text
├── main.py          # Core Python script
├── requirements.txt # Project dependencies
└── README.md        # Project documentation
```
## Git Clone
git clone [https://github.com/your-username/phone-osint-lookup.git](https://github.com/your-username/phone-osint-lookup.git)

cd phone-osint-lookup
## Install dependencies
pip install -r requirements.txt
## Usage
python main.py
## Output
=== Phone OSINT Information Lookup Tool ===

Enter phone number with country code (e.g., +91... or +1...): +14155552671

--- Telecom Metadata ---

Formatted Number : +1 415-555-2671

Country / Region : United States

Carrier          : Unknown

Timezones        : America/Los_Angeles

--- OSINT Recon Links ---

[*] General Search: [https://www.google.com/search?q=%22%2B14155552671%22](https://www.google.com/search?q=%22%2B14155552671%22)...

[*] Social Media: [https://www.google.com/search?q=%22%2B14155552671%22](https://www.google.com/search?q=%22%2B14155552671%22)...

[*] Paste Sites (Leaks): [https://www.google.com/search?q=%22%2B14155552671%22](https://www.google.com/search?q=%22%2B14155552671%22)...
