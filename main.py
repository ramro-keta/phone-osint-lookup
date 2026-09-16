import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import urllib.parse
import webbrowser
generated_links=[]

def get_phone_info(phone_number_str):
    try:
        # Parse number with international country code
        parsed_num = phonenumbers.parse(phone_number_str)
        
        # Check if the number is valid
        if not phonenumbers.is_valid_number(parsed_num):
            print("\n[!] Invalid phone number format.")
            return

        # Fetch basic details
        country = geocoder.description_for_number(parsed_num, "en")
        network_carrier = carrier.name_for_number(parsed_num, "en")
        time_zones = timezone.time_zones_for_number(parsed_num)

        # Print basic telecom details
        print("\n--- Telecom Metadata ---")
        print(f"Formatted Number : {phonenumbers.format_number(parsed_num, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
        print(f"Country / Region : {country if country else 'Unknown'}")
        print(f"Carrier          : {network_carrier if network_carrier else 'Unknown'}")
        print(f"Timezones        : {', '.join(time_zones)}")

        # OSINT Web Footprint (Google Dorks)
        # Sanitizing raw number to clean digits for query matching
        raw_digits = "".join([char for char in phone_number_str if char.isdigit()])
        
        dorks = {
            "General Search": f'"{phone_number_str}" OR "{raw_digits}"',
            "Social Media": f'"{phone_number_str}" (site:facebook.com OR site:linkedin.com OR site:instagram.com)',
            "Messaging Platforms": f'"{phone_number_str}" (site:t.me OR site:wa.me OR site:whatsapp.com)',
            "Paste Sites (Leaks)": f'"{phone_number_str}" site:pastebin.com'
        }

        print("\n--- OSINT Recon Links ---")
        for title, query in dorks.items():
            encoded_query = urllib.parse.quote(query)
            google_url = f"https://www.google.com/search?q={encoded_query}"
            generated_links.append((title, google_url))
            print(f"[*] {title}: {google_url}")

        print("\n--------------------------------------------------")
        choice = input("Do you want to open all Dork links in your browser? (y/n): ").strip().lower()
        
        if choice == 'y':
            print("\n[*] Opening search tabs in your browser...")
            for title, url in generated_links:
                webbrowser.open_new_tab(url)
        else:
            print("[*] Skipped opening browser tabs.")
    except Exception as err:
        print(f"\n[!] Error encountered: {err}")

# Main execution block
if __name__ == "__main__":
    print("=== Phone OSINT Information Lookup Tool ===")
    user_input = input("Enter phone number with country code (e.g., +91... or +1...): ").strip()
    get_phone_info(user_input)
