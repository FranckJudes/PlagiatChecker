
def Typefile(f):
    ref_file=f
    extension=ref_file.split('.')[-1]
    return extension


def EnregistrerPDF(f):
    with open('./media/pdf/'+f.name, 'wb+') as file:
        for chunk in f.chunks():
            file.write(chunk)


def Enregistrerautre(f):
    with open('./media/autre/'+f.name, 'wb+') as file:
        for chunk in f.chunks():
            file.write(chunk)
