# Business Plan Terza Parte

# Il Business Plan alla base della gestione aziendale (terza parte): dai dati economici a quelli finanziari.
### Abstract
Nella seconda parte dell’articolo è stato determinato il risultato prima degli interessi, delle partite straordinarie e delle imposte.
Per prevedere gli interessi occorre fare riferimento alle fonti finanziarie a lungo termine andando ad analizzare i piani di ammortamento presenti e futuri.
Il tool Business Plan_24 comprende un vero e proprio calcolatore di piani di ammortamento di qualsiasi tipo (Francese/Italiana, con riscatto, con preammortamento) che consente di ipotizzare qualsiasi tipo di forma di finanziamento e ricavarne gli oneri finanziari.
Più complesso è invece il calcolo degli interessi derivanti dalla posizione finanziaria netta a breve termine.
La posizione finanziaria netta finale sarà determinata da tutte le variazioni di cassa derivanti dagli elementi del budget esaminati fino a questo punto e dalle variazioni patrimoniali. È importante notare che tra gli oneri finanziari e la posizione finanziaria netta si instaura un’interrelazione complessa: gli oneri finanziari scaturiscono dalla posizione finanziaria netta, mentre quest’ultima è influenzata dagli oneri finanziari dovuti alle banche. Per risolvere questa interdipendenza circolare, è necessario ricalcolare gli oneri finanziari in modo iterativo. Pertanto, il calcolo degli oneri finanziari viene così strutturato.
Figura : Calcolo degli oneri finanziari
Come si nota dalla figura 1 gli Oneri finanziari su Debiti Fin. A breve ipotizzati sono pari a 25.000 tale valore non corrisponde a 706.858*0,04364=30.847,28 ma tiene conto del calcolo iterativo degli interessi attraverso la formula
= 706.858*(0,04364+0,0019+ 0,000083) = 32.249,38
Dove i è pari al costo medio dell’indebitamento che è storicamente noto e può essere ipotizzato mentre l’indebitamento medio necessita della determinazione della posizione finanziaria netta. Per procedere con i calcoli, è indispensabile redigere il bilancio previsionale o, meglio, il rendiconto finanziario.
In fase di consuntivazione, il rendiconto finanziario viene compilato solo dopo la redazione del conto economico e dello stato patrimoniale. In fase di preventivazione, invece, il processo è inverso: si parte dal conto economico per poi redigere lo stato patrimoniale previsionale attraverso le variazioni previste nel rendiconto finanziario.
Figura : La logica di costruzione dei dati previsionali
### Le dinamiche del capitale circolante
L'analisi delle variazioni delle componenti del capitale circolante, come crediti commerciali, debiti commerciali e scorte, consente di determinare l'impatto sulle disponibilità liquide dell'azienda. Alcune di queste componenti quali le rimanenze sono state già determinate in occasione del calcolo degli acquisti altre andranno ricavate partendo dalle previsioni economiche.
Per quanto concerne debiti e crediti di natura commerciale la variazione di cassa corrisponderà alla formula.
Crediti iniziali – Crediti finali + Debiti Finali – Debiti Iniziali
Dando per noti i valori iniziali di debiti e crediti, occorre determinare i valori finali che corrispondono al debito/credito nei confronti del fornitore/cliente al termine dell’esercizio e possono essere così determinati.
Voce di conto economico*(1+aliquota media Iva)*giorni previsti/365
I giorni previsti, da indicare distintamente per ciascuna voce, non coincideranno con i giorni di dilazione, ma verranno utilizzati per determinare l'eventuale credito o debito previsto. Ad esempio, se l’azienda paga il collegio sindacale, il cui costo è di 12.000 euro, due volte all’anno: una a giugno e una ai primi di gennaio; risulta evidente che al 31/12 di ciascun anno il debito verso i sindaci sarà pari alla metà dell'importo fatturato. Pertanto, nello schema in corrispondenza di tale voce, si indicheranno 180 giorni a prescindere dalle condizioni di pagamento e così pure per tutte le voci che avranno manifestazione economica nell’esercizio e monetaria interamente nel successivo andrà riportato 365.
Figura : Calcolo dei crediti verso clienti
Per determinare i crediti verso clienti, è stata calcolata l’IVA sul fatturato Italia per aliquota storica. Poi, ipotizzando i giorni di rotazione, si è cercato di avvicinare il dato calcolato (500.360,66) a quello reale (500.000). Successivamente, sono stati ipotizzati i giorni di rotazione futuri (mantenendoli costanti) per determinare il valore dei crediti.
Analogo procedimento è stato compiuto con i debiti di fornitura.
Per gli altri debiti e altri crediti che non derivano direttamente da voci del conto economico occorre invece analizzarne la composizione per determinarne l’andamento.
### I debiti e crediti IVA
Figura : Calcolo del debito IVA
Il calcolo dell’IVA deriva da quanto già sopra spiegato: l’indicazione di un’aliquota per ogni tipo di ricavo/costo consente di calcolare il debito/credito IVA. Poiché l’IVA viene versata mensilmente, è necessario ipotizzare quale parte dell’eventuale debito IVA residuerà al termine dell’esercizio. Nel caso esaminato la cifra è stata ipotizzata pari a un dodicesimo del valore del debito totale.
Le assunzioni fino a qui sviluppate consentono di determinare la prima parte del rendiconto finanziario previsionale.
Figura : Il calcolo del flusso finanziario dopo le variazioni del CCN
### Il calcolo del flusso della gestione reddituale e la dinamica delle imposte dirette
Figura : Il calcolo del flusso della gestione reddituale
Il flusso della gestione reddituale tiene conto del pagamento degli interessi, delle imposte sul reddito e della riduzione dei fondi. Per interessi e fondi, sarà sufficiente indicare le variazioni monetarie.
Per quanto concerne le imposte, occorrerà tenere conto della dinamica tra saldi e acconti.
Innanzi tutto, occorre procedere al calcolo delle imposte dovute per ciascun esercizio indicando eventuali riprese in aumento e diminuzione, così facendo sarà possibile calcolare il saldo, ossia la differenza tra l'imposta dovuta sui redditi effettivamente conseguiti e gli acconti già versati. Se gli acconti risultano superiori all'imposta dovuta, il contribuente ha diritto a un rimborso o può utilizzare l'eccedenza in compensazione per futuri debiti fiscali. Al contrario, se gli acconti sono stati inferiori all'importo effettivamente dovuto, sarà necessario versare la differenza a saldo. In Italia, gli acconti d'imposta sono generalmente pari al 40% dell'importo totale dovuto entro il 30 giugno e al 60% entro il 30 novembre. Quindi al 31/12 di ciascun anno l’azienda dovrebbe aver saldato interamente i propri debiti e versato interamente i propri acconti.
Nel caso in esame l’azienda non aveva acconti 2024 versati; pertanto, il carico finanziario sul 2025 risulta il doppio delle imposte calcolate per il 2024.
### Investimenti
La lista degli investimenti è già stata redatta in occasione del calcolo degli ammortamenti, ora si tratta solo di indicare: l’eventuale IVA, il metodo di pagamento, l’eventuale debito residuo al termine di ciascun esercizio nonché flussi da disinvestimenti.
Figura : Investimenti e disinvestimenti
### Fonti finanziarie
Le fonti finanziarie sono di due tipi: mezzi di terzi e mezzi propri.
Per quanto concerne le fonti di terzi, dovremo considerare le accensioni dei finanziamenti e il rimborso delle relative rate, che verranno ricavate dal foglio dedicato ai piani di ammortamento.
Per quanto concerne i mezzi propri, dovremo quindi considerare le variazioni di capitale o, al contrario le distribuzioni di eventuali dividendi.
Figura : Le fonti finanziarie proprie e la determinazione del flusso di cassa
Nell’esempio l’azienda prevede nuova liquidità apportata dai soci per 200.000,00 che contribuiscono alla determinazione della variazione della posizione finanziaria netta che potrà essere destinata per variare i debiti bancari o per incrementare le disponibilità liquide.
### Lo Stato Patrimoniale Previsionale
Completato il rendiconto finanziario abbiamo tutti gli elementi per compilare lo stato patrimoniale previsionale: le immobilizzazioni saranno aumentate degli investimenti e ridotte da ammortamenti e cessioni, le variazioni delle voci del circolante sommate ai saldi iniziali daranno i saldi finali, i fondi saranno incrementati degli accantonamenti e diminuiti delle distribuzioni, il patrimonio netto sommato algebricamente al risultato netto godrà degli apporti e si ridurrà per le distribuzioni, i finanziamenti saranno incrementati delle accensioni e decrementati dal pagamento delle rate infine la posizione finanziaria netta varierà nelle sue componenti attive e passive per effetto del cash flow netto.
Figura : Conto economico e Stato Patrimoniale previsionale
### Il monitoraggio
La mensilizzazione è fondamentale per ottenere un buon monitoraggio delle performance aziendali. Attraverso la suddivisione dei dati in periodi mensili, è possibile individuare con maggiore precisione le variazioni e le tendenze nel tempo. Questo approccio consente di rilevare tempestivamente eventuali anomalie o problemi, permettendo di intervenire prontamente per correggerli. Inoltre, la mensilizzazione facilita la comparazione dei dati tra diversi periodi, migliorando la capacità di analisi e la pianificazione strategica.
Figura : Lo schema di mensilizzazione
Nel tool il tema è affrontato consentendo all’utente di assegnare ad ogni voce del conto economico uno schema di distribuzione mensile degli importi come indicato in figura.
Si conclude così la redazione della parte numerica di un business plan che ci ha accompagnato per tre articoli. Per quanto possa sembrare complesso redigere un Business Plan, non è niente rispetto alla sfida di realizzarlo! Avere avuto la pazienza di leggere e comprendere quanto abbiamo raccontato può essere considerata già una buona metà strada.
Ricorda, ogni grande impresa inizia con un piano... E ogni piano con una buona dose di caffè!