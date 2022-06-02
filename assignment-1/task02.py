import datetime
from rich import print


def trigger_lamps():
    lamp = True
    print("Turned light on")


if __name__ == "__main__":
    room_temp = int(input("Enter Room temperature in degree celsius\n"))

    if room_temp >= 30:
        print(f"Turned on thermostat at: ", room_temp)
    else:
        print("Thermostat is turned off")

    current_time = datetime.datetime.now()
    now = current_time.strftime("%H:%M:%S")
    if now.split(":")[0] >= "18":
        trigger_lamps()
