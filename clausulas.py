# -- coding: utf-8 --
#passar a lista de professores que estao em um arquivo para uma lista
nomeProfessores = ['rafaelIvo','gastao','felipeMaciel','andersnoMagno','rosineide','gleison','alexandre', 'annaBeatriz', 'bonfim', 'danielMarcio', 'eurinardo', 'nauber', 'osvaldo', 'josimeire', 'marcioCosta', 'joaoVictor', 'pablo', 'tatiane', 'patricia', 'alexLima','andersonFeitoza', 'nilde']
cadeiras = ['gastao_matBasica_cc1','gleison_matBasica_es1','marcioCosta_fundProg_cc1','marcioCosta_fundProg_es1','josimeire_eticaProfissional_cc1','josimeire_eticaProfissional_es1','rafaelIvo_introComp_cc1','annaBeatriz_introEngSoft_es1','andersonFeitoza_matDiscreta_cc2','andersonFeitoza_matDiscreta_es2','alexLima_arquitComp_cc2','alexLima_arquitComp_es2','tatiane_estrutDados_cc2','tatiane_estrutDados_es2','eurinardo_labProg_cc2','eurinardo_labProg_es2','osvaldo_introProReqSoft_es2','gleison_calculo_cc2','pablo_algGrafos_cc3','pablo_algGrafos_es3','joaoVictor_progOrientObj_cc3','joaoVictor_progOrientObj_es3','rosineide_probEstatistica_cc3','nilde_probEstatistica_es3','rafaelIvo_lingProg_cc3','nauber_lingProg_es3','patricia_reqSoft_es3','gastao_algLinear_cc3','marcioCosta_projetoAnaliseAlgoritmos_cces','eurinardo_edAvanc_cc4','danielMarcio_fundBancDados_cc4','danielMarcio_fundBancDados_es4','alexandre_logicaComp_cc4','alexandre_logicaComp_es4','patricia_engSoft_cc4','nauber_procSoft_es4','osvaldo_analiseProjetoSistemas_cces','rafaelIvo_sistemaOperacional_cc5','alexLima_sistemaOperacional_es5','patricia_interHumanComp_cc5','patricia_interHumanComp_es5','felipeMaciel_redesComputadores_cces','danielMarcio_compGrafica_cc5','joaoVictor_projetoDetalhadoSoft_es5','osvaldo_gerencProjSoft_es5','alexLima_intelArtific_cc6','tatiane_matComputacional_cc6','felipeMaciel_sistemasDistribuidos_cc6','felipeMaciel_desenvWeb_cc6','bonfim_lingFormaisAutomatas_cc6','joaoVictor_verificValid_es6','nauber_manutSoft_es6','annaBeatriz_qualSoftware_es6','annaBeatriz_arquitSoft_es6','josimeire_empreendedorismo_cces','bonfim_compiladores_cc7','bonfim_teoriaComp_cc7']
horariosAulas = ['H1','H2','H3','H4']
dias = ['seg','terc','quart', 'quint','sext']
curso = ['cc','es','cces']
cadeirasUmVez = ['andersnoMagno_preCalculo_cc1', 'annaBeatriz_projetoPCeT_cces']   
folgaDia = ['seg', 'sext']

cc1=['andersnoMagno_preCalculo_cc1','gastao_matBasica_cc1','marcioCosta_fundProg_cc1','josimeire_eticaProfissional_cc1','rafaelIvo_introComp_cc1']
cc2=['andersonFeitoza_matDiscreta_cc2','gleison_calculo_cc2','alexLima_arquitComp_cc2','tatiane_estrutDados_cc2','eurinardo_labProg_cc2']
cc3=['gastao_algLinear_cc3','pablo_algGrafos_cc3','joaoVictor_progOrientObj_cc3','rosineide_probEstatistica_cc3','rafaelIvo_lingProg_cc3']
cc4=['marcioCosta_projetoAnaliseAlgoritmos_cces','eurinardo_edAvanc_cc4','danielMarcio_fundBancDados_cc4','alexandre_logicaComp_cc4','patricia_engSoft_cc4']
cc5=['rafaelIvo_sistemaOperacional_cc5','patricia_interHumanComp_cc5','felipeMaciel_redesComputadores_cces','danielMarcio_compGrafica_cc5', 'osvaldo_analiseProjetoSistemas_cces']
cc6=['alexLima_intelArtific_cc6','tatiane_matComputacional_cc6','felipeMaciel_sistemasDistribuidos_cc6','felipeMaciel_desenvWeb_cc6','bonfim_lingFormaisAutomatas_cc6']
cc7=['annaBeatriz_projetoPCeT_cces','bonfim_compiladores_cc7','bonfim_teoriaComp_cc7','josimeire_empreendedorismo_cces']

