from .C_M import CM; C = CM()
from .Files_Check import FileCheck

F = FileCheck(); F.set_paths();
C_Line = f"{C.r}{'_' * 61}"; G = "\n" * 3; G2 = "\n" * 2

# Anti_Split
def Anti_Split(apk_path, isMerge):
    try:
        base_name, Ext = C.os.path.splitext(apk_path)
        Merge_Ext = ['.apks', '.apkm', '.xapk']

        if Ext in Merge_Ext:
            output_path = f"{base_name.replace(' ', '_')}.apk"
            print(f"{C_Line}{G}{C.lb}[ {C.pr}* {C.lb}] {C.c} Anti-Split Start...")
            print(f"{C.g}  |\n  └──── {C.r}Decompiling ~{C.g}$ java -jar {C.os.path.basename(F.APKEditor_Path)} m -i {apk_path} -f -o {output_path}{G2}{C_Line}{C.g}\n")
            command = ["java", "-jar", F.APKEditor_Path, "m", "-i", apk_path, "-f", "-o", output_path]
            try:
                result = C.subprocess.run(command, check=True)
                print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Anti-Split Successful  {C.g}✔{C.r}{G2}{C_Line}\n")
                if isMerge: exit()
                return output_path
            except C.subprocess.CalledProcessError as e:
                exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Anti-Split Failed ! ✘{C.r}{G2}{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Error Output: {e.stderr}\n")
        if isMerge and Ext not in Merge_Ext:
            exit(f"\n{C.lb}[{C.c} Info {C.lb}] {C.rd}Split ✘{C.r}{G}{C.lb}[ {C.pr}* {C.lb}] {C.c} Only Supported Extensions {C.g}{Merge_Ext}\n")
        return apk_path
    except (FileNotFoundError, Exception) as e:
        exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} {str(e)} ✘{C.r}\n")