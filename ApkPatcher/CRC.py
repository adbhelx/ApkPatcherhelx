from.C_M import CM
C=CM()
def Format_Time(timestamp):return C.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
def CRC_Fix(apk_path,build_dir,file_types):
	L='little';H=apk_path;D=build_dir;I,J=0,[]
	with C.zipfile.ZipFile(H)as M,C.zipfile.ZipFile(D)as N:K=lambda Z:{A.filename:(A.CRC,A.date_time)for A in Z.infolist()if any(B in A.filename for B in file_types)};O,B=K(M),K(N)
	for(A,(F,P))in O.items():
		if A in B and F!=B[A][0]:
			with open(D,'rb+')as G:Q=G.read().replace(B[A][0].to_bytes(4,L),F.to_bytes(4,L));G.seek(0);G.write(Q)
			I+=1;J.append((A,f"{F:08x}",f"{B[A][0]:08x}",Format_Time(C.datetime(*P).timestamp()),Format_Time(C.datetime(*B[A][1]).timestamp())))
	print(f"\n{'':20}✨ {C.g}CRCFix by {C.rkj}Kirlif{C.g}' ✨\n");print(f"{C.c}{'File Name':<22}{'CRC':<12}{'FIX':<12}{'Modified'}")
	for E in J:print(f"\n{C.g}{E[0]:<22}{E[1]}{'':<4}{E[2]}{'':<4}{E[4]}\n")
	print(f"\n{C.lb}[{C.c}  INPUT  {C.lb}] {C.g}➸❥ {C.y}{H}\n");print(f"{C.lb}[{C.c}  OUTPUT  {C.lb}] {C.g}➸❥ {C.y}{D}\n");print(f"\n{C.lb}[{C.c}  CRCFix  {C.lb}] {C.g}➸❥ {C.pr}{I}{C.r}\n");return D