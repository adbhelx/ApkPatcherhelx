
<p align="center">
<a href="https://t.me/TechnoYemen"><img alt="TechnoYemen" src="https://img.shields.io/badge/MADE%20IN-YEMEN-SCRIPT?color=%23ff0000&style=for-the-badge"></a>
</p>

<a name="readme-top"></a>

# ApkPatcher

<p align="center"> 
<a href="TechnoYemen"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=800&size=35&pause=1000&color=F74848&center=true&vCenter=true&random=false&width=435&lines=ApkPatcher" /></a>
</p>

## طريقة التثبيت
-------
**💢 المتطلبات الأساسية 💢**

```bash
termux-setup-storage && pkg update -y && pkg upgrade -y && pkg install python -y
```

👉🏻 لتثبيت ApkPatcher، قم بتنفيذ أي أمر من الأوامر التالية

💢 PYPI ( للاختبار فقط ) 💢

```bash
pip install ApkPatcher-install
```

أو

```bash
pip install ApkPatcher_install
```

الطريقة الأولى

💢 لأحدث إصدار ( من الفرع الرئيسي ) 💢

```bash
pip install --force-reinstall https://github.com/TechnoYemen/ApkPatcher/archive/refs/heads/main.zip
```

أو

```bash
pip install --force-reinstall https://github.com/TechnoYemen/ApkPatcher/archive/refs/heads/main.tar.gz
```

أو

```bash
curl -Ls https://github.com/TechnoYemen/Tools/releases/download/Tools/ApkPatcher.sh | bash
```

الطريقة الثانية

```bash
pkg install python git && pip install git+https://github.com/TechnoYemen/ApkPatcher.git
```

إزالة التثبيت

---

```bash
pip uninstall ApkPatcher
```

طريقة الاستخدام

---

ApkPatcher

وضع -i ➸ تعديل Smali (أدخل مسار APK)

```bash
ApkPatcher -i مسار_التطبيق.apk
```

بشهادة خاصة ( أدخل مسار pem / crt / cert )

```bash
ApkPatcher -i مسار_التطبيق.apk -c مسار_الشهادة.cert
```

شهادات متعددة

```bash
ApkPatcher -i مسار_التطبيق.apk -c /sdcard/HttpCanary/certs/HttpCanary.pem /sdcard/Download/Reqable/reqable-ca.crt /sdcard/Download/ProxyPinCA.crt
```

إذا كنت تستخدم محاكي على الكمبيوتر فاستخدم العلم: -e

```bash
ApkPatcher -i مسار_التطبيق.apk -e -c مسار_الشهادة.cert
```

وضع -i & -f / -p ➸ تجاوز حماية SSL لـ Flutter و Pairip

```bash
ApkPatcher -i مسار_التطبيق.apk -f
```

لـ Pairip

```bash
ApkPatcher -i مسار_التطبيق.apk -p
```

بشهادة خاصة ( أدخل مسار pem / crt / cert )

```bash
ApkPatcher -i مسار_التطبيق.apk -f -p -c مسار_الشهادة.cert
```

وضع -i & -D ➸ معرف Android وتعديل Smali

بمعرف Android مخصص ( أدخل معرف Android مكون من 16 رقم )

```bash
ApkPatcher -i مسار_التطبيق.apk -D 7e9f51f096bd5c83
```

وضع -i & -pkg ➸ تزوير كشف الحزمة (Dex/Manifest/Res)

```bash
ApkPatcher -i مسار_التطبيق.apk -pkg
```

وضع -i & -P ➸ الشراء/المدفوع/السعر

```bash
ApkPatcher -i مسار_التطبيق.apk -P
```

وضع -i & --rmads / rmsc / -rmu ➸ تجاوز الإعلانات وتقييد لقطة الشاشة / USB

إزالة الإعلانات: -rmads

```bash
ApkPatcher -i مسار_التطبيق.apk -rmads
```

تجاوز تقييد لقطة الشاشة: -rmsc

```bash
ApkPatcher -i مسار_التطبيق.apk -rmsc
```

تجاوز صلاحية تصحيح USB: -rmu

```bash
ApkPatcher -i مسار_التطبيق.apk -rmu
```

وضع -i & -skip ➸ تخطي التعديل (مثل: getAcceptedIssuers)

```bash
ApkPatcher -i مسار_التطبيق.apk -skip getAcceptedIssuers
```

وضع -i & -A ➸ حقن سجلات AES

حقن سجلات AES MT

```bash
ApkPatcher -i مسار_التطبيق.apk -A
```

هل تريد ملف Dex منفصل لـ AES.smali

```bash
ApkPatcher -i مسار_التطبيق.apk -A -s
```

وضع -i & -r ➸ معلومات جهاز عشوائية/مزيفة

معلومات جهاز عشوائية/مزيفة

