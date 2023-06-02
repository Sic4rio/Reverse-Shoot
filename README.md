# SICARIOS Reverse Shoot

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

SICARIOS Reverse Shoot is a Python script that retrieves domains associated with a given list of URLs using the AskDNS and RapidDNS APIs. It performs reverse IP lookup and extracts domains from the results.

## Usage

1. Make sure you have Python 3 installed on your system.

2. Install the required dependencies using the following command:
pip install requests colorama


3. Create a file containing the list of URLs (one URL per line) that you want to perform reverse IP lookup on.

4. Run the script using the following command:
```
python reverse_shoot.py
```

5. When prompted, enter the name of the file containing the URLs.

6. Enter the desired number of threads to control the speed of the lookup process. A higher number of threads may increase the speed but can also overload the network.

7. The script will start performing reverse IP lookup on each URL in parallel using the specified number of threads.

8. The extracted domains will be saved to a file named `rdms.txt` in the same directory.