es1=['annaBeatriz_introEngSoft_es1','gleison_matBasica_es1','marcioCosta_fundProg_es1','josimeire_eticaProfissional_es1']
es2=['eurinardo_labProg_es2','osvaldo_introProReqSoft_es2','tatiane_estrutDados_es2','alexLima_arquitComp_es2', 'andersonFeitoza_matDiscreta_es2']
es3=['nauber_lingProg_es3','joaoVictor_progOrientObj_es3','pablo_algGrafos_es3','patricia_reqSoft_es3','nilde_probEstatistica_es3']
es4=['danielMarcio_fundBancDados_es4','nauber_procSoft_es4','osvaldo_analiseProjetoSistemas_cces','alexandre_logicaComp_es4', 'marcioCosta_projetoAnaliseAlgoritmos_cces']
es5=['osvaldo_gerencProjSoft_es5','joaoVictor_projetoDetalhadoSoft_es5','patricia_interHumanComp_es5', 'felipeMaciel_redesComputadores_cces','alexLima_sistemaOperacional_es5']
es6=['joaoVictor_verificValid_es6','josimeire_empreendedorismo_cces','nauber_manutSoft_es6','annaBeatriz_qualSoftware_es6','annaBeatriz_arquitSoft_es6']
es7=['annaBeatriz_projetoPCeT_cces']

alexandre = ['alexandre_logicaComp_cc4','alexandre_logicaComp_es4']
annaBeatriz = ['annaBeatriz_projetoPCeT_cces','annaBeatriz_introEngSoft_es1','annaBeatriz_arquitSoft_es6','annaBeatriz_qualSoftware_es6']
bonfim = ['bonfim_lingFormaisAutomatas_cc6','bonfim_compiladores_cc7', 'bonfim_teoriaComp_cc7']
danielMarcio = ['danielMarcio_fundBancDados_cc4','danielMarcio_compGrafica_cc5','danielMarcio_fundBancDados_es4']
eurinardo = ['eurinardo_labProg_cc2','eurinardo_edAvanc_cc4','eurinardo_labProg_es2',]
felipeMaciel = ['felipeMaciel_redesComputadores_cces','felipeMaciel_sistemasDistribuidos_cc6','felipeMaciel_desenvWeb_cc6']
nauber = ['nauber_procSoft_es4','nauber_manutSoft_es6','nauber_lingProg_es3',]
osvaldo = ['osvaldo_analiseProjetoSistemas_cces','osvaldo_introProReqSoft_es2','osvaldo_gerencProjSoft_es5']
josimeire = ['josimeire_eticaProfissional_cc1','josimeire_eticaProfissional_es1','josimeire_empreendedorismo_cces']
marcioCosta = ['marcioCosta_fundProg_cc1','marcioCosta_projetoAnaliseAlgoritmos_cces','marcioCosta_fundProg_es1']
joaoVictor = ['joaoVictor_progOrientObj_cc3','joaoVictor_progOrientObj_es3',' joaoVictor_projetoDetalhadoSoft_es5','joaoVictor_verificValid_es6']
pablo = ['pablo_algGrafos_cc3','pablo_algGrafos_es3',]
tatiane = ['tatiane_estrutDados_cc2','tatiane_matComputacional_cc6','tatiane_estrutDados_es2',]
patricia = ['patricia_engSoft_cc4','patricia_interHumanComp_cc5','patricia_reqSoft_es3','patricia_interHumanComp_es5',]
alexLima = ['alexLima_arquitComp_cc2','alexLima_intelArtific_cc6','alexLima_arquitComp_es2','alexLima_sistemaOperacional_cc5']
gleison = ['gleison_calculo_cc2','gleison_matBasica_es1']
gastao = ['gastao_matBasica_cc1','gastao_algLinear_cc3']
rosineide = ['rosineide_probEstatistica_cc3']
andersonFeitoza = ['andersonFeitoza_matDiscreta_cc2','andersonFeitoza_matDiscreta_es2']
nilde = ['nilde_probEstatistica_es3',]
andersnoMagno = ['andersnoMagno_preCalculo_cc1']
rafelivo = ['rafaelIvo_introComp_cc1','rafaelIvo_lingProg_cc3','rafaelIvo_sistemaOperacional_cc5']
#limpar lista que vem em formato de lista
def cleanList(stringAux):
    stringAux = stringAux.replace(',', '\n')
    stringAux = stringAux.replace('[', '')
    stringAux = stringAux.replace(']', '')
    stringAux = stringAux.replace("'", "")
    stringAux = stringAux.replace(" ", "")
    stringAux = stringAux.replace("*", " ")
    return stringAux

