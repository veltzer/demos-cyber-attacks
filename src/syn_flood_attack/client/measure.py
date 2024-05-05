#!/usr/bin/env python

import time
import requests

def fetch_url(url):
  """Fetches the URL and returns the elapsed time."""
  start_time = time.time()
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-2xx status codes
  except requests.exceptions.RequestException as e:
    print(f"Error fetching URL: {e}")
    return None
  end_time = time.time()
  return end_time - start_time

def main():
  url = "http://server:8080/"  # Replace with the actual URL
  window_size = 10  # Number of requests to use for calculating average
  window = []  # Stores elapsed times for the last window_size requests
  start_time = time.time()

  while True:
    elapsed_time = fetch_url(url)
    if elapsed_time is not None:
      window.append(elapsed_time)
      if len(window) > window_size:
        window.pop(0)  # Maintain a fixed window size

      average_time = sum(window) / len(window)
      print(f"Average time (last {window_size} requests): {average_time:.3f} seconds")

    # Wait for one second before the next request
    time.sleep(1 - (time.time() - start_time) % 1)

if __name__ == "__main__":
  main()
