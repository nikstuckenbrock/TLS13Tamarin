#!/usr/bin/env python3
"""
Downloads trace files from a server, iterating over i/j indices.
Usage: python download_traces.py <host> <output_folder>
Example: python download_traces.py localhost:3001 ./output
"""

import sys
import os
import requests


def download_traces(host: str, output_folder: str):
    # Normalize host
    if not host.startswith("http://") and not host.startswith("https://"):
        host = f"http://{host}"
    host = host.rstrip("/")

    base_url = f"{host}/thy/trace/2/interactive-graph-def/cases/refined"

    os.makedirs(output_folder, exist_ok=True)

    i = 1
    while True:
        j = 1
        found_any = False

        while True:
            url = f"{base_url}/{i}/{j}?unabbreviate=&no-auto-sources=&simplification=2"

            try:
                response = requests.get(url, timeout=30)
            except requests.RequestException as e:
                print(f"  Error fetching {url}: {e}")
                sys.exit(1)

            if response.status_code == 500:
                if j == 1:
                    # No files at all for this i — stop outer loop too
                    print(f"[{i}/{j}] 500 on first j — stopping.")
                    return
                else:
                    # Done with this i, move to next
                    print(f"[{i}/{j}] 500 — moving to next i.")
                    break

            if response.status_code != 200:
                print(f"[{i}/{j}] Unexpected status {response.status_code} — skipping.")
                j += 1
                continue

            # Save the file
            dir_path = os.path.join(output_folder, str(i))
            os.makedirs(dir_path, exist_ok=True)
            file_path = os.path.join(dir_path, f"{j}.dot")

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(response.text)

            print(f"[{i}/{j}] Saved → {file_path}")
            found_any = True
            j += 1

        if not found_any:
            break

        i += 1

    print("Done.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python download_traces.py <host> <output_folder>")
        print("Example: python download_traces.py localhost:3001 ./output")
        sys.exit(1)

    host_arg = sys.argv[1]
    folder_arg = sys.argv[2]

    download_traces(host_arg, folder_arg)