import re
import requests
import sys

# Function to search for phone numbers in a given text
def search_phone_numbers(text):
    phone_pattern = re.compile(r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}')
    phone_numbers = phone_pattern.findall(text)
    return phone_numbers

# Function to search for IP addresses in a given text
def search_ips(text):
    ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    ip_addresses = ip_pattern.findall(text)
    return ip_addresses

# Function to search for URLs in a given text
def search_urls(text):
    url_pattern = re.compile(r'(https?://[^\s]+)')
    urls = url_pattern.findall(text)
    return urls

# Function to test if an IP address is valid (optional)
def test_ip(ip):
    try:
        response = requests.get(f"http://{ip}", timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

# Main function to search for phone numbers, IP addresses, and URLs based on user input
def main():
    # Display the custom "SHERLOCK" banner
    banner = """
.d8888b.  888                       888                   888      
d88P  Y88b 888                       888                   888      
Y88b.      888                       888                   888      
 "Y888b.   88888b.   .d88b.  888d888 888  .d88b.   .d8888b 888  888 
    "Y88b. 888 "88b d8P  Y8b 888P"   888 d88""88b d88P"    888 .88P 
      "888 888  888 88888888 888     888 888  888 888      888888K  
Y88b  d88P 888  888 Y8b.     888     888 Y88..88P Y88b.    888 "88b 
 "Y8888P"  888  888  "Y8888  888     888  "Y88P"   "Y8888P 888  888 
                                                                    
                                                                    
    """
    print(banner)

    while True:
        print("Choose the type of search:")
        print("1. Search for Phone Numbers")
        print("2. Search for IP Addresses")
        print("3. Search for URLs")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice not in ['1', '2', '3']:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue  # Restart the loop if an invalid choice is entered
        
        text = input("Enter the text to search: ")

        if choice == '1':
            # Search for phone numbers
            phone_numbers = search_phone_numbers(text)
            if phone_numbers:
                print("\nPhone Numbers Found:")
                for number in phone_numbers:
                    print(number)
            else:
                print("No phone numbers found.")
        
        elif choice == '2':
            # Search for IP addresses
            ip_addresses = search_ips(text)
            if ip_addresses:
                print("\nIP Addresses Found:")
                for ip in ip_addresses:
                    print(ip)
                    # Optionally, you can test if the IP is reachable
                    if test_ip(ip):
                        print(f"IP {ip} is reachable.")
                    else:
                        print(f"IP {ip} is not reachable.")
            else:
                print("No IP addresses found.")
        
        elif choice == '3':
            # Search for URLs
            urls = search_urls(text)
            if urls:
                print("\nURLs Found:")
                for url in urls:
                    print(url)
            else:
                print("No URLs found.")
        
        # Exit the loop after a valid choice is processed
        break

if __name__ == "__main__":
    main()
