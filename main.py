#!/usr/bin/python3
import random

first = ('Andres','Estefania')
second = ('Javier','Torres')
flag = True
options = ['abismo','and',"aprendiendo"]
feelings = ("Abandono","Abatimiento","Abrumado","Aburrimiento","Abuso","Aceptación","Acompañamiento","Admiración","Afecto","Aflicción","Agobio","Agradecimiento","Agravio","Agresión","Alarma","Alborozo","Alegría","Alivio","Alteración","Amabilidad","Amargura","Ambivalencia","Amor","Angustia","Añoranza","Ansiedad","Apatía","Apego","Apoyo","Aprobación","Armonía","Arrepentimiento","Arrogancia","Arrojo","Asco","Asombro","Atracción","Ausencia","Autonomía","Benevolencia","Bondad","Fastidio","Felicidad","Fervor","Firmeza","Fobia","Fortaleza","Fracaso","Fragilidad","Frenesí","Frustración","Furia","Generosidad","Gozo","Hastío","Honestidad","Honorabilidad","Hostilidad","Humildad","Humillación","Ilusión","Impaciencia","Imperturbabilidad","Impotencia","Incapacidad","Incompatibilidad","Incomprensión","Inconformidad","Incongruencia","Incredulidad","Indiferencia","Indignación","Inestabilidad","Infelicidad","Inferioridad","Injusticia","Inquietud","Insatisfacción","Inseguridad","Insuficiencia","Integridad","Interés","Intolerancia","Intrepidez","Intriga","Invasión","Ira","Irritación","Júbilo","Justicia","Lástima","Libertad","Logro","Lujuria","Manipulación","Melancolía","Menosprecio","Mezquindad","Miedo","Molestia","Motivación","Necesidad","Nostalgia","Obligación","Obnubilación","Obstinación","Odio","Omnipotencia","Optimismo","Orgullo","Ostentación","Paciencia","Pánico","Parálisis","Pasión","Pavor","Paz","Pena","Pereza","Persecución","Pertenencia","Pesadumbre","Pesimismo","Placer","Plenitud","Preocupación","Prepotencia","Pudor","Rabia","Rebeldía","Recelo","Rechazo","Regocijo","Rencor","Repudio","Resentimiento","Reserva","Resignación","Respeto","Resquemor","Satisfacción","Seguridad","Serenidad","Simpatía","Soledad","Solidaridad","Sometimiento","Sorpresa","Sosiego","Suficiencia","Sumisión","Temor","Templanza","Tentación","Ternura","Terquedad","Terror","Timidez","Tolerancia","Traición","Tranquilidad","Tristeza","Turbación","Unidad","Temor","Templanza","Tentación","Ternura","Terquedad","Terror","Timidez","Tolerancia","Traición","Tranquilidad","Tristeza","Turbación")
verbs = ("abrir","amar","asesinar","bastar","callar","cantar","cerrar","comer","conseguir","coser","culpar","decir","destruir","durar","encontrar","esconder","estar","faltar","gustar","intentar","lanzar","llamar","luchar","mentir","necesitar","ofrecer","parar","pelear","perdonar","preferir","prometer","recibir","repetir","salir","sentir","soñar","tener","trabajar","vender","acabar","andar","atacar","bañar","calmar","cazar","citar","comparar","contar","costar","dar","dejar","disculpar","elegir","enseñar","escribir","estudiar","forzar","haber","ir","largar","llegar","mandar","mirar","negociar","olvidar","parecer","peligrar","permitir","preguntar","pulsar","reconocer","responder","saltar","ser","suceder","terminar","traer","venir","acercar","apoyar","ayudar","beber","cambiar","cenar","cocinar","comprar","continuar","crear","dañar","descansar","divertir","empezar","entender","escuchar","existir","funcionar","hablar","jugar","lavar","llenar","matar","morir","nombrar","orar","partir","penar","pisar","preocupar","quedar","recordar","reír","salvar","significar","suponer","tirar","tratar","ver","aconsejar","aprender","bailar","buscar","caminar","centrar","coger","conducir","correr","creer","deber","describir","doler","empujar","entrar","esperar","explicar","ganar","hacer","jurar","leer","llevar","mejor","mostrar","ocurrir","oír","pasar","pensar","poder","preparar","quemar","regalar","saber","seguir","sonar","tardar","tocar","usar","viajar","acordar","armar","bajar","caer","campar","cercar","comenzar","conocer","cortar","cuidar","decidir","desear","dormir","encantar","equipar","esposar","extrañar","gritar","importar","lamentar","limpiar","llorar","mejorar","mover","odiar","pagar","pelar","perder","poner","probar","querer","regresar","sacar","sentar","sonreír","temer","tomar","valer","visitar")
def abismo():
    novela = f"Abismo de {random.choice(feelings)}"
    return novela

def and_novela():
    feelign1 = random.choice(feelings)
    feelign2 = random.choice(feelings)
    novela = f"{feelign1} y {feelign2}"
    return novela

def aprendiendo():
    verb1 = random.choice(verbs)
    novela = f"Aprendiendo a {verb1}"
    return novela


print("Bienvenido al generador de nombres para novelas")
while flag:
    choosen = random.choice(options)
    if choosen == 'abismo':
        novela_title = abismo()
    elif choosen == 'and':
        novela_title = and_novela()
    elif choosen == 'aprendiendo':
        novela_title = aprendiendo()
    print(f"Tu novela es: \n {novela_title}")
    end = input("Si quieres salir presiona 'q'")
    if end == 'q':
        break






