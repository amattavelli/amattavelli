# Excellere in Studio3

# Excellere in Studio 3: Collegare i dati tra loro (I parte)
## INTRODUZIONE
Ecco dunque un principio essenziale: insegnare i dettagli significa portare confusione. Stabilire la relazione tra le cose, significa portare la conoscenza.
(Maria Montessori)
Nella scorsa puntata abbiamo proseguito il nostro viaggio verso la conoscenza di Excel svelando tutte le tecniche per formattare correttamente i numeri e le date. Chi ha avuto la pazienza di seguirmi fin dall’inizio si è già elevato rispetto alla stragrande maggioranza degli utilizzatori di Excel, in questo e nel prossimo intervento però cominceremo il salto di qualità: impareremo a collegare i dati tra loro, una delle tecniche più utili e impiegate dagli utenti professionali Excel.
Da oggi non avranno più segreti i collegamenti tra tabelle anche provenienti da fonti diverse e le operazioni sui dati in esse contenuti. Se pensiamo che qualsiasi gestionale, pur complesso che sia, non è altro che un insieme ordinato di tabelle con procedure per l’opportuna compilazione e interrogazione, non è poco avere uno strumento in grado di interagire con esse tenendo conto delle relazioni e restituendo elaborazioni di qualità con pochi semplici passaggi. Se ad esempio colleghiamo un piano dei conti ad una contabilità e raggruppiamo per codice di riclassificazione, otteniamo un bilancio; se colleghiamo un’anagrafica con il venduto per articolo, potremo ottenere il venduto per ciascun elemento presente nell’anagrafica mettendo, per esempio, in relazione il fatturato per cliente con le condizioni di pagamento. Potremmo proseguire a lungo ad elencare le applicazioni professionali di quanto impareremo oggi, ma sono certo che al termine dell’articolo con un po’ di sana pratica il lettore saprà trovare il miglior uso delle preziose informazioni che sveleremo nelle prossime righe.
Tre verbi possono rappresentare gli step che dovremo affrontare: nominare, collegare, raggruppare; è il percorso seguito anche da chi è solito costruire applicativi e gestionali e noi dovremo ripercorrerlo passo passo per entrare nel magico mondo dell’analisi dati. Oggi ci occuperemo soprattutto dei primi due passaggi, mentre il prossimo articolo sarà interamente dedicato al raggruppamento, alla sintesi e alla somma dei dati, sia con le formule che con la nuovissima interfaccia Get & Transform, tradotto Recupera e Trasforma (googlate questo termine, ne scoprirete delle belle!); cominceremo col dare un nome alle celle e ai gruppi di celle, introdurremo le Tabelle, un oggetto fondamentale che d’ora in avanti ci accompagnerà per tutte le successive puntate, e collegheremo tra loro i dati, avendo così la possibilità di allargare il nostro modello dati e di conseguenza le nostre capacità di analisi.
## DARE UN NOME AGLI OGGETTI
Come si suole dire partiamo da Adamo ed Eva. Uno degli episodi più rilevanti nel racconto della creazione è il momento in cui Adamo dà il nome alle cose create per lui, quale segno di padronanza su di esse. Dare un nome ci consente di dominare e conoscere meglio quanto abbiamo di fronte. È giunto il momento allora di appropriarci ancora di più della “materia Excel” proprio attraverso l’utilizzo dei nomi.
Assegnare un nome ad un oggetto, una cella, a un gruppo di celle o addirittura a una formula, significa avere la possibilità di poter richiamare quell’oggetto velocemente ogni qualvolta occorra. La cella o il gruppo di celle, che chiameremo l’oggetto nominato, potrà essere visualizzato in qualsiasi momento oppure utilizzato all’interno di una formula. Solitamente si nominano le celle o i gruppi di celle che  contengono un’informazione che vogliamo riutilizzare più volte nella nostra cartella di lavoro: potrebbe trattarsi di una data, del nome dell’autore oppure del soggetto per cui stiamo predisponendo le nostre analisi.
Nell’esempio si vuole nominare la data del documento.
Se avessimo bisogno di riportare tale cella in tutta la cartella di lavoro e non solo nel Foglio1, dovremo ricordarci di digitare la corretta sintassi: Foglio1!$A$2, sicuramente un po’ scomodo. Se però assegniamo un nome alla cella Foglio1!$A$2 chiamandola x sarà sufficiente digitare x in qualsiasi cella della cartella per riprodurre il contenuto della cella Foglio1!$A$2 e si potrà sostituire x a Foglio1!$A$2 in tutte le formule che contengono tale riferimento.
Per assegnare un nome esistono diversi metodi; il più veloce è sicuramente quello di posizionarsi sulla cella o il gruppo di celle cui intendiamo assegnare un nome e facendo clic sulla “casella nome” scrivere liberamente il nome. Proviamo a creare un nome per assegnarlo ad un gruppo di celle. Nella figura osserviamo un elenco di clienti con caratteristiche differenti in ordine alla nazione e alla tipologia. Se vogliamo creare il nome Clienti che consenta di richiamare immediatamente le celle $A$4:$C$14 basteranno due semplici passaggi.
- Selezionare (con tastiera o mouse) l’area $A$4:$C$14
- scrivere Clienti direttamente nella casella nome
Per la scelta dei nomi le regole sono poche e facili da ricordare. Possiamo usare qualsiasi nome a parte R (che indica la riga) e C (che indica la colonna), non possiamo usare spazi (da sostituire con “_” e “.”) e non sono ammessi nomi di riferimenti già esistenti: ad esempio, non potremo mai assegnare un gruppo di celle il nome TAB1 in quanto la cella TAB1 esiste, (anche se probabilmente non la utilizzeremo mai) dovremo optare per TAB.1 o TAB_1, l’uso della maiuscola non è importante (i nomi non sono “key sensitive”).
I nomi hanno anche un ambito di utilizzo. Fino ad ora abbiamo creato nomi riferiti all’intera cartella di lavoro: in qualsiasi cella di qualsiasi foglio digitando +x si otterrà 24/04/2018 ma è anche possibile scegliere ambiti diversi: ad esempio, potremmo dire che l’elenco che abbiamo chiamato Clienti potrebbe valere solo per il Foglio1 in maniera tale da creare altri elenchi e nominarli Clienti in altri fogli. Creando i nomi dalla casella nomi si creano solo nomi con ambito cartella di lavoro, se vogliamo controllare l’ambito dovremo utilizzare metodi alternativi. Un ottimo metodo per creare un nome e controllarne l’ambito consiste nel selezionare la cella o il gruppo di celle e usare il tasto destro (che spesso ci toglie dai guai) e scegliere “definisci nome” come indicato nella figura.
Nella finestra di dialogo, Excel assegna un nome scegliendo Nome_Cliente in quanto nella prima cella in alto a sinistra dell’intervallo è riportato Nome Cliente (si noti che lo spazio è sostituito da “_”) potremo confermarlo o cambiarlo a nostro piacimento, così come potremo cambiare l’ambito scegliendo tra Cartella di lavoro e Foglio1 e infine modificare l’estensione attualmente pari a Foglio1!$A$4:$C$14.
Analogo risultato si ottiene con il comando Gestione Nomi posto nella scheda Formule.
In questa finestra di dialogo potremo creare nuovi nomi, modificare quelli esistenti oppure eliminarli.
Una volta creato un nome, sarà possibile richiamarlo ossia spostare immediatamente la selezione sulle celle riferite al nome; per farlo è sufficiente premere F5 oppure attivare il menù a tendina della casella nome  e scegliere il nome tra quelli riportati.
Nella scheda gestione nomi è collocato il comando Crea da selezione: un ulteriore metodo per creare velocemente anche più nomi in contemporanea. Vediamo come funziona. Poniamo di avere i codici conto e la descrizione accanto, vogliamo assegnare a ciascuna cella contenente la descrizione il suo codice: la cella B21 dovrà chiamarsi SP_01, la cella B22 dovrà chiamarsi SP_2 e così via.
Per ottenere il risultato desiderato sarà sufficiente selezionare l’area comprendente sia i futuri nomi che le celle da nominare e cliccare sul comando Crea da selezione, spuntando l’opzione Colonna Sinistra nella finestra Crea nomi da Selezione.
## DAI NOMI ALLE TABELLE
Esiste un ultimo metodo per creare oggetti nominati ed è forse quello più affascinante tra tutti quelli descritti. I lettori più attenti si saranno accorti che non ho mai usato fino ad ora il termine Tabella per indicare un gruppo di celle. Per Excel le Tabelle sono un oggetto ben definito e diverso da un semplice report per quanto ordinato che sia. Creare una tabella o meglio trasformare un intervallo in tabella è semplicissimo, basta un click sul comando “Formatta come Tabella” nella scheda Home.
Se vogliamo trasformare l’intervallo Clienti in TabClienti procediamo così:
F5 e scelta dell’intervallo Clienti
Per comodità copiamo l’intervallo (CTRL + C) e incolliamolo nella cella E4 (invio o CTRL + V). Ora abbiamo due elenchi identici, trasformiamo quello di destra cliccando sul comando “Formatta come tabella”.
Il nome del comando, “Formatta come tabella”, non deve fuorviarci: la formattazione è solo un aspetto della scelta di lavorare con le tabelle invece che con gruppi di celle, il comando va ben al di là di una semplice formattazione; stiamo infatti dicendo ad Excel che d’ora in poi tutto quello che inseriremo dovrà essere trattato come se riportato in un database; per cominciare Excel pone in rilievo la nostra intestazione e colloca dei filtri in corrispondenza delle intestazioni, apre un menù progettazione dal quale è possibile, tra le altre funzionalità, nominare la Tabella sostituendo quello assegnato automaticamente.
Tabella2 è un nuovo nome degli oggetti della cartella di lavoro e può essere richiamato con F5 oppure attraverso la casella nome come abbiamo visto per gli altri oggetti.
Le Tabelle hanno fatto la loro apparizione con Excel 2007, da allora hanno rappresentato una vera rivoluzione e oggi rappresentano lo standard e il modo migliore per importare e trattare i dati. Se per ipotesi volessimo importare una tabella di un database in Excel il risultato sarebbe proprio una tabella nominata col nome della connessione al database. Le Tabelle sono molto di più che un semplice intervallo nominato, il modo migliore per apprezzarle è quello di cominciare ad utilizzarle sostituendole alle classiche matrici.
Per citare solo alcune delle caratteristiche che le rendono uno strumento di grande utilità e di velocizzazione del lavoro possiamo menzionare:
- l’intestazione automatica allo scorrimento verticale: scorrendo la tabella verso il basso i nomi dei campi si sostituiscono alle lettere intestazioni di colonna;
- il completamento automatico: inserendo una formula in una cella viene riportata automaticamente in tutte le celle della colonna
- Facilità di formattazione
- Totali automatici
- Uso di riferimenti strutturati: anziché riferimenti di cella, ad esempio A1 e R1C1
- Facilità di utilizzo con Get & Transform (vedremo in seguito l’importanza di questa caratteristica)
Potremmo definire le Tabelle l’elemento atomico di un modello dati che, a sua volta, altro non è che un insieme di Tabelle legate tra loro da relazioni e il modo più semplice per creare una relazione è utilizzare la funzione CERCA.VERT().
## La funzione CERCA.VERT()
Ogni qualvolta occorra collegare i dati di due differenti tabelle, è necessario individuare almeno un campo presente in entrambe. Chiameremo questo campo comune chiave.
Se voglio collegare una scrittura con il piano dei conti userò il codice conto quale chiave; se desidero conoscere il costo standard dei prodotti venduti, la chiave sarà il codice articolo; se mi interessa sapere a quale paese corrisponde un determinato codice paese nel rigo RW, userò i codici paesi della tabella paesi in allegato alla dichiarazione dei redditi e così via. In tutti questi casi esiste una tabella in cui la chiave è presente una sola volta (il piano dei conti, l’anagrafica articoli, la tabella paesi) e un’altra tabella in cui tale campo è presente una o più volte. Si tratta di relazioni uno a molti. La relazione “uno a molti” prevede che l’elemento in una tabella venga ripetuto una sola volta (nel listino prezzi, ad esempio, avremo una sola riga per ogni articolo) e il medesimo elemento venga ripetuto più volte in un’altra Tabella (nella tabella righe-ordini “l’articolo x” sarà presente più volte). La relazione uno a molti è la reazione più comune che si può instaurare tra le tabelle, ma non è l’unica.
Si pensi ad un elenco di aziende e l’anagrafe tributaria oppure alle lettere presenti nel codice fiscale per indicare il mese di nascita, l’elenco delle associazioni Italia e l’elenco delle associazioni ammesse al 5×1000  o ancora i votanti con l’elenco degli aventi diritto. In tutti questi casi le chiavi (il codice fiscale, la lettera indicante il mese, i nominativi) sono presenti una sola volta in entrambe le tabelle: sono quindi tutte relazioni uno a uno.
Oltre alle relazioni uno a molti e uno a uno è il caso di citare le relazioni molti a molti, meno frequenti ma comunque importanti: nelle righe di un estratto conto e nelle scritture di un mastrino la stessa cifra può essere ripetuta più volte sia nell’estratto conto che nel Mastrino.
Compreso il concetto di relazione, possiamo affrontare una tecnica per collegare due tabelle, le funzioni di ricerca e riferimento tra le quali il CERCA.VERT() è la più popolare.
Digitando +CERCA.VERT() nella barra della formula si ottiene il Tag della sintassi della funzione
Tradotta in linguaggio comune e utilizzando i concetti trattati diventa:
Cerca un valore nella prima colonna di una matrice_tabella e restituisci la colonna indice con il livello di approssimazione definito dall’argomento intervallo.
Riconosciamo 4 argomenti, separati come di consueto da punto e virgola: è importante comprenderli a fondo e per approfondirne la conoscenza utilizziamo un semplice esempio immaginando di dover collegare un prezzo ad un codice articolo.
- Valore: è quello che abbiamo definito chiave, può essere espresso da un numero, un testo, una cella, una colonna (non ortodosso ma funziona), un nome o un campo di una tabella. L’argomento Valore è ciò che consente il collegamento tra le due tabelle o elenchi, se cerchiamo un prezzo è l’articolo di cui vogliamo conoscere il prezzo quindi, nel nostro esempio, E42;
- Matrice_tabella: è il “luogo” in cui dovremo cercare il Valore, può essere espresso da un gruppo di celle, da un nome riferito ad un intervallo, da una tabella, purché la prima colonna a sinistra contenga il campo chiave, o da intere colonne. È la fonte da cui ricaveremo l’informazione che cerchiamo: se cerchiamo un prezzo è la tabella listino, quindi utilizzeremo l’intervallo A40:C47 o le colonne A:C o l’eventuale nome ad esso assegnato;
- Indice: è il numero di colonna in cui è contenuta l’informazione che cerchiamo. Può consistere in un numero, una cella e più raramente da un nome o un campo di una tabella. È la colonna in cui è contenuto il prezzo, poiché nel listino sono riportati articolo, descrizione e prezzo è pari a 3;
- [Intervallo] è la specifica in merito al tipo di ricerca da effettuare se esatta o approssimativa. Assume solo valore 0 che equivale a FALSO (nella maggioranza dei casi) per la corrispondenza esatta oppure VERO che equivale a 1 per la corrispondenza approssimativa da usarsi solo nel caso la matrice_tabella sia ordinata in maniera crescente. Si consiglia di impostare sempre il valore del campo su FALSO o meglio ancora su 0 salvo non si cerchino risultati particolari che tratteremo nell’ultimo degli esempi del prossimo paragrafo. Omettere il parametro equivale ad impostarlo su VERO. Poiché se cerchiamo un prezzo non è detto che gli articoli siano in ordine crescente imposteremo il parametro su 0 o FALSO.
Risolviamo l’esempio.  Se non impostiamo alcun nome la formula per ricavare in F42 il prezzo corretto diventa
+CERCA.VERT(E42; A40:C47; 3; 0)
Attenzione però se abbiamo intenzione di copiare la formula nelle righe sottostanti dovremo avere l’accortezza di trasformare la matrice_tabella in riferimento assoluto scrivendo
+CERCA.VERT(E42; $A$40:$C$47; 3; 0) oppure se assegniamo il nome listino all’intervallo $A$40:$C$47 abbiamo:
+CERCA.VERT(E42; listino; 3; 0)
Se però abbiamo intenzione di aggiungere nuovi articoli dopo la riga 47 dovremo cambiare il riferimento assoluto e l’estensione del nome, per questo motivo potrebbe convenire riscrivere la formula come CERCA.VERT(E42; A:C; 3; 0) oppure, meglio ancora, trasformare l’intervallo A40:C47 in Tabella.
Fino a qui abbiamo collegato solo una tabella ad un valore, spingiamoci oltre e proviamo a collegare due o più tabelle.
Stabiliamo prima però una “best practice”, una sorta di modus operandi per risparmiare più tempo possibile e limitare gli errori.
- Individuare l’intervallo o la tabella in cui è presente l’informazione che cerchiamo e una chiave di collegamento;
- Se possibile, trasformare gli intervalli in nomi o meglio ancora in tabelle (TAB_1; TAB_2 o altri nomi a piacere)
- Individuare la chiave e verificare che sia scritta nel medesimo modo sia in TAB_1 che in TAB_2. Basta uno spazio invisibile per mandare in errore #N/D la funzione, assicurandosi che la chiave occupi la prima colonna a sinistra di TAB_2
- Individuare il numero colonna in cui si trova l’informazione desiderata (n)
- Scrivere la funzione CERCA.VERT([chiave];[TAB_2];[n];0)
Nei prossimi esempi applicheremo i 5 passaggi appena descritti. A diverse aree dell’attività professionale, con la pratica poi tutto diverrà più semplice e automatico.
## ESEMPI DI APPLICAZIONI PROFESSIONALI
Ciò che abbiamo appena appreso consente innumerevoli applicazioni in ambito professionale e in certi casi dà la possibilità di risparmiare ore ed ore di lavoro con un click. Vediamo di seguito alcune applicazioni ai più svariati campi della professione.
### Esempio 1: Applicazione alla contabilità: i movimenti contabili
Abbiamo una tabella che contiene i movimenti ma non contiene le descrizioni dei conti e un’altra tabella che contiene il piano dei conti completo. Vogliamo naturalmente unire le due informazioni per ottenere una tabella che contenga sia i movimenti che le descrizioni.
Una volta trasformati gli intervalli in tabelle con il comando formatta come tabelle, assegniamo (nella scheda progettazione) il nome TAB_1 alla tabella a sinistra e TAB_2 alla tabella a destra, individuiamo come chiave il codice conto, denominato in un caso CODICE e nell’altro COD e, poiché ci interessa la seconda colonna di TAB_2, scriviamo
=+CERCA.VERT([@CODICE];TAB_2;2;0)
Si noti che selezionando A53 con tastiera o mouse si ottiene in automatico l’espressione [@CODICE], la formula avrebbe funzionato ugualmente anche digitando +CERCA.VERT(A53;TAB_2;2;0) oppure +CERCA.VERT(A53;E:F;2;0)
Qualora nella TAB_1 esistesse un codice non presente nella TAB_2, verrebbe restituito l’errore #N/D e per correggerlo occorrerebbe integrare la TAB_2 del codice mancante.
### Esempio 2: Applicazione alle procedure concorsuali: lo stato passivo
Abbiamo un’anagrafica creditori con importo e classe e dobbiamo compilare lo Stato Passivo.
Una volta trasformati gli intervalli in tabelle con il comando “formatta come tabella”, assegniamo (nella scheda progettazione) il nome STATOPASSIVO alla tabella a sinistra e ANAGRAFICA alla tabella a destra, individuiamo come chiave il codice creditore denominato in un caso COD e nell’altro COD CREDITORE. Ci interessano la seconda, la terza e la quarta colonna.
- Nella colonna B in corrispondenza del campo Nominativo scriveremo
=+CERCA.VERT([@COD];ANAGRAFICA;2;0)
- Nella colonna C in corrispondenza del campo Importo Ammesso scriveremo liberamente l’importo deliberato per l’ammissione
- Nella colonna D in corrispondenza del campo Tipo scriveremo
=+CERCA.VERT([@COD];ANAGRAFICA;4;0)
- Nella colonna E che contiene il campo Non Ammesso e che corrisponde alla differenza tra il credito originario (nella terza colonna del foglio anagrafica) e l’Importo ammesso scriveremo
=+CERCA.VERT([@COD];ANAGRAFICA;3;0)- [@[Importo Ammesso]]
### Esempio 3: Applicazione al diritto: verbali di assemblea
Immaginiamo un’assemblea molto affollata, potrebbe essere un’assemblea di condominio, di una società a larga base azionaria o un’adunanza di creditori. Vogliamo poter riportare i nomi dei soggetti presenti e ottenere mano a mano la quota di diritti rappresentati.
Una volta trasformati gli intervalli in tabelle con il comando formatta come tabelle, assegniamo (nella scheda progettazione) il nome PRESENTI alla tabella a sinistra e AVENTIDIRITTO alla tabella a destra, individuiamo come chiave il nominativo denominato in un caso PRESENTI e nell’altro AVENTE DIRITTO. Ci interessa la somma del campo diritti di voto quindi attiviamo subito i totali automatici con il comando riportato nella scheda progettazione.
Quello che otteniamo è una tabella pronta ad accogliere i nomi dei presenti che sommerà i diritti di voto degli intervenuti.
Basterà a questo punto posizionarsi sulla colonna C in corrispondenza del campo Diritti di voto e digitare
=CERCA.VERT([Presenti];AVENTIDIRITTO;2;0) per avere ad ogni inserimento di presenza la tabella il totale dei diritti rappresentati e verificare così rapidamente eventuali quorum deliberativi e costitutivi.
È fondamentale che i diritti di voto occupino sempre la seconda colonna della tabella AVENTIDIRITTO; se per ipotesi volessimo completare le anagrafiche aggiungendo ad esempio il CODICE FISCALE interponendolo tra la colonna E e la colonna F, la tabella PRESENTI non riporterà più i diritti di voto ma i codici fiscali, in quanto occupanti la seconda colonna; dovremo allora cambiare la formula in:
=CERCA.VERT([Presenti];AVENTIDIRITTO;3;0).
Nella seconda parte che occuperà l’articolo del prossimo numero, vedremo una tecnica per evitare questo problema: l’uso della funzione CONFRONTA() e della funzione INDICE().
### Esempio 4: Applicazione al controllo di gestione: l’analisi di fatturato
Questa volta abbiamo ben 4 elenchi diversi già trasformati in tabelle: una Tabella Vendite da completare con Nome Cliente, Paese, Area e Categoria che si trovano in altre tabelle. Procediamo con ordine.
Il Nome cliente e il Paese possono essere ricavati dalla tabella AnClienti utilizzando l’Id Cliente come chiave; l’Area può essere aggiunta alla tabella AnClienti utilizzando come chiave il campo Paese, la Categoria richiede infine di puntare sulla Prodotti usando il campo prodotto come chiave.
- Nella colonna F in corrispondenza del campo Nome Cliente scriveremo
=+CERCA.VERT([@COD];ANCLIENTI;2;0)
- Nella colonna G in corrispondenza del campo Paese scriveremo
=+CERCA.VERT([@COD];ANCLIENTI;3;0)
- La colonna H, Area, richiede un passaggio intermedio. Occorre infatti ricavare prima l’Area nella tabella ANCLIENTI con la formula da riportare in colonna D =+CERCA.VERT([@Paese];Aree;2;0) e successivamente potremo scrivere in colonna H in corrispondenza del campo Area
- =+CERCA.VERT([@COD];ANCLIENTI;3;0).
- Gli amanti delle funzioni nidificate (che se posso evito) avrebbero potuto scrivere: =+CERCA.VERT(CERCA.VERT([@Cliente];AnClienti;3;0);Aree;2;0)), ma perché complicarsi la vita?
- Per ricavare nella colonna I il campo Categoria dovremo cambiare la chiave e ricercare prodotto nella tabella Prodotti ma dovremo fare attenzione: il campo Prodotto non è il primo campo a sinistra della tabella Prodotti, quindi dovremo selezionare le colonne da J a L o i campi da prodotto a categoria e scrivere:
- +CERCA.VERT([@Prodotto];Prodotti[[Prodotti]:[Categoria]];3;0)
- oppure
- +CERCA.VERT([@Prodotto];J:L;3;0)
Si noti che nonostante la Categoria occupi la quarta colonna, nella formula scriviamo 3 perché ci interessa la terza colonna a partire dalla chiave Prodotto.
### Esempio 5: Applicazione alla revisione: la riconciliazione contabile
Abbiamo due partitari, vogliamo sapere subito quali importi siano presenti nel Conto_1 e non nel Conto_2 e viceversa.
Per farlo confronteremo la colonna Importo del Conto_1 con la colonna Importo del Conto_2 e l’importo del Conto_2 con la colonna importo del Conto_2, ad ogni mancata corrispondenza la formula restituirà l’errore #N/D che ci indicherà le poste da riconciliare. Ecco le due formule:
In cella C144 scriveremo : =+CERCA.VERT(B144;F:F;1;0)
Mentre in G144 =+CERCA.VERT(F144;B:B;1;0)
Si noti che essendo la matrice_tabella formata da un’unica colonna non potevamo che avere 1 nella colonna indice.
Sarà così facile, come riportato in figura, ottenere le due cifre non corrispondenti.
### Esempio 6: Applicazione alla fiscalità: il calcolo dell’IRPEF
Fino ad ora abbiamo sempre detto che l’ultimo argomento deve essere impostato su 0 o FALSO.  Vediamo ora un esempio in cui l’approssimazione non esatta torna molto utile.
Il sistema progressivo di tassazione, di cui l’art. 11 del TUIR, prevede che occorre calcolare una quota fissa pari all’imposta corrispondente al limite dello scaglione precedente e una percentuale sull’eccedenza. Costruiamo una formula per poter inserire un importo in una cella che nomineremo reddito e ottenere l’IRPEF.
Nominiamo la cella F163 Reddito e la tabella a sinistra Aliquote
Se utilizzassimo la funzione CERCA.VERT() con la consueta sintassi e con l’argomento intervallo FALSO o 0 otterremmo l’errore #N/D per tutti i redditi inseriti nella cella F163, salvo che per quelli presenti in colonna A.
Impostando invece l’argomento intervallo su 1 o VERO o omettendolo del tutto, il CERCA.VERT() restituirà un valore compreso tra una riga e la riga successiva.
Cominciamo col trovare l’imposta sullo scaglione, poiché ci interessa la seconda colonna scriveremo:
+CERCA.VERT(Reddito;Aliquote;2)
Omettendo l’argomento INTERVALLO la formula restituisce la seconda colonna corrispondente al più prossimo inferiore al Reddito.
Aliquota sull’eccedenza, poiché ci interessa la terza colonna scriveremo:
+CERCA.VERT(Reddito;Aliquote;3)
Per l’Eccedenza dobbiamo ricavare il limite inferiore dello scaglione posto nella prima colonna e quindi
+CERCA.VERT(Reddito;Aliquote;1)
Il resto sono solo moltiplicazioni e somme.
Come spero avete avuto modo di apprezzare Le potenzialità del CERCA.VERT() sono incredibili e illimitate e richiedono solo un po’ di pratica e di attenzione per essere sfruttate al pieno delle loro potenzialità. Sono certo che una volta compreso il funzionamento entreranno a far parte del vostro bagaglio quotidiano. Nel frattempo potete esercitarvi cliccando qui.
Nel prossimo articolo avremo modo di approfondire l’argomento collegamento e introdurremo le Power Query o Get and Transform (Recupera e trasforma) che rappresentano una vera e propria rivoluzione nell’utilizzo di Excel e nell’analisi dei dati in genere tanto da rendere quasi obsoleta la funzione CERCA.VERT().
Abbiate pazienza, un passo alla volta e arriverete lontano!