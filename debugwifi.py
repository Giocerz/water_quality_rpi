import subprocess

def get_essid_and_signal_level():
    try:
        result = subprocess.run(['iwconfig'], capture_output=True, text=True, check=True)
        
        essid = None
        signal_level = None

        for line in result.stdout.splitlines():
            line = line.strip()
            if "ESSID" in line:
                essid_start = line.find('ESSID:') + len('ESSID:')
                essid = line[essid_start:]
            elif "Signal level" in line:
                signal_start = line.find('Signal level=') + len('Signal level=')
                signal_level = line[signal_start:].split()[0]

        return essid, signal_level
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar iwconfig: {e}")
        return None, None

essid, signal_level = get_essid_and_signal_level()
print("ESSID:", essid)
print("Signal level:", signal_level)