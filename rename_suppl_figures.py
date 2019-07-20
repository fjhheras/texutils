import shutil
from pathlib import Path
from TexSoup import TexSoup

def fig_file(x): return x.includegraphics.args[1].contents[0]
def fig_label(x): return x.label.args[0].contents[0]
def is_supp(filepath): return 'SuppFig' in filepath
def new_filenames(index_file):
    i, filename = index_file
    return Path(filename), Path('S{}_fig.pdf'.format(i+1))

with open ("main.tex", "r") as myfile:
     data = myfile.readlines()
soup = TexSoup(data)

original_names = filter(is_supp, map(fig_file, soup.find_all('figure')))
original_and_new_names = map(new_filenames, enumerate(original_names))

#print(list(original_and_new_names))

for original, new in original_and_new_names:
    assert not new.exists()
    assert original.exists()
    copied_file = shutil.copy2(original, new)
    print(copied_file, " successfully created")