```bash
ApkPatcher -i مسار_التطبيق.apk -r
```

بمعرف Android مخصص ( أدخل معرف Android مكون من 16 رقم )

```bash
ApkPatcher -i مسار_التطبيق.apk -r -D 7e9f51f096bd5c83
```

وضع -m ➸ دمج APK فقط

```bash
ApkPatcher -m مسار_التطبيق.apk
```

وضع -C ➸ الاعتمادات والتعليمات

```bash
ApkPatcher -C
```

وضع -h ➸ المساعدة

```bash
ApkPatcher -h
```

وضع -O ➸ أعلام التعديل الإضافية

```bash
ApkPatcher -O
```

ملاحظة

---

🇾🇪 مرحباً بكم من TechnoYemen

https://img.shields.io/badge/TELEGRAM-CHANNEL-red?style=for-the-badge&logo=telegram
</a><p>
https://img.shields.io/badge/TELEGRAM-OWNER-red?style=for-the-badge&logo=telegram

</p>

**2nd. Method**

    pkg install python git && pip install git+https://github.com/TechnoIndian/ApkPatcher.git


Uninstall ApkPatcher
-----

    pip uninstall ApkPatcher


Usage
-----

**ApkPatcher**

**Mode -i ➸ Smali Patcher (Input Your Apk Path)**

    ApkPatcher -i YourApkPath.apk
    
`With Your Certificate ( Input Your pem/ crt / cert Path )`

    ApkPatcher -i YourApkPath.apk -c YourCertificatePath.cert

`Multiple Certificate`

    ApkPatcher -i YourApkPath.apk -c /sdcard/HttpCanary/certs/HttpCanary.pem /sdcard/Download/Reqable/reqable-ca.crt /sdcard/Download/ProxyPinCA.crt

`If using emulator on PC then use Flag: -e`

    ApkPatcher -i YourApkPath.apk -e -c YourCertificatePath.cert

**Mode -i & -f / -p ➸ Flutter & Pairip SSL Bypass**

    ApkPatcher -i YourApkPath.apk -f

`For Pairip`

    ApkPatcher -i YourApkPath.apk -p

`With Your Certificate ( Input Your pem / crt / cert Path )`

    ApkPatcher -i YourApkPath.apk -f -p -c YourCertificatePath.cert

**Mode -i & -D ➸ Android ID & Smali Patcher**

`With Your Android ID ( Input Your Custom 16 Digit Android ID )`

    ApkPatcher -i YourApkPath.apk -D 7e9f51f096bd5c83

**Mode -i & -pkg Spoof Package Detection (Dex/Manifest/Res)**

    ApkPatcher -i YourApkPath.apk -pkg

**Mode -i & -P ➸ Purchase/Paid/Price**

    ApkPatcher -i YourApkPath.apk -P

**Mode -i & --rmads / rmsc / -rmu ➸ Bypass Ads & Screenshot / USB Restriction**

`Remove Ads Flag: -rmads`

    ApkPatcher -i YourApkPath.apk -rmads

`Bypass Screenshot Restriction Flag: -rmsc`

    ApkPatcher -i YourApkPath.apk -rmsc

`Bypass USB Debugging Permission Flag: -rmu`

    ApkPatcher -i YourApkPath.apk -rmu

**Mode -i & -skip ➸ Skip Patch (e.g., getAcceptedIssuers)**

    ApkPatcher -i YourApkPath.apk -skip getAcceptedIssuers

**Mode -i & -A ➸ AES Logs Inject**

`AES MT Logs Inject`

    ApkPatcher -i YourApkPath.apk -A

`Do U Want Separate AES.smali Dex`

    ApkPatcher -i YourApkPath.apk -A -s

**Mode i & -r ➸ Random/Fake Device Info**

`Random/Fake Device Info`

    ApkPatcher -i YourApkPath.apk -r

`With Your Android ID ( Input Your Custom 16 Digit Android ID )`

    ApkPatcher -i YourApkPath.apk -r -D 7e9f51f096bd5c83

**Mode -m ➸ Only Merge Apk**

    ApkPatcher -m YourApkPath.apk

**Mode -C ➸ Credits & Instruction**

    ApkPatcher -C
    
**Mode -h ➸ Help**

    ApkPatcher -h

**Mode -O ➸ Other Patch Flags**

    ApkPatcher -O

Note
----

## 🇾🇪 Welcome By TechnoYemenn

[![Telegram](https://img.shields.io/badge/TELEGRAM-CHANNEL-red?style=for-the-badge&logo=telegram)](https://t.me/TechnoYemenn)
  </a><p>
[![Telegram](https://img.shields.io/badge/TELEGRAM-OWNER-red?style=for-the-badge&logo=telegram)](https://t.me/rktechnoindianshnoindians)
</p>
