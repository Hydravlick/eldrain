from importlib.machinery import SourceFileLoader
import json,re
w=SourceFileLoader('w','.refactor_work.py').load_module()
mapping=json.loads((w.ROOT/'.refactor_moves.json').read_text(encoding='utf-8'))
changed=[]
for p in w.ROOT.rglob('*'):
 if not p.is_file() or any(x in p.parts for x in ['.git','.obsidian','__pycache__']) or p.name.startswith('.refactor') or p.suffix not in ['.md','.py','.ps1','.json','.js','.base','.canvas','.yaml','.yml']:continue
 if p.name in ['00_Index.md','00_Routes.md']:continue
 s=p.read_text(encoding='utf-8-sig');n=s
 for old,new in mapping.items():
  n=n.replace(old,new).replace(old[:-3],new[:-3])
  oldstem=old.rsplit('/',1)[-1][:-3];newstem=new.rsplit('/',1)[-1][:-3]
  if oldstem!=newstem:n=re.sub(r'(?<![\w])'+re.escape(oldstem)+r'(?![\w])',lambda _:newstem,n)
 # Stable family queries no longer depend on physical storage.
 n=re.sub(r'^FROM "(?:04_Player_Entities/(?:Races|Specs)|05_Combat_Survival/Weapons|03_Factions_Societies/Lore)"\n(?=WHERE entity_kind)', '',n,flags=re.M)
 if n!=s:w.write(p,n);changed.append(p.relative_to(w.ROOT).as_posix())
print('Repaired literal consumers:',len(changed))
for x in changed:print(x)
