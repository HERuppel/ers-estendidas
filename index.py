import re

def exec(file_name):
  regexDecimal = re.compile('\d+(?:\.\d+)')
  regexIP = re.compile('[0-9]+[.][0-9]+[.][0-9]+[.][0-9]')
  regexUrl = re.compile('(http://|https://)?(www.)?([a-zA-Z])+.(com|net|com.br)$')

  with open (file_name, "r", encoding="utf-8") as file:
    lines = file.readlines()

    print(f'\nINICIANDO PROCURA NO ARQUIVO {file_name}')

    for line in lines:
      matchIP = regexIP.findall(line.strip())
      matchDecimal = regexDecimal.findall(line.strip())
      matchUrl = re.search(regexUrl, line.strip())
      
      if len(matchDecimal) != 0:
        print(f"Encontrou número decimal na linha: {lines.index(line) + 1} -> {matchDecimal}")

      if len(matchIP) != 0:
        print(f"Encontrou IP na linha: {lines.index(line) + 1} -> {matchIP}")

      if matchUrl != None:
        print(f"Encontrou URL na linha: {lines.index(line) + 1} -> {matchUrl.group(0)}")

if __name__ == '__main__':
  exec('./var/1')
  for i in range(1,8):
    exec(f'./sent_items/{i}')
  for i in range(1,54):
    exec(f'./_sent_mail/{i}')