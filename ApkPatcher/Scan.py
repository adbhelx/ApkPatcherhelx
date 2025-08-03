from .C_M import CM; C = CM();
from .Files_Check import FileCheck

F = FileCheck(); F.set_paths();

# Apk Package Name
def Scan_Apk(apk_path, isFlutter, Flutter_lib, isPairip, Pairip_lib):

    print(f"\n{C.r}{'_' * 61}\n")
    Package_Name = ''

    if C.os.name == 'posix':
        # Extract Package Name with aapt
        Package_Name = C.subprocess.run(['aapt', 'dump', 'badging', apk_path], capture_output=True, text=True).stdout.split("package: name='")[1].split("'")[0]
        if Package_Name:
            print(f"\n{C.lb}[ {C.c}Package Name {C.lb}] {C.rkj}➸❥ {C.pr}'{C.g}{Package_Name}{C.pr}'{C.g} ✔")
            
    # Extract Package Name with APKEditor
    if not Package_Name:
        Package_Name = C.subprocess.run(["java", "-jar", F.APKEditor_Path, "info", "-package", "-i", apk_path], capture_output=True, text=True).stdout.split('"')[1]
        print(f"\n{C.lb}[ {C.c}Package Name {C.lb}] {C.rkj}➸❥ {C.pr}'{C.g}{Package_Name}{C.pr}'{C.g} ✔")
            
    if Flutter_lib:
        if Flutter_lib:
            def check_java_installed():
                try:
                    C.subprocess.run(['radare2', '-v'], capture_output=True, text=True)
                except (C.subprocess.CalledProcessError, FileNotFoundError):
                    if C.os.name == 'posix':
                        for pkg in ['radare2']:
                            try:
                                result = C.subprocess.run(['pkg', 'list-installed'], capture_output=True, text=True)
                                if pkg not in result.stdout:
                                    print(f"\n{C.lb}[ {C.pr}Installing {C.lb}] {C.c}{pkg}...{C.g}\n")
                                    C.subprocess.check_call(['pkg', 'install', '-y', pkg])
                                    print(f"\n{C.lb}[ {C.pr}Installed {C.lb}] {C.c}{pkg} Successfully.{C.g} ✔\n")
                                    C.os.system('cls' if C.os.name == 'nt' else 'clear')
                            except (C.subprocess.CalledProcessError, Exception) as e:
                                exit(f"\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} No Internet Connection. ✘\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Internet Connection is Required to Installation {C.rd}'{C.g}pkg install {pkg}{C.rd}' ✘\n")
                    else:
                        exit(f'\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Radare2 is not installed on Your System. ✘\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Install Radare2 and Run Script Again in New CMD. ✘\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Verify Radare2 installation using {C.rd}"{C.g}radare2 -v{C.rd}" command in CMD')
            check_java_installed()
        if not isFlutter:
            exit(f"\n\n{C.lb}[ {C.c}Flutter Protection {C.lb}] {C.rkj}➸❥ {C.pr}'{C.g}{', '.join(C.os.path.basename(lib) for lib in Flutter_lib)}{C.pr}'{C.g} ✔\n\n{C.lb}[ {C.y}WARN ! {C.lb}] {C.rd}This is a Flutter app. To bypass SSL, you will have to use the {C.g}'-f' {C.rd}Flag.\n")
        else:
            if isFlutter:
                print(f"\n\n{C.lb}[ {C.c}Flutter Protection {C.lb}] {C.rkj}➸❥ {C.pr}'{C.g}{', '.join(C.os.path.basename(lib) for lib in Flutter_lib)}{C.pr}'{C.g} ✔")
    if Pairip_lib:
        if not isPairip:
            exit(f"\n\n{C.lb}[ {C.c}Pairip Protection {C.lb}] {C.rkj}➸❥ {C.pr}'{C.g}{', '.join(C.os.path.basename(lib) for lib in Pairip_lib)}{C.pr}'{C.g} ✔\n\n{C.lb}[ {C.y}WARN ! {C.lb}] {C.rd}This is a Pairip app. To bypass SSL, you will have to use the {C.g}'-p' {C.rd}Flag.\n")
        else:
            if isPairip:
                print(f"\n\n{C.lb}[ {C.c}Pairip Protection {C.lb}] {C.rkj}➸❥ {C.pr}'{C.g}{', '.join(C.os.path.basename(lib) for lib in Pairip_lib)}{C.pr}'{C.g} ✔")