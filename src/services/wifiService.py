import subprocess

class WifiService:
    @staticmethod
    def scan():
        subprocess.run("sudo wpa_cli scan", check=True)
    
    @staticmethod
    def scan_results() -> list:
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
    def add_network(ssid:str, psk: str) -> int:
        network_id = subprocess.check_output(
            "sudo wpa_cli add_network", shell=True).decode("utf-8")
        try: 
            network_id = int(network_id)
        except:
            return -1
        
        result = subprocess.check_output(
            f'sudo wpa_cli set_network {network_id} ssid "{ssid}"', shell=True).decode("utf-8")
        
        if "OK" not in result:
            return -1
        
        result = subprocess.check_output(
            f'sudo wpa_cli set_network {network_id} psk "{psk}"', shell=True).decode("utf-8")
        
        if "OK" not in result:
            return -1
        
        result = subprocess.check_output(
            f'sudo wpa_cli enable_network {network_id}', shell=True).decode("utf-8")
        
        if "OK" not in result:
            return -1
        
        result = subprocess.check_output(
            f'sudo wpa_cli select_network {network_id}', shell=True).decode("utf-8")
        
        if "OK" not in result:
            return -1
        
        result = subprocess.check_output(
            'sudo wpa_cli reconnect', shell=True).decode("utf-8")
        
        if "OK" not in result:
            return -1
        
        return network_id
    
    #Execute between three and five minutes after add_network
    def verify_network_and_save(id:int) -> bool:
        result = subprocess.check_output(
            'sudo wpa_cli status', shell=True).decode("utf-8")
        if "COMPLETED" not in result:
            subprocess.run(f'sudo wpa_cli disable_network {id}', check=True)
            subprocess.run(f'sudo wpa_cli remove_network {id}', check=True)
            subprocess.run(f'sudo wpa_cli save_config', check=True)
            return False
        subprocess.run(f'sudo wpa_cli save_config', check=True)
        return True
    
    #Execute to delete saved network
    def delete_network(ssid:str) -> bool:
        lines = subprocess.check_output(
            "sudo wpa_cli list_networks", shell=True).decode("utf-8")
        lines: list = lines.split("\n")[2:]
        if len(lines) == 0:
            return False
        id = -1
        for line in lines:
            if ssid in line:
                id = line.split("\t")[0]
                break
        if id == -1:
            return False
        subprocess.run(f'sudo wpa_cli disable_network {id}', check=True)
        subprocess.run(f'sudo wpa_cli remove_network {id}', check=True)
        subprocess.run(f'sudo wpa_cli save_config', check=True)
        return True
        
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