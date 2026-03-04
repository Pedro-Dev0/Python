# escrever um arquivo
file = open('C:\\Users\\suporte\\Documents\\GitHub\\Python\\python\\Primeiro Modulo\\16 - arquivos\\texto.txt', 'w')
file.write(f'BERSERK é um anime e manga feito por Kentaro Miura e Tetsuya Saito e fala sobre a luta pela sobrevivência em um mundo pós-apocalíptico, tudo isso interpretado por seu protagonista o Guts que se depara com inúmeras adversidades e desafios juntamente com a marca da maldição.\n')             
file.writelines(['\n', 'O anime é conhecido por sua história sombria, personagens complexos e cenas de ação intensas, e é considerado um dos melhores animes de todos os tempos.'])           
file.writelines('\n')
file.writelines(['\n', 'O manga é publicado desde 1989 e ainda está em andamento, e é considerado um dos mangas mais influentes e aclamados da história.'])                   
file.close()

