from Config.Util import *
from Config.Config import *
try:
    import webbrowser
except Exception as e:
    ErrorModule(e)

def display_menu():
    w = color.WHITE
    r = color.BLUE
    y = color.YELLOW

    Slow(f"""
            {w}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            {w}┃                                          {r}Dark Web{w}                                         ┃
            {w}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
            {w}┃{y}1. Search Engines{w}                                                                          ┃
            {w}┃{y}2. Bitcoin Anonymity{w}                                                                       ┃
            {w}┃{y}3. Stresser / Ddos{w}                                                                         ┃
            {w}┃{y}4. Market{w}                                                                                  ┃
            {w}┃{y}5. Database{w}                                                                                ┃
            {w}┃{y}6. Email{w}                                                                                   ┃
            {w}┃{y}7. Hosting{w}                                                                                 ┃
            {w}┃{y}8. Social{w}                                                                                  ┃
            {w}┃{y}9. Images{w}                                                                                  ┃
            {w}┃{y}0. Quitter{w}                                                                                 ┃
            {w}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """)

def display_links(category):
    w = color.WHITE
    r = color.BLUE

    if category == 1:
        Slow(f"""
            {w}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            {w}┃{r}Search Engine:{w}                                                                             ┃
            {w}┃[{r}Torch{w}]        : {r}http://xmh57jrzrnw6insl.onion/{w}                                            ┃
            {w}┃[{r}visiTOR{w}]      : {r}http://visitorfi5kl7q7i.onion/{w}                                            ┃
            {w}┃[{r}searx{w}]        : {r}http://5plvrsgydwy2sgce.onion/{w}                                            ┃
            {w}┃[{r}Not Evil{w}]     : {r}http://hss3uro2hsxfogfq.onion/{w}                                            ┃
            {w}┃[{r}Danex{w}]        : {r}http://danexio627wiswvlpt6ejyhpxl5gla5nt2tgvgm2apj2ofrgm44vbeyd.onion/{w}    ┃
            {w}┃[{r}Sentor{w}]       : {r}http://e27slbec2ykiyo26gfuovaehuzsydffbit5nlxid53kigw3pvz6uosqd.onion/{w}    ┃
            {w}┃[{r}Candle{w}]       : {r}http://gjobqjj7wyczbqie.onion/{w}                                            ┃
            {w}┃[{r}Ahmia.fi{w}]     : {r}http://msydqstlz2kzerdg.onion/{w}                                            ┃
            {w}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
    elif category == 2:
        Slow(f"""
            {w}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            {w}┃{r}Bitcoin Anonymity:{w}                                                                         ┃
            {w}┃[{r}WeBuyBitcoins{w}]: {r}http://jzn5w5pac26sqef4.onion/{w}                                            ┃
            {w}┃[{r}Dark Mixer{w}]   : {r}http://y22arit74fqnnc2pbieq3wqqvkfub6gnlegx3cl6thclos4f7ya7rvad.onion/{w}    ┃
            {w}┃[{r}Mixabit{w}]      : {r}http://hqfld5smkr4b4xrjcco7zotvoqhuuoehjdvoin755iytmpk4sm7cbwad.onion/{w}    ┃
            {w}┃[{r}EasyCoin{w}]     : {r}http://easycoinsayj7p5l.onion/{w}                                            ┃
            {w}┃[{r}Onionwallet{w}]  : {r}http://ow24et3tetp6tvmk.onion{w}                                             ┃
            {w}┃[{r}VirginBitcoin{w}]: {r}http://ovai7wvp4yj6jl3wbzihypbq657vpape7lggrlah4pl34utwjrpetwid.onion/{w}    ┃
            {w}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
    elif category == 3:
        Slow(f"""
            {w}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            {w}┃{r}Stresser / Ddos:{w}                                                                           ┃
            {w}┃[{r}Stresser{w}]     : {r}http://ecwvi3cd6h27r2kjx6ur6gdi4udrh66omvqeawp3dzqrtfwo432s7myd.onion/{w}    ┃
            {w}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
    elif category == 4:
        Slow(f"""
            {w}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            {w}┃{r}Market:{w}                                                                                    ┃
            {w}┃[{r}Kamagra{w}]      : {r}http://k4btcoezc5tlxyaf.onion/{w}                                            ┃
            {w}┃[{r}Brainmagic{w}]   : {r}http://ll6lardicrvrljvq.onion/{w}                                            ┃
            {w}┃[{r}NLGrowers{w}]    : {r}http://25ffhnaechrbzwf3.onion/{w}                                            ┃
            {w}┃[{r}CannabisUK{w}]   : {r}http://fzqnrlcvhkgbdwx5.onion/{w}                                            ┃
            {w}┃[{r}BitPharma{w}]    : {r}http://s5q54hfww56ov2xc.onion/{w}                                            ┃
            {w}┃[{r}Smokeable{w}]    : {r}http://smoker32pk4qt3mx.onion/{w}                                            ┃
            {w}┃[{r}EUCanna{w}]      : {r}http://rso4hutlefirefqp.onion/{w}                                            ┃
            {w}┃[{r}Deep Market{w}]  : {r}http://deepmar4ai3iff7akeuos3u3727lvuutm4l5takh3dmo3pziznl5ywqd.onion/{w}    ┃
            {w}┃[{r}DrChronic{w}]    : {r}http://iwggpyxn6qv3b2twpwtyhi2sfvgnby2albbcotcysd5f7obrlwbdbkyd.onion/{w}    ┃
            {w}┃[{r}TomAndJerry{w}]  : {r}http://rfyb5tlhiqtiavwhikdlvb3fumxgqwtg2naanxtiqibidqlox5vispqd.onion/{w}    ┃
            {w}┃[{r}420prime{w}]     : {r}http://ajlu6mrc7lwulwakojrgvvtarotvkvxqosb4psxljgobjhureve4kdqd.onion/{w}    ┃
            {w}┃[{r}Can*abisUK{w}]   : {r}http://7mejofwihleuugda5kfnr7tupvfbaqntjqnfxc4hwmozlcmj2cey3hqd.onion/{w}    ┃
            {w}┃[{r}DeDope{w}]       : {r}http://sga5n7zx6qjty7uwvkxpwstyoh73shst6mx3okouv53uks7ks47msayd.onion/{w}    ┃
            {w}┃[{r}AccMarket{w}]    : {r}http://55niksbd22qqaedkw36qw4cpofmbxdtbwonxam7ov2ga62zqbhgty3yd.onion/{w}    ┃
            {w}┃[{r}Cardshop{w}]     : {r}http://s57divisqlcjtsyutxjz2ww77vlbwpxgodtijcsrgsuts4js5hnxkhqd.onion/{w}    ┃
            {w}┃[{r}Darkmining{w}]   : {r}http://jbtb75gqlr57qurikzy2bxxjftzkmanynesmoxbzzcp7qf5t46u7ekqd.onion/{w}    ┃
            {w}┃[{r}MobileStore{w}]  : {r}http://rxmyl3izgquew65nicavsk6loyyblztng6puq42firpvbe32sefvnbad.onion/{w}    ┃
            {w}┃[{r}EuroGuns{w}]     : {r}http://t43fsf65omvf7grt46wlt2eo5jbj3hafyvbdb7jtr2biyre5v24pebad.onion/{w}    ┃
            {w}┃[{r}UKpassports{w}]  : {r}http://3bp7szl6ehbrnitmbyxzvcm3ieu7ba2kys64oecf4g2b65mcgbafzgqd.onion/{w}    ┃
            {w}┃[{r}ccPal{w}]        : {r}http://xykxv6fmblogxgmzjm5wt6akdhm4wewiarjzcngev4tupgjlyugmc7qd.onion/{w}    ┃
            {w}┃[{r}Webuybitcoins{w}]: {r}http://wk3mtlvp2ej64nuytqm3mjrm6gpulix623abum6ewp64444oreysz7qd.onion/{w}    ┃
            {w}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
    elif category == 5:
        Slow(f"""
            {w}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            {w}┃{r}DataBase:{w}                                                                                  ┃
            {w}┃[{r}Database{w}]     : {r}http://breachdbsztfykg2fdaq2gnqnxfsbj5d35byz3yzj73hazydk4vq72qd.onion/{w}    ┃
            {w}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
    elif category == 6:
        Slow(f"""
            {w}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            {w}┃{r}Email:{w}                                                                                     ┃
            {w}┃[{r}BitMessage{w}]   : {r}http://bitmailendavkbec.onion/{w}                                            ┃
            {w}┃[{r}Mailpile{w}]     : {r}http://clgs64523yi2bkhz.onion/{w}                                            ┃
            {w}┃[{r}Protonmail{w}]   : {r}http://protonirockerxow.onion/{w}                                            ┃
            {w}┃[{r}secMail.pro{w}]  : {r}http://secmailw453j7piv.onion/{w}                                            ┃
            {w}┃[{r}Tor Box{w}]      : {r}http://torbox3uiot6wchz.onion/{w}                                            ┃
            {w}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
    elif category == 7:
        Slow(f"""
            {w}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            {w}┃{r}Hosting:{w}                                                                                   ┃
            {w}┃[{r}Web Hosting{w}]  : {r}http://hosting6iar5zo7c.onion/{w}                                            ┃
            {w}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
    elif category == 8:
        Slow(f"""
            {w}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            {w}┃{r}Social:{w}                                                                                    ┃
            {w}┃[{r}Facebook{w}]     : {r}https://www.facebookcorewwwi.onion/{w}                                       ┃
            {w}┃[{r}Keybase{w}]      : {r}http://fncuwbiisyh6ak3i.onion/{w}                                            ┃
            {w}┃[{r}Stranger{w}]     : {r}http://tetatl6umgbmtv27.onion/{w}                                            ┃
            {w}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
    elif category == 9:
        Slow(f"""
            {w}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            {w}┃{r}Images:{w}                                                                                    ┃
            {w}┃[{r}Matrix Image{w}] : {r}http://matrixtxri745dfw.onion/{w}                                            ┃
            {w}┃[{r}NNTPChan imageboard{w}]: {r}http://oniichanylo2tsi4.onion/{w}                                      ┃
            {w}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
    else:
        Slow(f"\n{ERROR} {w}{primary}Option non valide.{w}")

def main():
    Title("Dark Web Links")
    while True:
        try:
            display_menu()
            choice = input(f"{INPUT} Choose a category -> ")
            
            if choice.isdigit():
                choice = int(choice)
                if choice == 0:
                    Slow(f"{color.WHITE}Quitting...{color.RESET}")
                    break
                elif 1 <= choice <= 9:
                    display_links(choice)
                else:
                    Slow(f"\n{ERROR} {primary}Option non valide.\n")
            else:
                Slow(f"\n{ERROR} {primary}Please enter a valid number.\n")

            Continue()
            Reset()
        except Exception as e:
            Error(e)

if __name__ == "__main__":
    main()