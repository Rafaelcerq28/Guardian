#Metodos para tudo não virar uma favela
class Diversos:
    #Rever no futuro
    #Metodo para criar mascara do cnpj (pode ser substituido por js mas ainda não sei :/)
    def mask_cnpj(cnpj):
        try:
            if len(str(cnpj)) < 14 or len(str(cnpj)) > 14 or str(cnpj).isalpha() or str(cnpj).isalnum():
                return cnpj
            mask = ''
            cnt = 0
            for letra in cnpj:
                if cnt == 2 or cnt == 5:
                    mask += '.'
                    mask += letra
                elif cnt == 8:
                    mask += '/'
                    mask += letra
                elif cnt == 12:
                    mask += '-'
                    mask += letra
                else:
                    mask += letra
                cnt+=1
            return mask
        except TypeError:
            return cnpj