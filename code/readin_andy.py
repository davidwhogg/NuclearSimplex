# I have sent you my pickle file of the saved id's and labels the list of labels in the array is below. 
# the errors on each element are essentially the cross validation errors, given in the paper for each element 
# 
rcParams['figure.figsize'] = 14, 6
import matplotlib 
import pickle 
a = open('open_clusters4_tags_dr13_30eB_nofilt_5026_norm8.pickle', 'r' ) # can do with aspcap 
b = pickle.load(a)
a.close()
dataout = b[0]
dataout_labels = ["teff", "logg", "[Fe/H]", "C", "N", "O", "Na", "Mg", "Al", "Si", "S", "K", "Ca", "Ti", "V", "Mn", "Ni", "P", "Cr", "Co", "Cu", "Rb", "FWHM"]
2mass_ids = b[-1]

a = open('open_clusters_name4.txt', 'r')
al = a.readlines()
names = []
for each in al:
    names.append(each.strip()) 


