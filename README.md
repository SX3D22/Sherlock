# Sherlock
A tool made for looking up stuff
Sherlock - A Search Tool for Phone Numbers, IPs, and URLs
Overview:

Sherlock is a Python-based tool designed to help you search for phone numbers, IP addresses, and URLs within a given text. This program allows users to input any text, and it will search and display any phone numbers, IP addresses, or URLs present in that text. The program also includes an optional IP validation feature, where you can test if the found IP addresses are reachable over the web.

Features:

Phone Number Search:

The script looks for phone numbers in various formats (e.g., (123) 456-7890, 123-456-7890).
IP Address Search:

It detects and lists IP addresses from the provided text (e.g., 192.168.1.1, 10.0.0.255).
Includes an optional feature that checks if the found IP addresses are reachable online.
URL Search:

The tool identifies URLs starting with http:// or https:// within the text (e.g., https://example.com, http://google.com).
Custom Banner:

Upon running the script, a custom ASCII art banner with the word "SHERLOCK" is displayed, half in white and half in blue, making the tool visually appealing and user-friendly.
Interactive User Interface:

After seeing the banner, the user is prompted to choose which search they want to perform (phone numbers, IPs, or URLs).
The program guides the user through the search process and gives feedback on the results.
Error Handling:

If an invalid choice is entered, the program will inform the user and restart, ensuring that only valid inputs are accepted.
How it Works:

When the program starts, a custom "SHERLOCK" banner is printed in two colors: white for the left half and blue for the right half.
The user is prompted to select a search option (phone numbers, IPs, or URLs).
After making a selection, the user is asked to input the text to search through.
Based on the selection, the program processes the input text and displays any matches found.
If IPs are found, the script optionally checks whether they are reachable over the web.
The script continues to loop if an invalid choice is made, ensuring a smooth user experience.
Installation Requirements:

Python 3.x (required for running the script).
colorama library (used to colorize the banner):
Install it by running:
bash
Copy
pip install colorama
Use Case Example:

You run the script, and it shows the custom banner.
You choose the type of search (e.g., searching for phone numbers).
You input a block of text, and the program scans it, showing any phone numbers it finds.
If you choose IP address search, the tool will list IPs and check if they're reachable.
