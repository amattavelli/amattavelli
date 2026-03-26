# Excellere in Studio2

### Excellere in Studio 2: Lavorare al meglio con i formati numerici, data e testo
## INTRODUZIONE
Nella scorsa puntata abbiamo cominciato ad esplorare i segreti di Excel andando a scoprire qualche trucco per risparmiare tempo quando utilizziamo i fogli di lavoro. Abbiamo scoperto quanto sia più efficiente la tastiera rispetto al mouse e l’importanza dell’uso dei riferimenti assoluti e relativi, la causa più frequente di errori da parte degli utenti di Excel di qualsiasi livello (compreso chi sta scrivendo).
Chiariti i capisaldi e prima di entrare nel fantastico mondo delle formule e dell’analisi dati, in questo articolo soffermeremo l’attenzione sulla formattazione dei numeri e delle date, del resto cos’è la contabilità se non un insieme più o meno ordinato di date, numeri e testo?
Se vogliamo allora utilizzare al meglio il “nostro miglior alleato verde con la X” dobbiamo necessariamente saper padroneggiare il modo in cui Excel tratta i numeri e come consente di rappresentarli.
Scopriremo allora che è possibile scegliere formati che “parlano” al lettore, specificando unità di misura o colorandosi al verificarsi di determinate condizioni o, ancora, che aiutano la lettura e scrittura di numeri e codici particolarmente complessi quali l’IBAN (quante volte abbiamo sbagliato il numero degli zeri?). Infine impareremo a padroneggiare una funzione utilissima per costruire vere e proprie relazioni accompagnatorie ai numeri rappresentandoli all’interno di una frase. Un passo alla volta, ma siamo destinati ad arrivare lontano.
## I FORMATI NUMERICI
Spesso ci sarà capitato di volere i numeri negativi in rosso per evidenziare maggiormente i costi o i risultati negativi o di volere aggiungere un testo ad un numero (ad esempio “Kg” o “Euro”), o di voler visualizzare un testo aggiuntivo se nella cella è presente un testo, o di distanziare il segno meno dal numero per evidenziarlo, o di non fare sparire gli zeri da un codice fiscale o da un IBAN o, magari, di voler rappresentare i numeri in migliaia di euro. Per fare tutto ciò la barra formati, a meno di eventuali personalizzazioni, non basta più.
Dovremo invece accedere alla maschera Formato celle attraverso la scheda Numeri nel Menù Home mediante la freccia posta in basso a destra
Oppure aprire l’elenco a discesa e selezionare “Altri formati numerici”.
Meglio ancora, per abituarci all’uso dei tasti come visto nella precedente puntata, utilizzare la combinazione di tasti, CTRL + 1.
In ogni caso apparirà la scheda numero della finestra Formato celle che ci consentirà di sbizzarrirci con i nostri numeri.
Se ci soffermiamo sull’elenco a sinistra osserviamo le diverse tipologie di formati numerici; per il momento approfondiamo i formati: Generale, Numero, Contabilità, Valuta, Percentuale, Frazione, Scientifico, Testo.
- Generale: è il formato di default di Excel quando scriviamo un numero (se non cambiamo formato Excel propone quello), non ha il separatore delle migliaia, lo zero è rappresentato come “0” e il segno negativo è posto accanto alla prima cifra a sinistra, il formato comprende i decimali se presenti nel numero;
- Numero è la scelta più frequente insieme al formato “contabilità”. Selezionando tale opzione è possibile poi scegliere se applicare o meno il separatore delle migliaia, il numero di cifre decimali, il colore e la visualizzazione dei numeri negativi. Lo zero è rappresentato come “0”, il segno negativo è posto accanto alla prima cifra a sinistra, i numeri positivi in colonna risultano allineati con i negativi.
- Contabilità: si ottiene con la pressione del tasto “000” della sezione numeri nella scheda Home
- questo e lo pone tra i formati più utilizzati. Lo zero è rappresentato come “-”, il segno negativo è posto all’inizio della cella e ciò gli conferisce un aspetto più elegante.
- Valuta: è come il formato contabilità ma con un simbolo di valuta posto all’inizio della cella.
- Percentuale: formato per rappresentare percentuali, si possono aggiungere cifre decimali e per selezionarlo è sufficiente cliccare sul simbolo   o più semplicemente porre il simbolo “%” dopo il numero, Excel capirà.
- Frazione: poco usato ma utile in certi casi (si pensi alle divisioni ereditarie, alle comunioni di beni o alle suddivisioni condominiali). Una volta selezionato il formato, si dovrà scegliere il numero di cifre al numeratore e al denominatore. Attenzione! Se si scrive in una cella ½ Excel tradurrà l’inserimento con il giorno 1 febbraio; per far capire che si intende scrivere la frazione sarà sufficiente scrivere: “0 1/2"
- Scientifico: poco utilizzato in ambito contabile e quindi talvolta scambiato per un errore, viene utilizzato per rappresentare numeri particolarmente grandi: ogni numero viene infatti rappresentato come un prodotto tra un numero di decimale di una cifra e 10n : un milione diventa 1,00 E+6, mille miliardi diventano 1,00 E+12.
- Testo: Con questo formato nonostante i numeri continuino ad apparire come tali, non è possibile eseguire formule: +1+1 non fa più 2 ma resta +1+1 per selezionarlo in automatico è possibile anteporre un apice “ ‘ “ al numero.
- Speciale: Formato poco utilizzato e solo per casi specifici, sarà approfondito al termine del paragrafo come utile punto di partenza per i formati personalizzati.
Il mio formato preferito?  Numero con migliaia e 2 cifre decimali per 2 ragioni: si ottiene con una combinazione di tasti facile da ricordare, CTRL + MAIUSC + 1 e, qualora si deselezioni l’opzione “Visualizza zero nelle celle con valore zero”, tutte le celle a zero appaiono come vuote, caratteristica che si rivela molto utile in più di un’occasione.
Ciascuno dei formati appena visti è ulteriormente personalizzabile attraverso la selezione dell’ultimo elemento dell’elenco, “Personalizzato”.
È più semplice di quanto possa sembrare!
La strada migliore è scegliere un formato da cui partire, capirne la sintassi, posizionarsi sulla casella “Tipo:” per modificarlo a nostro piacimento.
Prendiamo il numero 19091997 e vediamo quali possibilità offrono i diversi formati predefiniti e a quale sintassi corrisponde ciascun formato.
Se osserviamo la colonna Sintassi notiamo la presenza di alcuni caratteri e codici, vediamone il significato:
### ;
Il punto e virgola è un carattere fondamentale in Excel e non solo per i formati numerici, serve a distinguere e separare tra loro le parti di un comando, nel caso dei formati numerici distingue i seguenti 4 elementi:
- Formato in caso di numero positivo;
- Formato in caso di numero negativo ;
- Come rappresentare lo zero;
- Che testo aggiungere qualora nella cella ci sia un testo al posto di un numero
Non tutte le parti devono necessariamente essere presenti: il formato 0 ha solo la prima parte, mentre il formato 0;[Blu]-0;”zero”; “Qta_” @ le ha tutte e quattro.
Se scomponiamo 0;[Blu]-0;”zero”; “Qta” @ nelle quattro parti (separate da punto e virgola) che lo compongono, siamo in grado di descrivere facilmente la sintassi che può essere tradotta in:
- numeri positivi senza separatore delle migliaia e formato decimale senza virgole;
- numeri negativi in blu senza separatore delle migliaia e formato decimale senza virgole;
- se la cella riporta il valore zero scrivi: “zero”;
- qualora nella cella sia presente un testo anziché un numero anteponi “Qta ” al testo inserito; se ad esempio scrivessi “prodotto 1” in una cella così formattata otterrei: “Qta prodotto 1”.
### -
Il meno serve per anteporre o post porre il segno “-” ad un numero. Ad esempio il formato 0;0- rappresenta il numero -19091997 come 19091997-.
0
Serve per “costringere” Excel a non omettere gli zeri prima dei numeri o nei numeri dopo la virgola, utilissimo per i codici fiscali e non solo. Ad esempio, per scrivere 01 al posto di 1 useremo il formato 00, per ottenere 1,50 al posto di 1,5 useremo il formato 0,00.
#.
Segnaposto per cifre, gli zeri in eccedenza vengono omessi.
_
Il segno di underscore è utilizzato per creare degli spazi prima del numero. Anteposto ai numeri positivi permette l’allineamento con quelli negativi.
?
Segnaposto da utilizzare per allineare i numeri decimali secondo la virgola, interessante ma utilizzato molto raramente.
*
Altra rarità ma utile nei sommari. Ripete un determinato carattere, al fine di riempire la colonna in larghezza. Il formato  0*-  riempie la cella di trattini dopo il numero, il formato *_0 crea una sottolineatura prima del numero.
@
Da aggiungere alla fine del formato per specificare il testo che dovrà essere anteposto qualora nella cella venga inserito un testo in luogo di una cifra.
.
Posto al termine di un formato numerico lo trasforma il numero in migliaia, milioni, miliardi … Il funzionamento è semplice: basterà aggiungere un punto “.” per ogni migliaia desiderato.
Per le migliaia: #.##0.;[Rosso](#.##0.)
Per i milioni: #.##0..;[Rosso](#.##0..)
[Colore]
Specifica il colore che deve assumere una cella al verificarsi di determinate condizioni. Il più utilizzato è [Rosso] ma è possibile scegliere tra [Nero] – [Celeste] – [Fucsia] – [Bianco] – [Blu] – [Verde] – [Giallo] e non necessariamente la condizione deve essere maggiore/minore di zero. Il formato [Blu][<100] #.##0,00;[Verde]#.##0,00 restituisce i numeri inferiori a 100 in colore blu, con delimitatore delle migliaia e due cifre decimali e i numeri uguali o maggiori di 100 in colore verde
“”
Servono per aggiungere testo prima o dopo le cifre. Ad esempio, qualora volessimo vedere i numeri positivi come “Dare” e i negativi come “Avere”, scriveremmo:
"Dare "#.##0_ ;"Avere "#.##0
stesso procedimento per aggiungere ai numeri prefissi o suffissi quali: “Mt”, “Kg”, “gg”, “h”, “Euro”...
Spesso in contabilità i numeri negativi vengono riportati tra parentesi, tanto che, se si scrive un numero tra parentesi, Excel restituisce in automatico un valore negativo: scrivendo in una cella qualsiasi: (19091997) si otterrà -19091997, come ottenere il risultato opposto? Basterà creare il formato, partendo dal formato numero, (#.##0);[Rosso](#.##0).
## DATE E ORE
Per Excel le date non esistono! E allora perché le vediamo? Le date in Excel non sono altro che la formattazione di un numero decimale.
Se scriviamo in una qualsiasi cella +Oggi() apparirà la data del giorno, ma se applichiamo alla stessa cella un formato numerico otterremo un numero superiore a 43.000, perché per Excel le date non sono altro che numeri che vanno dall’1, che corrisponde a domenica 1 gennaio 1900, al 2.958.465° giorno successivo, che sarà venerdì 31 dicembre 9999; dopo quella data non sarà possibile rappresentare date, ma non mi sembra un grosso problema.
E le virgole? sono naturalmente le ore, i minuti e i secondi, dove 1/24 corrisponde ad un’ora, 1/1440 ad un minuto e 1/86400 ad un secondo.
Sebbene ad un primo giudizio questo metodo possa apparire bizzarro, ha un suo fondamento e si rivela molto utile quando vi è la necessità di operare differenze tra date o somme tra date e giorni. Per calcolare i giorni che mancano al nostro prossimo compleanno potremmo scrivere in una cella la data del nostro prossimo compleanno, in un’altra +Oggi() e nella cella risultato la differenza tra le due. Le operazioni sulle date sono un argomento tanto affascinante quanto vasto che sarà trattato in maniera approfondita in un prossimo intervento, per il momento limitiamoci ad imparare a gestire la corretta rappresentazione e formattazione.
Partiamo dalla data 19/09/1997 che corrisponde al numero 35.692 e che può essere rappresentata come data nei modi indicati in figura:
Analogamente a quanto descritto nel paragrafo precedente, potremo intervenire sui formati data tenendo presente che:
- g corrisponde a giorno scritto in cifre, i numeri inferiori a 10 saranno rappresentati da un unico carattere
- gg corrisponde a giorno scritto in cifre, i numeri inferiori a 10 saranno rappresentati da due caratteri ad esempio 1=01
- ggg corrisponde a giorno scritto in testo abbreviato: lunedì diventa lun
- gggg corrisponde a giorno scritto in testo completo
- m corrisponde al mese scritto in cifre, i numeri inferiori a 10 saranno rappresentati da un unico carattere
- mm corrisponde al mese scritto in cifre, i mesi fino a settembre saranno rappresentati da due caratteri ad esempio 9=09
- mmm corrisponde al mese abbreviato: settembre diventa set
- mmmm corrisponde al mese scritto in testo completo
- mmmmm corrisponde al mese con solo una lettera: gennaio diventa g, febbraio f …
- aa corrisponde alle ultime due cifre dell’anno
- aaaa corrisponde all’anno completo
- hh corrisponde all’ora
- mm ai minuti
- ss ai secondi
I passaggi per la personalizzazione sono i medesimi: scelta di un formato più simile possibile al formato desiderato, click su “Personalizzato” e quindi su tipo, scelta delle parti e del modo in cui andranno riportate (per esteso, abbreviate, in cifre…), scelta dei separatori tra una parte della data e l’altra (-, /, spazio…).
## FORMATI SPECIALI
E i numeri telefonici possibilmente intervallati da spazi o trattini tra una parte e l’altra?
Tutto è possibile! Basterà, ancora una volta, giocare con formati già esistenti che personalizzeremo a nostro piacimento.
Quale base di partenza utilizzeremo i formati speciali.
Come si osserva il numero di telefono è formato da un prefisso di 3 numeri, un trattino ed un interno di 5 numeri; per scoprire come sia stato possibile costruire il formato clicchiamo su “Personalizzato” ed ecco cosa appare:
[<=9999999]####-####;(0###) ####-####
Che tradotto significa:
- per numeri inferiori alle otto cifre  (<=9999999) rappresenta il numero con un suffisso di 4 cifre preceduto da un trattino ad esempio 1234 sarà visualizzato come -1234, 12345 come 1-2345;
- per i numeri superiori alle otto cifre lascia un suffisso di 4 cifre, visualizza fino a 4 cifre prima del segno “-”, e riporta gli altri numeri tra parentesi anteponendo uno zero. Ecco allora che il numero 299999999 diventa (02) 9999-9999. Ovviamente cambiando la sintassi è possibile personalizzare il risultato. Se per esempio volessi la barra “/” per separare il prefisso potrei scrivere 0###"/" ########.
E l’IBAN?
Il codice IBAN è un codice alfanumerico formato da parti predefinite, fissato a 27 caratteri, prevedendo un testo di due caratteri iniziali, un numero a due cifre, una lettera per il CIN, 5 numeri per l'ABI, 5 numeri per il CAB e 12 caratteri (alfanumerici) per il conto corrente.
Per ciascuna delle parti utilizzeremo un formato ad Hoc
Si noti in particolare il formato del numero di conto corrente che aggiunge gli zeri sufficienti a far risultare sempre un numero di 12 cifre: 1 diventa 000000000001.
Se volessi riunire tutte le parti in unica cella, ricreando il codice IBAN potrei utilizzare la funzione CONCATENA() oppure il simbolo “&” tra una cella e l’altra.
Il risultato di tale formula però ci lascerebbe ahimè insoddisfatti, otterremmo infatti:  IT12T630054831 e non, come avremmo sperato, IT12T63005483000000000001.
Perché? Semplice, perché la formattazione è solo una visualizzazione differente di uno stesso numero: 000000000001 è e resta sempre 1. Per risolvere il problema e ampliare ulteriormente la nostra conoscenza di Excel, dobbiamo introdurre una funzione utilissima anche se non molto conosciuta, la funzione TESTO().
## LA FUNZIONE TESTO()
La funzione TESTO() trasforma qualsiasi numero in testo nel formato specificato dall’utente.
La sua sintassi è:
TESTO(val; formato)
Dove “val” è una cella o una formula il cui risultato si intende riportare all’interno di un testo e formato è il formato in cui il numero andrà rappresentato. Il formato andrà sempre posto tra “” e riportato con la sintassi utilizzata per i formati numerici.
Pertanto nell’esempio precedente scriveremo =I15&J15&K15&L15&M15&TESTO(N15;"000000000000") al posto di =I15&J15&K15&L15&M15&N15 ottenendo così il risultato IT12T63005483000000000001
La funzione TESTO() trova però il suo utilizzo migliore in un altro contesto, il commento ai numeri. Capita spesso di voler aggiungere ai report dei commenti contestualizzati in base ai risultati. Ad esempio, in una tabella che mostra il fatturato di due anni consecutivi oltre alla variazione percentuale, potrebbe essere interessante scrivere la frase “il fatturato è variato del…” completandola con l’effettiva variazione.
È noto che per calcolare la variazione del fatturato rispetto all’anno precedente la formula è:
[Fatt (anno t) – Fatt (anno t-1)] / Fatt (anno t-1) = Fatt (anno t)/Fatt (anno t-1)-1
Cominciamo con scrivere nel nostro foglio Excel i due fatturati da confrontare
Ora vogliamo che in A3 appaia la frase: “Il fatturato 2017 ha subito una variazione del ...,.. rispetto all’anno …”.
Esaminiamo il problema: dovremo scrivere un testo (costante) poi una data (variabile), che dovrà essere rappresentata con il giusto formato aaaa e un numero (variabile) con formato percentuale con due cifre decimali del tipo 0,00% e infine un testo e di nuovo una data (variabile) sempre con formato aaaa.
Per concatenare le parti testuali e le variabili useremo, come già visto in precedenza per l’IBAN, l’operatore “&” che unirà le diverse parti avendo l’accortezza di mettere il testo sempre tra “” e senza dimenticare gli spazi.
La formula sarà quindi:
="Il fatturato "&TESTO(C1;"aaaa")& " ha subito una variazione del "&TESTO(C2/B2-1;"0,00%")& " rispetto all'anno "&TESTO(B1;"aaaa")
È importante fare pratica con questa tecnica perché trova numerosi utilizzi in relazioni, perizie o in commenti ai dati di bilancio.
Beh in fondo avete un mese per esercitarvi…
Alla prossima!