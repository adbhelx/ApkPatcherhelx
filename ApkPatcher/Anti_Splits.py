from.C_M import CM
C=CM()
from.Files_Check import FileCheck
F=FileCheck()
F.set_paths()
C_Line=f"{C.r}{'_'*61}"
G='\n'*3
G2='\n'*2
def Anti_Split(apk_path,isMerge):
	H=isMerge;A=apk_path
	try:
		J,I=C.os.path.splitext(A);B=['.apks','.apkm','.xapk']
		if I in B:
			D=f"{J.replace(' ','_')}.apk";print(f"{C_Line}{G}{C.lb}[ {C.pr}* {C.lb}] {C.c} Anti-Split Start...");print(f"{C.g}  |\n  └──── {C.r}Decompiling ~{C.g}$ java -jar {C.os.path.basename(F.APKEditor_Path)} m -i {A} -f -o {D}{G2}{C_Line}{C.g}\n");K=['java','-jar',F.APKEditor_Path,'m','-i',A,'-f','-o',D]
			try:
				L=C.subprocess.run(K,check=True);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Anti-Split Successful  {C.g}✔{C.r}{G2}{C_Line}\n")
				if H:exit()
				return D
			except C.subprocess.CalledProcessError as E:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Anti-Split Failed ! ✘{C.r}{G2}{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Error Output: {E.stderr}\n")
		if H and I not in B:exit(f"\n{C.lb}[{C.c} Info {C.lb}] {C.rd}Split ✘{C.r}{G}{C.lb}[ {C.pr}* {C.lb}] {C.c} Only Supported Extensions {C.g}{B}\n")
		return A
	except(FileNotFoundError,Exception)as E:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} {str(E)} ✘{C.r}\n")