#Gerar arquivo que garante que diciplinas de um credito irao ocorrer pelo menos uma vez por semana
def garantirExistenciaUmCredito():
    gerarExistenciaCadeiras = []
    for cadeira in range(0, len(cadeirasUmVez)):
        for dia in range(0, len(dias)):
            for horarios in range(0, len(horariosAulas)):
                    gerarExistenciaCadeiras += [cadeirasUmVez[cadeira]+"_"+dias[dia]+"_"+horariosAulas[horarios]]

    info = open("clausulasGerais.txt", "w")
    cleanList(str(gerarExistenciaCadeiras))
    info.write(cleanList(str(gerarExistenciaCadeiras)))
    info.close()



#Gerar arquivo que garante que diciplinas de um credito irao ocorrer pelo menos uma vez por semana
def garantiExistenciaDoisCreditos():
    gerarExistenciaCadeiras = []
    for cadeira in range(0, len(cadeiras)):
        for dia in range(0, len(dias)):
            for horarios in range(0, len(horariosAulas)):
                    gerarExistenciaCadeiras += [cadeiras[cadeira]+"_"+dias[dia]+"_"+horariosAulas[horarios]]

    info = open("clausulasGerais.txt", "a")
    cleanList(str(gerarExistenciaCadeiras))
    info.write(cleanList(str(gerarExistenciaCadeiras)))
    info.close()


#Gerando cadeiras de um credito de maneira que elas nao se repitam nos outros dias
def gerarClausulasUmCredito():
    cadeirasDoisCreditos = []
    for cadeiras in range(0, len(cadeirasUmVez)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for dia2 in range(0, len(dias)):   
                    for horario2 in range(0, len(horariosAulas)):
                        if(dia1 != dia2):
                            cadeirasDoisCreditos += ["-"+cadeirasUmVez[cadeiras]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+" *"+"-"+cadeirasUmVez[cadeiras]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]
                        elif(horario1 != horario2):
                            cadeirasDoisCreditos += ["-"+cadeirasUmVez[cadeiras]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+" *"+"-"+cadeirasUmVez[cadeiras]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDoisCreditos))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDoisCreditos)))
    info.close()

#Gerar para dois dias na semana obedecendo regra de pareamento
#Gerando de maneiro que caso acontece em um dia nao acontece em outro
def gerarClausulasDoisCredito():
    cadeirasDoisCreditos = []
    for cadeira in range(0, len(cadeiras)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for dia2 in range(0, len(dias)):   
                    for horario2 in range(0, len(horariosAulas)):
                        if(dia1+2 == dia2 and horario1 == horario2):
                            cadeirasDoisCreditos += ["-"+cadeiras[cadeira]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*"+cadeiras[cadeira]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]
                            """if (dia2-2 == dia1 and horario2 == horario1): else:
                                cadeirasDoisCreditos += ["-"+cadeiras[cadeira]+"_"+dias[dia2]+"_"+horariosAulas[horario1]+" "+"*"+cadeiras[cadeira]+"_"+dias[dia1]+"_"+horariosAulas[horario2]]"""
                                
                            if(dia1 != dia2):
                                cadeirasDoisCreditos += ["-"+cadeiras[cadeira]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+" *"+"-"+cadeiras[cadeira]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]
                            elif(horario1 != horario2):
                                cadeirasDoisCreditos += ["-"+cadeiras[cadeira]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+" *"+"-"+cadeiras[cadeira]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDoisCreditos))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDoisCreditos)))
    info.close()


