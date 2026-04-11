import psutil
import argparse
import logging
import sys
import os
from datetime import datetime
import subprocess

# 1. Logging Setup
LOG_DIR = os.environ.get("LOG_DIR", "/app/logs")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "devguard.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# 2. CLI Setup
parser = argparse.ArgumentParser(description="DevGuard Pro - System Health Monitor")
parser.add_argument("--check", required=True, help="Kya check karna hai? (all/ram/disk)")
args = parser.parse_args()

print(f"🚀 DevGuard Pro Started at {datetime.now().strftime('%H:%M:%S')}")
logging.info("DevGuard Pro Started")

# 3. Health Checks
if args.check == "ram" or args.check == "all":
	ram = psutil.virtual_memory()
	if ram.percent < 85:
		print(f"🧠 RAM Used: {ram.percent}%")
		logging.info(f"RAM Used: {ram.percent}%")
	else :
		print(f"CRITICAL: RAM Used: {ram.percent}% too high")
		logging.error(f"CRITICAL: RAM Used {ram.percent}% too high")

if args.check == "disk" or args.check == "all":
	disk = psutil.disk_usage('/')
	if disk.percent < 85:
		print(f"💾 Disk Used: {disk.percent}%")
		logging.info(f"Disk Used: {disk.percent}%")
	else :
		print(f"CRITICAL: Disk Usage {disk.percent}% is too high")
		logging.error(f"CRITICAL: Disk Usage {disk.percent}% is too high")

if args.check == "cpu" or args.check == "all":
	cpu = psutil.cpu_percent(interval=1)
	if cpu < 85:
		print(f"CPU Used: {cpu}%")
		logging.info(f"CPU Used: {cpu}%")
	else :
		print(f"CRITICAL: CPU Used {cpu}% too high")
		logging.error(f"CRITICAL: CPU Used {cpu}% too high")


log_file = os.path.join(LOG_DIR, "devguard.log")
error_found = False
if os.path.exists(log_file):
	with open(log_file, 'r') as f:
		for line in f:
			if "ERROR" in line:
				error_found = True
				break

if error_found:
    print("CRITICAL: Error found in logs!")
    logging.error("CRITICAL: Error found in logs!")
    sys.exit(1)

print("✅ Check Complete!")
logging.info("DevGuard Pro Finished")

if not os.environ.get("DOCKER_ENV"):
	try:
		subprocess.run(["git", "add", "."], check=True)
		message=(f"Auto push {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
		subprocess.run(["git", "commit", "-m", message], check=True)
		subprocess.run(["git", "push"], check=True)

		print(f"push finished: {message}")
		logging.info(f"Git pushed {message}")

	except subprocess.CalledProcessError as e:
		print("Git push failed")
		logging.warning(f"Git push failed: {e}")

sys.exit(0)
