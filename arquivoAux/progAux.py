#-geração de predicados generalizados
def gerarPredicadosCadCursoHorarioUmCredito():
    cadCursoHorarioUmCredito = []
    info = open("predicadosCadCursoHorarioUmCredito", "w")
    for i in range(0, len(cadeiras)):
       for j in range(0, len(curso)):
           for n in range(0, len(diasUmCreditos)):
               for k in range(0, len(horariosAulas)):
                  cadCursoHorarioUmCredito +=[cadeiras[i]+"_"+curso[j]+"_"+diasUmCreditos[n]+"_"+horariosAulas[k]]
    cleanList(str(cadCursoHorarioUmCredito))
    info.write(cleanList(str(cadCursoHorarioUmCredito)))
    info.close()



#geração de predicados generalizados

def gerarPredicadosCadCursoHorarioDoisCreditos():
    cadCursoHorarioDoisCreditos = []
    info = open("predicadosCadCursoHorarioDoisCreditos", "w")
    for i in range(0, len(cadeiras)):
       for j in range(0, len(curso)):
           for n in range(0, len(diasDoisCreditos)):
               for k in range(0, len(horariosAulas)):
                  cadCursoHorarioDoisCreditos +=[cadeiras[i]+"_"+curso[j]+"_"+diasDoisCreditos[n]+"_"+horariosAulas[k]]
    cleanList(str(cadCursoHorarioDoisCreditos))
    info.write(cleanList(str(cadCursoHorarioDoisCreditos)))
    info.close()

    #gerar todas as possobilidades
    
def gerarTodasPossibilidades():
    info = open('todasPossibProf.txt', 'w')
    profCadCurso = []
    for i in range(0, len(nomeProfessores)):
       for j in range(0, len(cadeiras)):
           for n in range(0, len(curso)):
            profCadCurso+=[nomeProfessores[i]+"_"+cadeiras[j]+"_"+curso[n]]
    cleanList(str(profCadCurso))
    info.write(cleanList(str(profCadCurso)))
    info.close()
def listaProfessores(): #cria predicados no modelo: professor_cadeira-curso e armazena no vetor profCAdCurso
    profCadCurso = []
    for i in range(0, len(nomeProfessores)):
       for j in range(0, len(cadeiras)):
           for n in range(0, len(curso)):
            profCadCurso+=[nomeProfessores[i]+"_"+cadeiras[j]+"_"+curso[n]]
    stringProfessores = str(profCadCurso)
    return stringProfessores #foi criado como uma funçaõ de retorno para caso seja necessário durante a exec.do programa
