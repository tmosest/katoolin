# TODO test this... I'm sure I broke some of them by messing up the ordering or something...

from cmd_utils import install_tool, run_cmd, run_eval
from menu import INVALID_COMMAD, OPTION_1

def is_integer(s):
    try:
        int(s)  # Attempt to convert the string to an integer
        return True
    except ValueError:
        return False  # If a ValueError occurs, it's not a valid integer string


class ToolData:
    def __init__(self, title, TOOLS_STR, EXCEPTIONS):
        self.title = title
        self.TOOLS_STR = TOOLS_STR
        self.TOOLS_ARR = TOOLS_STR.split(" ")
        self.EXCEPTIONS = EXCEPTIONS
        pass


    def TOOLS_MENU(self):
        result =  f'''
        \033[1;36m=+[ {self.title} tools\033[1;m\n\t\t'''
        for i in range(0, len(self.TOOLS_ARR), 2):
            result += f"\t{i + 1}) {self.TOOLS_ARR[i]}"
            if i + 1 < len(self.TOOLS_ARR):
                result += f"					{i + 2}) {self.TOOLS_ARR[i + 1]}\n"
            else:
                result += "\n"

        result += f'''
        0) Install all {self.title} tools
                    
        '''
        return result
    
    def install_tool_by_index(self, i):
        i = int(i) - 1
        if i in self.EXCEPTIONS:
            return run_cmd(self.EXCEPTIONS[i])
        
        install_tool(self.TOOLS_ARR[i])

    def install_all(self):
        for i in range(0, len(self.TOOLS_ARR)):
            self.install_tool_by_index(i + 1)
    
TOOL_PROMPT = "\033[1;32mInsert the number of the tool to install it .\n\033[1;m"

TOOLS_STR = "acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali"

TOOLS_DATA= ToolData("Information Gathering", TOOLS_STR, 
                     {4: "wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/"
                      , 35: 'echo ntop is unavailable'})

VUL_STR="bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia"

VUL_DATA = ToolData("Vulnerability Analysis", VUL_STR, {
    7: "apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install",
    8: "echo 'download page : http://www.cqure.net/wp/tools/database/dbpwaudit/'",
    12: "apt-get install git && git clone git://git.kali.org/packages/gsd.git",
    14: "Please download inguma from : http://inguma.sourceforge.net"
})

WIRELESS_ATTACKS_STR = "aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite"

WIRELESS_ATTACK_DATA = ToolData("Wireless Attacks", WIRELESS_ATTACKS_STR, {
    3: "apt-get install git && git clone git://git.kali.org/packages/bluemaho.git",
    4: "apt-get install git && git clone git://git.kali.org/packages/bluepot.git",
    15: "apt-get install git && git clone git://git.kali.org/packages/gr-scan.git"
})

WEB_ATTACKS_STR = "apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy"

WEB_ATTACKS_DATA = ToolData("Web Applications", WEB_ATTACKS_STR, {
    6: "apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install",
    34: "echo Webshag is unavailable",
    35: "apt-get install git && git clone git://git.kali.org/packages/webslayer.git"
})

SPOOFING_STR = "burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy"

SPOOFIND_DATA = ToolData("Sniffing & Spoofing", SPOOFING_STR, {8: "apt-get install git && git clone git://git.kali.org/packages/isr-evilgrade.git"})

ACCESS_STR = "cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely"

ACCESS_DATA = ToolData("Maintaining Access", ACCESS_STR, {})

REPORTING_STR = "casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal"

REPORTING_DATA = ToolData("Reporting Tools", REPORTING_STR, {})

EXPLOIT_STR = "armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss"

EXPLOIT_DATA = ToolData("Exploitation Tools", EXPLOIT_STR, {})

Forensics_STR = "binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico"

Forensics_DATA = ToolData("Forensics Data", Forensics_STR, {
    2: "apt-get install git && git clone git://git.kali.org/packages/capstone.git",
    8: "apt-get install git && git clone git://git.kali.org/packages/distorm3.git"})

STRESS_STR = "dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos"

STRESS_DATA = ToolData("Stress Testings", STRESS_STR, {3: "apt-get install git && git clone git://git.kali.org/packages/inundator.git"})

PASSWORD_STR = "acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy"

PASSWORD_DATA = ToolData("Password Attacks", PASSWORD_STR, {
    8: "apt-get install git && git clone git://git.kali.org/packages/dbpwaudit.git",
    13: "echo 'please visit : https://www.thc.org/thc-hydra/' ",
    24: "echo 'please visit : http://www.leidecker.info/projects/phrasendrescher/index.shtml' ",
    29: "echo Sqldict is unavailable"
    })

REVERSE_STR = "apktool dex2jar python-diStorm3 edb-debugger jad javasnoop JD OllyDbg smali Valgrind YARA"

REVERSE_DATA = ToolData("Reverse Engineering", REVERSE_STR, {})

HARDWARE_STR = "android-sdk apktool arduino dex2jar sakis3g smali"

HARDWARE_DATA = ToolData("Hardware Hacking", HARDWARE_STR, {})

MISC_STR = "wifresti squid3"

MISC_DATA = ToolData("Extra", MISC_STR, {0: "git clone https://github.com/LionSec/wifresti.git && cp wifresti/wifresti.py /usr/bin/wifresti && chmod +x /usr/bin/wifresti && wifresti"})

TOOL_CAT_MAP = {
    "1": TOOLS_DATA,
    "2": VUL_DATA,
    "3": WIRELESS_ATTACK_DATA,
    "4": WEB_ATTACKS_DATA,
    "5": SPOOFIND_DATA,
    "6": REPORTING_DATA,
    "7": ACCESS_DATA,
    "8": EXPLOIT_DATA,
    "9": Forensics_DATA,
    "10": STRESS_DATA,
    "11": PASSWORD_DATA, 
    "12": REVERSE_DATA,
    "13": HARDWARE_DATA,
    "14": MISC_DATA
}

def handle_options(opcion1):
    if opcion1 in TOOL_CAT_MAP:
        tool_data = TOOL_CAT_MAP[opcion1]
        print (tool_data.TOOLS_MENU())
        print (TOOL_PROMPT)
        opcion2 = run_eval(OPTION_1)

        if is_integer(opcion2) and 0 <  int(opcion2) and int(opcion2) <= len(tool_data.TOOLS_ARR):
            tool_data.install_tool_by_index(opcion2)
        elif opcion2 == "back":
            # Go back instead.
            return True
        elif opcion2 == "gohome":
            # Go Home instead.
            return None		
        elif opcion2 == "0":
            tool_data.install_all()
        else:
            print (INVALID_COMMAD)

    return False

def install_all():
    for key in TOOL_CAT_MAP:
        handle_options(key)