from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='1oy6', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='1oy6', atom_files='1oy6.pdb')
aln.append(file='protein.ali', align_codes='protein')
aln.align2d()
aln.write(file='protein-1oy6.ali', alignment_format='PIR')
aln.write(file='protein-1oy6.pap', alignment_format='PAP')
