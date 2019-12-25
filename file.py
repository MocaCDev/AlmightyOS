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

adapt = adapt()
adapt.gather_found_files(files=append_found)
