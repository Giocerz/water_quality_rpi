import subprocess
import time

class WifiService:
    @staticmethod
    def list_wifi_networks() -> dict:
        ok = subprocess.check_output(
            "sudo wpa_cli scan", shell=True).decode("utf-8")
        if 'OK' not in ok:
            return []
        lines = subprocess.check_output(
            "sudo wpa_cli scan_results", shell=True).decode("utf-8")
        current_network = subprocess.check_output(
            "sudo iwgetid -r", shell=True).decode("utf-8").strip()
        lines: list = lines.split("\n")[2:]
        if len(lines) == 0:
            return []
        networks_dict = {}
        for line in lines:
            columns = line.split("\t")
            if len(columns) >= 5:
                bssid = columns[0]
                frequency = int(columns[1])
                signal_level = int(columns[2])
                flags = columns[3]
                ssid = columns[4]

                if ssid not in networks_dict or signal_level > networks_dict[ssid]["signal"]:
                    networks_dict[ssid] = {
                        "BSSID": bssid,
                        "frequency": frequency,
                        "signal": signal_level,
                        "security": flags,
                        "ssid": ssid,
                        "connect": ssid == current_network
                    }
        return list(networks_dict.values())

    @staticmethod
    def connect_wifi(ssid, password=""):
        time.sleep(2)
        if password == "@WATCH_DRIVE Proj" or password == "":
            return True
        else:
            return False
        
    @staticmethod
    def get_essid_and_signal_level():
        try:
            result = subprocess.run(['iwconfig'], capture_output=True, text=True, check=True)
            essid = None
            signal_level = None

            for line in result.stdout.splitlines():
                line = line.strip()
                if "ESSID" in line:
                    essid_start = line.find('ESSID:') + len('ESSID:')
                    essid = line[essid_start:].strip()
                elif "Signal level" in line:
                    signal_start = line.find('Signal level=') + len('Signal level=')
                    signal_level = line[signal_start:].split()[0].strip()
            if "None" in signal_level:
                signal_level = None
            if "off" in essid:
                essid = None
            return essid, signal_level
        except subprocess.CalledProcessError as e:
            return None, None