import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pickle
import time
import os
import random
import csv
from urllib.parse import urlparse

COOKIES_PATH = "linkedin_cookies.pkl"

# Optional proxy setup
USE_PROXY = False
PROXY = "http://your_proxy_here:port"

# Functions for cookie management
def save_cookies(driver, filename=COOKIES_PATH):
    with open(filename, "wb") as f:
        pickle.dump(driver.get_cookies(), f)
    log_output(f"✅ Cookies saved to {filename}")

def load_cookies(driver, cookies_file):
    try:
        with open(cookies_file, "rb") as f:
            cookies = pickle.load(f)
            for cookie in cookies:
                if 'sameSite' in cookie and cookie['sameSite'] not in ['Strict', 'Lax', 'None']:
                    del cookie['sameSite']
                driver.add_cookie(cookie)
        log_output("✅ Cookies loaded successfully.")
        return True
    except Exception as e:
        log_output(f"❌ Failed to load cookies: {e}")
        return False

def clean_profile_url(url):
    parsed = urlparse(url)
    return f"https://www.linkedin.com{parsed.path}"

log_area = None

def log_output(message):
    if log_area:
        log_area.insert(tk.END, message + "\n")
        log_area.see(tk.END)
    else:
        print(message)

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    if USE_PROXY:
        options.add_argument(f'--proxy-server={PROXY}')
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def login_and_save():
    driver = get_driver()
    driver.get("https://www.linkedin.com/login")
    log_output("⏳ Please log in manually within 60 seconds...")
    time.sleep(60)
    save_cookies(driver)
    driver.quit()

def scrape_event_attendees(event_id):
    driver = get_driver()
    try:
        driver.get("https://www.linkedin.com")
        if not load_cookies(driver, COOKIES_PATH):
            log_output("⚠️ Cannot proceed without cookies.")
            return

        time.sleep(2)
        attendees_url = f'https://www.linkedin.com/search/results/people/?eventAttending=%5B%22{event_id}%22%5D&origin=EVENT_PAGE_CANNED_SEARCH'
        driver.get(attendees_url)
        time.sleep(5)

        attendees = []
        seen_profiles = set()
        page = 1

        while True:
            log_output(f"🔍 Scraping page {page}...")

            for _ in range(5):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.uniform(2, 4))  # Human-like delay

            try:
                wait = WebDriverWait(driver, 10)
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".search-results-container")))
            except TimeoutException:
                log_output("⚠️ Timeout waiting for results container. Breaking.")
                break

            cards = driver.find_elements(By.CSS_SELECTOR, "li[class*='reusable-search__result-container'], li[class^='sJSsJclASieKJlXPEfXvrZdYKxGlCkFU']")

            new_attendee_found = False
            for card in cards:
                try:
                    name_elem = card.find_element(By.CSS_SELECTOR, "span[aria-hidden='true']")
                    name = name_elem.text.strip()

                    profile_link_elem = card.find_element(By.CSS_SELECTOR, "a[href*='/in/']")
                    raw_url = profile_link_elem.get_attribute("href")
                    profile_url = clean_profile_url(raw_url)

                    if profile_url in seen_profiles:
                        continue

                    headline_elem = card.find_element(By.CSS_SELECTOR, "div.t-14.t-black.t-normal")
                    headline = headline_elem.text.strip()

                    location_elem = card.find_elements(By.CSS_SELECTOR, "div.t-14.t-normal")
                    location = location_elem[1].text.strip() if len(location_elem) > 1 else "No location"

                    attendee = {
                        "name": name,
                        "headline": headline,
                        "location": location,
                        "profile_url": profile_url
                    }

                    seen_profiles.add(profile_url)
                    attendees.append(attendee)
                    new_attendee_found = True
                    log_output(f"✅ {len(attendees)}. {name} - {headline} - {location}")
                except Exception:
                    continue

            if not new_attendee_found:
                log_output("⚠️ No new attendees found on this page. Possibly end of results.")
                break

            try:
                next_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Next"]'))
                )
                driver.execute_script("arguments[0].click();", next_button)
                page += 1
                time.sleep(random.uniform(3, 6))  # Randomized delay
            except (TimeoutException, NoSuchElementException):
                log_output("🔚 No more pages or next button missing.")
                break

        # Save to CSV
        filename = f"event_{event_id}_attendees.csv"
        with open(filename, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "headline", "location", "profile_url"])
            writer.writeheader()
            writer.writerows(attendees)

        log_output(f"\n🎉 Done! {len(attendees)} attendees saved to {filename}")

    finally:
        driver.quit()

def launch_gui():
    global log_area

    root = tk.Tk()
    root.title("LinkedIn Event Scraper")
    root.geometry("700x500")

    frame = ttk.Frame(root, padding=10)
    frame.pack(fill=tk.BOTH, expand=True)

    ttk.Label(frame, text="Select Action:").pack(anchor="w")

    action_var = tk.StringVar(value="scrape")
    actions = [("Login & Save Cookies", "login"), ("Scrape Attendees", "scrape")]

    for text, value in actions:
        ttk.Radiobutton(frame, text=text, variable=action_var, value=value).pack(anchor="w")

    ttk.Label(frame, text="Event ID:").pack(anchor="w", pady=(10, 0))
    event_entry = ttk.Entry(frame)
    event_entry.pack(fill=tk.X)

    log_area = scrolledtext.ScrolledText(frame, height=20)
    log_area.pack(fill=tk.BOTH, expand=True, pady=10)

    def run_selected():
        action = action_var.get()
        event_id = event_entry.get().strip()
        log_area.delete("1.0", tk.END)

        if action == "login":
            login_and_save()
        elif action == "scrape":
            if not event_id:
                messagebox.showwarning("Missing Input", "Please enter an Event ID.")
                return
            scrape_event_attendees(event_id)

    ttk.Button(frame, text="Run", command=run_selected).pack()

    root.mainloop()

if __name__ == "__main__":
    launch_gui()
