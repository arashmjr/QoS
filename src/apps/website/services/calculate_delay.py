import subprocess
from time import time

from src.apps.website.services.set_delay import set_delay


def calculate_delay_service(host: str):

    ping = subprocess.Popen(
        ["ping", "-c", "1", host],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    time_before = time()
    ping.communicate()
    time_after = time()
    delay = time_after - time_before
    set_delay(address=host, delay=delay)
    print("end")
