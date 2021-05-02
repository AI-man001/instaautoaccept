from colorama import Fore, init, Style


class Helpers:
  @staticmethod
  def title():
    return (f'''{Fore.LIGHTBLUE_EX}
 █████╗ ██╗   ██╗████████╗ ██████╗      █████╗  ██████╗ ██████╗███████╗██████╗ ████████╗ ██████╗ ██████╗ 
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗    ██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
███████║██║   ██║   ██║   ██║   ██║    ███████║██║     ██║     █████╗  ██████╔╝   ██║   ██║   ██║██████╔╝
██╔══██║██║   ██║   ██║   ██║   ██║    ██╔══██║██║     ██║     ██╔══╝  ██╔═══╝    ██║   ██║   ██║██╔══██╗
██║  ██║╚██████╔╝   ██║   ╚██████╔╝    ██║  ██║╚██████╗╚██████╗███████╗██║        ██║   ╚██████╔╝██║  ██║
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝╚══════╝╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═╝
{Style.RESET_ALL}
                                                                        by DIVINE ZVENYIKA                                                                                             
                                                                                                 ''')

  @staticmethod
  def temp_headers():
    return {
        "accept":
        "*/*",
        "accept-language":
        "en-US,en;q=0.9",
        "content-type":
        "application/x-www-form-urlencoded",
        "sec-fetch-dest":
        "empty",
        "sec-fetch-mode":
        "cors",
        "sec-fetch-site":
        "same-origin",
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    }

  @staticmethod
  def mainheaders():
    return {
        "accept":
        "*/*",
        "accept-language":
        "en-US,en;q=0.9",
        "content-type":
        "application/x-www-form-urlencoded",
        "sec-fetch-dest":
        "empty",
        "sec-fetch-mode":
        "cors",
        "sec-fetch-site":
        "same-origin",
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    }