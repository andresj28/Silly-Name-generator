#!/usr/bin/python3
import random

first = ('Andres','Estefania')
second = ('Javier','Torres')
flag = True
options = ['abismo','and']
feelings = ("Abandono","Abatimiento","Abrumado","Aburrimiento","Abuso","Aceptación","Acompañamiento","Admiración","Afecto","Aflicción","Agobio","Agradecimiento","Agravio","Agresión","Alarma","Alborozo","Alegría","Alivio","Alteración","Amabilidad","Amargura","Ambivalencia","Amor","Angustia","Añoranza","Ansiedad","Apatía","Apego","Apoyo","Aprobación","Armonía","Arrepentimiento","Arrogancia","Arrojo","Asco","Asombro","Atracción","Ausencia","Autonomía","Benevolencia","Bondad","Fastidio","Felicidad","Fervor","Firmeza","Fobia","Fortaleza","Fracaso","Fragilidad","Frenesí","Frustración","Furia","Generosidad","Gozo","Hastío","Honestidad","Honorabilidad","Hostilidad","Humildad","Humillación","Ilusión","Impaciencia","Imperturbabilidad","Impotencia","Incapacidad","Incompatibilidad","Incomprensión","Inconformidad","Incongruencia","Incredulidad","Indiferencia","Indignación","Inestabilidad","Infelicidad","Inferioridad","Injusticia","Inquietud","Insatisfacción","Inseguridad","Insuficiencia","Integridad","Interés","Intolerancia","Intrepidez","Intriga","Invasión","Ira","Irritación","Júbilo","Justicia","Lástima","Libertad","Logro","Lujuria","Manipulación","Melancolía","Menosprecio","Mezquindad","Miedo","Molestia","Motivación","Necesidad","Nostalgia","Obligación","Obnubilación","Obstinación","Odio","Omnipotencia","Optimismo","Orgullo","Ostentación","Paciencia","Pánico","Parálisis","Pasión","Pavor","Paz","Pena","Pereza","Persecución","Pertenencia","Pesadumbre","Pesimismo","Placer","Plenitud","Preocupación","Prepotencia","Pudor","Rabia","Rebeldía","Recelo","Rechazo","Regocijo","Rencor","Repudio","Resentimiento","Reserva","Resignación","Respeto","Resquemor","Satisfacción","Seguridad","Serenidad","Simpatía","Soledad","Solidaridad","Sometimiento","Sorpresa","Sosiego","Suficiencia","Sumisión","Temor","Templanza","Tentación","Ternura","Terquedad","Terror","Timidez","Tolerancia","Traición","Tranquilidad","Tristeza","Turbación","Unidad","Temor","Templanza","Tentación","Ternura","Terquedad","Terror","Timidez","Tolerancia","Traición","Tranquilidad","Tristeza","Turbación")

def abismo():
    novela = f"Abismo de {random.choice(feelings)}"
    return novela

def and_novela():
    feelign1 = random.choice(feelings)
    feelign2 = random.choice(feelings)
    novela = f"{feelign1} y {feelign2}"
    return novela


print("Bienvenido al generador de nombres para novelas")
while flag:
    choosen = random.choice(options)
    if choosen == 'abismo':
        novela_title = abismo()
    elif choosen == 'and':
        novela_title = and_novela()
    print(f"Tu novela es: \n {novela_title}")
    end = input("Si quieres salir presiona 'q'")
    if end == 'q':
        break






