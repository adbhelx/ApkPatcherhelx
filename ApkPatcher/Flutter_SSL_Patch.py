# -* coding: utf-8 *-
# @auhtor: AbhiTheModder
_C=True
_B='x86'
_A='arm'
from.C_M import CM
C=CM()
patterns={'arm64':['F. 0F 1C F8 F. 5. 01 A9 F. 5. 02 A9 F. .. 03 A9 .. .. .. .. 68 1A 40 F9','F. 43 01 D1 FE 67 01 A9 F8 5F 02 A9 F6 57 03 A9 F4 4F 04 A9 13 00 40 F9 F4 03 00 AA 68 1A 40 F9','FF 43 01 D1 FE 67 01 A9 .. .. 06 94 .. 7. 06 94 68 1A 40 F9 15 15 41 F9 B5 00 00 B4 B6 4A 40 F9'],_A:['2D E9 F. 4. D0 F8 00 80 81 46 D8 F8 18 00 D0 F8'],_B:['55 41 57 41 56 41 55 41 54 53 50 49 89 fe 48 8b 1f 48 8b 43 30 4c 8b b8 d0 01 00 00 4d 85 ff 74 12 4d 8b a7 90 00 00 00 4d 85 e4 74 4a 49 8b 04 24 eb 46','55 41 57 41 56 41 55 41 54 53 50 49 89 f. 4c 8b 37 49 8b 46 30 4c 8b a. .. 0. 00 00 4d 85 e. 74 1. 4d 8b','55 41 57 41 56 41 55 41 54 53 48 83 EC 18 49 89 FF 48 8B 1F 48 8B 43 30 4C 8B A0 28 02 00 00 4D 85 E4 74','55 41 57 41 56 41 55 41 54 53 48 83 EC 38 C6 02 50 48 8B AF A. 00 00 00 48 85 ED 74 7. 48 83 7D 00 00 74','55 41 57 41 56 41 55 41 54 53 48 83 EC 18 49 89 FE 4C 8B 27 49 8B 44 24 30 48 8B 98 D0 01 00 00 48 85 DB']}
def get_r2_version():
	try:
		A=C.subprocess.run(['r2','-V'],capture_output=_C,text=_C,check=_C);B=A.stdout.strip().split()
		for A in B:
			if A.startswith('5.'):A=A.split('-')[0];return A
		return
	except(C.subprocess.CalledProcessError,FileNotFoundError):return
def find_offset(r2,patterns,is_iA=False):
	I='bins';G=patterns;D=r2
	if is_iA:A=C.json.loads(D.cmd('iAj'))
	else:A=C.json.loads(D.cmd('iaj'))
	F=A[I][0]['arch'];H=A[I][0]['bits']
	if F==_A and H==64:A='arm64'
	elif F==_A and H==16:A=_A
	elif F==_B and H==64:A=_B
	else:print(f"\n{C.lb}[ {C.rd}Error {C.lb}]{C.rd} Unsupported architecture: {F}\n");return
	if A in G:
		for A in G:
			for J in G[A]:
				B=D.cmd(f"/x {J}");B=B.strip().split(' ')[0]
				if B:
					E=D.cmd(f"{B};afl.").strip().split(' ')[0];print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} ssl_verify_peer_cert found at: {C.lb}{B}\n")
					if not E and A==_B:E=B;D.cmd(f"af @{E}")
					print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} function at: {C.y}{E}\n");return E
def Patch_Flutter_SSL(decompile_dir,isAPKEditor):
	E=decompile_dir;print(f"\r{C.lb}[ {C.pr}* {C.lb}] {C.c} Flutter SSL Patch, Script by {C.rkj}🇮🇳 AbhiTheM0dder 🇮🇳\n")
	try:
		K=tuple(map(int,get_r2_version().split('.')));L=tuple(map(int,'5.9.5'.split('.')))
		if K<=L:F=_C
		else:F=False
	except Exception as M:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} {str(M)}\n")
	G=['arm64-v8a','armeabi-v7a','armeabi','x86_64'];B=None
	for H in G:
		N='root/lib'if isAPKEditor else'lib';I=C.os.path.join(E,N,H,'libflutter.so')
		if C.os.path.exists(I):B=I;break
	if B:print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c}Found {C.g}➸❥ {C.y}{H}/{C.os.path.basename(B)} {C.g}✔\n")
	else:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd}libflutter.so not found in any of the specified architectures {G}\n");C.shutil.rmtree(E)
	import r2pipe as D
	if D.in_r2():A=D.open();A.cmd('e log.quiet=true');A.cmd('oo+')
	else:A=D.open(B,flags=['-w','-e','log.quiet=true'])
	print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.g}Analyzing function calls...\n");A.cmd('aac');print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.g}Searching for offset...\n");J=find_offset(A,patterns,F)
	if J:A.cmd(f"{J}");A.cmd('wao ret0');print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c}ssl_verify_peer_cert {C.g}Patched Successfully ! ✔\n")
	else:print(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd}ssl_verify_peer_cert Not Found. ✘\n")
	print(f"{C.r}{'_'*61}\n\n");A.quit()