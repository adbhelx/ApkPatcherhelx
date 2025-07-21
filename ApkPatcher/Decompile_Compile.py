_E='-o'
_D='-f'
_C='-jar'
_B='java'
_A=True
from.C_M import CM
C=CM()
from.Files_Check import FileCheck
F=FileCheck()
F.set_paths()
F.isEmulator()
C_Line=f"{C.r}{'_'*61}"
G='\n'*3
G2='\n'*2
def Decompile_Apk(apk_path,decompile_dir,isEmulator,isAPKEditor,isAES):
	D=isAPKEditor;B=apk_path;A=decompile_dir;E=F.APKTool_Path_E if isEmulator else F.APKTool_Path;print(f"\n{C_Line}\n")
	if D:G=[_B,_C,F.APKEditor_Path,'d',_D,'-no-dex-debug','-i',B,_E,A];print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompile with APKEditor...");print(f"{C.g}  |\n  └──── {C.r}Decompiling ~{C.g}$ java -jar {C.os.path.basename(F.APKEditor_Path)} d -f -no-dex-debug -i {B} -o {C.os.path.basename(A)}{G2}{C_Line}{C.g}\n")
	else:G=[_B,_C,E,'d',_D,'--only-main-classes']+(['-b']if isAES else[])+[B,_E,A,'-p',A];print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompiling APK...");print(f"{C.g}  |\n  └──── {C.r}Decompiling ~{C.g}$ java -jar {C.os.path.basename(E)} d -f {B} -o {C.os.path.basename(A)}{G2}{C_Line}{C.g}\n")
	try:C.subprocess.run(G,check=_A);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompile Successful  {C.g}✔{G2}{C_Line}{G2}")
	except C.subprocess.CalledProcessError:
		C.shutil.rmtree(A)
		if not D:print(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Decompile Failed ! ✘{G2}{C_Line}\n");exit(f"\n{C.lb}[ {C.y}Suggest ! {C.lb}]{C.c} Try With APKEditor, Flag {C.g}-a\n     |\n     └──── {C.r}~ Ex. {C.g}$ {C.rkj}ApkPatcher -i {C.y}{B} {C.g}-a\n")
		exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Decompile Failed ! ✘\n");return None,None
def Recompile_Apk(decompile_dir,apk_path,build_dir,isEmulator,isAPKEditor):
	B=build_dir;A=decompile_dir;E=F.APKTool_Path_E if isEmulator else F.APKTool_Path
	if isAPKEditor:
		D=[_B,_C,F.APKEditor_Path,'b','-i',A,_E,B,_D];print(f"{C_Line}{G}{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile APK...");print(f"{C.g}  |\n  └──── {C.r}Recompiling ~{C.g}$ java -jar {C.os.path.basename(F.APKEditor_Path)} b -i {C.os.path.basename(A)} -o {C.os.path.basename(B)} -f{G2}{C_Line}{C.g}\n")
		try:C.subprocess.run(D,check=_A);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile Successful  {C.g}✔{G2}{C_Line}\n")
		except C.subprocess.CalledProcessError:C.shutil.rmtree(A);exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Recompile Failed with APKEditor ! ✘\n")
	else:
		D=[_B,_C,E,'b',_D,A,_E,B,'-p',A];print(f"{C_Line}{G}{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile APK...");print(f"{C.g}  |\n  └──── {C.r}Recompiling ~{C.g}$ java -jar {C.os.path.basename(E)} b -f {C.os.path.basename(A)} -o {C.os.path.basename(B)}\n");print(f"{C_Line}{G}{C.lb}[ {C.pr}* {C.lb}] {C.c} ApkTool Default...{C.g}\n")
		try:C.subprocess.run(D,check=_A);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile Successful  {C.g}✔{G2}{C_Line}\n")
		except C.subprocess.CalledProcessError:
			print(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Default Recompile Failed! ✘\n");D=[_B,_C,E,'b',_D,'-use-aapt1',A,_E,B,'-p',A];print(f"{C_Line}{G}{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile APK...");print(f"{C.g}  |\n  └──── {C.r}Recompiling with aapt2 ~{C.g}$ java -jar {C.os.path.basename(E)} b -f -use-aapt1 {C.os.path.basename(A)} -o {C.os.path.basename(B)}\n");print(f"{C_Line}{G}{C.lb}[ {C.pr}* {C.lb}] {C.c} ApkTool AAPT2...{C.g}\n")
			try:C.subprocess.run(D,check=_A);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile Successful with aapt2 {C.g} ✔{G2}{C_Line}\n")
			except C.subprocess.CalledProcessError:C.shutil.rmtree(A);print(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} AAPT2 Recompile Failed! ✘{G2}{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Recompile Failed with both Default & aapt2 ! ✘{G2}{C_Line}\n");exit(f"\n{C.lb}[ {C.y}Suggest ! {C.lb}]{C.c} Try With APKEditor, Flag {C.g}-a\n     |\n     └──── {C.r}~ Ex. {C.g}$ {C.rkj}ApkPatcher -i {C.y}{apk_path} {C.g}-a\n")
	if C.os.path.exists(B):print(f"\n{C.lb}[ {C.c}APK Created {C.lb}] {C.g}➸❥ {C.y}{B} {C.g}✔{G2}{C_Line}\n")
	C.shutil.rmtree(A)
def FixSigBlock(decompile_dir,apk_path,build_dir,rebuild_dir):
	D=build_dir;A=rebuild_dir;C.os.rename(D,A);E=decompile_dir.replace('_decompiled','_SigBlock')
	for B in['d','b']:
		G=[_B,_C,F.APKEditor_Path,B,'-t','sig','-i',apk_path if B=='d'else A,_D,'-sig',E]
		if B=='b':G.extend([_E,D])
		C.subprocess.run(G,check=_A,text=_A,capture_output=_A)
	C.shutil.rmtree(E);C.os.remove(A)
def Sign_Apk(build_dir):
	A=build_dir;D=[_B,_C,F.Sign_Jar,'--overwrite','-a',A];print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Signing APK...");print(f"{C.g}  |\n  └──── {C.r}Signing ~{C.g}$ java -jar {C.os.path.basename(F.Sign_Jar)} --overwrite -a {A}{G2}{C_Line}{C.g}\n")
	try:
		C.subprocess.run(D,check=_A);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Sign Successful  {C.g}✔\n");B=A+'.idsig'
		if C.os.path.exists(B):C.os.remove(B)
		print(f"{C_Line}{G2}")
	except C.subprocess.CalledProcessError:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Sign Failed ! ✘\n")