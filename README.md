# farm
Module 8 : Winc-assignment : VPS => continous deployment, git actions, ssh secrets

beschrijving van de opdracht :

Creating and provisioning a server at Digital Ocean;
Connecting to a Linux server over SSH;
Running basic terminal commands on a Linux server;
Deploying a Flask application on a Linux server.

componenten:

1 Het aanmaken van de droplet via Digital Ocean ging snel maar het navigeren op de VPS zelf kostte meer tijd.
Het navigeren naar de default HTML om daar de FLask-app actief te krijgen duurde een tijd voordat ik het door had.
2 Gunicorn installeren ging snel via de pip install gunicorn --upgrade. Maar daanra kreeg ik veel errors. Door de status te testen in VPS zag ik dat hij wél actief staat. 
Door de functie command /usr/local/bin/gunicorn --bind 0.0.0.0 --chdir /home/farm main:app werkte Gunicorn uiteiendelijk wel.
3 De flask installatie kon ik goed testen via github. Ik koos de tests dmv het zoeken naar de juiste route van de pagina's zoals route @mice 

problemen:
1
2
3

Het creëren van een VPS deploy via Digital Ocean vond ik erg intrigerend en interessant. De systax en workflow in de VPS environment was in het begin erg wennen maar uiteindelijk juist heel effectief en krachtig.
Zoals veel andere opdrachten moest ik hier echt de tijd voor nemen om de lesstof en de 'stappen' goed te kunnen plaatsen. In de modules komt veel snel achter alkaar aan bod en om dat goed 'visueel' te volgen was een echte uitdaging. Nginx en Gunicorn bijvoorbeeld. Eigenlijk gebeurt er met een paar stappen heel veel achter de schermen waar ik graag overzicht van probeerde te krijgen. Het manoevreren tussen github naar de VPS, die als default dient werken op het gegeven IP adres was zeker veel gepuzzel. Maar zoals ik merk tijdens coderen is dat de stappen rustig moeten worden gedaan. 
Uiteindelijk ben ik helemaal vast gelopen en heb mijn eerste deploy 'gekilled' en ben helemaal opnieuw begonnen.

In de lesstof in deze module 8 is het op een paar momenten niet duidelijk waaruit je dient te werken. Dit zorgde voor redelijk wat verwarring. 
Het ene moment kan het in BASH ingelogd op de VPS. Maar andere files creëer je in github ( YML )

Het creeëren van de secret key was iets waar ik een beetje tegenop zag tijdens het proces maar werkte uiteindelijk redelijk snel en logisch.
Het grote voordeel van de github actions en secrets is mij nog niet erg duidelijk maar dat zal in de praktijk wel duidelijk worden wanneer projecten non stop worden de gecommit, vermoed ik. Ook begrijp ik wel de veilgiheid maar omdat dit de eerste keer is er mee te werken ben ik vooral blij dat de site runt en de tests doorkomen.

Ondanks dat de requirements van deze opdracht maar een paar regels waren was het veel zoekwerk en gepuzzel. Maar daardoor is het gevoel en het idee wat VPS en deployment doet juist gegroeid.

Dit gedeelte ervaar ik als het meest interessante van de Back-end opleiding omdat er zoveel processen samenkomen. En dan is er nog niets gebeurd qua front-end!

 



 
 


