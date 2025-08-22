from .C_M import CM; C = CM()

# ---------------- Set Path ----------------
run_dir = C.os.path.dirname(C.os.path.abspath(C.sys.argv[0]))
script_dir = C.os.path.dirname(C.os.path.abspath(__file__))

class FileCheck:
    # ---------------- Set Jar & Files Paths ----------------
    def Set_Path(self):
        self.APKEditor_Path = C.os.path.join(run_dir, "APKEditor.jar")
        self.APKTool_Path = C.os.path.join(run_dir, "APKTool_AP.jar")
        self.Sign_Jar = C.os.path.join(run_dir, "Uber-Apk-Signer.jar")
        self.AES_Smali = C.os.path.join(script_dir, "AES.smali")
        self.Pairip_CoreX = C.os.path.join(script_dir, "lib_Pairip_CoreX.so")

    def isEmulator(self):
        self.APKTool_Path_E = C.os.path.join(run_dir, "APKTool_OR.jar")

    # ---------------- SHA-256 CheckSum ----------------
    def calculate_checksum(self, file_path):
        sha256_hash = C.hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except FileNotFoundError:
            return None

    # ---------------- Download Files ----------------
    def Download_Files(self, Jar_Files):
        import requests
        downloaded_urls = set()
        for file_url, local_path, expected_checksum in Jar_Files:
            lo_path = C.os.path.basename(local_path)

            if C.os.path.exists(local_path):
                current_checksum = self.calculate_checksum(local_path)
                if current_checksum == expected_checksum:
                    continue
                else:
                    print(f"{C.rd}[ {C.pr}File {C.rd}] {C.c}{lo_path} {C.rd}is Corrupt (Checksum Mismatch).\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Re-Downloading, Need Internet Connection.\n")
                    C.os.remove(local_path)
            try:
                Version = C.re.findall(r'version = "([^"]+)"', requests.get("https://raw.githubusercontent.com/TechnoIndian/ApkPatcher/main/pyproject.toml").text)[0]
                if Version != "2.0":
                    print(f"\n{C.lb}[ {C.y}Update {C.lb}]{C.c} Updating ApkPatcher 𒁍 {C.g}{Version}...\n\n")
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
                    exit(f'\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Failed to download {C.y}{lo_path} {C.rd}Status Code: {response.status_code}\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Restart Script...\n')
            except requests.exceptions.RequestException:
                exit(f'\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Got an error while Fetching {C.y}{local_path}\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} No internet Connection\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Internet Connection is Required to Download {C.y}{lo_path}\n')

    # ---------------- Files Download Link ----------------
    def F_D(self):

        self.Download_Files([
            ("https://github.com/TechnoIndian/Tools/releases/download/Tools/APKEditor.jar", self.APKEditor_Path, "c242f5fc4591667a0084668320d0016a20e7c2abae102c1bd4d640e11d9f60ee"),
            (("https://github.com/TechnoIndian/Tools/releases/download/Tools/APKTool.jar" if C.os.name == 'nt' else "https://github.com/TechnoIndian/Tools/releases/download/Tools/APKTool_Modified.jar"), self.APKTool_Path, "effb69dab2f93806cafc0d232f6be32c2551b8d51c67650f575e46c016908fdd" if C.os.name == 'nt' else "3920022a7e3da9c3e89540400f907b9963ce9a375b39c4a6b9d11c4395d7abf7"),
            ("https://github.com/TechnoIndian/Tools/releases/download/Tools/Uber-Apk-Signer.jar", self.Sign_Jar, "e1299fd6fcf4da527dd53735b56127e8ea922a321128123b9c32d619bba1d835"),
            ("https://raw.githubusercontent.com/TechnoIndian/Objectlogger/refs/heads/main/AES.smali", self.AES_Smali, "09db8c8d1b08ec3a2680d2dc096db4aa8dd303e36d0e3c2357ef33226a5e5e52"),
            ("https://github.com/TechnoIndian/Tools/releases/download/Tools/lib_Pairip_CoreX.so", self.Pairip_CoreX, "22a7954092001e7c87f0cacb7e2efb1772adbf598ecf73190e88d76edf6a7d2a")
        ])

        C.os.system('cls' if C.os.name == 'nt' else 'clear')
        
    # ---------------- Files Download isEmulator ----------------
    def F_D_A(self):

        self.Download_Files([("https://github.com/TechnoIndian/Tools/releases/download/Tools/APKTool.jar", self.APKTool_Path_E, "effb69dab2f93806cafc0d232f6be32c2551b8d51c67650f575e46c016908fdd")])