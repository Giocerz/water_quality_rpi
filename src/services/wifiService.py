import subprocess

class WifiService:
    @staticmethod
    def scan():
        subprocess.run(["sudo", "wpa_cli", "scan"])
    
    @staticmethod
    def scan_results() -> list:
        try:
            lines = subprocess.check_output(
                ["sudo", "wpa_cli", "scan_results"], text=True
            ).split("\n")[2:]

            current_network = subprocess.check_output(
                ["sudo", "iwgetid", "-r"], text=True
            ).strip()

            if not lines:
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
        except subprocess.CalledProcessError:
            return []

    @staticmethod
    def add_network(ssid: str, psk: str) -> int:
        try:
            network_id = subprocess.check_output(
                ["sudo", "wpa_cli", "add_network"], text=True
            ).strip().split("\n")[-1]
            network_id = int(network_id) if network_id.isdigit() else -1
            if network_id == -1:
                return -1

            for cmd in [
                ["sudo", "wpa_cli", "set_network", str(network_id), "ssid", f'"{ssid}"'],
                ["sudo", "wpa_cli", "set_network", str(network_id), "psk", f'"{psk}"'],
                ["sudo", "wpa_cli", "enable_network", str(network_id)],
                ["sudo", "wpa_cli", "select_network", str(network_id)],
                ["sudo", "wpa_cli", "reconnect"]
            ]:
                result = subprocess.check_output(cmd, text=True).strip()
                if "OK" not in result:
                    return -1

            return network_id
        except subprocess.CalledProcessError:
            return -1

    @staticmethod
    def verify_network_and_save(network_id: int) -> bool:
        try:
            result = subprocess.check_output(["sudo", "wpa_cli", "status"], text=True)
            if "COMPLETED" not in result:
                for cmd in [
                    ["sudo", "wpa_cli", "disable_network", str(network_id)],
                    ["sudo", "wpa_cli", "remove_network", str(network_id)],
                    ["sudo", "wpa_cli", "save_config"]
                ]:
                    subprocess.run(cmd, check=True)
                return False

            subprocess.run(["sudo", "wpa_cli", "save_config"], check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    @staticmethod
    def delete_network(ssid: str) -> bool:
        try:
            lines = subprocess.check_output(
                ["sudo", "wpa_cli", "list_networks"], text=True
            ).split("\n")[2:]

            if not lines:
                return False

            network_id = -1
            for line in lines:
                if ssid in line:
                    network_id = line.split("\t")[0]
                    break

            if network_id == -1:
                return False

            for cmd in [
                ["sudo", "wpa_cli", "disable_network", str(network_id)],
                ["sudo", "wpa_cli", "remove_network", str(network_id)],
                ["sudo", "wpa_cli", "save_config"]
            ]:
                subprocess.run(cmd, check=True)

            return True
        except subprocess.CalledProcessError:
            return False

    @staticmethod
    def get_essid_and_signal_level():
        try:
            result = subprocess.run(["iwconfig"], capture_output=True, text=True, check=True)
            essid = None
            signal_level = None

            for line in result.stdout.splitlines():
                line = line.strip()
                if "ESSID" in line:
                    essid_start = line.find("ESSID:") + len("ESSID:")
                    essid = line[essid_start:].strip()
                elif "Signal level" in line:
                    signal_start = line.find("Signal level=") + len("Signal level=")
                    signal_level = line[signal_start:].split()[0].strip()

            if "None" in str(signal_level):
                signal_level = None
            if "off" in str(essid):
                essid = None

            return essid, signal_level
        except subprocess.CalledProcessError:
            return None, None

    @staticmethod
    def is_network_saved(ssid: str) -> bool:
        try:
            saved_networks = subprocess.check_output(
                ["sudo", "wpa_cli", "list_networks"], text=True
            )
            return ssid in saved_networks
        except subprocess.CalledProcessError:
            return False

    @staticmethod
    def scan_results_mocker():
        import random
        networks = []
        current_network_index = random.randint(0, 5)  # Solo una red tendrá connect=True
        
        for i in range(6):
            network = {
                "BSSID": f"00:1A:2B:3C:4D:{random.randint(10, 99)}",
                "frequency": random.choice([2400, 5400]),
                "signal": random.randint(-100, 0),
                "security": random.choice(["WPA", ""]),
                "ssid": f"Network_{i+1}",
                "connect": i == current_network_index
            }
            networks.append(network)
        
        return networks
