# Rev Excellere in Studio6 SETTEMBRE

# Excellere in Studio 6: le Tabelle Pivot (II parte): applicazione ai dichiarativi
## INTRODUZIONE
“Da qui messere si domina la valle” cantava nel secolo scorso il Banco del Mutuo Soccorso.
Chi ha avuto la pazienza, che a questo punto si può quasi definire dedizione, di seguirmi dalla prima puntata, può pronunciare con cognizione di causa la stessa frase riferita al proprio livello di conoscenza di Excel. Non siamo ancora “in cima” (vi si arriva mai?), ma sicuramente dove siamo arrivati vale la pena di fare una sosta e godersi il meritato panorama, fermandosi un poco nell’apprendimento di nuove funzioni e strumenti e approfittandone per testare quanto appreso fin qui in due casi concreti e molto frequenti nella vita di un commercialista: la dichiarazione dei redditi e l’analisi di bilancio.
Svilupperemo i casiutilizzando unicamente gli strumenti e le funzioni viste nelle scorse cinque puntate. Invito chi le avesse perse a darci un’occhiata ma, allo stesso tempo, a non scoraggiarsi e abbandonare la lettura: essere un bell’esempio di come Excel possa diventare un valido compagno nella vita professionale quotidiana.
## POCHE SEMPLICI REGOLE
Prima di affrontare le applicazioni, facciamo un piccolo riassunto delle puntate precedenti, ci servirà per comprendere meglio quanto seguirà. Nel primo articolo, apparso sul numero di marzo, abbiamo imparato l’importanza dei riferimenti assoluti e in quello di maggio abbiamo introdotto i “nomi”, che consentono di richiamare rapidamente parti del foglio di lavoro, e le Tabelle, punto di partenza ideale per qualsiasi tipo di funzione e strumento, che possono essere collegate tra loro con la funzione CERCA.VERT() o con lo strumento “Recupera trasforma” (Power Query) e sintetizzate conteggiandone il numero di elementi o ricavandone la somma con le funzioni di aggregazione: CONTA.SE(), SOMMA.SE(), CONTA.PIÙ.SE() e SOMMA.PIÙ.SE(), che sono state trattate nel numero di giugno.
Il numero di luglio infine e in parte anche questo articolo, sono dedicati ad un altro metodo molto rapido ed efficace per analizzare i dati, le Tabelle Pivot, report componibili e strutturabili liberamente da utilizzare quali alternativa o comprimari delle funzioni di aggregazione.
Se dovessimo riassumere, in una sorta di decalogo, le regole d’oro trattate da marzo a oggi suonerebbe circa così:
- Distinguere sempre i dati (input) dai report (output) collocandoli in intervalli, aree e possibilmente fogli diversi
- Se un intervallo o una cella sono utilizzati più volte fare ricorso ai nomi
- Se possibile trasformare gli intervalli in Tabella
- Limitare righe e colonne vuote inutili
- Ogni volta che si scrive una formula chiedersi, in base a dove dovrà essere copiata, se i riferimenti devono essere assoluti o relativi
- Prediligere la tastiera al mouse
- Immedesimarsi in chi utilizzerà il foglio e prevenirne i comportamenti e gli errori
- Evitare “formule fiume”, scomporre se possibile
- Non esagerare con i colori, utilizzarli solo se servono e dicono qualcosa
- Non inserire due o più volte lo stesso dato di input
Nei paragrafi che seguono, applicheremo le nozioni e tecniche apprese cercando di attenerci ai consigli appena enunciati; affronteremo  di studiola dichiarazione dei redditi in due fasi: la creazione del modello dati e due soluzioni alternative: la prima che non prevede l’utilizzo delle Tabelle Pivot ma solo delle funzioni di aggregazione, la seconda che invece prevede l’uso e le funzionalità delle Tabelle Pivot.
## LA DICHIARAZIONE DEI REDDITI
La compilazione di un quadro redditi di una qualsiasi dichiarazione riferito a qualsiasi soggetto e tipo di reddito professionale o di impresa (RE, RG, RF) si può ridurre in estrema sintesi ad una somma condizionale di una serie di dati. L’importo che andremo ad inserire in un determinato rigo della dichiarazione non è altro infatti che la somma delle voci del conto economico che rispettano un determinato criterio, ad esempio fare parte delle spese auto e pertanto essere parzialmente deducibili. Nel momento in cui redigiamo una dichiarazione dei redditi abbiamo uno schema da completare, il quadro della dichiarazione, e abbiamo dei dati contabili a cui andranno applicate le regole di deducibilità al fine di determinare il reddito imponibile, che altro non sarà che la somma degli elementi del conto economico al netto dei costi non deducibili e ricavi non imponibili. La corretta gestione delle riprese in aumento e in diminuzione sui dati contabili, risolve la maggior parte del lavoro svolto in sede di dichiarazione e poterlo fare in poco tempo e in maniera automatizzata può far apprezzare i vantaggi di un buon utilizzo di Excel.
### Modello Dati
Nella cartella di lavoro Excellere in Studio6-1.xlsx sono presenti due fogli: DATICONTABILI e DICHIARAZIONE.
Nel foglio DATICONTABILI è riportato il conto economico dell’azienda, formato da quattro colonne: CODICE_CONTO, DESCRIZIONE, DARE, AVERE
Il foglio DICHIARAZIONE simula il quadro redditi della dichiarazione, in questo caso il quadro
RF, e si compone di tre colonne: CodRigo, Rigo e Descrizione.
La creazione del modello dati è un momento cruciale nella progettazione di un’applicazione Excel e non solo. Si tratta di modificare i dati, aggiungendo colonne e calcoli per far sì che le operazioni successive possano essere svolte nella maniera più efficace ed efficiente possibile. Nel nostro esempio dovremo operare in maniera tale che, compilando il foglio dati contabili, si formi automaticamente la dichiarazione.
Cominciamo con l’applicare la terza regola del decalogo: trasformiamo gli intervalli dei due fogli in altrettante Tabelle: Tabella1 per i dati contabili e Tabella2 per la dichiarazione. Compiremo quest’operazione (numero di maggio) selezionando gli intervalli e cliccando sul tasto  della scheda Home.
Nel foglio dati in ossequio alla regola 10, che ci induce a non ripetere su più colonne un’informazione che può essere contenuta in unica colonna, occorre creare un campo che riporti la differenza tra DARE e AVERE.  Aggiungiamo quindi la colonna SALDO che riporterà la formula
+[@DARE]-[@AVERE]
Per facilitare la comprensione di chi utilizzerà il foglio (regola 7) potremmo applicare al SALDO il formato numerico #.##0,00 “D”; #.##0,00 “A”; avremo così i saldi positivi, in Dare, seguiti dalla lettera D e quelli negativi dalla lettera A.
Ricordiamo (numero di aprile) che il percorso per ottenere il formato personalizzato è:
- Selezionare l’intera colonna che si intende modificare, in questo caso il campo SALDO
- Utilizzare la combinazione di tasti CTRL +1 per accedere alla finestra formati numerici
- Scegliere la categoria Personalizzato
- Entrare nella casella Tipo e modificare il formato #.##0,00; -#.##0,00 in #.##0,00 “D”; #.##0,00 “A” (si noti l’assenza del segno meno sostituito da “A”)
- Cliccare su Ok
Il risultato è quello mostrato dalla figura.
Ora siamo pronti ad aggiungere le colonne che servono per la corretta classificazione e compilazione della dichiarazione, le riprese in aumento e in diminuzione. Esistono due differenti modalità per determinare una ripresa:
- come percentuale del dato contabile: ad esempio il 20% dell’importo delle spese telefoniche è la quota da inserire nel rigo RF27, insieme alle altre spese ed altri componenti negativi eccedenti la quota deducibile ai sensi dell’art. 109, comma 5
- come valore assoluto: ad esempio l’importo indeducibile di un leasing immobiliare, da inserire in RF31, non è calcolabile come percentuale del costo ma è frutto di un calcolo (che esula gli scopi di questo articolo) basato sulla quota capitale dei canoni.
Aggiungiamo allora due colonne: %Indeducibile e ValAssindeducibile.
Useremo le due colonne per calcolare le riprese che occuperanno l’ottava colonna del nostro foglio, che consentiranno di determinare l’importo netto, pari all’importo contabile al netto delle riprese.
Ciascuna ripresa deriverà alternativamente dalla colonna %Indeducibile o da ValAssIndeducibile e risulterà dalla seguente espressione, che otterremo naturalmente con la combinazione di mouse e tastiera (numeri di maggio e giugno) e non digitando alcuna formula:
+SE([@ValAssIndeducibile]>0;[@ValAssIndeducibile];[@SALDO]*[@[%Indeducibile]])
La traduzione in linguaggio potrebbe essere: se è inserito un valore nel campo ValAssindeducibile, allora quello è il valore da riportare nel campo Ripresa, altrimenti scrivi il prodotto tra %Indeducibile e Saldo.
Nella tabella il costo indeducibile o ripresa sui CARBURANTI E LUBRIFICANTI è calcolato come 80%*600 e così pure la ripresa sugli ALTRI ACQUISTI INDEDUCIBILI, che è pari a 100%*9.500, ma gli ALTRI ACQUISTI sono indeducibili solo per 1.000e pertanto la ripresa è pari a 1.000. La funzione scongiura anche l’errore di inserimento contemporaneo di dati nella colonna %Indeducibile e ValAssindeducibile: qualora venissero inseriti entrambi i campi il risultato sarebbe comunque il valore assoluto.
Creiamo nfine il campo ImportoFiscalmenteRilevante.
Il campo torna utile in quanto trasforma il dato contabile in risultanza fiscale e può essere particolarmente prezioso, qualora si voglia gestire anche il quadro contabile degli studi di settore.
Ora si tratta di dare “un nome” alla ripresa; osserviamo che il foglio DICHIARAZIONE riporta un codice crescente di 10 in 10 accanto ciascun rigo.
Avremmo potuto usare direttamente i righi (colonna B) come codici, ma utilizzando un codice numerico avremo il vantaggio di poter riordinare i righi (apprezzeremo questa facoltà soprattutto quando vedremo le Tabelle Pivot) e gestire eventuali mutamenti quadri redditi: se in futuro dovessero comparire nuovi righi o mutare alcune descrizioni sarà sufficiente lasciare immutato il codice e modificare gli altri campi.
Per collegare la Tabella del foglio DatiContabili al foglio Dichiarazione useremo la funzione CERCA.VERT(), ampiamente trattata nel numero di maggio.
Aggiungiamo tre colonne alla DATICONTABILI: CodRipresa, Rigo e Descrizione.
Inserendo nel campo CodRipresa della tabella DATICONTABILI uno dei numeri da 10 a 410 riportati nella colonna A del foglio DICHIARAZIONE dovranno compilarsi i campi Rigo e DescrRipresa.
Scriveremo quindi per il campo Rigo (la seconda colonna di DATICONTABILI):
+CERCA.VERT([@CodRipresa];DICHIARAZIONE!$A:$C;2;0)
E per il campo DescrRipresa (la terza colonna di DATICONTABILI)
+CERCA.VERT([@CodRipresa];DICHIARAZIONE!$A:$C;3;0)
Osserviamo la riga 30: se non viene compilato il campo CodRipresa, entrambe le formule restituiscono l’errore “#N/D” che si verifica quando la funzione non trova alcuna corrispondenza. Ci sono due alternative per gestire l’errore (come suggerito dalla regola 7):
- utilizzare la funzione SE() per applicare la funzione CERCA.VERT() solo in caso di compilazione del campo CodRipresa trasformando così la formula in:
+SE([@CodRipresa]=“”;””;CERCA.VERT([@CodRipresa];DICHIARAZIONE!$A:$C;3;0))
- Utilizzare la funzione di gestione errori SE.ERRORE(), disponibile a partire dalla versione Excel 2007, la cui sintassi è
SE.ERRORE(valore; valore_se_errore)
La preparazione del foglio dati a questo punto è completa e possiamo procedere a compilare il foglio DICHIARAZIONE seguendo due strade: la prima prevede l’uso delle sole funzioni di aggregazione, la seconda introduce anche le Tabelle Pivot.
### Soluzione A la ichiarazione con le funzioni di aggregazione
La soluzione A è molto semplice: si tratta di sommare rigo per rigo nel foglio DICHIARAZIONE i dati contenuti nei DATICONTABILI: la colonna Importo dovrà sommare il campo Ripresa della Tabella1 del foglio DATICONTABILI, in base alla corrispondenza tra il CodRigo della Tabella2 del foglio DICHIARAZIONE con il CodRipresa della Tabella1 del foglio DATICONTABILI.
Utilizziamo la funzione di aggregazione SOMMA.SE()
+SOMMA.SE(Tabella1[CodRipresa];[@CodRigo];Tabella1[Ripresa])
Che equivale a dire: somma gli importi contenuti nel campo Ripresa per tutte le righe che hanno quale CodRipresa quello indicato nel campo CodRigo.
Inserendo la somma automatica con la casella di spunta nella scheda Progettazione, si ottiene il totale delle riprese.
E se ci fossero riprese non legate ai dati contabili? Niente di più facile: poiché ci siamo imposti di separare i dati di input da quelli di output, dovremo tornare nel foglio DATICONTABILI e aggiungere una riga, avendo cura di lasciare vuoti il campo Dare e il campo Avere e compilare solo il campo ValAssRipresa.
Poniamo ad esempio di dover riportare la ripresa in aumento relativa a una delle 5 rate di ripartizione di una plusvalenza complessiva di 25.000, riferita all’anno 2016 e quindi non legata ad alcun dato di bilancio.
Aggiungeremo quindi una riga alla Tabella1; potremo utilizzare come Codice_Conto il conto utilizzato dal gestionale contabile per le plusvalenze oppure inventarne uno, ad esempio “Plusvalenze 2016 2/5”; non avendo compilato i campi Dare e Avere, il Saldo sarà pari a zero.
Nel campo ValAssRipresa scriveremo la quota della plusvalenza che formerà reddito dell’esercizio, 5.000; la colonna Ripresa assumerà valore 5.000 e la colonna ImportoFiscalmenteRilevante diventerà 5.000 A. Classificheremo infine la ripresa con il CodRipresa 20 che corrisponde al rigo RF7 Quote costanti delle plusvalenze patrimoniali e delle sopravvenienze attive imputabili all’esercizio.
Potremo procedere come abbiamo appena visto anche per inserire le altre componenti del reddito non strettamente legate ai dati di bilancio.
La somma automatica del campo SALDO fornirà il risultato d’esercizio mentre la somma di ImportoFiscalmenteRilevante l’imponibile fiscale. Possiamo riportare il totale del campo Saldo nel foglio DICHIARAZIONE per calcolare l’IRES dovuta.
Un obiettivo secondario, ma non di minor importanza in sede di dichiarazione, è la possibilità di mostrare la composizione di ogni voce in caso di successivi controlli. Per spiegare, ad esempio, quali voci compongano la voce RF18, possiamo utilizzare un filtro direttamente sul campo Rigo.
Una strada alternativa particolarmente raffinata consiste nell’inserire un Filtro dei dati o slicer, un oggetto già presente per le Tabelle Pivot e recentemente reso disponibile nella scheda Progettazione.
Confermando con Ok, possiamo far apparire il filtro che renderà ancora più immediata la selezione.
### Soluzione B le Tabelle Pivot
Utilizzando le Tabelle Pivot non avremo bisogno del foglio DICHIARAZIONE, l’imponibile sarà calcolato direttamente con la Tabella Pivot basata sulla Tabella1 del foglio DATICONTABILI.
Posizioniamoci su una cella qualsiasi della Tabella1 del foglio DATICONTABILI e selezioniamo il comando
Confermiamo con Ok senza selezionare nessuna opzione e spostiamoci direttamente nel Foglio1 appena creato. Aggiungiamo i campi collocando:
- Nelle Righe: CodRipresa (in maniera da ottenere una rappresentazione crescente delle riprese), Rigo e Descrizione Ripresa
- Nei Valori: Ripresa e ImportoFiscalmenteRilevante
Impostiamo i formati numerici e cambiamo il nome ai campi. Abbiamo ottenuto così un report strutturato che indica per ciascun CodRipresa, il Rigo, la descrizione, l’importo della ripresa e quello fiscalmente rilevante.
In fondo alla tabella appare la scritta (vuoto) ad indicare tutte quelle righe per le quali non sono state specificate riprese; la riga riporta importo zero nel campo Riprese Fiscali (che contiene la Somma di Riprese), e nel campo imponibile (che contiene la Somma di ImportoFiscalmenteRilevante) mostra il Saldo da assoggettare a imposta.
Per calcolare l’impatto fiscale di ogni voce e di conseguenza l’IRES, possiamo fare ricorso ad uno strumento delle Tabelle Pivot molto interessante, i campi calcolati, disponibili nella scheda Calcoli tabella pivot/Analizza/Campi, elementi …/Campo calcolato.
Compileremo la finestra di dialogo rinominando il campo “IRES”, spostandoci sulla casella formula (click o tasto Tab) cliccheremo due volte direttamente sul campo ImportoFiscalmenteRilevante e aggiungeremo “*24%” e daremo conferma con Ok.
La Tabella Pivot si completerà con una nuova colonna e la misura appena creata sarà collocata nell’elenco campi.
Il Totale Complessivo della colonna D riporta esattamente l’IRES da imputare all’esercizio. Se desideriamo ottenere i dettagli possiamo aggiungere il campo Descrizione.
In qualsiasi momento potremo espandere o comprimere i dettagli con i tasti  e
Gli obiettivi che ci eravamo posti, calcolo dell’IRES e tenere traccia dei dettagli, sono stati raggiunti ma il risultato non è di certo esaltante da un punto di vista grafico. Proviamo a formattare meglio la tabella e vediamo fino a che punto possiamo arrivare e dove invece occorre fermarsi.
Modifichiamo il Layout della tabella con il comando Layout del Report contenuto nella scheda Progettazione; scegliamo il “Mostra in formato tabella”; togliamo poi i subtotali per rendere il report più leggibile selezionando il comando “Non mostrare i subtotali”, disponibile sempre nel comando Layout del foglio Progettazione.
Le tabelle pivot hanno un’opzione particolarmente interessante per la formattazione. Nella cheda Analizza il comando Seleziona contiene l’opzione Attiva Selezione che consente di formattare i campi per categoria, garantendo così un notevole risparmio di tempo. Per mettere in corsivo tutti i Totali, ad esempio, sarà sufficiente selezionarne uno solo (avvicinandosi al campo col mouse da sinistra a destra e facendo assumere al mouse la forma di freccia nera verso destra) e scegliere il formato corsivo.
Se invece vogliamo modificare l’intera visualizzazione possiamo accedere alla scheda Progettazione e scegliere uno degli stili visivi disponibili o addirittura crearne uno personalizzato da riutilizzare anche in successive occasioni.
I margini manovra, come si osserva, sono piuttosto ampi ma presentano dei limiti invalicabili quali:
- non si possono aggiungere righe o colonne nella tabella
- non è possibile cambiare anche un solo numero della tabella inserendo una formula
- certe descrizioni della tabella sono immutabili
Questi limiti rendono macchinose alcune operazioni che in un report risulterebbero elementari.
Prendiamo ad esempio di dover effettuare un semplice calcolo: verificare l’incidenza effettiva dell’IRES sul risultato d’esercizio.
Tornando per un momento alla soluzione A, sarà sufficiente collocarsi nel foglio DICHIARAZIONE e nella cella D48 digitare +D47/D45
Nella soluzione B ottenere lo stesso risultato richiede innanzi tutto l’inserimento nelle Righe del campo Saldo Excel lo collocherà nell’elenco valori in ultima posizione; spostiamolo in prima posizione e poi rinominiamolo Saldo Cont., posizioniamoci sulla cella I207, scriviamo + e poi spostiamoci sulle celle che dovranno formare il rapporto  probabile (dipende anche dalle impostazioni in sede di installazione) che appaia questa formula:
=+INFO.DATI.TAB.PIVOT("Somma di Ires";$A$3)/INFO.DATI.TAB.PIVOT("Saldo Cont.";$A$3)
che può essere tradotto come: esegui il rapporto tra il totale del campo IRES e il totale del capo Saldo Cont. della Tabella Pivot collocata in A3.
INFO.DATI.TAB.PIVOT() è una funzione estremamente complessa, auto-generata da Excel quando richiamiamo un dato di una Tabella Pivot, che serve per creare una sorta di riferimento assoluto ad un elemento della Tabella pivot a prescindere da eventuali modifiche alla forma e alla lunghezza della tabella.
Se per ipotesi aggiungessimo una riga alla Tabella1 del foglio DATICONTABILI, il totale si sposterebbe dalla riga 207 alla 208 ma la formula in I207 continuerebbe a dare un risultato corretto; se invece avessimo inserito in I207 la formula H207/G207, la cella avrebbe restituito un risultato corretto fino a che la tabella non avesse cambiato dimensione.
Per quanto utile e meritevole di ulteriori approfondimenti, la funzione INFO.DATI.TAB.PIVOT() può essere talvolta scomoda e pertanto può essere disattivata dal Menù opzioni della Tabella Pivot accessibile con il tasto destro da una cella della tabella, oppure direttamente dalla scheda Analizza.