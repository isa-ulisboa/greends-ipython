import csv
f = open("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv", "r")
lst = f.readlines()[1:]
f1=csv.DictReader(lst)
f.close()


