# PhoneInfo
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
