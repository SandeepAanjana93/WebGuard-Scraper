import requests
from bs4 import BeautifulSoup
import re
import whois
import pandas as pd
from urllib.parse import urlparse
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, scrolledtext

SUSPICIOUS_TLDS = [".xyz", ".tk", ".ml", ".ga", ".cf", ".gq", ".dark"]
SPAM_KEYWORDS = ["spam", "casino", "bet", "adult", "porn", "xxx", "hack"]

def extract_contacts(text):
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    phones = re.findall(r"\+?\d[\d\-\s]{8,}\d", text)
    return list(set(emails)), list(set(phones))

def get_website_age(url):
    try:
        domain = urlparse(url).netloc
        domain_info = whois.whois(domain)
        creation_date = domain_info.creation_date
        
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        
        age = (datetime.now() - creation_date).days // 365
        return f"{age} years"
    except:
        return "Not Available"

def check_spam(url):
    domain = urlparse(url).netloc.lower()
    
    if any(domain.endswith(tld) for tld in SUSPICIOUS_TLDS):
        return "Yes"
    
    if any(word in domain for word in SPAM_KEYWORDS):
        return "Yes"
    
    return "No"

def scrape_website(url):
    spam_status = check_spam(url)
    
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text()

        title = soup.title.string.strip() if soup.title else "Not Found"
        emails, phones = extract_contacts(text)

        return {
            "Website Name": title,
            "Emails": ", ".join(emails) if emails else "Not Found",
            "Phone Numbers": ", ".join(phones) if phones else "Not Found",
            "Location": "Not Found",
            "Website Age": get_website_age(url),
            "Spam Status": spam_status
        }
    except:
        return {
            "Website Name": "Not Accessible",
            "Emails": "Not Found",
            "Phone Numbers": "Not Found",
            "Location": "Not Found",
            "Website Age": "Not Available",
            "Spam Status": spam_status
        }

def start_scraping():
    urls = url_text.get("1.0", tk.END).strip().split("\n")
    urls = [u.strip() for u in urls if u.strip()]
    
    if not urls:
        messagebox.showerror("Error", "Please enter at least one URL")
        return
    
    data = []
    status_text.delete("1.0", tk.END)
    
    for url in urls:
        if not url.startswith("http"):
            url = "https://" + url
        
        status_text.insert(tk.END, f"Processing {url}...\n")
        status_text.update()
        
        info = scrape_website(url)
        data.append(info)
        status_text.insert(tk.END, "  → Done ✔\n\n")
    
    df = pd.DataFrame(data)
    df.to_csv("website_data.csv", index=False)
    messagebox.showinfo("Success", "Data saved to website_data.csv")

root = tk.Tk()
root.title("Website Data Scraper")
root.geometry("700x500")

tk.Label(root, text="Enter Website URLs (one per line):", font=("Arial", 12)).pack(pady=5)

url_text = scrolledtext.ScrolledText(root, width=80, height=10)
url_text.pack(pady=5)

tk.Button(root, text="Start Scraping", font=("Arial", 12), bg="green", fg="white", command=start_scraping).pack(pady=10)

tk.Label(root, text="Status:", font=("Arial", 12)).pack()

status_text = scrolledtext.ScrolledText(root, width=80, height=10)
status_text.pack(pady=5)

root.mainloop()