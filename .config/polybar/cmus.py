import os
import warnings

cmus = os.popen("cmus-remote --query").read()

isplaying = False

for line in cmus.splitlines():
  if "tag title " in line:
    title = line.replace("tag title ", "")
    isplaying = True
  if "tag artist " in line:
    artist = line.replace("tag artist ", "")
  if "tag tracknumber " in line:
    num = line.replace("tag tracknumber ", "")
  if "status stopped" in line:
    exit()

if isplaying == True:
  print(f'{num}. {title} - {artist}')
else:
  print("")



