from .C_M import CM; C = CM()
G2 = "\n" * 2

run_dir = C.os.path.dirname(C.os.path.abspath(C.sys.argv[0]))

class FileCheck:
    # Full path to jar & other
    def set_paths(self):
        self.APKEditor_Path = C.os.path.join(run_dir, "APKEditor.jar")
        self.APKTool_Path = C.os.path.join(run_dir, "APKTool_AP.jar")
        self.Sign_Jar = C.os.path.join(run_dir, "Uber-Apk-Signer.jar")
        self.AES_Smali = C.os.path.join(C.os.path.dirname(C.os.path.abspath(__file__)), "AES.smali")
    def isEmulator(self):
        self.APKTool_Path_E = C.os.path.join(run_dir, "APKTool_OR.jar")

    # Calculate SHA-256 checksum of a file
    def calculate_checksum(self, file_path):
        sha256_hash = C.hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except FileNotFoundError:
            return None

    # Function to download files
    def download_file(self, Jar_Files):
        import requests
        downloaded_urls = set()
        for file_url, local_path, expected_checksum in Jar_Files:
            lo_path = C.os.path.basename(local_path)

            if C.os.path.exists(local_path):
                current_checksum = self.calculate_checksum(local_path)
                if current_checksum == expected_checksum:
                    continue
                else:
                    print(f"{C.rd}[ {C.pr}File {C.rd}] {C.c}{lo_path} {C.rd}is Corrupt (Checksum Mismatch).{G2}{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Re-Downloading, Need Internet Connection.{C.r}\n")
                    C.os.remove(local_path)
            try:
                Version = C.re.findall(r'version = "([^"]+)"', requests.get("https://raw.githubusercontent.com/TechnoIndian/ApkPatcher/main/pyproject.toml").text)[0]
                if Version != "2.0":
                    print(f"\n{C.lb}[ {C.y}Update {C.lb}]{C.c} Updating ApkPatcher 𒁍 {C.g}{Version}...{G2}")
                    cmd = (["pip", "install", "git+https://github.com/TechnoIndian/ApkPatcher.git"] if C.os.name == "nt" else "pip install --force-reinstall https://github.com/TechnoIndian/ApkPatcher/archive/refs/heads/main.zip")
                    C.subprocess.run(cmd, shell=isinstance(cmd, str), check=True)

                print(f"\n{C.lb}[ {C.pr}Downloading {C.lb}] {C.c}{lo_path}", end='', flush=True)
                response = requests.get(file_url, stream=True, timeout=10)

                if response.status_code == 200:
                    total_size = int(response.headers.get('content-length', 0))
                    block_size = 1024
                    downloaded = 0
                    with open(local_path, 'wb') as f:
                        for data in response.iter_content(block_size):
                            downloaded += len(data)
                            f.write(data)
                            progress = downloaded / total_size * 100 if total_size > 0 else 0
                            mb_downloaded = downloaded / (1024 * 1024)
                            total_mb = total_size / (1024 * 1024) if total_size > 0 else 0
                            progress_line = f"\r{C.lb}[ {C.pr}Downloading {C.lb}] {C.c}{lo_path} {C.g}➸❥ {progress:.2f}% ({mb_downloaded:.2f}/{total_mb:.2f} MB)"
                            print(progress_line, end='\r')

                    print(f"\n{C.g}       |\n       └──── {C.r}Downloaded ~{C.g}$ {lo_path} Successfully. ✔\n")

                else:
                    exit(f'{G2}{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Failed to download {C.y}{lo_path} {C.rd}Status Code: {response.status_code}{G2}{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Restart Script...{C.r}\n')
            except requests.exceptions.RequestException:
                exit(f'{G2}{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Got an error while Fetching {C.y}{local_path}{G2}{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} No internet Connection{G2}{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Internet Connection is Required to Download {C.y}{lo_path}\n')

    def F_D(self):
        Jar_Files = [
            ("https://github.com/TechnoIndian/Tools/releases/download/Tools/APKEditor.jar", self.APKEditor_Path, "c242f5fc4591667a0084668320d0016a20e7c2abae102c1bd4d640e11d9f60ee"),
            (("https://github.com/TechnoIndian/Tools/releases/download/Tools/APKTool.jar" if C.os.name == 'nt' else "https://github.com/TechnoIndian/Tools/releases/download/Tools/APKTool_Modified.jar"), self.APKTool_Path, "effb69dab2f93806cafc0d232f6be32c2551b8d51c67650f575e46c016908fdd" if C.os.name == 'nt' else "cd06421602202fc23de9e4e0425d35ab62897660b76b2d938a72db16ac7aab8e"),
            ("https://github.com/TechnoIndian/Tools/releases/download/Tools/Uber-Apk-Signer.jar", self.Sign_Jar, "e1299fd6fcf4da527dd53735b56127e8ea922a321128123b9c32d619bba1d835"),
            ("https://raw.githubusercontent.com/TechnoIndian/Objectlogger/refs/heads/main/AES.smali", self.AES_Smali, "09db8c8d1b08ec3a2680d2dc096db4aa8dd303e36d0e3c2357ef33226a5e5e52")
        ]
        self.download_file(Jar_Files)
        C.os.system('cls' if C.os.name == 'nt' else 'clear')
        
    def F_D_A(self, isEmulator):
        Jar_Files = []
        if isEmulator:
            Jar_Files.append(("https://github.com/TechnoIndian/Tools/releases/download/Tools/APKTool.jar", self.APKTool_Path_E, "effb69dab2f93806cafc0d232f6be32c2551b8d51c67650f575e46c016908fdd"))
        if Jar_Files:
            self.download_file(Jar_Files)