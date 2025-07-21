from.C_M import CM
C=CM()
G='\n'*3
Tag=f"\n{C.r}————|———————|————{C.g}•❀ {C.rkj}Tag {C.g}❀•{C.r}————|———————|————\n"
EX=f"{C.pr}\n   |\n   ╰{C.r}┈{C.rkj}➢ {C.g}ApkPatcher -i Your_Apk_Path.apk {C.rkj}"
Info=f"{C.lb}[ {C.y}INFO {C.lb}] {C.c}"
class CustomArgumentParser(C.argparse.ArgumentParser):
	def error(E,message):
		D=message;B=''
		for A in E._actions:
			if A.option_strings and any(A in D for A in A.option_strings):
				if A.dest=='input':B=f'\n{C.lb}[ {C.y}FYI ! {C.lb}] {C.g}Make Sure There Is "No Extra Space" In The Folder/Apk Name In The Input Text. If Yes, Then Remove Extra Space & Correct It By Renaming It.{G}{Info}With Your Certificate Flag: {C.rkj}-c {C.pr}( Input Your pem/crt/cert Path ){EX}-c {C.y}certificate.cert{G}{Info}If you are using an Emulator in PC Then Use Flag: {C.rkj}-e{EX}-c {C.y}certificate.cert {C.rkj}-e\n'
				elif A.dest=='Merge':B=f"\n{Info}Only Merge Apk{G}{Info}Merge Extension {C.y}( .apks/.xapk/.apkm ){G}{C.lb}[ {C.y}Ex. {C.lb}] {C.g}ApkPatcher {C.rkj}-m {C.g}Your_Apk_Path.apks\n"
				break
		exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} {D}\n\n{B}")
	def print_help(A):super().print_help();print(f"\n{Info} ApkPatcher Default Patch is VPN & SSL Bypass, Show Other Patch Flags List with: {C.g}ApkPatcher -O{C.c}\n")
	def Other_Patch(D):
		A='Tag';print(f"""
{C.lb}[ {C.pr}* {C.lb}] {C.c}Other Patch Flags Help ( Keep Sequence in Mind )

 <Flags>                 {C.g}─•❀•❀ {C.c}Info Patch {C.g}❀•❀•─{C.rkj}

  -A, {C.c}--AES_Logs         {C.y}➸ {C.g}AES Logs Inject{C.rkj}
  -D, {C.c}--Android_ID       {C.y}➸ {C.g}Hook Android ID for One Device Login Bypass{C.rkj}
  -f, {C.c}--Flutter          {C.y}➸ {C.g}Flutter SSL Bypass{C.rkj}
  -p, {C.c}--Pairip           {C.y}➸ {C.g}Pairip CERT SSL Bypass (No Sign){C.rkj}
  -P, {C.c}--Purchase         {C.y}➸ {C.g}Purchase/Paid/Price{C.rkj}
  -r, {C.c}--Random_Info      {C.y}➸ {C.g}Fake Device Info{C.rkj}
  -rmads, {C.c}--Remove_Ads   {C.y}➸ {C.g}Bypass Ads{C.rkj}
  -rmsc, {C.c}--Remove_SC     {C.y}➸ {C.g}Bypass Screenshot Restriction{C.rkj}
  -rmu, {C.c}--Remove_USB     {C.y}➸ {C.g}Bypass USB Debugging Permission{C.rkj}
  -pkg, {C.c}--Spoof_PKG      {C.y}➸ {C.g}Spoof Package Detection{C.rkj}
  -skip {C.c}[Skip_Patch ...] {C.y}➸ {C.g}Skip Specific Patches (e.g. getAcceptedIssuers){C.rkj}
  -s, {C.c}--AES_S            {C.y}➸ {C.g}Do U Want Separate AES.smali Dex{C.rkj}""");B=input(f"\n\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Do See Example\n{C.g}  |\n  └──── {C.r}~ y / Exit to Enter {C.g}$ : {C.y}")
		if B.lower()=='y':print(f"""
{Tag.replace(A,"AES Logs Inject")}

{Info}AES MT Logs Inject Flag: {C.rkj}-A{EX}-A{G}{Info}Do U Want Separate AES.smali Dex Use Flag: {C.rkj}-A -s{EX}-A -s

{Tag.replace(A,"Hook Android ID")}

{Info}Hook Android ID For One Device Login Bypass Use Flag: {C.rkj}-D {C.pr}( Input Your Original 16 Digit Android ID ){EX}-D {C.y}7e9f51f096bd5c83

{Tag.replace(A,"isFlutter / isPairip")}

{Info}If Apk is Flutter Then Use Additional Flag: {C.rkj}-f{EX}-f {C.y}-c certificate.cert{G}{Info}If Apk is Pairip Then Use Additional Flag: {C.rkj}-p {C.pr}( Without Sign Apk Use Only in VM / Multi_App ){EX}-p {C.y}-c certificate.cert

{Tag.replace(A,"Spoof PKG / Device Info")}

{Info}Spoof Package Detection Flag: {C.rkj}-pkg {C.pr}( Dex / Manifest / Res ){EX}-pkg{G}{Info}Fake Device Info Flag: {C.rkj}-r{EX}-r{G}{Info}With Your Android ID Flag: {C.rkj}-r -D {C.pr}( Input Your Custom 16 Digit Android ID ){EX}-r -D {C.y}7e9f51f096bd5c83

{Tag.replace(A,"Bypass Ads / SC / USB")}

{Info}Bypass Ads Flag: {C.rkj}-rmads{EX}-rmads{G}{Info}Bypass Screenshot Restriction Flag: {C.rkj}-rmsc{EX}-rmsc{G}{Info}Bypass USB Debugging Permission Flag: {C.rkj}-rmu{EX}-rmu

{Tag.replace(A,"isPurchase / Skip Patch")}

{Info}Purchase / Paid / Price Flag: {C.rkj}-P{EX}-P{G}{Info}Skip Patch Flag: {C.rkj}-skip{EX}-skip {C.y}getAcceptedIssuers""")
		else:return