#Gerando clausulas de maneira que não tenha choque de horario entre as cadeiras de um mesmo semestre no curso de CC.
def gerarClausulasHorarioCC():
    cadeirasDiasHorarios = []
    for cadeira1 in range(0, len(cc1)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(cc1)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+cc1[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+cc1[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(cc2)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(cc2)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+cc2[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+cc2[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(cc3)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(cc3)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+cc3[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+cc3[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(cc4)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(cc4)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+cc4[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+cc4[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(cc5)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(cc5)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+cc5[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+cc5[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(cc6)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(cc6)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+cc6[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+cc6[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(cc7)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(cc7)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+cc7[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+cc7[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]


    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()


#Gerando clausulas de maneira que não tenha choque de horario entre as cadeiras de um mesmo semestre no curso de ES.
def gerarClausulasHorarioES():
    cadeirasDiasHorarios = []
    for cadeira1 in range(0, len(es1)):
        for dia1 in range(0, len(dias)):  
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(es1)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+es1[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+es1[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(es2)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(es2)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+es2[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+es2[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(es3)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(es3)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+es3[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+es3[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(es4)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(es4)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+es4[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+es4[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(es5)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(es5)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+es5[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+es5[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(es6)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(es6)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+es6[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+es6[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(es7)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(es7)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+es7[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+es7[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()


#gerando clausulas  que causam conflito nos horários da disciplinas de um mesmo professor.
def gerarConflitoProfessores():
    cadeirasDiasHorarios = []
    for cadeira1 in range(0, len(alexandre)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(alexandre)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+alexandre[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+alexandre[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]


    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()


    for cadeira1 in range(0, len(annaBeatriz)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(annaBeatriz)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+annaBeatriz[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+annaBeatriz[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(bonfim)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(bonfim)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+bonfim[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+bonfim[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(danielMarcio)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(danielMarcio)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+danielMarcio[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+danielMarcio[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(eurinardo)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(eurinardo)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+eurinardo[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+eurinardo[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(felipeMaciel)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(felipeMaciel)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+felipeMaciel[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+felipeMaciel[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(nauber)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(nauber)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+nauber[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+nauber[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(osvaldo )):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(osvaldo )):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+osvaldo [cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+osvaldo[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(josimeire)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(josimeire )):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+josimeire [cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+josimeire[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(marcioCosta)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(marcioCosta)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+marcioCosta[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+marcioCosta[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(joaoVictor)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(joaoVictor)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+joaoVictor[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+joaoVictor[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(pablo)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(pablo)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+pablo[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+pablo[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(tatiane )):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(tatiane )):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+tatiane [cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+tatiane[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()
    for cadeira1 in range(0, len(patricia)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(patricia)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+patricia[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+patricia[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()
    for cadeira1 in range(0, len(alexLima)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(alexLima)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+alexLima[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+alexLima[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(gleison)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(gleison)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+gleison[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+gleison[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(gastao)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(gastao)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+gastao[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+gastao[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(rosineide)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(rosineide)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+rosineide[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+rosineide[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(andersonFeitoza)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(andersonFeitoza)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+andersonFeitoza[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+andersonFeitoza[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()
    for cadeira1 in range(0, len(nilde)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(nilde)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+nilde[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+nilde[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(andersnoMagno)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(andersnoMagno)):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+andersnoMagno[cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+andersnoMagno[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()

    for cadeira1 in range(0, len(rafelivo)):
        for dia1 in range(0, len(dias)):   
            for horario1 in range(0, len(horariosAulas)):
                for cadeira2 in range(0, len(rafelivo )):
                    for dia2 in range(0, len(dias)):   
                        for horario2 in range(0, len(horariosAulas)):
                            if(cadeira1 != cadeira2):
                                if(dia1 == dia2 and horario1 == horario2):
                                    cadeirasDiasHorarios += ["-"+rafelivo [cadeira1]+"_"+dias[dia1]+"_"+horariosAulas[horario1]+" "+"*-"+rafelivo[cadeira2]+"_"+dias[dia2]+"_"+horariosAulas[horario2]]

    print(str(cadeirasDiasHorarios))
    info = open('clausulasGerais.txt', 'a')
    info.write(cleanList(str(cadeirasDiasHorarios)))
    info.close()


#Gerando clausulas em que os professores folgam seg ou sexta mas nao ambos
def gerarFolga():
    professoresDias = []
    for nomeprof1 in range(0, len(nomeProfessores)):
        for dia1 in range(0, len(folgaDia)):
            for nomeprof2 in range(0, len(nomeProfessores)):
                for dia2 in range(0, len(folgaDia)):
                    if(dia1 != dia2 and nomeProfessores[nomeprof1] == nomeProfessores[nomeprof2]):
                        professoresDias += ["-"+nomeProfessores[nomeprof1]+"_"+folgaDia[dia1]+" "+"*-"+nomeProfessores[nomeprof2]+"_"+ folgaDia[dia2]]

    info = open("clausulasGerais.txt", "a")
    info.write(cleanList(str(professoresDias)))
    info.close()

garantirExistenciaUmCredito()
garantiExistenciaDoisCreditos()
gerarClausulasUmCredito()
gerarClausulasDoisCredito()
gerarClausulasHorarioCC()
gerarClausulasHorarioES()
gerarConflitoProfessores()
gerarFolga()