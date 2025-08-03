# 🛠️ LinkedIn Event Attendees Scraper

A desktop application built with **Python**, **Selenium**, and **Tkinter** to scrape attendee profiles from LinkedIn events. Features a modern GUI interface with real-time logging and advanced scraping capabilities.

---

## ✅ Features

- 🖥️ **Modern Tkinter GUI** - User-friendly desktop interface with real-time logging
- 🔐 **Cookie-based Authentication** - Secure login session management
- 👥 **Comprehensive Data Extraction** - Name, headline, location, and profile URL
- 🕒 **Smart Anti-Detection** - Human-like scrolling with randomized delays (2-6 seconds)
- 🔄 **Multi-page Scraping** - Automatically navigates through all result pages
- 📊 **Real-time Progress Tracking** - Live updates in GUI log area with timestamps
- 🛡️ **Duplicate Prevention** - Ensures no duplicate profiles in results
- 📁 **CSV Export** - Clean data export compatible with Excel and Google Sheets
- ⚡ **Headless Mode Toggle** - Option to run browser in background
- 🌐 **Optional Proxy Support** - Enhanced privacy for larger scraping sessions
- 🔧 **URL Cleaning** - Removes tracking parameters from LinkedIn URLs
- 📝 **Detailed Logging** - Saves all activities to `scraper_log.txt`ent Attendees Scraper

A desktop application built with **Python**, **Selenium**, and **Tkinter** to scrape attendee profiles from a LinkedIn event and save them to a CSV file.

---

## ✅ Features

- 🔐 Manual LinkedIn login with cookie saving
- 👥 Scrapes name, headline, location, and profile URL of event attendees
- 🕒 Human-like scrolling and randomized delay for safe scraping
- 💻 Easy-to-use **GUI** for non-technical users
- 🌐 Optional proxy support for larger scraping sessions
- � Saves results in `.csv` format (compatible with Excel, Google Sheets)
- ⚡ Automated ChromeDriver management with webdriver-manager
- � Advanced HTML parsing with BeautifulSoup integration
- 🛡️ Robust error handling and timeout management

---

## 📸 Screenshot

![LinkedIn Scraper GUI](linkedin.png)

---

## 🧰 Technologies Used

- **Python 3.7+** - Core programming language
- **Tkinter** - Native desktop GUI framework with ScrolledText logging
- **Selenium 4.15+** - Web automation and browser control
- **WebDriver Manager** - Automatic ChromeDriver installation and management
- **CSV Module** - Data export functionality
- **Random & Time** - Anti-detection timing mechanisms
- **URLParse** - URL cleaning and normalization
- **Pickle** - Secure cookie session persistence

---

## � How to Use

### 1. Clone the repo or download the `.zip`

```bash
git clone https://github.com/twaheedgj/Scrape-The-Event.git
cd Scrape-The-Event
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
```

### 3. Activate the virtual environment

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the App

```bash
python linkedin_scraper.py
```

The application will launch with a modern GUI interface featuring:
- **Radio buttons** to select action (Login or Scrape)
- **Event ID input field** for LinkedIn event identification
- **Headless mode checkbox** to run browser in background
- **Real-time log area** showing progress and results
- **Run button** to execute selected action

## 🖥️ GUI Interface

### Available Actions:
1. **Login & Save Cookies** - Opens browser for manual LinkedIn login (60-second window)
2. **Scrape Attendees** - Extracts attendee data from specified event ID

### Settings:
- **Headless Mode** - Toggle browser visibility (enabled by default for scraping)
- **Event ID Field** - Enter LinkedIn event ID (e.g., `7292514458252312576`)

> **First-time setup:** Use **Login & Save Cookies** to authenticate with LinkedIn manually.  
> **Then:** Enter the Event ID and select **Scrape Attendees** to extract data.

---

## � Windows Executable

A compiled `.exe` version is available for non-technical users. Just double-click to run (no Python installation needed).

---

## 📁 Output Files

### CSV Export (`event_<event_id>_attendees.csv`)
Clean, structured data format:
```csv
name,headline,location,profile_url
"John Doe","Software Engineer at Google","San Francisco, CA","https://linkedin.com/in/johndoe"
"Jane Smith","Product Manager at Microsoft","Seattle, WA","https://linkedin.com/in/janesmith"
```

### Log File (`scraper_log.txt`)
Detailed activity log with timestamps:
```
[2025-08-03 14:30:15] ✅ Cookies loaded successfully.
[2025-08-03 14:30:18] 🔍 Scraping page 1...
[2025-08-03 14:30:22] ✅ 1. John Doe - Software Engineer at Google - San Francisco, CA
[2025-08-03 14:30:25] ✅ 2. Jane Smith - Product Manager at Microsoft - Seattle, WA
[2025-08-03 14:32:10] 🎉 Done! 150 attendees saved to event_7292514458252312576_attendees.csv
```

**Features:**
- **Excel/Google Sheets compatible** CSV format
- **Cleaned LinkedIn URLs** without tracking parameters
- **Duplicate-free results** using profile URL deduplication
- **Comprehensive logging** for debugging and monitoring

---

## ⚠️ Disclaimer

This tool is for **educational and ethical use only**. Scraping LinkedIn may violate their [Terms of Service](https://www.linkedin.com/legal/user-agreement). Use it responsibly and at your own risk.

### Important Guidelines

- **Personal Use Only**: Intended for personal research and networking purposes
- **Respect Rate Limits**: The tool includes built-in delays to avoid overwhelming LinkedIn's servers
- **Data Privacy**: Handle scraped data responsibly and in compliance with privacy regulations
- **Public Data Only**: Can only access publicly visible attendee information
- **Legal Compliance**: Users are responsible for complying with applicable laws and LinkedIn's Terms of Service

---

## 👤 Author

**Talha Waheed**  
📧 talhawaheed7807@gmail.com

---

## 🛠️ Troubleshooting

### Common Issues

**Chrome/ChromeDriver Issues:**
- The tool automatically downloads and manages ChromeDriver
- Ensure Google Chrome is installed and up to date
- WebDriver Manager handles version compatibility automatically

**Login Problems:**
- Use "Login & Save Cookies" action in GUI for initial setup
- Ensure you complete login within the 60-second window
- Check for two-factor authentication requirements
- Clear cookies file if authentication fails: delete `linkedin_cookies.pkl`

**No Attendees Found:**
- Event may be private or have restricted attendee visibility
- Verify the Event ID is correct (19-digit number)
- Ensure your LinkedIn account has access to view the event
- Check the log area for specific error messages

**GUI/Display Issues:**
- Disable headless mode to see browser activity
- Check the real-time log area for detailed progress updates
- Review `scraper_log.txt` for complete activity history

**Performance Optimization:**
- Enable headless mode for faster scraping
- Adjust delays in code if needed for different network speeds
- Use proxy settings for large-scale operations

### Configuration Options

**Headless Mode:** 
- Enabled by default for scraping efficiency
- Disable to watch browser activity for debugging

**Proxy Support:**
- Set `USE_PROXY = True` and configure `PROXY` variable in code
- Useful for enhanced privacy or bypassing rate limits

**Timing Adjustments:**
- Random delays (2-6 seconds) prevent detection
- Scrolling patterns mimic human behavior
- Configurable in the `scrape_event_attendees()` function

---

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Test your changes thoroughly
4. Submit a pull request with a clear description

---

**Disclaimer**: This tool is provided as-is for educational purposes. Users are solely responsible for ensuring ethical and legal use in compliance with LinkedIn's Terms of Service and applicable laws.
