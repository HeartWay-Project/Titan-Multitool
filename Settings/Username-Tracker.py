from Config.Util import *
from Config.Config import *
try:
    import requests
    from bs4 import BeautifulSoup
except Exception as e:
   ErrorModule(e)

Title("Username Tracker (Osint)")

try:
    sites = {
        "Twitter": "https://twitter.com/{}",
        "Instagram": "https://www.instagram.com/{}",
        "Facebook": "https://www.facebook.com/{}",
        "Pinterest": "https://www.pinterest.com/{}",
        "Tumblr": "https://{}.tumblr.com",
        "YouTube": "https://www.youtube.com/{}",
        "Vimeo": "https://vimeo.com/{}",
        "SoundCloud": "https://soundcloud.com/{}",
        "DeviantArt": "https://www.deviantart.com/{}",
        "About.me": "https://about.me/{}",
        "Flickr": "https://www.flickr.com/people/{}",
        "Twitch": "https://www.twitch.tv/{}",
        "Steam": "https://steamcommunity.com/id/{}",
        "Medium": "https://medium.com/@{}",
        "Blogger": "https://{}.blogspot.com",
        "Goodreads": "https://www.goodreads.com/{}",
        "Keybase": "https://keybase.io/{}",
        "VK": "https://vk.com/{}",
        "Spotify": "https://open.spotify.com/user/{}",
        "TripAdvisor": "https://www.tripadvisor.com/members/{}",
        "Last.fm": "https://www.last.fm/user/{}",
        "Slideshare": "https://www.slideshare.net/{}",
        "Dribbble": "https://dribbble.com/{}",
        "Behance": "https://www.behance.net/{}",
        "AngelList": "https://angel.co/{}",
        "ProductHunt": "https://www.producthunt.com/@{}",
        "500px": "https://500px.com/{}",
        "LinkedIn": "https://www.linkedin.com/in/{}",
        "Snapchat": "https://www.snapchat.com/add/{}",
        "WhatsApp": "https://wa.me/{}",
        "Discord": "https://discord.com/users/{}",
        "Telegram": "https://t.me/{}",
        "Quora": "https://www.quora.com/profile/{}",
        "TikTok": "https://www.tiktok.com/@{}",
        "Patreon": "https://www.patreon.com/{}",
        "Weibo": "https://weibo.com/{}",
        "OKCupid": "https://www.okcupid.com/profile/{}",
        "Meetup": "https://www.meetup.com/members/{}",
        "Myspace": "https://myspace.com/{}",
        "Kaggle": "https://www.kaggle.com/{}",
        "CodePen": "https://codepen.io/{}",
        "StackOverflow": "https://stackoverflow.com/users/{}",
        "HackerRank": "https://www.hackerrank.com/{}",
        "Xing": "https://www.xing.com/profile/{}",
        "Deezer": "https://www.deezer.com/en/user/{}",
        "Mix": "https://mix.com/{}",
        "Snapfish": "https://www.snapfish.com/{}",
        "Periscope": "https://www.pscp.tv/{}",
        "Tidal": "https://tidal.com/{}",
        "Yelp": "https://www.yelp.com/user_details?userid={}",
        "Disqus": "https://disqus.com/by/{}",
        "Dailymotion": "https://www.dailymotion.com/{}",
        "Ravelry": "https://www.ravelry.com/people/{}",
        "ReverbNation": "https://www.reverbnation.com/{}",
        "Vine": "https://vine.co/u/{}",
        "Foursquare": "https://foursquare.com/user/{}",
        "Mastodon": "https://mastodon.social/@{}",
        "Ello": "https://ello.co/{}",
        "GitLab": "https://gitlab.com/{}",
        "Giphy": "https://giphy.com/{}",
        "Hootsuite": "https://hootsuite.com/{}",
        "LiveJournal": "https://{}.livejournal.com",
        "Linktree": "https://linktr.ee/{}",
        "Prezi": "https://prezi.com/{}",
        "Groupon": "https://www.groupon.com/profile/{}",
        "Liveleak": "https://www.liveleak.com/c/{}",
        "Joomla": "https://www.joomla.org/user/{}",
        "StackExchange": "https://stackexchange.com/users/{}",
        "Weebly": "https://{}.weebly.com",
        "CodeWars": "https://www.codewars.com/users/{}",
        "Taringa": "https://www.taringa.net/{}",
        "Gumroad": "https://gumroad.com/{}",
        "Shopify": "https://{}.myshopify.com",
        "8tracks": "https://8tracks.com/{}",
        "Couchsurfing": "https://www.couchsurfing.com/people/{}",
        "OpenSea": "https://opensea.io/{}",
        "Trello": "https://trello.com/{}",
        "Tinder": "https://www.tinder.com/@{}",
        "Strava": "https://www.strava.com/athletes/{}",
        "Fiverr": "https://www.fiverr.com/{}",
        "Coursera": "https://www.coursera.org/user/{}",
        "Badoo": "https://badoo.com/profile/{}",
        "Rumble": "https://rumble.com/user/{}",
        "Wix": "https://www.wix.com/website/{}",
        "GitHub": "https://github.com/{}",
        "ResearchGate": "https://www.researchgate.net/profile/{}",
        "Bandcamp": "https://bandcamp.com/{}",
        "GaiaOnline": "https://www.gaiaonline.com/profiles/{}",
        "Flipboard": "https://flipboard.com/@{}",
        "Plurk": "https://www.plurk.com/{}",
        "Houzz": "https://houzz.com/user/{}",
        "Audiomack": "https://audiomack.com/{}",
        "CashApp": "https://cash.app/${}",
        "Venmo": "https://venmo.com/{}",
        "Bitbucket": "https://bitbucket.org/{}",
        "BuyMeACoffee": "https://www.buymeacoffee.com/{}",
        "DevTo": "https://dev.to/{}",
        "Loom": "https://www.loom.com/{}",
        "Reddit": "https://www.reddit.com/user/{}",
        "Investopedia": "https://www.investopedia.com/contributors/{}",
        "Koo": "https://www.kooapp.com/profile/{}",
        "ResearchGate": "https://www.researchgate.net/profile/{}",
        "MyAnimeList": "https://myanimelist.net/profile/{}",
        "Gitee": "https://gitee.com/{}",
        "Gogs": "https://gogs.io/{}",
        "Pexels": "https://www.pexels.com/@{}",
        "RedBubble": "https://www.redbubble.com/people/{}",
        "Fotolog": "https://fotolog.com/{}",
        "Ello": "https://ello.co/{}",
        "Audiomack": "https://audiomack.com/{}",
        "Vero": "https://www.vero.co/{}",
        "BandLab": "https://www.bandlab.com/{}",
        "Threema": "https://threema.id/{}",
        "Wattpad": "https://www.wattpad.com/user/{}",
        "PicsArt": "https://picsart.com/{}",
        "HubPages": "https://hubpages.com/@{}",
        "Minds": "https://www.minds.com/{}",
        "CafeMom": "https://www.cafemom.com/profile/{}",
        "Newgrounds": "https://newgrounds.com/{}",
        "Crunchyroll": "https://www.crunchyroll.com/user/{}",
        "Photobucket": "https://photobucket.com/user/{}",
        "Behance": "https://www.behance.net/{}",
        "Zynga": "https://zynga.com/profile/{}",
        "DLive": "https://dlive.tv/{}",
        "Peertube": "https://peertube.social/accounts/{}",
        "Bitchute": "https://www.bitchute.com/channel/{}",
        "MeWe": "https://mewe.com/i/{}",
        "Uplive": "https://global.upliveapp.com/profile/{}",
        "BandLab": "https://www.bandlab.com/{}",
        "DLive": "https://dlive.tv/{}",
        "Uplive": "https://global.upliveapp.com/profile/{}",
        "Mixcloud": "https://www.mixcloud.com/{}",
        "Anchor": "https://anchor.fm/{}",
        "HackerOne": "https://hackerone.com/{}",
        "PeerList": "https://peerlist.io/{}",
        "HackerEarth": "https://www.hackerearth.com/@{}",
        "Devpost": "https://devpost.com/{}",
    }


    number_site = 0
    number_found = 0
    username = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Username -> {reset}")
    Censored(username)
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Account search..")
    username_lower = username.lower()
    for site, url_template in sites.items():
        url = url_template.format(username)
        try:
            response = requests.get(url, timeout=2)
            number_site += 1
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                page_text = soup.get_text().lower()
                if username_lower in page_text:
                    number_found += 1
                    print(f"{BEFORE + current_time_hour() + AFTER} {ADD} {site}: {secondary + url}")
        except: pass

    print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Total Website: {secondary}{number_site}{primary}, Found: {secondary}{number_found}{primary}")
    Continue()
    Reset()
except Exception as e:
    Error(e)