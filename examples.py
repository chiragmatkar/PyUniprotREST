from PyUniprotREST import PyUniprotREST

u = PyUniprotREST('proteins')
print u.getbyAccession('P9WI81')
print u.getbyAccessioninFASTA('P9WNK7')
