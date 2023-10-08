# Farm

Module 8 : Winc-assignment : VPS => continous deployment, git actions, ssh secrets

Beschrijving van de opdracht :

Creating and provisioning a server at Digital Ocean;
Connecting to a Linux server over SSH;
Running basic terminal commands on a Linux server;
Deploying a Flask application on a Linux server.

Componenten:

1 : Het aanmaken van de droplet via Digital Ocean ging snel maar het navigeren op de VPS zelf kostte wat meer tijd.
Het navigeren naar de default HTML om daar de Flask-app actief te krijgen duurde een even voordat deze in de lucht was.
2 : Gunicorn installeren ging snel via de pip install gunicorn --upgrade. Maar daanrna kreeg ik veel errors. Door de status te testen in VPS zag ik dat hij wél actief staat. 
Door de functie command /usr/local/bin/gunicorn --bind 0.0.0.0 --chdir /home/farm main:app werkte Gunicorn uiteindelijk wel.
3 : De flask installatie kon ik goed testen via github. Ik koos de tests dmv het zoeken naar de juiste route van de pagina's zoals route @mice 
def test_mice(client):
    response = client.get("/mice")

    assert response.status_code == 200
    assert response.data == b"Cheese!"

Problemen:

1:  Gunicorn: 
Met Gunicorn ben ik tegen meerdere moeilijkheden aangelopen. Het navigeren tussen de locale pc (VS code) en Git Bash via Github en naar de VPS was in het begin veel zoeken. I
Uiteindelijk heb ik de lesstof keer op keer gelezen en stap voor stap uitgevoerd. De stap via Nginx i.c.m Gunicorn ging snel maar ik moest vaker systemctl restart farm gebruiken om de site in de lucht te krijgen of te houden.
 
2:  GITHUB : 
een aantal keren liep github niet goed:
error: cannot pull with rebase: Your index contains uncommitted changes.
error: please commit or stash them.
Dit heb ik kunnen oplossen door de boel recht te trekken :
git status
git add <file(s) to stage>
git commit -m "Your commit message"
git pull --rebase

3: VPS Default : 
In het begin van het opzetten en uitvoeren van de opdrachten in de map /var/www/html ging er veel fout op mijn local.host o.a. poort :80 
Mijn browser was BRAVE en hier bleken veel security plan instellingen tegen te werken. 
De aanapssingen in de default pagine ( ip ) adres van de VPS werkte wél goed dus moest het probleem in mijn pc en instellingen zitten. 
Na lang zoeken bleek ook mijn firewall tóch aan te staan en werkte het uiteindelijk wel. Dit heeft meerdere dagen geduurd.

4: De Secrets heb ik vaker opnieuw moeten uitzoeken omdat ik niet begreep dat in de Secrets ook de Host , Port en Username moesten worden gewaarborgd .
Deze heb ik vaker via de workflow aangepast en zo kwam ik na elke deploy test stap voor stap naar de uiteindelijke authorisatie.


De CD-opdracht opdracht was een echte uitdaging: 
Het werken via VPS is erg fascinerend en een vd leukste onderdelen van de BACK-End opleiding.
Het overzicht behouden in de opdrachten kostte veel tijd omdat meerdere ingewikkelede stappen zich snel opvolgden. 
De combinatie van de Id_isra en Id_isra.pub heb ik een paar keer verkeerd om gebruikt waardoor meerdere erros lang onopgelost bleven. 
Uiteindelijk is het superfascinerend dat het werkt en achteraf (altijd) ook nog logisch.

see the pipelines working: 

http://161.35.19.72

http://161.35.19.72/cow

http://161.35.19.72/mice





 
 


