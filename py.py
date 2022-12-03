# f had tmrin tlbo mna n3tew les noms w les valeurs diyal kola 
#tlmid w ghadi nhktaro tani assghar valeurs ila l9ina bli kaynin 
#2 b7al b7al kan7to ssmiyathom b trtib alphobetic
score_lst = []
marksheet = []

for _ in range(int(input("number of students : "))):
    name = input(" name : ")
    score = float(input(" score : "))
    score_lst.append(score)
    marksheet.append([name,score])#stock the name and score in list
second_low = sorted(list(set(score_lst)))[1]#select the seconde lower scrore
names = [ name for name,scores in sorted(marksheet) if scores == second_low] 
# if we have 2 scores with the same values we will show them by aphabitic order
print('\n'.join(names))