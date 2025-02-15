# YouTube Watch History Extractor: Convert HTML to CSV & JSON

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-HTML%20Parsing-brightgreen) ![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📌 Overview
YouTube Watch History Extractor is a Python script that **parses and extracts structured data** from a YouTube `watch-history.html` file. It converts your YouTube watch history into **CSV and JSON formats**, making it easier to analyze trends, track favorite creators, and build datasets for further research.

## 🚀 Features
- ✅ Extracts **video titles, URLs, channel names, timestamps** from YouTube history.
- ✅ Outputs structured **CSV and JSON files** for easy data manipulation.
- ✅ Efficient **HTML parsing** with BeautifulSoup.
- ✅ Handles **large history files** smoothly.
- ✅ Useful for **personal analytics, recommendations, and archiving.**

## 📂 Example Output

**CSV (watched_history.csv)**
| video_title      | video_url        | channel_name | channel_url   | date       | time     |
|-----------------|-----------------|-------------|--------------|-----------|---------|
| Sample Video 1  | abc123xyz        | Tech Guru   | channel456   | 2024-01-20 | 15:34:12 |

**JSON (watched_history.json)**
```json
[
    {
        "video_title": "Sample Video 1",
        "video_url": "abc123xyz",
        "channel_name": "Tech Guru",
        "channel_url": "channel456",
        "date": "2024-01-20",
        "time": "15:34:12"
    }
]
```


---

## **How to Download Your YouTube Watch History**  
Follow these steps to download your **watch-history.html** file from Google:  

### **Step 1: Go to Google Takeout**  
1. Visit [Google Takeout](https://takeout.google.com/).  
2. Sign in with your Google account if prompted.  

### **Step 2: Select Only YouTube History**  
1. Click **"Deselect all"** to remove all other Google data.  
2. Scroll down and check **"YouTube and YouTube Music"**.  
3. Click **"All YouTube data included"**, uncheck everything except **"History"**, then click OK.  

### **Step 3: Configure the Export**  
1. Scroll down and click **"Next step"**.  
2. Under "Delivery method," choose **"Download link via email"** (or another preferred option).  
3. Select **"Export once"** and **".ZIP"** format (recommended).  
4. Click **"Create Export"**.  

### **Step 4: Download and Extract Your Data**  
1. Wait for Google to process your request (it may take minutes to hours).  
2. Once done, download the ZIP file from the email link.  
3. Extract the ZIP file to access the folder named **"Takeout"**.  

### **Step 5: Locate Your Watch History File**  
1. Inside the extracted folder, navigate to:  
   **`Takeout > YouTube and YouTube Music > history`**  
2. Look for a file named **`watch-history.html`**.  
3. Copy this file to the same directory where you'll run this script.  

> ✅ Now you're ready to use the YouTube Watch History Extractor! 🚀  

---

## 🛠️ Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/youtube-watch-history-extractor.git
   cd youtube-watch-history-extractor
   ```

2. **Install dependencies**
   Ensure you have Python 3.8+ installed, then run:
   ```sh
   pip install -r requirements.txt
   ```

3. **Place your YouTube history file**
   Download your `watch-history.html` from [Google Takeout](https://takeout.google.com/) and move it to the script directory.

## ▶️ Usage
Run the script to extract and save history data:
```sh
python extract_watch_history.py
```
This generates `watched_history.csv` and `watched_history.json`.

## 🎯 Potential Use Cases
- **Data Analysis**: Track watch patterns and preferences.
- **Machine Learning**: Train recommendation models based on user history.
- **Personal Archiving**: Keep records of watched content.
- **Integration**: Use extracted data for custom dashboards or automation.

## 🤝 Contributing
Contributions are welcome! Feel free to:
- Report issues 🐞
- Suggest improvements 🚀
- Submit pull requests 📌

## 📜 License
This project is licensed under the **MIT License**.

## 📧 Contact
Created by **[Your Name]**
- GitHub: [yourusername](https://github.com/yourusername)
- LinkedIn: [yourprofile](https://linkedin.com/in/yourprofile)
