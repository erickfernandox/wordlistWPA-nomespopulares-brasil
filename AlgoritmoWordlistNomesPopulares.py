Nomes=['souza','silva','sousa','borges','maria','lucas','enzo','cristo','moreira','moura','senha','leila','afonso','ferreira','xavier','marco','jesuscristo',
'lima','pereira','costa','rodrigues','alves','carvalho','ribeiro','araujo','almeida','lemos','alan','allan',
'maysa','maira','joao','jose','pedro','luana','diego','renata','camila','natalia','edson','agnlado','vander','antonia','leite',
'ryan','felipe','adrina','adriano','alessandro','alex','aline','amanda','ana','andre','angela','arthur','artur',
'barbara','bete','beto','hugo','bruno','carlos','carol','dani','daniel','valentina','duda','nina','duda','filipe',
'flavio','gabi','gui','gustavo','hana','helen','hotel','iago','yasmin','igor','iris','israel','ivo','nati','jack',
'jair','jean','jeova','jessica','jess','jesus','jonas','joyce','julia','juliana','julio','junior','kamila','karla',
'carla','kely','kelly','katia','kleber','laila','lais','larissa','taisa','leo','leandro','leonardo','leticia'
'ligia','lorena','luiz','luis','familia','manoel','marcelo','marcio','marcos','marilia','marina','mateus','matheus',
'mayara','maykon','mayra','mica','micaeli','milena','moises','murilo','natanael','neto','olavo','oliveira','emily',
'pablo','pamela','patricia','paula','paulo','pedro','carlos','casa','cesar','chico','daniel','danilo','david',
'dayse','douglas','dudu','edna','elizete','elisete','enio','erica','erika','erick','eric','fabi','mary','rafa','acesso',
'rafael','rafaela','raquel','rayane','ricardo','rodrigo','rogerio','rosa','rosi','sabrina','samira','samuel',
'saulo','sara','silvio','suelen','talita','talles','tayna','thayna','theo','tiago','tony','valmir','valeria',
'vinicius','vitor','vivian','wagner','weber','wesley','wilian','tritan','monica','wilson','eduardo','sophia',
'laura','isabela','manuela','gabriel','helena','heitor','giovanna','eduarda','beatriz','nicolas','clara',
'lorenzo','guilherme','heloisa','lara','livia','henrique','isadora','sarah','analuiza','nicole','gabriela',
'pietro','isabelly','benjamin','melissa','isaac','cecilia','esther','joaquim','lucca','emanuelly',
'caio','caua','rebeca','bryan','vitoria','miguel','isis','vicente','lavinia','francisco',
'antonio','bianca','benicio','fernanda','catarina','alicia','thiago','alice','thomas','emanuel','enrico','aguinaldo']

arq = open('nomespopularesTudo5.txt','w')

for Nome in Nomes:
    
    Tamanho = len(Nome)
    
    #Nome acima de 6 caracteres

    if(Tamanho >= 7):
        for i in range(0,10,1):
            arq.writelines(Nome+str(i)+"\n")
            Nome2 = Nome[0].upper()+Nome[1::]
            arq.writelines(Nome2+str(i)+"\n")
            arq.writelines(str(i)+Nome+"\n")
    
    if(Tamanho >= 6):
        for i in range(0,10,1):
            for j in range(0,10,1):
                arq.writelines(Nome+str(i)+str(j)+"\n")
                Nome2 = Nome[0].upper()+Nome[1::]
                arq.writelines(Nome2+str(i)+str(j)+"\n")
                arq.writelines(str(i)+str(j)+Nome+"\n")

    if(Tamanho >= 5):
    #Nome acima de 5 caracteres
        for i in range(0,10,1):
            for j in range(0,10,1):
                for k in range(0,10,1):
                    arq.writelines(Nome+str(i)+str(j)+str(k)+"\n")
                    Nome2 = Nome[0].upper()+Nome[1::]
                    arq.writelines(Nome2+str(i)+str(j)+str(k)+"\n")

    if(Tamanho >= 4):
    #Nome acima de 4 caracteres
        for i in range(0,10,1):
            for j in range(0,10,1):
                for k in range(0,10,1):
                    for m in range(0,10,1):
                        arq.writelines(Nome+str(i)+str(j)+str(k)+str(m)+"\n")
                        Nome2 = Nome[0].upper()+Nome[1::]
                        arq.writelines(Nome2+str(i)+str(j)+str(k)+str(m)+"\n")

    if(Tamanho >= 3):
        for i in range(0,10,1):
            for j in range(0,10,1):
                for k in range(0,10,1):
                    for m in range(0,10,1):
                        for n in range(0,10,1):
                            arq.writelines(Nome+str(i)+str(j)+str(k)+str(m)+str(n)+"\n")
                            Nome2 = Nome[0].upper()+Nome[1::]
                            arq.writelines(Nome2+str(i)+str(j)+str(k)+str(m)+str(n)+"\n")


arq.close()

