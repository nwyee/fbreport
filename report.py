import http.cookiejar
import json
import threading
import time

import bs4
import mechanize

"""
@ https://github.com/nwyee/fbreport

Facebook Profile 
Tags: 
       - profile_impersonation, 
       - profile_fake_account, 
       - profile_fake_name, 
       - profile_posting_inappropriate_things, 
       - harassment_or_bullying, 
       - profile_lost_access_to_account, 
       - profile_help, profile_something_else


"""


class Report(threading.Thread):
    def __init__(self, email, pw, target, times):
        threading.Thread.__init__(self)
        self.email = email
        self.pw = pw
        self.tg = target
        self.times = times
        self.settings = json.dumps(
            {
                "fake": "profile_fake_account",
                "checked": "yes"
            }
        )

    def run(self):
        print(f'Start Logging In ...\n[-] Target is {self.tg} \n')
        """
        Log In
        """
        br = mechanize.Browser()
        url = "https://mbasic.facebook.com"
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.set_cookiejar(http.cookiejar.LWPCookieJar())
        br.addheaders = [
            (
                "User-Agent", "Mozilla/5.0 (Linux; U; Android 5.1)"
            )
        ]
        br.open("https://mbasic.facebook.com")
        br.select_form(nr=0)
        br.form["email"] = "{}".format(
            self.email
        )
        br.form["pass"] = "{}".format(
            self.pw
        )
        br.submit()
        """
        Report Process
        """
        for i in range(self.times):
            print("report : ", i + 1, " \n")
            br.open(
                "https://www.facebook.com/{}".format(
                    self.tg
                )
            )
            bb = bs4.BeautifulSoup(
                br.response().read(),
                features="html.parser"
            )
            kntl = ''
            for x in bb.find_all("a", href=True):
                if "rapid_report" in x["href"]:
                    kntl = x["href"]
            br.open(kntl)
            br._factory.is_html = True
            js = json.loads(self.settings)
            br.select_form(nr=0)
            br.form["tag"] = [js["fake"]]
            br.submit()
            br._factory.is_html = True
            try:
                br.select_form(nr=0)
                for control in br.form.controls:
                    if control.type == 'checkbox':
                        br.form["checked"] = [js["checked"]]

                br.submit()
                res = br.response().read()
                if b"You have submitted a report" in res:
                    print("[*] Reported.")
                else:
                    print("[-] Unreported.")
            except Exception as e:
                print("Error : \n", e)
                print("\r[-] Already Reports.")

            print("Please wait, I need to sleep 5 sec ... \n")
            time.sleep(5)

        """
        Log Out
        """
        print("[-] I am logging out")
        br.open("https://www.facebook.com/logout")

