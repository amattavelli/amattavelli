# Excellere in Studio9rev

# Excel per i sistemi di allerta
Esploratori di Excel Bentrovati! Nelle Puntate precedenti abbiamo avuto modo di affrontare le funzioni più comuni per la ricerca e selezione dei dati e per le somme condizionali le Pivot e le Power Query.
Nel frattempo, si sono verificati due eventi che hanno sconvolto e sconvolgeranno la nostra professione: la fattura elettronica e il codice della crisi d’impresa. Si tratta di cambi di prospettiva così radicali che se non gestiti correttamente rischiano di avere un impatto quanto meno destabilizzante. Se proviamo a vedere questi due cambiamenti sotto una luce diversa possiamo individuare oltre alle succitate minacce anche opportunità altrettanto interessanti e sfidanti. Pur nella loro diversità e ambito entrambe le misure sembrano far tendere la professione verso il controllo di gestione inteso come quella capacità di ricavare degli indirizzi dalla lettura dei dati: la fattura elettronica contribuisce  a migliorare la tempestività delle informazioni e in certi casi potrebbe dare la possibilità di analizzare dati che in precedenza erano solo su supporti cartacei, il codice della crisi impone a tutte le aziende, come recita il novellato art. 2086 del codice civile, di predisporre un adeguato “…assetto organizzativo, amministrativo e contabile anche in funzione della rilevazione tempestiva della crisi dell'impresa e della perdita della continuità aziendale, nonché di attivarsi senza indugio per l'adozione e l'attuazione di uno degli strumenti previsti dall'ordinamento per il superamento della crisi e il recupero della continuità aziendale”. Contemporaneamente e la circostanza non è a mio avviso casuale, è entrato in vigore il nuovo modello di scoring del Medio Credito Centrale per l’eleggibilità al Fondo di garanzia che, rispetto al precedente, presenta più indici con gradi di giudizio più ampi e ambiti diversificati per settore di appartenenza.
Cosa c’entra Excel con tutto questo? Ogni volta che parliamo di dati e di analisi, un buon utilizzo di Excel può fare la differenza in termini di tempo e soprattutto di qualità del lavoro. A dimostrazione di quanto appena affermato, in questo articolo affronteremo il tema dello scoring e vedremo come gestire al meglio i giudizi ad un indice in base a una scala di valori.
Per farlo ci avvarremo di alcune funzioni estremamente utili anche se meno conosciute: vedremo allora lE funzioni: SCARTO(), CONFRONTA(), INDICE() e INDIRETTO(), impareremo anche a migliorare graficamente i nostri Dashboard con immagini dinamiche, aggiungendo utensili preziosi alla cassetto degli attrezzi del data analyst.
## LA FUNZIONE CONFRONTA()
Quando abbiamo affrontato il CERCA.VERT() abbiamo messo in guardia dagli effetti indesiderati che si ottengono se aggiungiamo una colonna nella tabella che abbiamo collegato. Osserviamo il seguente esempio
Nella Tabella 1 abbiamo le vendite per Cliente nella Tabella 2 L’anagrafica Clienti ci serve riportare la nazione nella Tabella 2.
Niente di più facile basta collegare i campi Id con la formula collocandoci in D3 (o in qualunque cella del campo Nazione della Tabella 1) e comporre la formula: =+CERCA.VERT([@IdCliente];Tabella2;2;0)
Se aggiungiamo però la colonna partita Iva tra la colonna F e la colonna G la stessa formula però restituisce un risultato indesiderato.
Il risultato era prevedibile: la funzione CERCA.VERT() restituisce sempre la seconda colonna ma ora nella seconda colonna c’è la partita IVA mentre la nazione occupa ora la terza colonna.
Occorre allora una funzione che individui la posizione di un determinato elemento in un elenco, questa funzione è appunto CONFRONTA()
CONFRONTA() è una funzione con tre argomenti (di cui due obbligatori):
Valore: è il valore di cui si intende trovare la posizione: se confrontassimo la lettera C in un elenco che contiene l’alfabeto otterremmo 3
Matrice è l’elenco in cui va ricercato il valore (nell’esempio precedente l’alfabeto) può essere disposto in verticale o in orizzontale
Corrisp è il tipo di approssimazione che si è disposti ad accettare nella ricerca: 0 indica la corrispondenza esatta, 1 restituisce il minore dei maggiori o uguali, -1 restituisce il maggiore dei minori o uguali. Se il campo è omesso l’argomento si intende impostato su 1.
Vediamo un’applicazione proprio agli indici di bilancio
Secondo le disposizioni operative … l’indice V1 Debiti a breve su fatturato, può essere giudicato secondo la seguente scala di valori
…
…
Se assegniamo il punteggio 1 a Basso e 5 ad Alto basterà usare la funzione CONFRONTA(…) per ottenere il risultato desiderato
…
…
Si noti che abbiamo omesso l’argomento Corrisp per ottenere il valore compreso tra un valore e l’altro della scala di valutazione.
Ora grazie al confronta possiamo rendere la funzione CERCA.VERT() più solida se nella Tabella 1 dell’esempio precedente riscriviamo la funzione CERCA.VERT() con CERCA.VERT(..;…;CONFRONTA()) abbiamo superato ogni problema di allargamento della tabella e slittamento campi. Ora infatti la funzione cercherà il valore … nella matrice … e restituirà sempre la colonna che corrisponde alla posizione in cui si trova la parola … rispetto all’intestazione; se aggiungiamo colonne la posizione si sposta e l’indice di conseguenza restituendo quindi sempre il medesimo risultato.
La funzione CONFRONTA() è spesso utilizzata insieme ad altre funzioni e l’accoppiata più riuscita e celebre è proprio con la funzione INDICE().
## LA FUNZIONE INDICE()
La funzione INDICE() combinata con la funzione CONFRONTA(), INDEX() MATCH() per gli anglosassoni, è tra le più amate dagli “Excel Ninja” tanto da prendere spesso il posto della funzione CERCA.VERT() nelle preferenze di utilizzo. Affrontiamo un passo alla volta, come sempre e tutto sembrerà più facile.
La funzione è di per sé elementare: si definisce un insieme di celle, matrice, e si individua una cella all’interno fornendo i riferimenti di riga e di colonna.
Se digitiamo +INDICE( in una cella ci accorgiamo che sono previste 2 forme differenti.
La seconda forma, meno utilizzata, serve in presenza di matrici multiple; nella prima sintassi gli argomenti assumono il seguente significato.
Nel modello del Mediocredito centrale