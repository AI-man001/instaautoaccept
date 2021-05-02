import os, time
from halo import Halo
from helpers.funcs import Helpers
from colorama import Fore, init, Style
from helpers.auth import USERNAME, PASSWORD
from helpers.instagram import InstagramAccept
init(convert=True)


def main():
  s = Style.RESET_ALL
  c = Fore.LIGHTBLUE_EX
  os.system('clear')
  print(Helpers.title())
  try:
    input_delay = int(input(f"[{c}x{s}] Check follow requests queue every (in seconds) [Optional] {c}>{s} "))
  except ValueError:
    input_delay = 9
  try:
    input_limit = int(
        input(f"[{c}x{s}] Limit number of accounts to accept in each iteration (int value) [Optional] {c}>{s} "))
  except ValueError:
    input_limit = 75
  post = {'username': USERNAME, 'enc_password': '#PWD_INSTAGRAM_BROWSER:0:0:' + PASSWORD}
  spinner = Halo(text='Loading', spinner='dots', color='blue')
  spinner.start()
  i = InstagramAccept(post)
  spinner.stop()
  os.system('clear')
  print(Helpers.title())

  spinner2 = Halo(text=f'Sleeping for {input_delay}s', spinner='dots', color='blue')
  if i.login() == True:
    while True:
      i.loop(input_limit)
      spinner2.start()
      time.sleep(input_delay)
      spinner2.stop()
  else:
    print('[!] User has failed to log in')
    input()
    main()


if __name__ == "__main__":
  main()
