#!/usr/bin/env python3

import subprocess

def main():
    # Check the status of httpd.service
    try:
        result = subprocess.Popen(['systemctl', 'is-active', 'httpd.service'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        status_output = stdout.decode('utf-8').strip()
        status_code = result.returncode

        # Debug: print the status output and status code
        print(f"Debug: status_output is '{status_output}', status_code is {status_code}")

        # Output the result in a format suitable for SolarWinds
        if status_output == 'active':
            print("Statistic: 0")
            print("Message: httpd.service is running")
            exit(0)
        else:
            print("Statistic: 1")
            print("Message: httpd.service is not running")
            exit(1)
    except Exception as e:
        print(f"Error checking httpd.service status: {e}")
        print("Statistic: 1")
        print("Message: Error checking httpd.service status")
        exit(1)

if __name__ == "__main__":
    main()