def parse_arguments():
	J='-C';B='store_true';G=C.sys.argv[1:]
	if'-O'in G:exit(CustomArgumentParser().Other_Patch())
	A=CustomArgumentParser(description=f"{C.c}ApkPatcher Script")if any(A.startswith('-')for A in G)else C.argparse.ArgumentParser(description=f"{C.c}ApkPatcher Script");H=A.add_mutually_exclusive_group(required=True);H.add_argument('-i',dest='input',help=f"{C.y}➸{C.g} Input APK Path...{C.c}");H.add_argument('-m',dest='Merge',help=f"{C.y}➸{C.g} Anti-Split ( Only Merge Apk ){C.c}");H.add_argument(J,dest='Credits_Instruction',action=B,help=f"{C.y}➸{C.g} Show Instructions & Credits{C.c}");I=A.add_argument_group(f"{C.rkj}[ * ] Additional Flags{C.c}");I.add_argument('-a','--APKEditor',action=B,help=f"{C.y}➸ {C.g}APKEditor ( Default APKTool ){C.c}");I.add_argument('-e','--For_Emulator',action=B,help=f"{C.y}➸{C.g} If using emulator on PC then use -e flag{C.c}");I.add_argument('-c',dest='CA_Certificate',type=str,nargs='*',help=f"{C.y}➸{C.g} Input Your HttpCanary/Reqable/ProxyPin etc. Capture Apk's CA-Certificate{C.c}");A.add_argument('-A','--AES_Logs',action=B,help=C.argparse.SUPPRESS);A.add_argument('-D','--Android_ID',action=B,help=C.argparse.SUPPRESS);A.add_argument('-f','--Flutter',action=B,help=C.argparse.SUPPRESS);A.add_argument('-p','--Pairip',action=B,help=C.argparse.SUPPRESS);A.add_argument('-P','--Purchase',action=B,help=C.argparse.SUPPRESS);A.add_argument('-r','--Random_Info',action=B,help=C.argparse.SUPPRESS);A.add_argument('-rmads','--Remove_Ads',action=B,help=C.argparse.SUPPRESS);A.add_argument('-rmsc','--Remove_SC',action=B,help=C.argparse.SUPPRESS);A.add_argument('-rmu','--Remove_USB',action=B,help=C.argparse.SUPPRESS);A.add_argument('-pkg','--Spoof_PKG',action=B,help=C.argparse.SUPPRESS);A.add_argument('-skip',dest='Skip_Patch',nargs='*',help=C.argparse.SUPPRESS);A.add_argument('-s','--AES_S',action=B,help=C.argparse.SUPPRESS);K='.apk','.apks','.apkm','.xapk';D=[];E=None;L=False
	for(M,F)in enumerate(G):
		if F in['-i','-m','-L','-rm','-r',J]:E,D=M+1,D+[F]
		elif E and(F.endswith(K)or C.os.path.isdir(F)):D,E=D+[' '.join(G[E:M+1])],None;L=True
		elif not E:D.append(F)
	if not L and C.sys.argv[1:2]!=[J]:print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Only Supported Extensions {C.g}{K}\n")
	print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Input Path {C.g}➸❥{C.y}",*D,f"{C.r}\n");return A.parse_args(D)