import datetime
import winsound
from rich import print
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel

console = Console()

if __name__ == "__main__":
    console.print("[yellow]Enter Hour time in 24 hour time\n", justify="center")
    set_alarm_hour = input()
    console.print("[yellow]Enter minute time in two digits\n", justify="center")
    set_alarm_min = input()
    console.print("[yellow]Enter second time in two digits\n", justify="center")
    set_alarm_sec = input()
    set_timer = [
        f"[b][red]{set_alarm_hour}",
        f"[b][red]{set_alarm_min}",
        f"[b][red]{set_alarm_sec}",
    ]
    user_renderables = [Panel(x) for x in set_timer]
    console.print(Columns(user_renderables))
    set_alarm_timer = f"{set_alarm_hour}:{set_alarm_min}:{set_alarm_sec}"
    current_time = datetime.datetime.now()
    while True:
        now = current_time.strftime("%H:%M:%S")
        if now == set_alarm_timer:
            console.print("[green]It's time to wake up\n")
            winsound.Beep(frequency=500, duration=60)
            # winsound.PlaySound("*", winsound.SND_ALIAS)
            break
        else:
            current_time = datetime.datetime.now()
