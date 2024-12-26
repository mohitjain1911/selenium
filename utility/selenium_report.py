from datetime import datetime
import os

LOG_FILE = "selenium_actions.log"
OUTPUT_HTML = "selenium_report.html"

def parse_log_line(line):
    """Parses a single line in the log file."""
    parts = line.strip().split(" - ", 3)  # Split by " - " only 3 times
    if len(parts) == 4:  # Ensure we have all required components
        timestamp, step_name, result, message = parts
        return timestamp.strip(), step_name.strip(), result.strip(), message.strip()
    return None, None, None, None

def remove_duplicates(log_entries):
    """Removes duplicate log entries."""
    seen = set()
    filtered_entries = []
    for entry in log_entries:
        step_key = (entry[1], entry[2], entry[3])  # Use Step Name, RESULT, and Message as unique identifiers
        if step_key not in seen:
            seen.add(step_key)
            filtered_entries.append(entry)
    return filtered_entries

def generate_html_report():
    """Parses log file and generates an HTML report."""
    if not os.path.exists(LOG_FILE):
        print(f"Log file '{LOG_FILE}' not found.")
        return

    # Read and parse the log file
    log_entries = []
    with open(LOG_FILE, "r") as file:
        for line in file:
            timestamp, step_name, result, message = parse_log_line(line)
            if timestamp and result:  # Ensure valid entries
                log_entries.append((timestamp, step_name, result, message))

    # Remove duplicates
    filtered_entries = remove_duplicates(log_entries)

    # Calculate total counts for Pass and Fail
    total_pass = sum(1 for _, _, result, _ in filtered_entries if result.lower() == "pass")
    total_fail = sum(1 for _, _, result, _ in filtered_entries if result.lower() == "fail")

    # Start building the HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Selenium Execution Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            table {{ width: 100%; border-collapse: collapse; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #4CAF50; color: white; }}
            tr:nth-child(even) {{ background-color: #f2f2f2; }}
            tr:hover {{ background-color: #ddd; }}
            .status-pass {{ color: green; font-weight: bold; }}
            .status-fail {{ color: red; font-weight: bold; }}
            .summary {{ font-size: 18px; margin-bottom: 10px; }}
        </style>
    </head>
    <body>
        <h1>Selenium Test Execution Report</h1>
        <div class="summary">
            <p><strong>Total Steps:</strong> {len(filtered_entries)}</p>
            <p><strong>Total Pass:</strong> <span style="color:green;">{total_pass}</span></p>
            <p><strong>Total Fail:</strong> <span style="color:red;">{total_fail}</span></p>
        </div>
        <table>
            <tr>
                <th>Sr No</th>
                <th>Step Name</th>
                <th>RESULT</th>
                <th>Message</th>
                <th>Timestamp</th>
            </tr>
    """

    # Generate HTML rows for each log entry
    for sr_no, (timestamp, step_name, result, message) in enumerate(filtered_entries, start=1):
        status_class = "status-pass" if result.lower() == "pass" else "status-fail"

        html_content += f"""
        <tr>
            <td>{sr_no}</td>
            <td>{step_name}</td>
            <td class="{status_class}">{result}</td>
            <td>{message}</td>
            <td>{timestamp}</td>
        </tr>
        """

    # Finish the HTML content
    html_content += """
        </table>
    </body>
    </html>
    """

    # Write to output HTML file
    with open(OUTPUT_HTML, "w") as report_file:
        report_file.write(html_content)

    print(f"HTML report generated: {OUTPUT_HTML}")

if __name__ == "__main__":
    generate_html_report()
