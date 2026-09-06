from pathlib import Path
from collections import Counter
import subprocess,re,json,sys
sys.stdout.reconfigure(encoding='utf-8')
R=Path.cwd();mapping=json.loads((R/'.refactor_moves.json').read_text(encoding='utf-8'))
tracked=subprocess.check_output(['git','ls-files','-z']).decode('utf-8').split('\0')
pattern=re.compile(r'\[(?:id|\w+_id|mob|boss|item|weapon|artifact|module|headwear|consumable|blueprint|biome)::\s*([a-z][a-z0-9_\.]+)\s*\]')
before=set();count=0
for path in tracked:
 if not path.endswith('.md') or not re.match(r'0[1-8]_',path):continue
 if '/_Registries/' not in path and not any(f'/{x}/' in path for x in ['Races','Specs','Weapons','Lore']):continue
 old=subprocess.check_output(['git','show','HEAD:'+path]).decode('utf-8-sig');before.update(pattern.findall(old));count+=1
after='\n'.join(p.read_text(encoding='utf-8-sig') for p in R.glob('[01][0-9]*/**/*.md'))
missing=sorted(before-set(pattern.findall(after)))
print('Source registry/entity/lore files:',count,'unique inline identifiers:',len(before),'missing:',missing)
failures=[]
for old,new in mapping.items():
 if (R/old).exists():failures.append('old path exists: '+old)
 if not (R/new).exists():failures.append('destination missing: '+new)
print('Native moves:',len(mapping),'path failures:',failures)
for key in ['faction_id','race_id','spec_id','frame_id']:
 old_values=[];new_values=[]
 for path in tracked:
  if not path.endswith('.md') or not re.match(r'0[1-8]_',path):continue
  if not any(f'/{x}/' in path for x in ['Races','Specs','Weapons','Lore']):continue
  old=subprocess.check_output(['git','show','HEAD:'+path]).decode('utf-8-sig');old_values+=re.findall(r'^'+key+r': (.+)$',old,re.M)
 new_values=re.findall(r'^'+key+r': (.+)$',after,re.M)
 delta=Counter(old_values)-Counter(new_values)
 print(key,'source entries:',len(old_values),'missing:',dict(delta))
 assert not delta
assert not missing and not failures
