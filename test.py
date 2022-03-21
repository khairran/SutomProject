def sutom():

    
    mot="poire"
    print("Entrez un mot")
    rep=input()
    s=0
    if(len(mot)!=len(rep)):
        print("Le mot saisi n'est pas de la bonne taille.")
        exit
    for i in range(0,len(mot)):
        if(rep[i]== mot[i]):
             i+1
        else:
            s+=1
    if(s!=0):
        print("Ce n'est pas le bon mot")
    else:
        print("Bravo, c'est le bon mot !!")
        exit
    
