import os, json

class adapt:

  def gather_found_files(self,**found_files):

    "this will setup paths to found directories"
    self.found_files = found_files['files']

    "we want to replace / with ."
    for i in range(len(self.found_files)):
      self.found_files[i] = os.path.abspath(self.found_files[i]).replace('/','.')
    
    os.chdir(os.getcwd())
    with open('changed_paths.json','w') as file:
      file.write(json.dumps(self.found_files,indent=2,sort_keys=False))
      file.close()
