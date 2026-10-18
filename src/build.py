from pathlib import Path
base=Path(__file__).resolve().parent
shell=(base/'shell.html').read_text()
js=(base/'game.js').read_text()
out=shell.replace('// __GAME_JS__', js)
Path(base.parent/'starweave.html').write_text(out)
print('built', len(out), 'bytes')
