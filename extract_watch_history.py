from bs4 import BeautifulSoup
import csv
import json
import time
from itertools import islice
from datetime import datetime

# Extracting watched video details from html file
def main():

    with open('watch-history.html', 'r') as file:
        # Read the entire html file
        contents = file.read()

        # Limit only to the first 45 or more lines in the html file
        # contents = list(islice(file, 45))
        # contents = "".join(contents)

        soup = BeautifulSoup(contents, 'html.parser')

    divs = soup.find_all(
        'div', class_='content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1')

    # List to store the extracted data
    data_list = []

    for div in divs:
        if "Watched " in div.text:
            # Extract the video title and link
            video_link = div.find('a', href=True)
            video_title = video_link.text.strip() if video_link else None
            video_url = video_link['href'].split(
                "https://www.youtube.com/watch?v=")[-1] if video_link else None

            # Extract the channel name and link
            channel_link = div.find_all('a', href=True)[1] if len(
                div.find_all('a', href=True)) > 1 else None
            channel_name = channel_link.text.strip() if channel_link else None
            channel_url = channel_link['href'].split(
                "https://www.youtube.com/channel/")[-1] if channel_link else None

            # Extract the date and time
            # Data cleaning : Normalize month abbreviation for September
            date_time_text = div.contents[-1].strip().replace("Sept", "Sep")
            date_time_obj = datetime.strptime(date_time_text[:-4].strip(), "%d %b %Y, %H:%M:%S")
            date_part = date_time_obj.strftime("%Y-%m-%d")
            time_part = date_time_obj.strftime("%H:%M:%S")

            # Save the extracted information in a dictionary
            data = {
                "video_title": video_title,
                "video_url": video_url,
                "channel_name": channel_name,
                "channel_url": channel_url,
                "date": date_part,
                "time": time_part
            }

            # Append the dictionary to the list
            data_list.append(data)

    # Save the extracted data to a CSV file
    with open('watched_history.csv', 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.DictWriter(
            csv_file, fieldnames=["video_title", "video_url", "channel_name", "channel_url", "date", "time"])
        csv_writer.writeheader()
        csv_writer.writerows(data_list)

    # Save to JSON
    with open('watched_history.json', 'w', encoding='utf-8') as json_file:
        json.dump(data_list, json_file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Program finished in {(end_time - start_time) / 60.} min")



