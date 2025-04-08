def main():
    country=input("Inserire nome paese: ")
    article=name(country)
    country=article+country
    print(country)
    return

def name(country):
    if (country[0]=='A' or country[0]=='E' or country[0]=='I' or country[0]=='O' or country[0]=='U'):
        article="l'"
    elif country[len(country)-1]=='e':
        if (country=="Belize" or country=="Cambodge" or country=="Mexique" or country=="Mozambique" or country=="Zaire" or country=="Zimbawe"):
            article="le "
        else:
            article="la "
    elif country=="Etats-Units" or country=="Pays-Bas":
        article="les "
    else:
        article="le "
    return article

main()
