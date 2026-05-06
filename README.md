# s3-api-calls
A Python script to count and display all S3 API Calls using Veeam 

This Python script is designed to automate the process of parsing log files and visualizing the frequency of specific API events. It essentially turns messy text logs into a clean, readable bar chart.

- File Discovery: It searches a specific folder for files ending in .log, .jsonl, or .json using the glob and os libraries.
  
- Data Extraction: It opens every file found and reads them line by line. It attempts to parse each line as a JSON object, specifically looking for a key named "eventName".
  
- Error Handling: It includes a try-except block to gracefully skip any lines that aren't valid JSON, ensuring the script doesn't crash if a log file contains plain text or corrupted data.
  
- Data Aggregation: It collects all found event names into a list called all_events.
  
- Frequency Analysis: It uses the Pandas library to convert that list into a "Series," which allows it to instantly count how many times each unique event name occurs (e.g., how many times "Login" vs. "GetBackup" appears).

- Visual Reporting: Finally, it uses Matplotlib to generate a bar chart.