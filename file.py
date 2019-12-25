import os
from files.server_setup import adapt

main_dir = os.environ.get('HOME')
os.chdir(main_dir)

watch_for = [
  'extras',
  'Eject_Script',
  'MiesPlatform',
  'replace_shell',
  '_Tool-Console_',
  'NewJson'
]

append_found = []

for i in range(len(os.listdir())):
  if os.listdir()[i] in watch_for:
    append_found.append(os.listdir()[i])

print('Found {} of {} files'.format(str(len(append_found)),str(len(watch_for))))

adapt = adapt()
adapt.gather_found_files(files=append_found)

"this is needed to startup the client side of AlmightyOS, or the operator that makes the application possible"
def Client():pass
