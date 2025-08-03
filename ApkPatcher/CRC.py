from .C_M import CM; C = CM()

def Format_Time(timestamp):
    return C.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

def CRC_Fix(apk_path, build_dir, file_types):
    Fix_Count, Logs = 0, []
    with C.zipfile.ZipFile(apk_path) as Zip_OR, C.zipfile.ZipFile(build_dir) as Zip_Fix:
        F = lambda Z: {i.filename: (i.CRC, i.date_time) for i in Z.infolist() if any(ft in i.filename for ft in file_types)}
        ORIGIN, Fix = F(Zip_OR), F(Zip_Fix)

    for filename, (OR_CRC, OR_Time) in ORIGIN.items():
        if filename in Fix and OR_CRC != Fix[filename][0]:
            with open(build_dir, "rb+") as f:
                D = f.read().replace(Fix[filename][0].to_bytes(4, 'little'), OR_CRC.to_bytes(4, 'little'))
                f.seek(0); f.write(D)
            Fix_Count += 1
            Logs.append((filename, f"{OR_CRC:08x}", f"{Fix[filename][0]:08x}", Format_Time(C.datetime(*OR_Time).timestamp()), Format_Time(C.datetime(*Fix[filename][1]).timestamp())))

    print(f"\n{'':20}✨ {C.g}CRCFix by {C.rkj}Kirlif{C.g}' ✨\n")
    print(f"{C.c}{'File Name':<22}{'CRC':<12}{'FIX':<12}{'Modified'}")

    for e in Logs:
        print(f"\n{C.g}{e[0]:<22}{e[1]}{'':<4}{e[2]}{'':<4}{e[4]}\n")
    print(f"\n{C.lb}[{C.c}  INPUT  {C.lb}] {C.g}➸❥ {C.y}{apk_path}\n")
    print(f"{C.lb}[{C.c}  OUTPUT  {C.lb}] {C.g}➸❥ {C.y}{build_dir}\n")
    print(f"\n{C.lb}[{C.c}  CRCFix  {C.lb}] {C.g}➸❥ {C.pr}{Fix_Count}{C.r}\n")
    return build_dir