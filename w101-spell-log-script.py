import psutil
import time

def main():
    for pid in psutil.pids():
        try:
            if psutil.Process(pid).name() == "WizardGraphicalClient.exe":
                path = psutil.Process(pid).exe()
        except psutil.NoSuchProcess:
            continue
    log_path = "{0}\\WizardClient.log".format(path.split("\\WizardGraphicalClient.exe")[0])
    print(f"Log path: {log_path}")
    log = open(log_path, "r")
    log.seek(0, 2)
    try:
        while True:
            log_lines = log.readlines()
            for line in log_lines:
                if "[STAT] CombatDetails   CombatResolver::ResolveCombatRound." in line:
                    print(line[77:])
            time.sleep(0.1)
    finally:
        log.close()

if __name__ == "__main__":
    main()
