# 2024 10 15 Guida operativa di intelligenza artificiale def

<!-- Pagina 1 -->

## L’ AIUTO INTELLIGENTE AL  C OMMERCIALISTA
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
#1
AREE DI DELEGA CNDCEC
I nnovazione e digitalizzazione degli studi professionali e delle imprese
CONSIGLIERE DELEGATO
Fabrizio Escheri
15 OTTOBRE 2024

<!-- Pagina 2 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
1

## Commissione di studio CNDCEC “Intelligenza Artificiale e Bilancio”

## Consigliere CNDCEC delegato
Fabrizio Escheri -  Consigliere delegato all’“Innovazione e digitalizzazione degli studi professionali e delle imprese”

## Presidente

## Robert Braga

## Segretario
Diego Barberi

## Componenti
Pietro Affè
Marcello Bubani
Marco Andrea Centore
Giovanni Emmi
Alessandro Failla

## Andrea Gardini
Federico Loffredo
Fabio Roperto
Fabrizio Scossa Lodovico
Giuseppe Seminara
Claudio Sica

## Esperti esterni
Paolo Attilio Catti
Alessandra Malerba

## Fondazione Nazionale di Ricerca dei Commercialisti
Cristina Bauco
Tommaso Di Nardo

<!-- Pagina 3 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
2

## Sommario
1.   A UTOMAZIONE REGISTRAZIONI  (M ACHINE  L EARNING E  R.P.A.  LA PARTE DI  AI  INDOVINA IL CONTO
CONTABILE CORRETTO DA UTILIZZARE )
8
1.1.   Premessa
8
1.2.   Le fatture elettroniche: una miniera di informazioni per il commercialista
8
1.3.   Struttura di Base
8
1.4.   Elementi Principali
8
1.5.   FatturaElettronicaBody
8
1.6.   Estrazione Automatica di Informazioni
9
1.7.   Vantaggi dell’Utilizzo del Formato XML nelle Fatture Elettroniche
9
1.8.   Utilizzo Pratico
10
1.9.   ChatGPT e l’elaborazione di fatture elettroniche XML
10
1.10.   Claude e l’elaborazione di XML
11
1.11.   Limitazioni e considerazioni
11
1.12.   Limiti dell’IA conversazionale nella gestione delle fatture
14
1.13.   Il potenziale dell’automazione RPA
14
1.14.   Suggerimenti di implementazione di un sistema RPA
14
2.   A CQUISIZIONE DATI
16
2.1.   Estrazione dati da documenti
16
2.2.   Estrazione dati di bilancio
20
2.3.   Conclusioni sull’esercitazione
24
3.   A NALISI DEI DATI E REPORTING
25
3.1.   Utilizzare l’AI per l’analisi dei dati
25
3.2.   Conclusioni sull’esercitazione
31
4.   R EDAZIONE DOCUMENTI STANDARD
33
4.1.   Creazione informative per i clienti
33
4.2.   Generazione automatica di contenuti, (creazione di newsletter o e-mail per clienti)
35
4.3.   Conclusioni sull’esercitazione
53
5.   G ESTIONE PROFILI SOCIAL
55
6.   E FFICIENTAMENTO PROCESSI
61
6.1.   Parte Prima - Procedura per Ottenere una Bozza di Relazione sulla Gestione e
un’analisi di Bilancio
61
6.2.   Parte Seconda - Esempio pratico: Analisi della Circolare 18/E 2024 AdE sul
Concordato Preventivo Biennale (CPB)
67
6.3.   Il fenomeno delle “allucinazioni”
71
6.4.   Conclusione dell’esercitazione
72

<!-- Pagina 4 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
3
7.   M ANUALI E PROCEDURE OPERATIVE
73
7.1.   Conclusione dell’esercitazione
84
8.   F ORMAZIONE
85
8.1.   La Ricerca in manuali
85
8.2.   Creazione di Piani di formazione personalizzati
87
8.3.   Supporto nell’utilizzo del software
104
9.   P OTENZIAMENTO DELLE TECNICHE DI RICERCA WEB TRAMITE  AI
108
9.1.   Conclusione dell’esercitazione
114
10.   A NALISI DELLE CONDIZIONI DI TRATTAMENTO DATI DEI PRINCIPALI SOFTWARE  AI
115
10.1.   ChatGPT
115
10.2.   Claude – Sonet
118
10.3.   Microsoft Copilot
121
10.4.   Google Gemini
123
10.5.   Sintesi
124
11.   C ONSIDERAZIONI CONCLUSIVE
126
12.   L IMITAZIONI AL LAVORO
127
13.   A PPENDICE
128

<!-- Pagina 5 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
4

## Prefazione
Nel giro di pochi anni, l’intelligenza artificiale sta profondamente modificando il lavoro intellettuale,
determinando un cambio paradigmatico che rende necessario un nuovo approccio culturale ed una
nuova metodica nello svolgimento delle attività professionali.
Tale fenomeno, che riguarda tutte le professioni intellettuali, ha un particolare rilievo nel campo
lavorativo dei dottori commercialisti, ossia nello svolgimento delle attività di consulenza, analisi e
supporto alle decisioni di chi governa le imprese, le aziende no-profit e le istituzioni pubbliche.
Essa sta modificando, altresì, le modalità di effettuazione degli adempimenti, contabili e fiscali, che
hanno costituito tradizionalmente, almeno negli ultimi decenni, la principale attività lavorativa dei
commercialisti italiani.
Il cambiamento in atto provocherà, da una parte, l’efficientamento dello svolgimento delle attività più
routinarie, con una riduzione dei costi di studio ed un miglioramento delle performances reddituali.
D’altra parte, determinerà il venir meno di alcune attività tradizionali, creando l’opportunità di
dedicarsi ad incarichi consulenziali a maggior valore aggiunto.
Per cogliere i potenziali benefici di tale innovazione, tuttavia, bisogna governare il cambiamento non
restando passivi nel subirlo.
Pochi decenni fa i commercialisti italiani hanno pagato, a proprie spese, gran parte dell’informatizzazione
di alcuni dei principali ambiti di servizio della pubblica amministrazione, dall’Erario al Registro delle
Imprese, dal processo telematico all’identità digitale, subendo tale processo.
Il Consiglio Nazionale, per evitare il ripetersi di tale fenomeno, ha posto in essere una serie di iniziative,
sia di studio che di confronto con gli altri attori istituzionali, in modo da consentire alla categoria di
farsi trovare pronta.
Non a caso, sono state istituite ben tre commissioni di studio sull’applicazione dell’intelligenza
artificiale (in ambito contabile, fiscale e giudiziario) che hanno approfondito gli aspetti più salienti di
tale fenomeno. L’attività di ricerca delle commissioni si è concretizzata nella pubblicazione del
documento “ Il lavoro del commercialista nell’era dell’intelligenza artificiale: scenari, opportunità e
rischi”  che è stato presentato in occasione del Congresso Nazionale di Torino del 2023.
Al contempo, è stata effettuata un’attività di interlocuzione con le istituzioni che stanno definendo le
regole di utilizzo dell’intelligenza artificiale in ambito professionale, in applicazione dei principi
contenuti nell’AI Act europeo.
Inoltre, atteso che l’evoluzione dei software per la contabilità è nella direzione dell’utilizzo di algoritmi
che consentano una, almeno parziale, automazione dei processi informativi di registrazione ed
elaborazione dei bilanci, si è avviato un confronto con le principali software house al fine di ridurre i
rischi derivanti dall’automazione ed i costi ad essi correlati.

<!-- Pagina 6 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
5
Essendo i dati contabili ormai contenuti in documenti nativi digitali, l’utilizzo dei sistemi basati su A.I.
consente di leggere i dati contenuti nei file, elaborare le scritture imputandone correttamente le poste,
nel rispetto dei principi contabili nazionali ed internazionali.
Nella consapevolezza che l’adozione di nuovi processi all’interno degli studi, coerenti con l’utilizzo delle
tecnologie basate sull’intelligenza artificiale, consentirà un miglioramento delle performances dei
colleghi, si è ritenuto utile elaborare un documento “ pratico ” che consenta di comprendere come
porre in essere i nuovi processi di svolgimento delle attività professionali.
Ciò consentirà di liberare tempo, la risorsa più scarsa a nostra disposizione, ad oggi prevalentemente
occupata dalle attività ripetitive e routinarie. Tempo che potrà essere dedicato allo studio,
all’approfondimento e, soprattutto, al recupero di quella relazione umana con i propri clienti che è
essenziale nella creazione del rapporto di fiducia reciproca connaturato all’attività professionale.
Ritengo, infatti, che solo restituendo centralità alle relazioni umane nel rapporto professionista/cliente
riusciremo a ridare dignità al ruolo sociale dei commercialisti, oggi spesso poco valorizzato nel sentire
comune.
Il mio ringraziamento va, dunque, ai colleghi che si sono impegnati nell’attività della Commissione di
studio Intelligenza Artificiale e Bilanci che ha elaborato, con il supporto costante dei ricercatori del
Consiglio Nazionale, questo pregevole documento, nella certezza che esso potrà costituire uno
strumento utile per chi voglia cogliere le sfide del cambiamento che le nuove tecnologie ci pongono
davanti.

### Fabrizio Escheri
Consigliere CNDCEC con delega
all’Innovazione e digitalizzazione degli
studi professionali e delle imprese

<!-- Pagina 7 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
6

## Premessa
Nell’ottobre 2023 le tre commissioni di studio istituite dal CNDCEC aventi il compito di analizzare
l’utilizzo dell’intelligenza artificiale nella professione del commercialista hanno predisposto il
Documento di ricerca intitolato “Il lavoro del commercialista nell’era dell’intelligenza artificiale:
scenari, opportunità e rischi”.
In quel documento, in parte elaborato da una piattaforma di intelligenza artificiale generativa, sono
stati analizzati gli ambiti di utilizzo di tale tecnologia nella nostra professione e i rischi e le opportunità
di questa introduzione.
Dopo questo primo elaborato è parso necessario, forse imprescindibile, evidenziare ai colleghi la
possibilità di utilizzare fin d’ora l’intelligenza artificiale generativa per svolgere molteplici attività
quotidiane presenti negli studi anche di modeste dimensioni.
Dall’esigenza sopra indicata è nato questo documento, che potrebbe essere definito come un
“quaderno del fare”: nei singoli paragrafi sono state individuare numerose attività da far svolgere
all’intelligenza artificiale generativa e con un linguaggio semplice e intuitivo sono stati indicati gli
strumenti da impiegare, i comandi da utilizzare, gli esiti ottenuti e un commento finale su quanto
effettuato.
Vista la condivisibile sensibilità sul tema da parte dei colleghi, risulterà decisamente gradito anche il
paragrafo che, con estrema sinteticità e in forma tabellare, effettua la cosiddetta “analisi compliance
privacy” delle principali piattaforme di intelligenza artificiale generativa e risponde sinteticamente alle
domande maggiormente significative aventi ad oggetto la sicurezza e protezione dei dati: chi è il
titolare del trattamento, quali dati personali vengono raccolti, quali sono le finalità del trattamento,
dove sono conservati i dati.
L’auspicio è che dopo aver letto questo documento qualsiasi collega dotato di minima curiosità sul
tema, anche sprovvisto di specifiche conoscenze informatiche e infrastrutture hardware consistenti,
possa provare a cimentarsi con queste funzionalità; infatti, si ritiene che soltanto l’esperienza diretta
possa far ben comprendere le effettive potenzialità di utilizzo dell’intelligenza artificiale generativa
anche in contesti non eccessivamente complessi.
Appare evidente che l’intelligenza artificiale è già decisamente presente nell’attuale società e lo sarà
ancora di più nel prossimo futuro: non tentare di conoscere questo strumento da parte dei colleghi, al
fine di utilizzarlo al meglio, rischia di essere un comportamento superficiale che potrebbe generare
una futura perdita di competitività.
Il documento non ha altro obiettivo se non quello di sensibilizzare i professionisti a un uso efficiente e
diligente dei sistemi di AI, nell'ambito di operazioni quotidiane all'interno degli studi professionali.
Ogni confronto tra i suddetti sistemi di AI è stato condotto a fini puramente informativi e scientifici,
senza alcuna intenzione commerciale o promozionale a favore di un sistema rispetto a un altro.

<!-- Pagina 8 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
7
Decliniamo ogni responsabilità per eventuali decisioni, azioni o scelte operative prese sulla base delle
informazioni fornite nella guida. Le valutazioni e i confronti esposti non devono essere interpretati
come consigli professionali, raccomandazioni commerciali o preferenze esplicite. L’utente finale è
incoraggiato a valutare autonomamente le caratteristiche e le funzionalità dei sistemi di AI considerati,
in base alle proprie esigenze specifiche.
In nessun caso gli autori della guida potranno essere ritenuti responsabili per danni diretti, indiretti,
accidentali o conseguenti derivanti dall’uso delle informazioni contenute nel presente documento o
dall’affidamento su tali informazioni.

<!-- Pagina 9 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
8

## 1.   Automazione registrazioni (Machine Learning e R.P.A. la parte di

## AI indovina il conto contabile corretto da utilizzare)

## 1.1.   Premessa
Questo primo argomento, che descrive uno scenario comune di tutti gli studi professionali
(contabilizzazione fatture), descrive l’utilità e le sfide nell’uso dell’intelligenza artificiale (IA) per
l’elaborazione delle fatture elettroniche in formato XML. Evidenzia la struttura standardizzata delle
fatture XML e i vantaggi che offre in termini di automazione e gestione dei dati. Inoltre, sono svolte delle
considerazioni sull’utilizzo di sistemi di automazione RPA ( Robotic Process Automation ) come soluzione
più completa per la gestione delle fatture elettroniche, offrendo capacità di accesso automatico ai sistemi
dell’Agenzia delle Entrate, elaborazione dati e integrazione con software contabili.

## 1.2.   Le fatture elettroniche: una miniera di informazioni per il commercialista
Il file XML della fattura elettronica italiana è un documento strutturato che contiene dati
standardizzati, permettendo una facile elaborazione automatica e l’estrazione di informazioni chiave.
Ecco una panoramica della sua struttura e dei principali elementi:

## 1.3.   Struttura di Base
Il file XML si compone di due sezioni principali:

### ●   FatturaElettronicaHeader :
Contiene
i
dati
di
trasmissione
e
le
informazioni
del
cedente/prestatore e del cessionario/committente.

### ●   FatturaElettronicaBody : Include i dati di dettaglio della fattura.

## 1.4.   Elementi Principali

### FatturaElettronicaHeader :
●   DatiTrasmissione : Informazioni sull’invio del file al Sistema di Interscambio (SdI).
●   CedentePrestatore : Dati del fornitore.
●   CessionarioCommittente : Dati del cliente.
●   TerzoIntermediarioOSoggettoEmittente : Eventuali dati dell’intermediario.

## 1.5.   FatturaElettronicaBody
●   DatiGenerali : Informazioni generali della fattura (tipo, numero, data, ecc.).
●   DatiBeniServizi : Dettagli dei beni/servizi fatturati.

<!-- Pagina 10 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
9
●   DatiPagamento : Modalità e termini di pagamento.
●   Allegati : Eventuali documenti allegati alla fattura.

## 1.6.   Estrazione Automatica di Informazioni
La struttura standardizzata del file XML permette l’estrazione automatica di numerose informazioni
utili:
1.   Dati fiscali: Partita IVA, codice fiscale di fornitore e cliente.
2.   Importi: Totale fattura, imponibile, IVA, ritenute, ecc.
3.   Date: Data di emissione, scadenza pagamento.
4.   Dettagli prodotti/servizi: Descrizioni, quantità, prezzi unitari.
5.   Modalità di pagamento: IBAN, scadenze, rate.

## 1.7.   Vantaggi dell’Utilizzo del Formato XML nelle Fatture Elettroniche
L’adozione del formato XML per la fatturazione elettronica offre molti vantaggi alle aziende. La velocità
di elaborazione è migliorata grazie alla leggerezza dei file XML, che riducono i tempi di attesa e
aumentano l’efficienza operativa. Inoltre, l’automatizzazione consente la gestione delle fatture con
meno intervento umano, diminuendo gli errori manuali e aumentando la precisione dei documenti
contabili. Il formato XML si integra facilmente con i sistemi gestionali esistenti, favorendo il flusso di
informazioni tra diversi software senza bisogno di ulteriori investimenti tecnologici. La
standardizzazione dei dati garantisce uniformità e conformità agli standard internazionali, facilitando
i controlli fiscali e le analisi finanziarie. In sintesi, l’uso di XML nelle fatture elettroniche ottimizza le
operazioni quotidiane e migliora la gestione strategica delle informazioni aziendali.

### Esempio di Struttura XML

### Ecco un esempio semplificato della struttura di un file XML di fattura elettronica:
<p:FatturaElettronica>
<FatturaElettronicaHeader>
<DatiTrasmissione>
<!-- Dati di trasmissione -->
</DatiTrasmissione>
<CedentePrestatore>
<!-- Dati del fornitore -->
</CedentePrestatore>
<CessionarioCommittente>
<!-- Dati del cliente -->

<!-- Pagina 11 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
10
</CessionarioCommittente>
</FatturaElettronicaHeader>
<FatturaElettronicaBody>
<DatiGenerali>
<!-- Informazioni generali della fattura -->
</DatiGenerali>
<DatiBeniServizi>
<!-- Dettagli dei beni/servizi fatturati -->
</DatiBeniServizi>
<DatiPagamento>
<!-- Modalità e termini di pagamento -->
</DatiPagamento>
</FatturaElettronicaBody>
</p:FatturaElettronica>

## 1.8.   Utilizzo Pratico
L’adozione del formato XML standardizzato per le fatture elettroniche offre numerosi vantaggi nel
contesto contabile e fiscale italiano. Utilizzando il Sistema di Interscambio (SdI), le fatture vengono
automaticamente controllate per conformità, assicurando correttezza e completezza dei dati e riducendo
gli errori umani. Per le aziende, questo formato migliora la gestione dei dati finanziari, permettendo analisi
rapide e decisioni informate. Inoltre, l’integrazione con i software gestionali automatizza l’importazione
dati, semplificando i processi amministrativi e migliorando l’efficienza operativa.

## 1.9.   ChatGPT e l’elaborazione di fatture elettroniche XML
Scopriamo in maggiore dettaglio quali sono le modalità con cui ChatGPT può essere efficacemente
impiegato in questo contesto.
Mediante l’upload di una fattura elettronica in formato XML, ChatGPT è dotato della capacità di
identificare ed estrarre informazioni chiave contenute nel documento stesso. Questo può includere,

### per esempio, elementi come l’ importo totale  della fattura o i dati specifici relativi al fornitore,
fornendo così un immediato accesso ad alcune delle informazioni più critiche senza dover ricorrere
alla lettura manuale del documento.
Quando ci si trova di fronte alla necessità di lavorare con un insieme di diversi documenti, ChatGPT si
dimostra particolarmente efficiente. È in grado di processare simultaneamente più fatture
elettroniche, rendendo significativamente più agevole il compito di confrontare i dati da esse derivati
e aggregare informazioni utili, migliorando così l’efficienza nell’analisi dei documenti contabili.

<!-- Pagina 12 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
11
Al fine di automatizzare i processi sopra descritti, ChatGPT può essere messo a frutto nella creazione di

### script Python personalizzati . Questi possono essere progettati per estrarre i dati dai file XML delle fatture
e convertirli in formati che risultano essere più facilmente gestibili e analizzabili, come potrebbero essere
i formati CSV o XLSX. Automatizzando queste operazioni attraverso la programmazione, si ottimizza il
workflow riducendo drasticamente il tempo richiesto per queste operazioni.

### Esiste inoltre la possibilità di sviluppare un modello  GPT customizzato,  che sia specificatamente
orientato alle esigenze legate alle fatture elettroniche italiane. Tale modello sarebbe in grado di
comprendere in modo avanzato la struttura e il contenuto delle fatture e, allo stesso tempo, di disporre

### di  script già predisposti  per la gestione di archivi ZIP contenenti molteplici fatture, semplificando così
ulteriormente il complesso lavoro di amministrazione dei documenti fiscali digitali.

## 1.10.   Claude e l’elaborazione di XML
Claude offre funzionalità simili a ChatGPT, ma presenta alcune restrizioni.

### ●   Analisi del testo XML : Senza la possibilità di caricare direttamente i file, Claude richiede che il
contenuto XML sia inserito come testo per poterlo analizzare ed estrarre informazioni.

### ●   Generazione di codice : Analogamente a ChatGPT, Claude può generare codici per processare i file
XML, sebbene si basi esclusivamente sul testo fornito.

## 1.11.   Limitazioni e considerazioni

### Nonostante l’efficacia di questi strumenti, ci sono delle  limitazioni  da tenere a mente:
Gli strumenti AI, come ChatGPT e Claude, non sono progettati per l’integrazione con sistemi contabili
o database aziendali, salvo elaborazioni o utilizzo di apposite API 1 . Preoccupazioni di sicurezza dei dati
e conformità emergono nell’utilizzo di queste piattaforme per gestire dati sensibili. L’accuratezza e
l’affidabilità di questi software di AI (basati su grandi modelli linguistici) richiedono sempre una verifica
umana, soprattutto nei dati finanziari critici.
Tuttavia, per un impiego contabile professionale e su larga scala, le organizzazioni tendono a preferire

### soluzioni software specializzate , che garantiscono integrazione, sicurezza dei dati e conformità fiscale.

### Nonostante ciò, questi strumenti AI possono essere estremamente utili per  sviluppare prototipi rapidi

### per l’analisi delle fatture,  estrarre dati occasionalmente  per fini non contabili,  apprendere la struttura

### delle fatture elettroniche e  creare script di base  che poi possono essere integrati in sistemi più completi.
Pertanto, sebbene offrano versatilità e notevoli capacità di elaborazione dati, l’uso di questi strumenti

### AI per la gestione contabile effettiva è limitato e dovrebbe essere considerato come un  supporto
anziché un sostituto dei sistemi contabili professionali.
1   Application programming interface : insieme di procedure atte a consentire la comunicazione tra diversi computer o tra
diversi software o tra diversi componenti di software (fonte Wikipedia).

<!-- Pagina 13 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
12
Ecco alcuni esempi di prompt mediante l’utilizzo di ChatGPT ver.4o:

### Un esempio di caricamento di file xml su ChatGPT
ChatGPT utilizza interprete di codice per estrarre informazioni dal file XML utilizzando Python.
Attenzione, il sistema potrebbe andare in “loop” e non riuscire a estrarre informazioni dal file XML,
anche perché non tutti i file XML sono identici, per cui potrebbe richiedere più tempo. Un trucchetto per
velocizzare l’estrazione è quello di chiedere di estrarre le informazioni come file di testo, quindi un
blocco di testo non strutturato. L’AI riuscirà poi a estrapolare le informazioni rilevanti da questo testo

<!-- Pagina 14 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
13
Il sistema riesce a estrarre le informazioni e inserirle in formato tabellare, in questo caso si tratta di una
fattura con più righe. Un altro approccio può essere quello di creare un database relazione in Excel con
due fogli, uno per i dati anagrafici della fattura e uno per le righe della fattura, connessi fra di loro da
un codice univoco di raccordo per identificare a quale fattura corrispondono le diverse righe.

### Altro esempio:
Inseriamo in ChatGPT il piano dei conti aziendale in formato txt.
ChatGPT riesce a riconoscere i dati di un piano dei conti in formato testuale, e sulla base della domanda
trova il conto più adatto sulla base del contesto:
Figura 1 di 2
Figura 2 di 2
Il software crea una tabella con l’accoppiamento del conto contabile rispetto alla descrizione della
fattura elettronica.
Questo è naturalmente un esempio per fare capire al lettore le potenzialità del software ma in termini
di tempo il risparmio si avrà con una integrazione diretta tra software gestionale e AI.

<!-- Pagina 15 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
14

## 1.12.   Limiti dell’IA conversazionale nella gestione delle fatture
L’IA conversazionale è utile in molti contesti, ma ha limiti significativi nella gestione attiva delle fatture
elettroniche. Questi strumenti non possono accedere direttamente ai sistemi dell’Agenzia delle
Entrate, non eseguono operazioni automatizzate e richiedono input manuale. Inoltre, la loro capacità
di memorizzare e processare dati continuativamente è limitata, rendendo difficile gestire flussi costanti
di fatture.

### Ad esempio, un commercialista potrebbe usare  ChatGPT  per interpretare il contenuto di una fattura o
per consigli su come categorizzare spese. Ma per gestire centinaia o migliaia di fatture mensili,
scaricandole dal sistema dell’Agenzia delle Entrate e integrandole nel software di contabilità, l’AI
conversazionale mostra i suoi limiti.

## 1.13.   Il potenziale dell’automazione RPA

### L’automazione RPA offre una soluzione completa che trasforma radicalmente la gestione delle

### fatture elettroniche. Un sistema RPA può:

### ●   Accedere autonomamente al portale dell’Agenzia delle Entrate con credenziali sicure
●   Scaricare automaticamente le fatture a intervalli regolari
●   Elaborare e organizzare i dati estratti, categorizzando automaticamente le transazioni

### ●   Integrare  le informazioni nei software di contabilità, aggiornando i registri IVA e i libri contabili
●   Generare report automatici per il monitoraggio del flusso di fatturazione
●   Segnalare anomalie o discrepanze che richiedono attenzione umana

### Immaginiamo uno studio commercialista che gestisce 50 clienti, ciascuno con 100 fatture mensili.

### Manualmente, questo significherebbe processare 5.000 fatture ogni mese, un compito lungo e

### faticoso. Con un sistema RPA, questo processo potrebbe essere completato in poche ore, senza

### intervento umano diretto.

## 1.14.   Suggerimenti di implementazione di un sistema RPA
L’implementazione di un sistema di Automazione Robotica dei Processi (RPA) in uno studio

### commercialista richiede un approccio metodico e ben strutturato. Il percorso inizia con la  selezione di

### una soluzione RPA open source  che si allinei con le esigenze specifiche dello studio. Questa fase è
fondamentale e richiede una valutazione attenta delle opzioni disponibili, tenendo conto di aspetti
come scalabilità, flessibilità e compatibilità con i sistemi esistenti.

### Successivamente, si passa alla  configurazione del bot per l’accesso sicuro al portale dell’Agenzia delle

### Entrate . Questa è una fase critica che comporta la gestione di dati sensibili, e pertanto deve essere
accompagnata dall’implementazione di rigorosi protocolli di sicurezza per garantire la protezione delle
informazioni.

<!-- Pagina 16 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
15

### La fase successiva prevede la  programmazione della logica di scarico, elaborazione e organizzazione

### delle fatture . Qui i processi manuali vengono convertiti in istruzioni automatizzate, con l’obiettivo di
creare un flusso di lavoro più efficiente e ordinato per la gestione delle diverse tipologie di fatture.

### Prima di rendere operativo il sistema su larga scala, è necessario eseguire  test approfonditi  per
assicurarsi che il sistema sia accurato e affidabile. Questa fase deve includere una vasta gamma di
scenari, incluse situazioni anomale, per garantire che il bot funzioni correttamente in ogni circostanza.

### Un altro passaggio cruciale è l’ integrazione con il software di contabilità esistente , fondamentale per
massimizzare l’efficienza del nuovo sistema. Questa fase richiede una stretta collaborazione tra
sviluppatori RPA ed esperti del software contabile, per garantire che tutto sia perfettamente
sincronizzato e che il flusso di lavoro digitale sia omogeneo.
Per garantire il funzionamento ottimale e continuo del sistema, è indispensabile implementare un

### sistema di monitoraggio con alert . Questo consentirà di rilevare rapidamente eventuali anomalie o
errori e di intervenire tempestivamente per risolverli.

### Infine, il successo a lungo termine del sistema RPA dipende dalla  formazione del personale  sull’uso e
la supervisione della nuova tecnologia. Non si tratta solo di un addestramento tecnico, ma anche di un
cambiamento culturale all’interno dello studio, per garantire che tutti comprendano e adottino il
nuovo approccio automatizzato.
Seguendo questo percorso ben strutturato, gli studi commercialisti possono trarre pieno vantaggio
dall’automazione, migliorando sia l’efficienza operativa che la qualità del servizio offerto ai propri clienti.

<!-- Pagina 17 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
16

## 2.   Acquisizione dati

## 2.1.   Estrazione dati da documenti

### Esempio  - Come creare un AGENT in ChatGPT e sfruttare le informazioni ottenute per compilare dei

### modelli word .
La lettura di informazioni in documenti, in particolare documenti standard come ad esempio la visura
camerale, può essere di aiuto nelle attività quotidiane soprattutto se si trova un modo di automatizzare
l’estrazione delle informazioni per poi poterle utilizzare in fase di controllo o compilazione di altri
documenti (mandati professionali, contratti, modulistica antiriciclaggio, etc.)
Vedremo come, utilizzando strumenti di intelligenza artificiale generativa, non solo è possibile fornire
istruzioni per cercare ed estrarre specifiche informazioni da un documento, ma è possibile anche
creare un Agent che svolga questa funzione specifica, trattandosi di un’attività ripetitiva su un
documento standard come la visura camerale. La creazione di un agent permette di avere sempre a
disposizione la risorsa senza dover ogni volta riscrivere un prompt da zero.
In Chat-GPT4 è possibile accedere ad una sorta di store dove è possibile trovare Agent già pronti all’uso,
esattamente come le APP dell’Apple Store o Play Store per Android. Ma c’è anche la possibilità di
creare il proprio Agent attraverso la funzione “Crea”.

<!-- Pagina 18 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
17
Utilizzando la funzione Crea saremo portati all’interno dell’Editor che si compone di due colonne. Nella
parte di sinistra sarà possibile scrivere per dire a Chat-GPT cosa vogliamo che il nostro agent faccia. È
la prima domanda che ci pone anche l’interfaccia. Nella parte di destra abbiamo un’anteprima del
nostro agent, dove sarà possibile testarne il funzionamento in tempo reale.
Per formulare un prompt corretto al fine di programmare il nostro Agent possiamo, farci aiutare dallo
stesso Chat-GPT. Il nostro scopo è creare un Agent che legga ed estragga i dati principali da una visura
camerale.
Quindi la prima cosa che possiamo fare è chiedere direttamente a Chat-GPT se sa cosa sia una visura
camerale:

### PROMPT:
Sai cos’è una visura camerale?

### RISPOSTA:
La visura camerale è un documento rilasciato dalla Camera di Commercio italiana che fornisce informazioni ufficiali
e dettagliate su un’impresa iscritta nel Registro delle Imprese. Questo documento può includere vari dati, tra cui:
Dati anagrafici dell’impresa: Ragione sociale, sede legale, codice fiscale, partita IVA.
Informazioni legali: Data di costituzione, forma giuridica, capitale sociale.
Attività svolte: Descrizione delle attività economiche e dei settori di appartenenza.
Amministratori e soci: Nomi dei rappresentanti legali, amministratori, soci e titolari di cariche.
Bilanci: Ultimi bilanci depositati, se disponibili.
Procedimenti: Eventuali procedure concorsuali o fallimentari in corso.
La visura camerale può essere richiesta per vari scopi, come la verifica della solvibilità di un’azienda, la
partecipazione a gare d’appalto, la richiesta di finanziamenti o semplicemente per avere una panoramica
completa su un’azienda con cui si intende instaurare rapporti commerciali.
Appurato che ha compreso cosa sia la Visura Camerale possiamo chiedere di scriverci un prompt per
la creazione di un Agent che estragga i dati che ci interessano

### PROMPT:
Creami un prompt da inserire nell’editor di agents per ChatGPT dove l’utente fa l’upload della visura camerale e
l’agent estrae in modo dettagliato le informazioni sulla società, sul legale rappresentante e sui soci. Restituisce
la risposta sotto forma di tabella

### RISPOSTA:
## Upload a Visura Camerale
Please upload the  visura camerale  for extraction of detailed company information.

<!-- Pagina 19 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
18
### Instructions:
1. **Upload** the visura camerale document (PDF format preferred).
2. **Click** the “Extract Information” button to process the document.
3. The agent will extract and present the information in a detailed table format.
### Information to be Extracted:
- **Company Details**:
- Ragione Sociale
- Sede Legale
- Codice Fiscale
- Partita IVA
- Data di Costituzione
- Forma Giuridica
- Capitale Sociale
- Attività Svolte
- **Legal Representative**:
- Nome
- Cognome
- Codice Fiscale
- Carica
- **Shareholders**:
- Nome
- Cognome
- Codice Fiscale
- Percentuale di Possesso
### Output Format:
The extracted information will be displayed in the following table format:
Section
Field
Details
Company Details
Ragione Sociale
[Company Name]
Sede Legale
[Registered Office]
Codice Fiscale
[Tax Code]
Partita IVA
[VAT Number]
Data di Costituzione
[Incorporation Date]
Forma Giuridica
[Legal Form]
Capitale Sociale
[Share Capital]
Attività Svolte
[Activities]

<!-- Pagina 20 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
19
Legal Representative
Nome
[First Name]
Cognome
[Last Name]
Codice Fiscale
[Tax Code]
Carica
[Position]

### Shareholders
Nome
[First Name]
Cognome
[Last Name]
Codice Fiscale
[Tax Code]
Percentuale di Possesso
[Ownership Percentage]
### Extract Information:
[Extract Information Button]
Abbiamo ottenuto dunque un prompt pronto da incollare all’interno dell’editor per creare il nostro
Agent. Sarà possibile testarne il funzionamento in tempo reale dall’anteprima, basterà allegare una
visura e senza scrivere niente premere invio per verificare che l’Agent svolga esattamente il compito
per cui è stato programmato :

<!-- Pagina 21 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
20
Appurato che l’Agent estrae le informazioni in modo corretto possiamo salvare e pubblicare il nostro
Agent, che sarà sempre disponibile nella barra laterale a sinistra dell’interfaccia di Chat-GPT. Basterà
richiamarla e fare l’upload del documento per estrarre i dati necessari.
Una volta estratti i dati sarà possibile chiedere altre cose, ad esempio sarà possibile fare l’upload di un
documento in word come un contratto o un mandato professionale.
Chat-GPT ci restituirà il file word scaricabile aggiornato con le informazioni estratte dalla visura
camerale, andando a scrivere in modo automatico nei campi vuoti mancanti che fanno riferimento a
società e legale rappresentante.

## 2.2.   Estrazione dati di bilancio
2.2.1.   Estrazione dati da PDF con AI
L’obiettivo di questa esercitazione è di mostrare come sia possibile importare dati o informazioni da
PDF (anche non strutturati/immagine) in modo che siano utilizzabili in tabelle Excel o similari, più
facilmente gestibili/elaborabili. Questa simulazione punta a replicare comuni attività quotidiana che
vengono svolte all’interno dello studio e che fino a oggi sono state fatte tramite trascrizione dei dati da
parte di un professionista/collaboratore di studio.

### Esempio: Bilancio di verifica
In questo primo caso d’uso ipotizziamo di ricevere un bilancio di verifica infrannuale, con il confronto
con lo stesso periodo dell’anno precedente. Situazione abbastanza comune nel corso dell’anno.
Solitamente il professionista riclassifica in Excel o con altri strumenti il bilancio per poter fare le analisi
necessarie per poi dare la consulenza al cliente.
La riclassificazione e la trascrizione dei numeri possono essere attività che richiedono tempo e non
sono prive di errori di trascrizione ad esempio.
Il bilancio può arrivare ad esempio in questo formato:

<!-- Pagina 22 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
21
Stato patrimoniale
Conto Economico
Estrarre dati da un file del genere utilizzando lo strumento di Power Query di Excel potrebbe essere
non facilissimo proprio per la struttura del PDF a sezioni contrapposte. Vediamo allora come è possibile
utilizzare un modello di LLM in particolare Chat-gpt4o.
Per prima cosa facciamo l’upload del file in pdf come si è arrivato e aiutiamo il modello a capire cosa
gli abbiamo inviato e assicuriamoci che abbia capito. Il prompt potrebbe essere il seguente:

<!-- Pagina 23 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
22
Ti ho allegato un pdf che rappresenta un bilancio di esercizio al mese di aprile 2024. è diviso in più colonne, a
destra i conti in DARE e a sinistra i conti in AVERE. Le colonne sono: il codice conto la descrizione del conto il
valore nel periodo aprile 2023 il valore corrente ad aprile 2024 la percentuale di differenza rispetto all’anno
precedente. Hai compreso la struttura del file?
ChatGPT ci risponde in questo caso che ha compreso il file e ci dà un primo feedback:

### RISPOSTA
Sì, ho compreso la struttura del file. Il bilancio di esercizio al mese di aprile 2024 è diviso in più colonne e presenta
la seguente struttura:
1.
Colonna del Codice Conto:  Ogni conto è identificato da un codice univoco.
2.
Colonna della Descrizione del Conto:  Viene fornita una descrizione del conto.
3.
Valore nel Periodo Aprile 2023:  Indica il valore del conto nel periodo corrispondente dell’anno precedente
(aprile 2023).
4.
Valore Corrente ad Aprile 2024:  Indica il valore attuale del conto ad aprile 2024.
5.
Percentuale di Differenza Rispetto all’Anno Precedente:  Mostra la variazione percentuale del valore del
conto rispetto all’anno precedente.
Il bilancio è inoltre suddiviso tra conti  DARE  (a sinistra) e conti  AVERE  (a destra).
Se desideri specifiche analisi o estrazioni di dati dal documento, fammi sapere come posso aiutarti ulteriormente.
A questo punto possiamo chiedere direttamente a Chat-GPT di trascriverci tutto il contenuto del pdf
sotto forma di tabella, in modo da poterlo gestire direttamente in Excel:
Riscrivi il contenuto del file sotto forma di tabella, mantenendo le colonne individuate: Codice Conto, Descrizione
conto, valore aprile 2023, valore aprile 2024, differenza rispetto all’anno precedente. Dividi le tabelle in Stato
patrimoniale Attivo, Stato patrimoniale Passivo, Conto economico costi, conto economico ricavi

### RISPOSTA:
Ho estratto i dati dallo stato patrimoniale e dal conto economico del documento PDF e li ho organizzati in tabelle
mantenendo le colonne originali. Ecco i dati:
Stato Patrimoniale
Codice
Descrizione
Imp. periodo confr. (Apr 2023)   Importo (Apr 2024)
% Differenza
1010001
CASSA CONTANTI
11.700,62
2.100,70
-82,05
1020005
BANCA 1
1.136.040,79
1.132.532,50
-0,31
1020006
BANCA 2
1.035.924,90
741.594,26
-28,41
1020009
BANCA 3
283.299,38
669.515,92
136,33
1020010
BANCA 4
1.033.943,25
866.954,13
-16,15
104
CLIENTI
2.715.236,45
2.259.450,08
-16,79
1050002
CONTO 1050002
5.899,74
5.899,74
1050003
CONTO 1050003
2.069.836,19
2.017.336,19
-2,54
1050004
CONTO 1050004
2.424.051,67
2.424.051,67
1050005
CONTO 1050005
19.683,17
19.683,17
1050006
CONTO 1050006
40.737,87
41.474,69
1,81

<!-- Pagina 24 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
23
Come è possibile vedere il software ha estratto correttamente i dati e li ha riscritti all’interno di una
tabella, e l’ha fatto per Attivo e Passivo dello stato patrimoniale, e ha fatto la medesima cosa per i Costi
e Ricavi del Conto economico.
Nella tabella sopra indicata è stata riportata solo una parte della risposta fornita da Chat-GPT per motivi
di lunghezza, e sono stati anonimizzati i conti nella colonna “Descrizione”. Nella versione originale
l’applicativo ha correttamente trascritto la descrizione dei conti come presenti sul file PDF originale.
A questo punto abbiamo la possibilità di chiedere di crearci un file Excel da scaricare (o copiare e
incollare le tabelle appena generate all’interno di Excel).
Oppure possiamo fare le nostre analisi direttamente all’interno di Chat-GPT: possiamo infatti chiedere
di riclassificare ad esempio il conto economico, secondo uno schema che possiamo fornirgli noi:
Riclassificami il conto economico, leggendo e riclassificando le varie voci della descrizione, secondo il criterio del
costo del venduto. Scrivimi come risultato una unica tabella con i soli totali. In particolare usa il seguente schema:
ricavi - costo del venduto = margine lordo industriale - costi commerciali e marketing - costi R&S e pubblicità -
costi amministrativi e generali = reddito operativo +/- gestione accessoria +/- gestione finanziaria +/- gestione
straordinaria = risultato di esercizio

### RISPOSTA
Ecco la riclassificazione del conto economico secondo il criterio del costo del venduto:
Riclassificazione del Conto Economico
Categoria
Apr 2023
Apr 2024
% Differenza
Ricavi di Vendita
7.725.898,06
6.862.923,69
-11,17
Costo del Venduto
- Materie prime/semilavorati/acquisti
5.753.733,44
4.798.050,05
-16,61
- Acquisti prodotti finiti
212.045,19
79.315,09
-62,60
- Esistenze iniziali
1.713.301,00
996.764,00
-41,82
- Costi di lavorazione presso terzi
562.542,98
596.401,75
6,02
Totale Costo del Venduto
8.241.622,61
6.470.530,89
-21,49
Margine Lordo Industriale
-515.724,55
392.392,80
-176,09
Costi Commerciali e Marketing
- Provvigioni
51.735,78
43.794,63
-15,35
- Costi per fiere
13.974,46
30.933,98
121,36
- Pubblicità
11.969,80
539,81
-95,49
Totale Costi Commerciali e Marketing
77.680,04
75.268,42
-3,10
Costi R&S e Pubblicità
- R&S e sviluppo prodotti
0,00
0,00
- Pubblicità
11.969,80
539,81
-95,49
Totale Costi R&S e Pubblicità
11.969,80
539,81
-95,49

<!-- Pagina 25 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
24

## 2.3.   Conclusioni sull’esercitazione
Come è possibile vedere, lo strumento di Intelligenza Artificiale Generativa può tornare utile in concreti
casi di utilizzo in studio nel momento in cui c’è da riportare o trascrivere in formato strutturato
informazioni contenute in file non facilmente gestibili. Nell’esempio mostrato si tratta di un bilancio di
verifica ricevuto da un cliente, ma lo stesso procedimento si può applicare per esempio a piani di
ammortamento di finanziamento, rateazioni di cartelle esattoriali da inserire poi all’interno di tabelle
o fogli di lavoro.

<!-- Pagina 26 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
25

## 3.   Analisi dei dati e reporting

## 3.1.   Utilizzare l’AI per l’analisi dei dati
Uno dei vantaggi che l’intelligenza artificiale generativa ha portato è quello di riuscire, tramite un
processo guidato dall’interazione tra il linguaggio naturare e l’interpretazione di dati, a compiere
analisi e statistiche anche avanzate su vari set di dati.
Il flusso di lavoro può essere svolto in duplice maniera.
Il chatbot non esegue direttamente i calcoli sui dati ma assiste l’utente nel processo di analisi come,
ad esempio:

### •   Input dei dati : ChatGPT può ricevere dati in vari formati (testo, tabelle CSV, Excel, ecc.). In base ai
dati forniti, può suggerire come importarli in strumenti di analisi o come procedere all’analisi
manuale.

### •   Pulizia dei dati : ChatGPT può aiutare a identificare errori nei dati, come valori mancanti,
formattazioni incoerenti o errori di battitura, e suggerire come risolverli. Ad esempio, può guidarti
su come uniformare i formati o gestire i dati mancanti.

### •   Riepilogo dei dati : Dopo aver caricato i dati, ChatGPT può fornire un riepilogo descrittivo, ad
esempio media, mediana, distribuzione, o frequenze di valori specifici, e spiegare il significato di
questi risultati.

### •   Visualizzazione : ChatGPT può suggerire come creare grafici come istogrammi, grafici a barre, linee
temporali, grafici a dispersione (scatter plot), per comprendere meglio i trend e le relazioni
all’interno dei dati. Ad esempio, può guidare nella creazione di un grafico per monitorare le
vendite nel tempo o segmentare i clienti.

### •   Individuazione di tendenze e pattern : ChatGPT può assistere nella scoperta di tendenze nei dati,
come stagionalità nelle vendite o comportamenti d’acquisto ricorrenti, evidenziando i periodi di
crescita o calo.

### •   Segmentazione : Può guidare nella segmentazione dei dati, ad esempio per identificare cluster di
clienti basati su acquisti, abitudini o altre variabili, creando così gruppi di analisi con caratteristiche
comuni.

### •   Interpretazione dei risultati : ChatGPT può aiutare a interpretare i risultati ottenuti dall’analisi e
fornire suggerimenti su come presentarli in report chiari e comprensibili. Ad esempio, può creare
descrizioni automatiche dei grafici e delle tendenze rilevate.
Oppure, nelle versioni più avanzate, come nel modello 4o di Chat-GPT, è possibile anche far eseguire
direttamente calcoli sui dati presentati. In questo caso l’applicativo aprirà delle sessioni di Python, o
altri linguaggi di programmazione dove andrà ad effettuare fisicamente i conteggi, generando in tempo
reale il codice necessario per eseguire i calcoli.

<!-- Pagina 27 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
26
Vediamo ora alcuni casi pratici di utilizzo di strumenti di AI Generativa per la gestione e analisi dei dati.
Il primo passaggio è quello di fornire a ChatGPT (o altro strumento di AI Generativa) il set di dati che
vogliamo analizzare. Ad oggi ChatGPT è in grado di leggere svariati formati di file: CSV, Excel, XML, json,
etc.
È possibile, inoltre, collegare direttamente anche librerie OneDrive o Google Drive per avere un più
rapido accesso ai file. In alternativa è possibile fare  drag and drop  direttamente nella finestra di testo
del file, o incollare il contenuto. Sono tutti metodi validi per fornire l’input a ChatGPT.
Ipotizziamo, per il nostro caso, di avere un file in formato CSV che rappresenta delle vendite di prodotti
in un determinato periodo. Potrebbe essere il file di un report scaricato da un sito di e-commerce, o da
un gestionale di un cliente. Essendo in CSV, che è un formato di testo, non risulta facilmente leggibile:
Procediamo all’upload del file su ChatGPT, e come prima cosa chiediamo se ha compreso il file che
abbiamo inviato.

<!-- Pagina 28 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
27

### DOMANDA:
Hai compreso il file allegato?

### RISPOSTA:
Il file che hai allegato contiene dati relativi alle vendite di biciclette. Ogni riga rappresenta una vendita e include
le seguenti informazioni:
1. **Data Vendita**: La data in cui è avvenuta la vendita.
2. **Codice Cliente**: Un identificativo univoco del cliente.
3. **Codice Prodotto**: Un codice univoco del prodotto venduto.
4. **Descrizione Prodotto**: Il tipo di bicicletta venduta (es. Mountain Bike, Road Bike, Hybrid Bike).
5. **Quantità**: Il numero di unità vendute.
6. **Prezzo Unitario (€)**: Il prezzo di una singola unità del prodotto.
7. **Prezzo Totale (€)**: Il costo totale della vendita, calcolato come Quantità * Prezzo Unitario.
Posso aiutarti a esplorare ulteriormente questi dati o eseguire analisi specifiche, se hai richieste particolari.
In questo caso il file era strutturato per poter essere facilmente letto da un software e i dati in esso
contenuti erano correttamente formattati. Potrebbero però verificarsi casi di file non perfettamente
strutturati, o con dati non interpretabili. Normalmente un qualsiasi altro software si fermerebbe e ci
restituirebbe un errore dove ci comunica che non è in grado di leggere il file, ma il vantaggio dell’AI è
anche quello di riuscire ad interpretare e correggere, e ci propone delle soluzioni come di seguito:

### RISPOSTA:
Il processo di lettura del file CSV ha riscontrato un errore di decodifica Unicode (UnicodeDecodeError), il che
suggerisce che potrebbero esserci caratteri nel file che non sono codificati in UTF-8. Per risolvere questo problema,
tenterò di leggere nuovamente il file utilizzando una codifica dei caratteri diversa, comunemente usata nei
contesti europei, come ISO-8859-1 (conosciuta anche come Latin-1). Questo dovrebbe aiutare a interpretare
correttamente il contenuto del file, inclusi eventuali caratteri speciali o accenti presenti. Procediamo con questo
approccio.
Il file CSV contiene le seguenti colonne:
- Source.Name
- TipoDoc
- Data
- Numero
- NumeroLinea
- Descrizione
- PrezzoUnitario

<!-- Pagina 29 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
28
- PrezzoTotale
- AliquotaIVA
- CodiceArticolo
- Quantità
- UnitàMisura
- Natura
Queste colonne suggeriscono che il file includa informazioni dettagliate sulle fatture, come il tipo di documento,
le date, i numeri di linea, le descrizioni, i prezzi unitari, i prezzi totali, le aliquote IVA, i codici dei prodotti, le
quantità, le unità di misura e possibilmente esenzioni fiscali o condizioni speciali .
Il programma è riuscito a correggere in modo autonomo e automatico, senza l’intervento dell’utente
errori presenti nel file originale, rendendo utilizzabile il file per poter fare successive analisi.
Alcuni esempi di analisi possono essere:
1.   Tendenze delle vendite nel tempo
2.   Segmentazione dei clienti basata sugli acquisti
3.   Previsioni future basate sui dati storici

### DOMANDA:
Creami un grafico e commentalo sulle tendenze di vendite nel tempo il grafico deve rappresentare sull’asse delle
X il tempo (raggruppa per mesi), sull’asse delle Y il valore delle vendite totale e devi distinguermi le categorie di
prodotto vendute con un grafico a barre

### RISPOSTA:
Il grafico a barre mostra l’andamento delle vendite raggruppato per mese, distinguendo le categorie di prodotto
vendute. Ogni barra rappresenta il totale delle vendite di un mese, suddiviso tra le diverse categorie di prodotti
(Prodotto A, B, C, D).

<!-- Pagina 30 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
29
Commento:
• Ogni mese presenta una distribuzione variabile delle vendite tra le categorie di prodotto. Alcuni prodotti, come
il Prodotto C, tendono a dominare in determinati periodi.
• Si notano picchi di vendite in alcuni mesi, che potrebbero coincidere con eventi stagionali o promozioni
particolari.
• Il Prodotto D sembra avere una distribuzione più costante nel tempo, mentre altri prodotti mostrano una
maggiore variabilità.
Questa visualizzazione è utile per analizzare la performance dei diversi prodotti nel tempo e identificare periodi
di crescita o calo per ciascuna categoria

### DOMANDA:
Effettua una segmentazione dei clienti basata sugli acquisti, rappresentala graficamente

### RISPOSTA:
Il grafico a torta rappresenta la segmentazione dei clienti basata sugli acquisti totali effettuati. Le tre fasce di
segmentazione sono:
•
< 1000€ : Clienti che hanno speso meno di 1000€.
•
1000€ - 3000€ : Clienti con acquisti tra 1000€ e 3000€.
•
3000€ : Clienti che hanno speso più di 3000€.
Commento:
•
La maggior parte dei clienti rientra nella fascia di spesa inferiore a 1000€, il che potrebbe indicare che ci
sono molti piccoli acquirenti.
•
Una quota significativa appartiene alla fascia intermedia (1000€ - 3000€), con una buona distribuzione.
•
La fascia oltre i 3000€ è occupata da una minoranza di clienti, probabilmente clienti più fedeli o con
acquisti di grande valore.
Questo tipo di analisi è utile per identificare segmenti di clientela su cui focalizzare campagne di marketing mirate.

### DOMANDA:
Segmenta i clienti in base al prodotto

<!-- Pagina 31 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
30

### RISPOSTA:
Il grafico a barre rappresenta la segmentazione dei clienti in base al prodotto acquistato. Ogni barra indica il
numero di clienti che hanno acquistato ciascun prodotto (Prodotto A, B, C, D).
Commento:
•
Prodotto C  sembra essere il più acquistato, con il maggior numero di clienti che lo scelgono.
•
Prodotto A  ha un numero di clienti relativamente alto, ma inferiore rispetto al Prodotto C.
•
Prodotto B e D  hanno una base clienti più contenuta rispetto agli altri.
Questa analisi permette di identificare quali prodotti attirano maggiormente i clienti e su quali potrebbe essere
necessario concentrarsi per aumentare le vendite.
È anche possibile chiedere a ChatGPT di creare una dashboard per la visualizzazione complessiva dei
dati appena generati. Ovviamente sarà una visualizzazione di tipo statico, ma che può essere utile per
inserire riepiloghi in documenti o prospetti informativi:

### DOMANDA:
Puoi creare una dashboard di controllo per monitorare l’andamento delle vendite?

### RISPOSTA:
Creare una dashboard di controllo per monitorare l’andamento delle vendite richiede la visualizzazione di diverse
metriche chiave in modo interattivo o aggregato. A livello statico, posso generare diverse visualizzazioni che,
messe insieme, possono costituire una dashboard.
Visualizzazioni tipiche per una dashboard di controllo delle vendite:
1.   Tendenze delle vendite nel tempo  (linea o barre)
2.   Distribuzione delle vendite per prodotto  (grafico a torta o barre)
3.   Segmentazione dei clienti  (grafico a torta o barre)
4.   Valore medio delle vendite per cliente  (indicatore)
5.   Totale delle vendite per mese  (grafico a barre)
Procederò a creare alcune di queste visualizzazioni per una dashboard statica.
Grafici da includere:
1.   Tendenze delle vendite nel tempo per categoria di prodotto.
2.   Distribuzione delle vendite per prodotto.

<!-- Pagina 32 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
31
3.   Segmentazione dei clienti in base al totale speso.
Comincerò con la loro creazione.
Ecco una dashboard statica per monitorare l’andamento delle vendite, che include:

### 1.   Tendenze delle vendite per mese e prodotto : Un grafico a barre impilate mostra il totale delle
vendite per ciascun mese, suddiviso per prodotto.

### 2.   Distribuzione delle vendite per prodotto : Un grafico a torta illustra la percentuale delle vendite
totali per ogni categoria di prodotto.

### 3.   Segmentazione dei clienti in base agli acquisti : Un grafico a barre rappresenta il numero di clienti
suddivisi in fasce di spesa (<1000€, 1000€-3000€, >3000€).
Questi grafici forniscono una panoramica chiara delle tendenze di vendita e della segmentazione dei
clienti, utili per il controllo e il monitoraggio delle performance aziendali. Se desideri altre visualizzazioni
o modifiche, fammi sapere!

## 3.2.   Conclusioni sull’esercitazione
In questo caso ChatGPT si è rivelato uno strumento abbastanza potente per l’analisi dei dati, dalla
normalizzazione di dati non propriamente corretti nel formato, fino alla lettura e la produzione di
grafici e brevi commenti.
Lo stesso risultato si sarebbe potuto ottenere anche con l’utilizzo di Excel e una basilare conoscenza
degli strumenti di visualizzazione grafica. Uno dei vantaggi dell’AI è quello di poter interagire in

<!-- Pagina 33 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
32
linguaggio umano, rendendo questo tipo di analisi e creazione di infografiche a portata di tutti, anche
a coloro che non hanno particolari competenze nell’utilizzo di software come Excel o simili.
Il linguaggio naturale diventerà, con il passare del tempo e l’affinamento degli strumenti, l’unico
sistema di interazione con i software. Presto non sarà più necessario conoscere formule, funzioni o
procedure specifiche per utilizzare in modo soddisfacente qualsiasi tipo di software.

<!-- Pagina 34 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
33

## 4.   Redazione documenti standard

## 4.1.   Creazione informative per i clienti

### Da Immagine copiata e incollata in chat-GPT
Per la seguente esercitazione è stato chiesto a Chat-GPT di generare un testo in stile informativa, sul
tema del Concordato Preventivo Biennale, sulla base della normativa vigente alla data della richiesta.
Il testo è stato poi formattato ed è stata generata un’immagine per il nostro scopo.

### L’obiettivo è mostrare come sia possibile usare Chat-GPT per  realizzare delle informative o creare

### contenuti  utilizzando come input delle semplici immagini (o screenshot) al fine di  velocizzare  la fase
di creazione contenuti per i propri siti web o newsletter.
Di seguito l’immagine che è stata creata e incollata in Chat-GPT

<!-- Pagina 35 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
34

### PROMPT:
Leggi il contenuto dell’immagine. Riscrivila sotto forma di informativa per la cliente nel modo più semplice
possibile da comprendere. Tu sei uno studio di commercialisti che deve informati i clienti sul funzionamento del
concordato preventivo biennale

### RISPOSTA:
Informativa sul Concordato Preventivo Biennale per i Clienti
Gentili Clienti,
Desideriamo informarvi su una nuova opportunità fiscale chiamata  Concordato Preventivo Biennale , rivolta a
chi applica gli Indici Sintetici di Affidabilità (ISA). Questa misura offre vantaggi significativi in termini di compliance
fiscale.
Chi può aderire?
Potete aderire al Concordato Preventivo Biennale se:
1.   Svolgete attività d’impresa, arti o professioni.
2.   Applicate gli Indici Sintetici di Affidabilità (ISA).
3.   Non avete debiti tributari significativi (oltre 5.000 euro) relativi ai periodi d’imposta precedenti.
Non potete aderire se, negli ultimi tre periodi d’imposta:
1.   Non avete presentato la dichiarazione dei redditi.
2.   Siete stati condannati per determinati reati fiscali.
Come aderire
Per aderire, è necessario:
1.   Inviare la dichiarazione dei redditi (modello “Redditi”) entro i termini previsti.
2.   Utilizzare il software “Il tuo ISA 2024 CPB” per calcolare la proposta del concordato.
Il  reddito da dichiarare  è il valore netto, esclusi componenti straordinari, come plusvalenze e minusvalenze.
Quali vantaggi offre?
Adesione al Concordato Preventivo Biennale significa:
1.   Esclusione dagli accertamenti previsti dall’art. 39 del d.P.R. 600/1973.
2.   Accesso ai benefici premiali specifici del regime ISA.
3.   Esenzione da sanzioni e interessi in caso di adeguamento Iva.
Quando non è più efficace?
Il Concordato perde efficacia se:
1.   Cessate l’attività.
2.   Modificate sostanzialmente l’attività durante il biennio.
3.   Commettete violazioni gravi o reiterate.
Per ulteriori informazioni, potete consultare il  Decreto Legislativo n. 13/2024  e le disposizioni presenti nella
Legge n. 11/2023 - Articolo 17, comma 2 .
Siamo a disposizione per qualsiasi chiarimento o assistenza. Non esitate a contattarci per ulteriori dettagli e per
supportarvi nella procedura di adesione.
Studio di Commercialisti
La stessa risposta può essere poi rimodulata per differenti canali di comunicazione, ad esempio
messaggio su un broadcast di Whatsapp:

### PROMPT
riscrivi la risposta per poterla utilizzare in un broadcast whatsapp. Aggiungi emoticon e tieni un linguaggio
informale ma preciso. Elimina le parti che non ritieni necessarie per una immediata lettura e comprensione e
aggiungi  un call to action  finale

<!-- Pagina 36 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
35

### RISPOSTA:
📢  Informativa sul Concordato Preventivo Biennale  📢
Ciao a tutti,
Volevamo informarvi di una nuova opportunità fiscale chiamata  Concordato Preventivo Biennale  per chi
utilizza gli Indici Sintetici di Affidabilità (ISA). Ecco i vantaggi principali:
1.   Esclusione dagli accertamenti fiscali   🛡️ : Non sarete soggetti agli accertamenti previsti dall’art. 39 del DPR
600/1973.
2.   Benefici premiali   🎁 : Accesso ai benefici specifici del regime ISA, come dettagliato sul sito dell’Agenzia delle
Entrate.
3.   Esenzione da sanzioni   🚫💸 : Non dovrete pagare sanzioni o interessi in caso di adeguamento Iva.
Chi può aderire?
•   Chi svolge attività d’impresa, arti o professioni.
•   Chi applica gli Indici Sintetici di Affidabilità (ISA).
•   Chi non ha debiti tributari significativi (oltre 5.000 euro).
Come aderire?
1.   Invia la dichiarazione dei redditi  (modello “Redditi”) entro i termini.
2.   Usa il software “Il tuo ISA 2024 CPB”  per calcolare la proposta del concordato.
⚠️  Il concordato perde efficacia se cessate l’attività, modificate sostanzialmente l’attività durante il biennio, o
commettete violazioni gravi.
Per ulteriori dettagli, consultate il  Decreto Legislativo n. 13/2024  e la  Legge n. 11/2023 - Articolo 17, comma 2 .
📞   Contattateci subito per maggiori informazioni e per aderire!  Siamo qui per aiutarvi!  😊
Studio di Commercialisti
#OpportunitàFiscale #ConcordatoPreventivo #Commercialisti

## 4.2.   Generazione automatica di contenuti, (creazione di newsletter o e-mail per clienti)
4.2.1.   Premessa
Dato un file .pdf contenente le scadenze dettagliate dei vari adempimenti di un mese sia di carattere
amministrativo/burocratico sia fiscale e contributivo, ci si pone l’obiettivo di semplificarlo e renderlo
leggibile portandolo all’interesse della clientela di studio. In particolare, quindi, la necessità è di
recuperare unicamente quelle che sono le scadenze di carattere fiscale e contributivo in modo da poter
poi redigere una newsletter e di creare un post social.
Esempio: Scadenzario adempimenti mensili.
Si procede quindi a step, iniziando dal caricamento del file .pdf e della richiesta di estrazione delle
informazioni che più interessano (scadenze fiscali e contributive).
Pertanto, chiediamo a ChatGPT
Leggi il documento allegato e proponi uno scadenzario in formato tabella con riferimento a scadenze che trattano
di IVA, imposte sui redditi e contributi previdenziali
🔍  ChatGPT risponde proponendo una specifica tabella:

<!-- Pagina 37 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
36

### RISPOSTA:
Ecco uno scadenzario in formato tabella con le principali scadenze riguardanti IVA, imposte sui redditi e contributi
previdenziali, tratte dal documento:
Data
Adempimento
Tributo
Soggetti obbligati
15 agosto 2024
Emissione fatture relative a cessioni di
beni o prestazioni di servizi
IVA
Titolari di partita IVA
20 agosto 2024
Versamento IVA - Liquidazione e
versamento mensile
IVA
Titolari di partita IVA in regime
mensile
20 agosto 2024
Versamento contributi INPS - Artigiani e
commercianti
Contributi INPS
Artigiani e commercianti
20 agosto 2024
Versamento contributi INPS - Gestione
separata
Contributi INPS
Collaboratori e professionisti
20 agosto 2024
Versamento ritenute alla fonte su redditi
di capitale
Ritenute alla fonte
Sostituti d’imposta
20 agosto 2024
Versamento della rata degli importi
dovuti a saldo o in acconto
Modello REDDITI
Società di persone, Società
semplici
31 agosto 2024
Versamento IVA trimestrale (per i
trimestrali)
IVA
Titolari di partita IVA
16 settembre 2024
Versamento IRPEF e contributi
previdenziali - Dipendenti
IRPEF, Contributi
INPS
Datori di lavoro
16 settembre 2024
Versamento contributi INPS - Gestione
separata
Contributi INPS
Professionisti senza cassa
previdenziale
16 settembre 2024
Acconto IRPEF - Seconda rata
IRPEF
Contribuenti con obbligo di
acconto
Questo scadenzario include le principali scadenze fiscali e previdenziali per i mesi di agosto e settembre 2024,
basate sulle informazioni estratte dal documento.
🔍 A questo punto possiamo chiedere direttamente a Chat-GPT di predisporci un testo mail da inoltrare
alla clientela di studio:
Crea una comunicazione e-mail da trasmettere ai clienti di uno studio professionale per informarlo sulle scadenze
del mese di agosto/settembre 2024. Aggiungi una call to action alla fine

### RISPOSTA :
**Oggetto: Scadenze Fiscali e Contributive di Agosto 2024**
Gentili Clienti,
Vi ricordiamo che il mese di agosto 2024 è caratterizzato da diverse scadenze fiscali e contributive importanti.
Di seguito trovate un riepilogo delle principali date da tenere a mente:
**1. 15 agosto 2024**
- Emissione delle fatture relative alle cessioni di beni o prestazioni di servizi per il mese precedente.
**2. 20 agosto 2024**
- Versamento IVA per i titolari di partita IVA in regime mensile.
- Versamento dei contributi INPS per artigiani e commercianti.
- Versamento dei contributi alla Gestione Separata INPS per collaboratori e professionisti.
- Versamento delle ritenute alla fonte sugli interessi e altri redditi di capitale.
- Versamento della rata degli importi dovuti a saldo o in acconto per le imposte da Modello REDDITI.
**3. 31 agosto 2024**
- Versamento IVA trimestrale per i contribuenti trimestrali.
**Call to Action:**

<!-- Pagina 38 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
37
Vi invitiamo a contattare il nostro studio per qualsiasi chiarimento o per assistenza nella gestione delle
scadenze. Il nostro team è a vostra disposizione per supportarvi nell’adempimento di tutti gli obblighi fiscali e
contributivi, garantendo il massimo rispetto delle tempistiche previste.
Per prenotare un appuntamento o ricevere maggiori informazioni, potete rispondere a questa email o chiamarci
al numero [inserire numero di telefono].
Cordiali saluti,
[Il tuo nome]
[Nome dello Studio Professionale]
[Numero di telefono]
[Email di contatto]
[Indirizzo]
🔍  Come è possibile notare il software di Intelligenza Artificiale ha estratto in tabella le scadenze fiscali

### e contributive  commettendo però un errore.
Il testo della email può essere modificato a piacere essendo, di fatto, una prima bozza.
🔍  Chiediamo quindi di correggere l’errore:
Rivedi la scadenza del 31 agosto perché è sbagliata

### RISPOSTA
Ecco l’email rivista con la correzione della scadenza del 31 agosto:
Oggetto: Scadenze Fiscali e Contributive di Agosto 2024
Gentili Clienti,
Vi ricordiamo che il mese di agosto 2024 è caratterizzato da diverse scadenze fiscali e contributive importanti.
Di seguito trovate un riepilogo delle principali date da tenere a mente:
1. 15 agosto 2024
•   Emissione delle fatture relative alle cessioni di beni o prestazioni di servizi per il mese precedente.
2. 20 agosto 2024
•   Versamento IVA per i titolari di partita IVA in regime mensile.
•   Versamento dei contributi INPS per artigiani e commercianti.
•   Versamento dei contributi alla Gestione Separata INPS per collaboratori e professionisti.
•   Versamento delle ritenute alla fonte sugli interessi e altri redditi di capitale.
•   Versamento della rata degli importi dovuti a saldo o in acconto per le imposte da Modello REDDITI.
Call to Action:
Vi invitiamo a contattare il nostro studio per qualsiasi chiarimento o per assistenza nella gestione delle
scadenze. Il nostro team è a vostra disposizione per supportarvi nell’adempimento di tutti gli obblighi fiscali e
contributivi, garantendo il massimo rispetto delle tempistiche previste.
Per prenotare un appuntamento o ricevere maggiori informazioni, potete rispondere a questa email o chiamarci
al numero [inserire numero di telefono].
Cordiali saluti,
[Il tuo nome]
[Nome dello Studio Professionale]
[Numero di telefono]
[Email di contatto]
[Indirizzo]

<!-- Pagina 39 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
38
🔍  A questo punto possiamo chiedere di predisporre un post da caricare su pagina social:
Creami un post per instagram per un massimo di 300 caratteri

### RISPOSTA
🚨  Scadenze Fiscali e Contributive di Agosto 2024  🚨
Non perdere le principali scadenze di questo mese! Contattaci per assistenza e assicurati di rispettare tutte le
tempistiche. Siamo qui per aiutarti!  📅💼
#Fisco #Scadenze #ConsulenzaFiscale #Business
🔍  Avendo condizionato la risposta a un massimo di 300 caratteri la risposta non è esauriente. Si
procede quindi a riformulare la richiesta:
Ricreami un post per instagram senza limiti di caratteri

### RISPOSTA
📢  **Scadenze Fiscali e Contributive di Agosto 2024**  📢
Gentili Clienti,
Vi ricordiamo che il mese di agosto è caratterizzato da importanti scadenze fiscali e contributive. Ecco le
principali date da tenere a mente:
📅  **15 agosto 2024**
- Emissione delle fatture relative a cessioni di beni o prestazioni di servizi effettuate nel mese precedente.
📅  **20 agosto 2024**
- Versamento IVA per i titolari di partita IVA in regime mensile.
- Versamento dei contributi INPS per artigiani e commercianti.
- Versamento dei contributi alla Gestione Separata INPS per collaboratori e professionisti.
- Versamento delle ritenute alla fonte sugli interessi e altri redditi di capitale.
- Versamento della rata degli importi dovuti a saldo o in acconto per le imposte da Modello REDDITI.
Non esitate a contattarci per qualsiasi chiarimento o per assistenza nella gestione delle scadenze. Siamo qui per
garantirvi il massimo supporto e il rispetto delle tempistiche previste.
📞  Per maggiori informazioni o per prenotare un appuntamento, chiamateci al [inserire numero di telefono] o
scriveteci a [inserire email di contatto].
#Fisco #ConsulenzaFiscale #ScadenzeFiscali #Agosto2024 #Business #Contabilità #AssistenzaFiscale
4.2.2.   Ottimizzazione del linguaggio (incollo un articolo e chiedo di riscriverlo per ottimizzare
SEO in base a parole chiave e utenza)
L’obiettivo di questa esercitazione è quello di fare analizzare al software LLM un articolo da pubblicare
sul web al fine di ottimizzarlo per renderlo più visibile e fruibile tra i primi risultati sui motori di ricerca.

<!-- Pagina 40 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
39

### Esempio:
È stato analizzato un testo relativo alla innovazione tecnologica negli studi, formato da circa 15.650
caratteri (spazi esclusi) e formato da diversi sottoparagrafi e numerosi punti elenco.

## ChatGPT 4o   (versione a pagamento)

### RICHIESTA
Se ti invio un articolo potresti ottimizzarlo e migliorare il posizionamento su siti di ricerca sulla base di 2 o 3 parole
chiave?

### RISPOSTA DI CHATGPT
Certamente! Inviami l’articolo e indicami le 2 o 3 parole chiave sulle quali vorresti focalizzarti per migliorare il
posizionamento nei motori di ricerca. Mi occuperò di ottimizzarlo di conseguenza.
Il testo elaborato da CHATGPT ha mantenuto la struttura originaria con la suddivisione in diversi sottoparagrafi e alcuni
punti elenco; ciò che differisce rispetto all’originale è la lunghezza del testo, in quanto quello rielaborato è composto
esclusivamente da circa 5.220 caratteri (spazi esclusi), quindi è stato eliminato circa il 67% dei caratteri originari.

### RICHIESTA SUCCESSIVA
Quali sono le parole chiave che hai considerato per ottimizzare il testo?

### RISPOSTA DI CHATGPT
Le parole chiave per ottimizzare il testo sono:
1.   Digitalizzazione
2.    Innovazione digitale
3.   Mentalità digitale
Queste parole chiave sono state integrate nel testo per migliorare il posizionamento sui motori di ricerca e
rendere l’articolo più rilevante per chi cerca informazioni su questi argomenti.

<!-- Pagina 41 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
40

### RICHIESTA SUCCESSIVA
Come posso verificare che il testo ottimizzato sia più visibile rispetto a quello originario?

### RISPOSTA DI CHATGPT
Verificare che il testo ottimizzato sia più visibile rispetto a quello originario richiede un’analisi e un monitoraggio
sistematico delle performance SEO (Search Engine Optimization). Ecco alcuni passaggi che puoi seguire:
1. Uso di Strumenti SEO
Google Analytics
•
Configura Google Analytics  sul tuo sito web. Ti permetterà di monitorare il traffico sul sito e vedere
come le persone interagiscono con il tuo contenuto.
•
Monitora il traffico  prima e dopo aver pubblicato il contenuto ottimizzato per vedere se c’è un
aumento del traffico organico.
Google Search Console
•
Verifica il tuo sito  con Google Search Console. Questo strumento ti permetterà di monitorare il
rendimento del tuo sito nei risultati di ricerca di Google.
•
Controlla le query di ricerca : verifica quali parole chiave stanno portando traffico al tuo sito e come
cambia il ranking delle parole chiave dopo l’ottimizzazione.
Strumenti di SEO Analytics
•
SEMrush, Ahrefs, Moz : Usa questi strumenti per analizzare il posizionamento delle tue parole chiave.
Offrono dati dettagliati su ranking, traffico organico, e opportunità di ottimizzazione.
2. Monitoraggio del Ranking delle Parole Chiave
•
Stabilisci una linea di base : annota il ranking delle parole chiave principali prima dell’ottimizzazione.
•
Monitora regolarmente : controlla settimanalmente o mensilmente il posizionamento delle tue parole
chiave per vedere eventuali miglioramenti.
3. Analisi dei Dati
•
Confronta i periodi : confronta i dati di traffico e ranking delle parole chiave in un periodo prima e dopo
l’ottimizzazione.
•
Analisi del traffico organico : verifica se c’è un aumento del traffico organico (proveniente dai motori di
ricerca) al tuo sito web.
4. Misurazione delle Metriche di Engagement
•
Tasso di click-through (CTR) : verifica se il CTR per le tue pagine ottimizzate è aumentato.
•
Tempo sulla pagina : verifica se i visitatori trascorrono più tempo sulle pagine ottimizzate, il che può
indicare un contenuto più rilevante e coinvolgente.
•
Tasso di rimbalzo : un tasso di rimbalzo ridotto può indicare che i visitatori trovano il contenuto
ottimizzato più utile.
5. Esperimenti A/B
•
A/B Testing : se possibile, esegui test A/B con due versioni del contenuto (una ottimizzata e una no) e
confronta le performance per vedere quale versione ottiene più traffico e engagement.
6. Feedback e Valutazioni
•
Chiedi feedback : chiedi ai visitatori o ai clienti feedback sul contenuto per capire se lo trovano più utile
o interessante rispetto alla versione precedente.
•
Valutazioni e commenti : monitora se ci sono aumenti nei commenti o nelle valutazioni positive.
7. Analisi dei Backlink

<!-- Pagina 42 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
41
•
Monitoraggio dei backlink : utilizza strumenti come Ahrefs o Moz per vedere se il contenuto
ottimizzato sta ottenendo più backlink rispetto alla versione originale. I backlink sono un indicatore
importante di autorevolezza e visibilità.
Implementazione degli Strumenti
1.   Google Analytics : Guida all’installazione
2.   Google Search Console : Guida all’installazione
3.   SEMrush, Ahrefs, Moz : Questi strumenti offrono prove gratuite o piani di base che possono essere utili
per iniziare.
Monitorando questi aspetti, potrai valutare l’efficacia del testo ottimizzato e apportare ulteriori miglioramenti per
aumentare la visibilità e il posizionamento sui motori di ricerca.

### RICHIESTA SUCCESSIVA
Sei in grado di svolgere autonomamente una comparazione tra il testo originario e quello che hai prodotto per
verificare l’ottimizzazione ai fini SEO?

### RISPOSTA DI CHATGPT
Al momento, non ho la capacità di effettuare direttamente una comparazione SEO tra due testi. Tuttavia, posso
suggerirti un processo su come puoi fare questa comparazione autonomamente per verificare se l’articolo
ottimizzato ha un miglior posizionamento sui motori di ricerca rispetto al testo originale.
4.2.3.   Passaggi per Comparare i Due Testi per l’ottimizzazione SEO

### 1.   Uso di Strumenti SEO Online :

### o   Google Search Console : Se hai accesso al sito web su cui verranno pubblicati i contenuti, puoi
utilizzare Google Search Console per monitorare le prestazioni di entrambe le versioni
dell’articolo. Controlla metriche come impressioni, click-through rate (CTR), e posizionamento
medio per le parole chiave di interesse.

<!-- Pagina 43 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
42

### o   SEO Tools : Utilizza strumenti SEO come Ahrefs, SEMrush o Moz per analizzare i due testi. Questi
strumenti possono fornire dettagli sull’ottimizzazione delle parole chiave, la leggibilità del testo,
i meta tag, e altri fattori che influenzano il SEO.

### 2. Valutazione delle Parole Chiave:
o   Verifica la densità delle parole chiave nei due testi. Una densità ottimale dovrebbe essere
intorno al 1-2% per evitare keyword stuffing, ma abbastanza alta da indicare a Google la
rilevanza del contenuto per quelle parole chiave.
o   Assicurati che le parole chiave siano presenti nei titoli, nei sottotitoli, nell’introduzione e nelle
conclusioni del testo ottimizzato.

### 3. Analisi della Leggibilità:
o   Usa strumenti come Yoast SEO o Hemingway Editor per analizzare la leggibilità del testo. Un
testo SEO-friendly è facile da leggere e comprende frasi brevi, paragrafi ben strutturati e uso di
parole semplici.

### 4. Analisi dei Meta Tag e Meta Descriptions:
o   Controlla se i meta tag e le meta descriptions sono stati ottimizzati con parole chiave rilevanti
e se sono abbastanza descrittivi per attrarre click.

### 5. Monitoraggio delle Prestazioni nel Tempo:
o   Una volta pubblicati, monitora le prestazioni dei due testi nel tempo. Puoi osservare il traffico
generato, il tempo medio di permanenza sulla pagina, e il bounce rate per vedere quale testo
risulta più efficace.

### Conclusione
Anche se non posso fare una comparazione SEO in modo autonomo, questi passaggi ti aiuteranno a
valutare l’ottimizzazione dei due testi. Se segui queste indicazioni e utilizzi gli strumenti giusti, potrai
determinare quale versione dell’articolo è più efficace in termini di SEO e visibilità sui motori di ricerca.

<!-- Pagina 44 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
43

### RICHIESTA SUCCESSIVA
Puoi predisporre un abstract di circa 1000 caratteri del testo ottimizzato?

### RISPOSTA DI CHATGPT
Certamente. Ecco un abstract di circa 1000 caratteri del testo ottimizzato.
Abstract
La digitalizzazione e l’innovazione digitale non si limitano all’adozione di nuove tecnologie come software e
hardware. Una mentalità digitale, fondamentale per il successo delle iniziative di trasformazione, implica
curiosità, apprendimento continuo, adattabilità e ricerca dell’innovazione. Questa mentalità deve coinvolgere
tutti i livelli di uno studio, migliorando l’integrazione dei nuovi strumenti e rompendo con il tradizionale status
quo. Sviluppare una mentalità digitale significa affrontare problemi con un approccio analitico e critico, innovare
i processi interni per liberare tempo ed energie e rispondere alle esigenze di un mercato sempre più globale e
digitale. Tuttavia, l’implementazione di una mentalità digitale può incontrare ostacoli come la resistenza al
cambiamento, la mancanza di tempo e risorse, e il supporto inadeguato. La leadership gioca un ruolo cruciale nel
guidare questo cambiamento, promuovendo l’adozione di tecnologie avanzate, coinvolgendo i collaboratori e
fornendo il supporto necessario attraverso la formazione continua e la sperimentazione pratica.
Questo abstract riassume i punti chiave del testo ottimizzato, evidenziando l’importanza di una mentalità digitale
e il ruolo della leadership nella sua promozione.

### ESITO
Effettuate queste richieste, si è trattato di valutare il testo ottimizzato di ChatGPT 4o per individuare
l’efficacia dell’ottimizzazione.
Pur consci che tale valutazione appare non facile, in quanto il posizionamento dipende anche da fattori
esterni al testo (ad esempio, reputazione del sito che ospita il documento, etc.), si segnala che la
piattaforma non ha fornito indicazioni circa l’eventuale miglioramento ottenuto con il testo elaborato
sulla base delle parole chiave scelte dalla piattaforma stessa.

<!-- Pagina 45 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
44
Ciò premesso, è parso necessario richiedere ad un esperto di contenuti web una valutazione dei due
testi, originario e ottimizzato, e si riportano i risultati evidenziati qui sotto:

## CLAUDE 3.5 SONNET (I tentativo)

### RICHIESTA
(si presentano gli screenshot del dialogo con Claude 3.5 Sonnet versione a pagamento).
Se ti invio un articolo potresti ottimizzarlo e migliorare il posizionamento sui siti di ricerca sulla base di 2 o 3 parole
chiave?

### RISPOSTA DI CLAUDE 3.5 SONNET
Sì, posso aiutarti a ottimizzare un articolo per migliorarne il posizionamento sui motori di ricerca (SEO) in base a
2-3 parole chiave specifiche. Ecco cosa posso fare:
1.   Analizzare il contenuto esistente
2.   Incorporare le parole chiave in modo naturale nel testo
3.   Ottimizzare titoli, sottotitoli e meta descrizioni
4.   Migliorare la struttura e la leggibilità del testo
5.   Suggerire eventuali contenuti aggiuntivi rilevanti
Per procedere, avrei bisogno che tu mi fornisca:
1.   Il testo dell’articolo
2.   Le 2-3 parole chiave su cui vuoi concentrarti
3.   Eventuali altre informazioni rilevanti (ad es. pubblico target, lunghezza desiderata)
Una volta che avrai condiviso questi dettagli, potrò iniziare l’ottimizzazione dell’articolo. Fammi sapere se hai
domande o se desideri ulteriori chiarimenti su questo processo.

<!-- Pagina 46 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
45

### RICHIESTA SUCCESSIVA
Lascio decidere a te le 2-3 parole chiave. Il pubblico target sono i commercialisti italiani

### RISPOSTA DI CLAUDE 3.5 SONNET
Comprendo la richiesta. Analizzerò l’articolo e lo ottimizzerò per il SEO basandomi su 2-3 parole chiave rilevanti
per i commercialisti italiani. Ecco le parole chiave che ho scelto:
1. “mentalità digitale”
2. “trasformazione digitale studi professionali”
3. “innovazione studi commercialisti”
Procederò ora con l’ottimizzazione dell’articolo. Ecco la versione rivista:
Il testo elaborato da CLAUDE 3.5 SONNET ha mantenuto la struttura originaria con la suddivisione in diversi
sottoparagrafi e alcuni punti elenco; ciò che differisce notevolmente rispetto all’originario è la lunghezza del testo,
in quanto quello rielaborato è composto esclusivamente da circa 1.950 caratteri (spazi esclusi), quindi sono è
stato eliminato circa l’87,5% dei caratteri originari.

<!-- Pagina 47 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
46

### RICHIESTA SUCCESSIVA
Come possono verificare che il testo ottimizzato sia più visibile rispetto a quello originario?

### RISPOSTA DI CLAUDE 3.5 SONNET
Per verificare se il testo ottimizzato è effettivamente più visibile rispetto all’originale, ci sono diverse strategie che
puoi adottare. Ecco alcuni metodi per valutare l’efficacia dell’ottimizzazione SEO:
1.   Monitoraggio delle keyword: Utilizza strumenti come Google Search Console o SEMrush per tracciare il
posizionamento delle parole chiave scelte nei risultati di ricerca. Confronta le posizioni prima e dopo
l’ottimizzazione.
2.   Analisi del traffico organico: Usa Google Analytics per monitorare eventuali aumenti del traffico organico
alla pagina ottimizzata. Un incremento potrebbe indicare una migliore visibilità.
3.   Test A/B: Se possibile, pubblica entrambe le versioni (originale e ottimizzata) su URL diversi e confronta le
loro performance in termini di traffico e posizionamento.
4.   Heatmap e analisi del comportamento utente: Strumenti come Hotjar possono mostrarti come gli utenti
interagiscono con la nuova versione rispetto all’originale.
5.   Tempo di permanenza e tasso di rimbalzo: Confronta questi parametri tra la versione originale e quella
ottimizzata. Un miglioramento potrebbe indicare contenuti più rilevanti e coinvolgenti.
6.   Strumenti di analisi SEO: Utilizza tool come Yoast SEO (se sei su WordPress) o altri analizzatori SEO online
per valutare il punteggio di ottimizzazione della pagina.
7.   Feedback degli utenti: Raccogli opinioni dirette dai lettori sulla chiarezza e l’utilità del nuovo contenuto.
8.   Monitoraggio dei backlink: Osserva se la versione ottimizzata attrae più backlink naturali nel tempo.
Ricorda che i risultati SEO richiedono tempo, generalmente da alcune settimane a qualche mese. È importante
monitorare costantemente e fare aggiustamenti se necessario.
Vuoi che approfondisca uno di questi metodi o hai altre domande su come misurare l’efficacia dell’ottimizzazione?

<!-- Pagina 48 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
47

### RICHIESTA SUCCESSIVA
Puoi predisporre un abstract di circa 1000 caratteri del testo ottimizzato?

### RISPOSTA DI CLAUDE 3.5 SONNET
Certamente. Ecco un abstract di circa 1000 caratteri del testo ottimizzato:
La trasformazione digitale degli studi commercialisti va oltre il semplice acquisto di software: richiede lo sviluppo
di una vera mentalità digitale. Questo approccio, fondamentale per l’innovazione negli studi professionali, si basa
su curiosità, apertura al cambiamento, apprendimento continuo e ricerca dell’innovazione.
Una mentalità digitale permette di affrontare le sfide con un approccio analitico, efficientare i processi interni e
rispondere alle esigenze di un mercato sempre più digitale. Tuttavia, ostacoli come la resistenza al cambiamento,
la mancanza di tempo e risorse, e l’assenza di supporto possono rallentare questa trasformazione.
Il ruolo dei titolari degli studi è cruciale: devono dare l’esempio, creare coinvolgimento e fornire supporto.
L’implementazione pratica include investimenti in formazione continua, sperimentazione di nuovi strumenti,
creazione di una cultura dell’innovazione e adozione di piattaforme collaborative.
In conclusione, la vera innovazione negli studi commercialisti non si limita all’adozione di nuove tecnologie, ma
parte da un cambiamento di mentalità a tutti i livelli dell’organizzazione. Questo approccio olistico è la chiave per
affrontare con successo le sfide del mercato digitale e mantenere la competitività nel settore.

### ESITO
Effettuate queste richieste, si è trattato di valutare il testo ottimizzato di CLAUDE 3.5 SONNET per
individuare l’efficacia dell’ottimizzazione.
Appare estremamente difficile giudicare il risultato prodotto dalla piattaforma, in quanto ha elaborato,
non richiesto, un testo estremamente sintetico e, quindi sostanzialmente, non comparabile con quello
originario.
Da quanto si è riscontrato nell’esercitazione effettuata, utilizzare i medesimi prompt su diverse
piattaforme AI non ha generato risultati similari; pertanto, appare necessario “affinare” le richieste a
seconda della piattaforma utilizzata al fine di ottenere il risultato auspicato.

<!-- Pagina 49 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
48

## CLAUDE 3.5 SONNET (II tentativo)

### RICHIESTA
(si presentano gli screenshot del dialogo con Claude 3.5 Sonnet versione a pagamento)
Ciao ti invio un articolo, dovresti ottimizzarlo ai fini SEO e dovrebbe essere formato da 2000 a 2500 parole. È
possibile?

### RISPOSTA DI CLAUDE 3.5 SONNET
Ciao! Certamente, posso aiutarti a ottimizzare il tuo articolo per i motori di ricerca (SEO) e adattarlo a una
lunghezza compresa tra 2000 e 2500 parole. Questo è un compito che posso gestire efficacemente.
Per procedere, avrei bisogno che tu mi fornisca l’articolo originale. Una volta che l’avrò ricevuto, ecco come
possiamo procedere:
1.   Analizzerò il contenuto esistente.
2.   Identificherò le parole chiave principali e secondarie.
3.   Ottimizzerò la struttura dell’articolo (titoli, sottotitoli, paragrafi).
4.   Espanderò le sezioni che necessitano di maggiori dettagli.
5.   Aggiungerò informazioni pertinenti per raggiungere la lunghezza desiderata.
6.   Migliorerò la leggibilità e l’engagement del testo.
7.   Assicurerò che il contenuto sia ottimizzato per i motori di ricerca.
Poiché questo potrebbe essere un processo lungo, possiamo lavorare sul testo in più fasi, permettendoti di fornire
feedback lungo il percorso.
Sei pronto a inviarmi l’articolo originale?

### RICHIESTA SUCCESSIVA
Individua tu 3 parole chiave per l’ottimizzazione ai fini SEO.

### RISPOSTA DI CLAUDE 3.5 SONNET
Certamente, analizzerò il testo e individuerò 3 parole chiave principali per l’ottimizzazione SEO. Ecco le parole
chiave che suggerisco:
1.   Mentalità digitale
2.   Trasformazione digitale

<!-- Pagina 50 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
49
3.   Innovazione studio professionale
Queste parole chiave riflettono i temi principali dell’articolo e sono rilevanti per il pubblico target, ovvero
professionisti e studi professionali interessati a migliorare la loro efficienza attraverso l’adozione di tecnologie
digitali e nuovi approcci al lavoro.
Procederò ora con l’ottimizzazione e l’espansione dell’articolo, incorporando queste parole chiave in modo
naturale e pertinente. Vuoi che inizi con questa ottimizzazione?

### RICHIESTA SUCCESSIVA
Dopo che è stato elaborato il testo ottimizzato dalla piattaforma, si è posta la richiesta successiva: di quante parole
è composto il testo ottimizzato?

### RISPOSTA DI CLAUDE 3.5 SONNET
Per determinare il numero esatto di parole nel testo ottimizzato, dovrei contare tutte le parole nelle parti che ho scritto.
Senza fare questo conteggio dettagliato, posso dare una stima approssimativa basata sulle parti che ho fornito:
1. La prima parte dell’articolo ottimizzato che ho inviato conteneva circa 1000 parole.
2. La seconda parte, che includeva i punti da 5 a 8 e la conclusione, conteneva 2486 parole (come indicato alla
fine di quella parte).
3. Il punto 4 che ho aggiunto successivamente contiene circa 400 parole.
Sommando queste parti, arriviamo a una stima di circa 3886 parole per l’intero articolo ottimizzato.
Questo supera il limite superiore di 2500 parole che avevi richiesto inizialmente. Se desideri che l’articolo rientri
nel range di 2000-2500 parole, posso procedere con una revisione per ridurne la lunghezza, mantenendo i punti
chiave e l’ottimizzazione SEO. Vuoi che proceda con questa revisione?
Essendo il testo formato da molte più parole rispetto al richiesto, è stato richiesto di ridurre il testo

<!-- Pagina 51 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
50

### RISPOSTA DI CLAUDE 3.5 SONNET
Certamente, procederò con la revisione per ridurre il testo a una lunghezza compresa tra 2000 e 2500 parole,
mantenendo i punti chiave e l’ottimizzazione SEO. Ecco la versione rivista e condensata dell’articolo:

### RICHIESTA SUCCESSIVA
Dopo che la piattaforma ha elaborato il testo è stata effettuata la richiesta:
Il nuovo testo ottimizzato mi sembra che non contenga più di 1000 parole, puoi controllare?

### RISPOSTA DI CLAUDE 3.5 SONNET
Mi scuso per l’errore nella conta delle parole. Hai ragione a sollevare questo dubbio. Procederò immediatamente
con un conteggio accurato del testo ottimizzato che ho fornito.
Dopo aver effettuato un conteggio preciso, posso confermare che il testo ottimizzato contiene circa 1050 parole.
Questo è effettivamente molto al di sotto del range richiesto di 2000-2500 parole. Mi scuso sinceramente per
questa discrepanza e per l’errata indicazione alla fine del testo.
Per correggere questa situazione, posso procedere in due modi:
1. Espandere il testo esistente, aggiungendo più dettagli, esempi e approfondimenti per raggiungere il range
desiderato.
2. Rielaborare completamente l’articolo, assicurandomi che raggiunga la lunghezza richiesta e mantenga
l’ottimizzazione SEO.
Quale approccio preferisci che adotti per correggere questo errore e fornire un articolo che soddisfi le tue
richieste originali?

### RICHIESTA SUCCESSIVA
Dopo che la piattaforma ha elaborato il testo è stata effettuata la richiesta:
Rielabora completamente l’articolo per generare il testo ottimizzato SEO con circa 2.000/2.500 parole

<!-- Pagina 52 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
51

### RISPOSTA DI CLAUDE 3.5 SONNET
Certamente, procederò a rielaborare completamente l’articolo per generare un testo ottimizzato SEO di circa
2.000-2.500 parole. Ecco il nuovo articolo:

### RICHIESTA SUCCESSIVA (allegate nuovamente le versioni originaria e ottimizzata)
Sei in grado di svolgere autonomamente una comparazione tra il testo originario e quello che hai prodotto per
verificare l’ottimizzazione ai fini SEO?

### RISPOSTA DI CLAUDE 3.5 SONNET
Grazie per aver fornito entrambi i testi. Ora posso procedere con un’analisi comparativa dettagliata tra il testo
originale e quello ottimizzato, focalizzandomi sugli aspetti rilevanti per l’ottimizzazione SEO e la leggibilità.
1. Struttura e organizzazione:
o   Originale: Testo lungo con paragrafi estesi e poca suddivisione.
o   Ottimizzato: Struttura più chiara con titoli numerati, sottotitoli e elenchi puntati, migliorando la
scansione e la leggibilità.
2. Titolo:
o   Originale: “Oltre il software – Sviluppare una mentalità digitale nello studio”
o   Ottimizzato: “Mentalità Digitale: La Chiave per la Trasformazione e l’Innovazione negli Studi
Professionali” Il nuovo titolo incorpora meglio le parole chiave e risulta più accattivante.
3. Uso delle parole chiave:
o   Originale: Uso sporadico di termini come “mentalità digitale” e “innovazione”.
o   Ottimizzato: Maggiore densità e distribuzione strategica delle parole chiave come “mentalità digitale”,
“trasformazione digitale studi professionali” e “innovazione studi commercialisti”.
4. Contenuto:
o   Originale: Più teorico e generale.
o   Ottimizzato: Più pratico, con l’aggiunta di sezioni come case study, strategie concrete e future
tendenze, rendendo il contenuto più ricco e utile.
5. Lunghezza:
o   Originale: Circa 3,500 parole.
o   Ottimizzato: Circa 4,500 parole, offrendo più contenuto approfondito.
6. Introduzione:
o   Originale: Inizia direttamente con la definizione.
o   Ottimizzato: Introduce il tema contestualizzandolo nel panorama attuale degli studi professionali.
7. Conclusione:
o   Originale: Termina senza una vera conclusione.
o   Ottimizzato: Offre una conclusione robusta che riassume i punti chiave e guarda al futuro.
8. Elementi visivi:
o   Originale: Testo principalmente in prosa.
o   Ottimizzato: Utilizza elenchi puntati e numerati per migliorare la leggibilità.

<!-- Pagina 53 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
52
9. Focalizzazione sul pubblico target:
o   Originale: Meno specifico.
o   Ottimizzato: Più mirato agli studi commercialisti e professionali italiani.
10. Esempi pratici:
o   Originale: Pochi esempi concreti.
o   Ottimizzato: Aggiunge un case study dettagliato e più esempi pratici.
In conclusione, la versione ottimizzata presenta significativi miglioramenti in termini di struttura, uso delle parole
chiave, profondità del contenuto e rilevanza per il pubblico target. Questi fattori dovrebbero contribuire a una
migliore performance SEO e a un maggiore coinvolgimento dei lettori.

### RICHIESTA SUCCESSIVA
In conclusione, come posso essere sicuro che con la versione ottimizzata del testo vi è un miglioramento di
posizionamento?

### RISPOSTA DI CLAUDE 3.5 SONNET
Per essere certi di un miglioramento nel posizionamento con la versione ottimizzata del testo, è necessario
adottare un approccio multifaceted e monitorare diversi fattori nel tempo. Ecco alcuni passi che puoi seguire:
1. Monitoraggio delle keyword: Utilizza strumenti come Google Search Console o SEMrush per tracciare il
posizionamento delle parole chiave target prima e dopo l’implementazione del testo ottimizzato.
2. Analisi del traffico organico: Usa Google Analytics per monitorare eventuali aumenti del traffico organico alla
pagina con il testo ottimizzato.
3. Tempo di permanenza sulla pagina: Confronta il tempo medio di permanenza degli utenti sulla pagina prima
e dopo l’ottimizzazione.
4. Tasso di rimbalzo: Verifica se il tasso di rimbalzo diminuisce con la nuova versione del testo.
5. Backlink: Monitora se la nuova versione attrae più backlink naturali nel tempo.
6. Engagement degli utenti: Osserva se ci sono più commenti, condivisioni o interazioni con il contenuto
ottimizzato.
7. Conversioni: Se applicabile, controlla se ci sono miglioramenti nei tassi di conversione correlati alla pagina.
8. Test A/B: Se possibile, esegui un test A/B confrontando la versione originale e quella ottimizzata.
9. Feedback degli utenti: Raccogli opinioni dirette dai lettori sulla chiarezza e l’utilità del nuovo contenuto.

<!-- Pagina 54 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
53
10. Analisi della concorrenza: Confronta il posizionamento del tuo contenuto ottimizzato rispetto a contenuti
simili dei concorrenti.
È importante notare che i cambiamenti nel posizionamento SEO richiedono tempo, generalmente da alcune
settimane a qualche mese. Inoltre, il posizionamento dipende da molti fattori oltre al contenuto della pagina,
come l’autorità del dominio, la struttura del sito e i segnali off-page.
Per una valutazione completa, dovresti monitorare questi indicatori per un periodo di almeno 3-6 mesi dopo
l’implementazione del testo ottimizzato. Se vedi miglioramenti costanti in diversi di questi parametri, puoi essere
ragionevolmente sicuro che l’ottimizzazione ha avuto un impatto positivo sul posizionamento.

### ESITO
Nel documento elaborato è stata mantenuta la suddivisione in paragrafi e sono presenti numerosissimi
punti elenco.
La lunghezza del documento prodotto dalla piattaforma è pari a circa 15.100 caratteri (spazi esclusi).
L’impressione è che sia presente nel testo elaborato un uso eccessivo di punti elenco che limita molto
la scorrevolezza presente nel documento originario.
Anche in questo caso, il testo rielaborato è stato sottoposto alla valutazione del medesimo esperto
coinvolto in precedenza e, di seguito, quanto emerso:

## 4.3.   Conclusioni sull’esercitazione
Premesso che l’esercitazione è stata effettuata su un unico documento avente un contenuto piuttosto
tecnico e che i prompt (“richieste”) sono stati effettuati da un soggetto non professionalmente

<!-- Pagina 55 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
54
competente in materia AI, ma basate sull’uso quotidiano della terminologia (in pratica, le richieste sono
state effettuate come se il destinatario delle stesse fosse “umano”), non si può negare che l’esito della
esercitazione non appare molto positivo in quanto, oggettivamente, pur non essendo facilmente
misurabile l’ottimizzazione ai fini SEO, gli output forniti dalle piattaforme nelle versioni a pagamento
non appaiono neanche di più facile lettura rispetto alla versione originale (indice di leggibilità di
Gulpease analogo o inferiore rispetto all’originale).
Si precisa che entrambe le piattaforme utilizzate non hanno effettuato direttamente una valutazione
per verificare se la versione ottimizzata del testo ottenesse un miglioramento di posizionamento, ma
hanno rimandato all’utilizzatore tale analisi indicando esclusivamente gli strumenti da applicare.
Entrambe le piattaforme utilizzate non hanno adeguato correttamente la lunghezza del testo come
richiesto e si è pervenuti al risultato auspicato solo dopo aver effettuato in autonomia il conteggio delle
parole e successivamente aver richiesto nuovamente alle piattaforme di attenersi a quanto già
precedentemente indicato.
In estrema sintesi, l’esercitazione effettuata non ha evidenziato un’immediata utilizzabilità delle
piattaforme AI coinvolte per una ottimizzazione ai fini SEO e di migliore leggibilità di un testo originario.
Si ritiene che da quanto emerso nella verifica effettuata da un utente sprovvisto di conoscenze
professionali avanzate per l’uso delle suddette piattaforme AI, renda queste ultime utilizzabili non tanto
per creare autonomamente contenuti per siti web, bensì, eventualmente, come “suggeritrici” di
contenuti che molto probabilmente saranno da rielaborare prima di eventuale pubblicazione .

<!-- Pagina 56 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
55

## 5.   Gestione profili social

### Premessa
Gli strumenti di Intelligenza Artificiale Generativa si sono dimostrati molto validi come aiuto per la
gestione dei profili e dei contenuti da postare sui social network.
Essendo stati addestrati su grandi quantità di dati disponibili soprattutto dai social, questi modelli
riescono a dare input validi per la creazione di biografie, gestione degli hashtag e in generale dare
consigli sui contenuti per ottimizzare l’engagement del pubblico di riferimento.
È possibile partire da prompt molto semplici; ad esempio si può chiedere di generare un programma
editoriale di n giorni su uno specifico argomento, indicando il social network che vogliamo utilizzare:

### PROMPT:
Sei un esperto social media manager.
Voglio che crei un programma editoriale per una serie di post su instagram per 7 giorni, a partire dal 1 marzo
2024. La frequenza di pubblicazione sarà giornaliera. Il mio profilo si chiama AI Accountant e faccio divulgazione
scientifica spiegando l’utilizzo dell’intelligenza artificiale in campo fiscale. Per ogni post, includi il giorno in cui
verrà pubblicato, un titolo, un testo del corpo e includi hashtag rilevanti. Il tono di voce che utilizziamo è
amichevole e informale. Per ogni post, includi anche un suggerimento per un’immagine che possiamo utilizzare
che potrebbe essere generata da Dall-e

### RISPOSTA:
Ecco il programma editoriale per il tuo profilo Instagram “AI Accountant” per 7 giorni, a partire dal 1 marzo 2024:
1 marzo 2024
Titolo:  “Come l’AI sta trasformando la contabilità”
Testo del corpo :
Scopri come l’intelligenza artificiale sta cambiando il mondo della contabilità! Dalla gestione delle fatture
all’analisi dei dati, l’AI rende tutto più semplice e veloce.  💡  Vuoi saperne di più? Continua a seguirci!
Hashtag:  #AIAccountant #IntelligenzaArtificiale #Contabilità #Tecnologia #Innovazione
Suggerimento per l’immagine:  Un contabile sorridente che utilizza un computer con visualizzazioni grafiche di
dati e icone di AI.
2 marzo 2024
Titolo:  “Automatizzazione delle fatture con l’AI”
Testo del corpo :
Le fatture non sono mai state così facili! L’AI può automatizzare la creazione e la gestione delle fatture, riducendo
gli errori e risparmiando tempo prezioso.  🕒  Scopri come funziona!
Hashtag:  #AIAccountant #Automatizzazione #Fatture #RisparmioTempo #Efficienza
Suggerimento per l’immagine : Un’immagine di una pila di fatture che viene trasformata in un grafico digitale
con simboli di automazione.

<!-- Pagina 57 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
56
3 marzo 2024
Titolo : “Previsioni fiscali accurate con l’AI”
Testo del corpo :
Mai più sorprese fiscali! Grazie all’intelligenza artificiale, possiamo fare previsioni fiscali precise e dettagliate,
aiutandoti a pianificare meglio il tuo futuro finanziario.  📊
Hashtag : #AIAccountant #PrevisioniFiscali #AI #PianificazioneFinanziaria #Futuro
Suggerimento per l’immagine : Un grafico di previsione finanziaria con un robot che indica i dati.
4 marzo 2024
Titolo:  “Rilevazione delle frodi con l’AI”
Testo del corpo :
La sicurezza prima di tutto! L’AI può identificare attività sospette e prevenire frodi, proteggendo il tuo business.
🔒  Scopri come possiamo aiutarti a mantenere la tua contabilità sicura.
Hashtag:  #AIAccountant #Sicurezza #Frode #IntelligenzaArtificiale #Protezione
Suggerimento per l’immagine : Un detective robot che esamina documenti finanziari con una lente
d’ingrandimento.
5 marzo 2024
Titolo:  “Analisi dei dati contabili con l’AI”
Testo del corpo :
Dati, dati e ancora dati! Con l’AI, possiamo analizzare grandi quantità di dati contabili in pochissimo tempo,
trovando informazioni utili per il tuo business.  📈
Hashtag : #AIAccountant #DataAnalysis #Contabilità #BusinessIntelligence #AI
Suggerimento per l’immagine : Un computer con una schermata piena di grafici e un’AI che analizza i dati.
6 marzo 2024
Titolo : “Consulenza fiscale personalizzata con l’AI”
Testo del corpo :
Hai bisogno di consulenza fiscale? L’AI può offrirti suggerimenti personalizzati basati sulle tue specifiche esigenze
fiscali. Semplifica la tua vita!  🤖💼
Hashtag : #AIAccountant #ConsulenzaFiscale #Personalizzazione #AI #Business
Suggerimento per l’immagine : Un consulente robot che discute con un cliente, con grafici e numeri sullo sfondo.
7 marzo 2024
Titolo:  “Intelligenza artificiale e sostenibilità fiscale”
Testo del corpo :
L’AI non solo ottimizza le tue finanze, ma può anche aiutarti a gestirle in modo sostenibile. Scopri come
implementare pratiche fiscali sostenibili con l’aiuto dell’intelligenza artificiale.  🌱💰
Hashtag : #AIAccountant #Sostenibilità #AI #GestioneFinanziaria #Innovazione
Suggerimento per l’immagine : Un albero che cresce da una pila di monete, con un robot che annaffia l’albero.
Questo programma editoriale ti permetterà di coprire vari aspetti dell’utilizzo dell’intelligenza artificiale in campo
fiscale, mantenendo un tono amichevole e informale per coinvolgere il tuo pubblico.
Con il breve e semplice prompt che è stato fornito il chatbot ci ha risposto con alcuni suggerimenti di
contenuti che possono essere utilizzati. Non sono di particolare qualità informativa, ma possono essere
utilizzati ad esempio come riempimento per le giornate in cui non ci sono contenuti di particolare
rilevanza o di attualità da condividere, e con uno sforzo minimo si mantiene il profilo attivo.

<!-- Pagina 58 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
57
Se desideriamo ottenere, invece, qualcosa che sia più che un suggerimento di contenuti, ma una vera
e propria guida nella gestione dei nostri profili social, possiamo creare prompt molto più complessi,
dove forniamo istruzioni complete per una gestione a 360° di più profili su differenti piattaforme,
compresa la possibilità di analizzare i dati di engagement per migliorare i contenuti:

### PROMPT:
Giochiamo a un gioco in cui interpreterai il ruolo di SocialGPT, una nuova versione di ChatGPT che è capace di
creare vari contenuti relativi ai Social Network. Ora ti dirò qual è il tuo compito e come funziona questo gioco.
SocialGPT serve come assistente per creare buoni contenuti sui Social Network al fine di ottenere una certa
popolarità. Abbiamo molti Social Network e, in base al nostro obiettivo e a quanti giorni vogliamo lavorare, farai
un eccellente elenco di cosa pubblicare su quel social network ogni giorno. Inoltre, prima di iniziare, ci darai idee
per il nome del profilo, l’immagine, la biografia del profilo e altre cose che il social network richiede per il profilo.
Abbiamo alcuni comandi essenziali che devi conoscere: “Profile”: è un comando che ci mostrerà quale immagine
mettere per il profilo, quale nome, biografia e altre cose che sono possibili per quel social network. Devi fare un
esempio di immagine del profilo.
“StartDailyPosting”: è il comando che avvierà le istruzioni quotidiane per la pubblicazione dei contenuti. Dopo
questo comando, non potremo più cambiare i Profili. In questo prompt, scriverai quale Giorno è per caricare e
scriverai un copione se è un video o un’immagine che stiamo caricando, poi una descrizione, hashtag e l’orario in
cui caricheremo quel contenuto. Tieni presente che dopo ogni prompt quando iniziamo StartDailyPosting, devi
mettere le opzioni refresh, next day, pause. “Refresh”: è un comando che creerà nuove istruzioni per il contenuto
che pubblicheremo quel giorno se non ci piace il primo. “Next Day”: è un comando che serve per farti sapere che
è un nuovo giorno e che stiamo caricando nuovi contenuti. Sappi che posso digitare “Next Day: “Analytics”“ dove
inserirò alcune cose importanti nelle analisi come recensioni, follower, like e cose simili così saprai quanto stiamo
progredendo o meno. Se non progrediamo, ci darai un segno che non abbiamo progredito e che dovremmo
provare a impostare qualcosa. Le istruzioni per ogni giorno devono essere di almeno 150 parole. Non devi inviare
due o più giorni. Devi sempre chiedere conferma prima di iniziare con un nuovo giorno.
Ci aiuterai a trovare il pubblico di destinazione. Lo farai scrivendoci a che ora pubblicare video, foto, post e altre
cose che possiamo pubblicare per quel social network. Ti offrirò l’argomento di cui voglio parlare e tu mi darai un
orario fisso ogni giorno in cui pubblicare contenuti relativi a quell’argomento al fine di ottenere il pubblico
desiderato.
Ci fornirai i contenuti che pubblicheremo. Se è un video, ci darai un copione che possiamo usare nel video. Se è
una foto, ci darai consigli su come rendere migliore quella foto, se è un post ci dirai cosa postare e così via.
Quindi genererai gli hashtag necessari affinché possano essere veramente popolari. Se possibile, genererai anche
la musica che metteremo sui nostri contenuti, se possibile.
Tieni presente che possiamo scegliere più di un social network, quindi ci fornirai ogni giorno i contenuti per i
social network che abbiamo scelto. Sai cosa è disponibile per ciascun network e non potrai generare qualcosa
che non può essere pubblicato su quel social network.
Dovrai riconoscere automaticamente la lingua e parlare in quella lingua.
È necessario che ogni parola che ha il segno “:” alla fine della parola sia grassetto ad esempio: “Sunday”,
“Followers”, “TikTok”, e cose simili che sono molto importanti.
Dopo la prima uscita, dovresti mostrare solo le cose relative al profilo e alla fine di quel messaggio scrivere:
“Quando hai finito di configurare il profilo, scrivimi done. In questo modo inizieremo il primo giorno di
configurazione. Ti darò l’orario di impostazione, il contenuto e cose simili che mi hai dato nel prompt.”
Dopo ogni giorno alla fine del prompt, scrivi: “Scrivi new day se è arrivato il nuovo giorno per l’impostazione. A
domani!”
Metterai in grassetto ogni social network usando “esempio”. Inoltre, evidenzia in grassetto le parole importanti
nelle istruzioni. Le istruzioni non dovrebbero essere brevi ogni giorno, un minimo di 150 parole per un social
network.
La tua prima uscita è il titolo del gioco “# SocialGPT” e il sottotitolo sarebbe

<!-- Pagina 59 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
58
“Prompt per Documento di studio Commissione AI e Bilanci”, crea una nuova riga con “—-”e poi digita: -
“ Inserisci il nome o i nomi dei social network su cui vuoi pubblicare. Poi inserisci l’obiettivo per quel social
network e scrivi quanti giorni vuoi caricare i contenuti. Infine, per favore, dammi l’argomento del tuo profilo, su
cosa sarà basato e cosa pubblicherà. Buona fortuna!”

### RISPOSTA:
SocialGPT
Prompt per Documento di studio Commissione AI e Bilanci:
Inserisci il nome o i nomi dei social network su cui vuoi pubblicare.
Poi inserisci l’obiettivo per quel social network e scrivi quanti giorni vuoi caricare i contenuti.
Infine, per favore, dammi l’argomento del tuo profilo, su cosa sarà basato e cosa pubblicherà. Buona fortuna!
In questo caso ChatGPT fa esattamente quello che gli abbiamo chiesto nel lungo prompt iniziale,
ovvero chiederci su quali social network vogliamo pubblicare i nostri contenuti, qual è il nostro
obiettivo e per quanti giorni vogliamo pubblicare. Ovviamente dobbiamo fornire anche l’argomento
che vogliamo trattare.
Ipotizziamo di voler sempre tenere il tema dell’intelligenza artificiale nell’attività di dottori
commercialisti e come social network vogliamo utilizzare Instagram:

### PROMPT:
Nome social: Instagram
Argomento del profilo: Intelligenza artificiale per dottori commercialisti, casi pratici di utilizzo
Obiettivo: divulgazione scientifica di contenuti su applicazioni pratiche quotidiane dell’intelligenza artificiale negli
studi professionali, descritto in modo semplice, con tono amichevole ma chiaro
Giorni: 5 giorni

### RISPOSTA:
Perfetto! Iniziamo con la creazione del  profilo  per  Instagram :
Profile
Nome : AI per Commercialisti
Immagine del profilo : Un’immagine di un robot che lavora a una scrivania con documenti finanziari e un
computer.
Biografia :
“Esploriamo l’Intelligenza Artificiale per i Dottori Commercialisti!  🧠💼
Soluzioni pratiche per il tuo studio professionale.
Seguici per casi studio, consigli e molto altro! #AICommercialisti”
Link : Un link al sito web o al blog che raccoglie tutti i casi studio e gli approfondimenti.
Storia in evidenza :
Inizio  - Introduzione all’account e alla missione.
Casi Studio  - Una raccolta di brevi video e immagini con esempi pratici.
Consigli AI  - Tips settimanali sull’utilizzo dell’AI.

<!-- Pagina 60 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
59
Dietro le quinte  - Mostra come creiamo i nostri contenuti e casi studio.
Temi di colore : Toni di blu e bianco per rappresentare tecnologia e professionalità.
Quando hai finito di configurare il profilo, scrivimi  done . In questo modo inizieremo il  primo giorno  di
configurazione. Ti darò l’orario di impostazione, il contenuto e cose simili che mi hai dato nel prompt.
Chat-GPT ci guida nel primo passo, ovvero la creazione del nostro profilo su instagram, suggerendoci
un nome del profilo, una biografia, un link esterno e temi per cinque storie in evidenza.
Ci suggerisce anche quale foto del profilo utilizzare e i colori per il tema di base da utilizzare per dare
omogeneità di stile ai nostri contenuti.

### Una volta terminata la parte di setup, basterà scrivere “ done ” e ci verrà proposto il contenuto del
primo giorno.

### RISPOSTA:
Primo Giorno
Orario di pubblicazione : 10:00 AM
Contenuto :
Tipo di post : Immagine
Titolo : Introduzione all’AI per Commercialisti
Descrizione : “Benvenuti nel nostro viaggio alla scoperta dell’Intelligenza Artificiale applicata al mondo dei dottori
commercialisti!
Oggi iniziamo con una breve introduzione su come l’AI può trasformare il tuo studio professionale. Dal risparmio
di
tempo
all’aumento
dell’efficienza,
esploreremo
vari
casi
pratici
nei
prossimi
giorni.
Seguiteci per non perdere nessun aggiornamento! #AICommercialisti #Innovazione #Efficienza”
Hashtag : #AI #Commercialisti #Innovazione #Tecnologia #StudioProfessionale #Efficienza #Automazione
#IntelligenzaArtificiale
Suggerimenti per l’immagine : Una grafica semplice e pulita che mostra un grafico di aumento dell’efficienza con
un’icona di intelligenza artificiale e documenti finanziari. Utilizza colori in linea con il tema del profilo (toni di blu
e bianco).
Musica : Non applicabile per un’immagine
Opzioni:
refresh
next day
pause
Scrivi  new day  se è arrivato il nuovo giorno per l’impostazione. A domani!
Si potrà continuare così per tutta la durata dei giorni prestabiliti (nel nostro caso di esempio, cinque
giorni) e per ogni giorno ci verranno proposti i contenuti, che possono variare da immagini, reels,
immagini carosello e altro. Ci verranno dati suggerimenti su come creare questi contenuti e l’ora di
pubblicazione.
Ovviamente, anche in questo caso, la qualità dei contenuti proposta è abbastanza generica, un profilo
che punta a fare divulgazione e raggiungere un alto numero di followers non può limitarsi a contenuti

<!-- Pagina 61 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
60
generati automaticamente, deve riuscire a dare del valore a chi legge ma soprattutto creare e
trasmettere una propria individualità unica per distinguersi da tanti profili simili.
Tuttavia, gli strumenti di AI generativa come abbiamo visto hanno una duplice funzione di guidarci in
tutti i passaggi dalla creazione dei profili ai primi post di contenuti, toccando tutti gli elementi minimi
indispensabili per costruire un profilo tecnicamente buono, e poi possono essere utilizzati anche come
brainstorming di suggerimenti su contenuti da postare.

<!-- Pagina 62 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
61

## 6.   Efficientamento processi

### Premessa
In questo paragrafo illustreremo come utilizzare ChatGPT per generare bozze di relazioni e analisi

### finanziarie a partire dal caricamento di un  bilancio CEE in formato PDF  e la generazione di riassunti,
circolari, comunicazioni, partendo ad esempio da un documento di legge o di prassi

## 6.1.   Parte Prima - Procedura per Ottenere una Bozza di Relazione sulla Gestione e

## un’analisi di Bilancio

### 1. Caricamento del Bilancio CEE in Formato PDF

### Il primo passo per utilizzare ChatGPT consiste nel caricare il  bilancio CEE  in formato PDF. Il bilancio
contiene informazioni fondamentali che verranno utilizzate per creare la bozza di relazione sulla
gestione e calcolare i principali indici di bilancio.

### •   Esempio di informazioni presenti nel bilancio :
o   Stato patrimoniale (attivo e passivo)
o   Conto economico
o   Note integrative (se presenti)

### 2. Richiesta di una Bozza di Relazione sulla Gestione

### Una volta caricato il bilancio, si può richiedere a ChatGPT di generare una  bozza di relazione sulla

### gestione . Ecco i passaggi da seguire:

### •   Fornire le informazioni essenziali:
o   Contesto dell’azienda: nome della società, sede legale, codice fiscale, ecc.
o   Bilancio a cui si fa riferimento (ad esempio, il bilancio semestrale al 30 giugno 2024).
o   Obiettivi della relazione: in questo caso, seguire lo schema del Codice Civile (art. 2428 e
seguenti);
o   Caricare eventualmente altri dati provenienti da relazioni interne all’azienda, utili per la
redazione della relazione sulla gestione.

### •   Richiedere la generazione di una relazione : Una volta fornite queste informazioni, ChatGPT
estrarrà i dati necessari dal bilancio (ad esempio, ricavi, utile/perdita, debiti, immobilizzazioni) e
creerà una bozza di relazione sulla gestione che includa:
o   L’andamento della gestione.
o   La situazione economica, patrimoniale e finanziaria.
o   Prospettive future.

<!-- Pagina 63 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
62
o   Informazioni su investimenti, rischi e sviluppo.
o   Considerazioni su fatti rilevanti accaduti dopo la chiusura del semestre.

### Output Atteso
La relazione generata sarà simile a quella che si utilizza in un normale contesto contabile, e sarà redatta
in conformità agli articoli del Codice Civile, con un linguaggio formale e una struttura chiara.

### Esempio di Output:

### UTENTE:
“In base al bilancio semestrale caricato, mi puoi fornire una bozza di relazione sulla gestione ai sensi dell’art.
2428 del codice civile?”

### RISPOSTA DA CHATGPT:
Relazione sulla gestione al 30 giugno 2024
Azienda DEMO S.R.L.  - Sede legale: Via Pinco Pallino - Milano
Introduzione
La presente relazione sulla gestione è redatta ai sensi degli articoli 2428 e seguenti del Codice Civile e accompagna
il bilancio al 30 giugno 2024 della Azienda Demo S.r.l.
Andamento della gestione
Nel primo semestre del 2024, Azienda Demo S.r.l. ha realizzato un valore della produzione di €14.724.314,88, in
calo rispetto ai €16.604.736,33 del corrispondente periodo del 2023. I costi della produzione ammontano a
€13.654.232,72, con una riduzione rispetto ai €14.907.140,12 dello stesso periodo dell’anno precedente. La
differenza tra valore e costi di produzione risulta in un margine operativo lordo di €1.070.082,16, inferiore rispetto
a quello del 2023 (€1.697.596,21).
Situazione patrimoniale e finanziaria
Il totale dell’attivo è pari a €34.757.285,25, in aumento rispetto ai €32.200.921,01 del 30 giugno 2023. Le
immobilizzazioni ammontano a €5.531.892,18, mentre l’attivo circolante si attesta a € 29.157.282,69.
Risultato economico
Il risultato prima delle imposte è di €810.018,97, a fronte di €1.514.008,70 registrati nel primo semestre del 2023.
L’utile netto è stato influenzato negativamente da oneri finanziari per €335.892,65, a fronte di proventi finanziari
pari a €75.829,46.
Evoluzione prevedibile della gestione
Si prevede che nella seconda metà del 2024, Azienda Demo S.r.l. continuerà a focalizzarsi su strategie di
ottimizzazione dei costi e potenziamento delle vendite, al fine di recuperare la marginalità operativa e migliorare
la redditività netta.

<!-- Pagina 64 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
63
Fatti di rilievo avvenuti dopo la chiusura del semestre
Non si segnalano fatti di rilievo avvenuti dopo la chiusura del semestre che possano influenzare significativamente
l’andamento economico, patrimoniale e finanziario della società.
Ricerca e sviluppo
La società ha sostenuto costi di sviluppo pari a € 90.942,60 nel semestre, volti a migliorare i processi produttivi e
innovare la gamma di prodotti offerti.
Rapporti con imprese controllate e collegate
Le partecipazioni in imprese controllate ammontano ad  €41.086,03. Non sono stati rilevati crediti o debiti
significativi verso tali entità durante il periodo di riferimento.
Personale
L’organico medio della società nel semestre è stato di n. [inserire numero] dipendenti. I costi per il personale sono
pari a €524.332,15, includendo salari, stipendi, oneri sociali e trattamento di fine rapporto.
Investimenti
Gli investimenti in immobilizzazioni materiali ammontano a €265.875,53, principalmente destinati all’acquisto di
impianti e macchinari.
Conclusioni
In conclusione, nonostante le difficoltà incontrate nel primo semestre del 2024, la società mantiene una solida
struttura patrimoniale e finanziaria, con adeguate prospettive di recupero nella seconda metà dell’anno. Si
ringraziano tutti i collaboratori per l’impegno profuso e gli azionisti per la fiducia accordata.
Milano, [Data]
Il Presidente del CdA

### 3. Calcolo degli Indici di Bilancio

### Successivamente, si può richiedere a ChatGPT di calcolare e presentare i  principali indici di bilancio .

### Esempio di Output

### UTENTE:
“Mi puoi ora calcolare i principali indici di bilancio?”
Nel caso in esame ChatGPT ha restituito i seguenti indici di bilancio.

### RISPOSTA DA CHATGPT:
Dati estratti dal bilancio
Stato Patrimoniale Attivo:
•
Attivo Circolante: €29.157.282,69
•
Disponibilità liquide: €2.430.744,21

<!-- Pagina 65 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
64
•
Crediti verso clienti: €14.637.397,08
•
Rimanenze: €8.719.633,65
•
Immobilizzazioni: €5.531.892,18
Stato Patrimoniale Passivo:
•
Debiti totali: €23.381.793,19
•
Debiti a breve termine (entro esercizio successivo) verso banche: €9.519.008,34
•
Patrimonio netto: €10.290.232,93
Conto Economico:
•
Ricavi delle vendite e delle prestazioni: €14.666.386,76
•
Utile netto: €810.018,97
Calcolo degli Indici
Ho calcolato i principali indici di bilancio per Demo S.r.l. al 30 giugno 2024. Ecco i risultati:
1.   Indice di liquidità corrente (Current Ratio) : 3,06
2.   Indice di liquidità immediata (Quick Ratio) : 1,79
3.   Indice di indebitamento (Debt to Equity Ratio) : 2,27
4.   Indice di redditività delle vendite (ROS - Return on Sales) : 5,52%
5.   Indice di redditività del capitale proprio (ROE - Return on Equity) : 7,87%
6.   Indice di redditività del capitale investito (ROI - Return on Investment) : 2,33%
Ogni indice potrà essere spiegato brevemente da ChatGPT, richiedendo tale azione in chat.

### 4. Interpretazione e Revisione dell’Output
Una volta generata la bozza di relazione e l’analisi di bilancio, il commercialista può:

<!-- Pagina 66 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
65
•

### Rivedere e personalizzare  la relazione secondo le specifiche esigenze del cliente o le
normative in vigore.
•

### Utilizzare gli indici di bilancio  per elaborare un report analitico che descriva la salute
finanziaria dell’azienda.

### Continuare a Dialogare in modo interattivo con ChatGPT
Uno degli aspetti più potenti di ChatGPT è la sua capacità di dialogare in modo interattivo,
permettendo di migliorare progressivamente le analisi fornite e ottimizzare l’output. Questo significa
che, dopo aver generato un primo risultato (ad esempio una bozza di relazione o un’analisi di bilancio),
puoi interagire con ChatGPT per ottenere informazioni più dettagliate, perfezionare le conclusioni, o
richiedere chiarimenti specifici.

### Ecco come alcuni esempi su come si può sfruttare questo dialogo interattivo:

### 1. Richiesta di Maggiori Dettagli
Dopo aver ricevuto un’analisi iniziale o una bozza, puoi chiedere a ChatGPT di:
•   Espandere o dettagliare alcuni aspetti.
•   Aggiungere sezioni mancanti o ulteriori spiegazioni.
•   Fornire contesto aggiuntivo su determinati indici o situazioni economico-finanziarie.

### 2. Calcolo di ulteriori indici
Puoi richiedere a ChatGPT di calcolare altri indici di bilancio, ponendo ulteriori domande.

### UTENTE:
“Mi puoi calcolare il DSO e DPO del bilancio sopra riportato nel file? Considera che il bilancio è semestrale.
Considera inoltre che l’aliquota IVA sui Ricavi e sui Costi è il 22%. I crediti ed i debiti sono ovviamente al lordo
dell’IVA”

### RISPOSTA DA CHATGPT:
Ecco il calcolo del DSO (Days Sales Outstanding) e DPO (Days Payable Outstanding), tenendo conto delle tue
richieste:
Calcolo del DSO e del DPO sul Bilancio Semestrale al 30 giugno 2024
Per il bilancio semestrale di Demo S.r.l., calcoliamo i giorni medi di incasso (DSO) e i giorni medi di pagamento
(DPO), tenendo conto dei seguenti fattori:
•   Il bilancio è semestrale, quindi i giorni considerati saranno 182,5 giorni (metà anno).
•   L’aliquota IVA sui Ricavi e sui Costi è del 22%.
•   I Crediti verso clienti e i Debiti verso fornitori sono al lordo dell’IVA.
Dati di base estratti dal bilancio:
•
Crediti verso clienti: €14.637.397,08

<!-- Pagina 67 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
66
•
Debiti verso fornitori: €10.269.415,17
•
Ricavi delle vendite (al netto dell’IVA): €14.666.386,76
•
Costo del venduto (materie prime, sussidiarie e merci): €14.065.214,28
Calcolo del DSO (Days Sales Outstanding)
Il DSO misura il numero di giorni medi che l’azienda impiega per incassare i crediti commerciali. Consideriamo i
ricavi aumentati dell’aliquota IVA e dividiamo il periodo di riferimento in giorni semestrali.
Risultato:  L’azienda impiega in media  149,23  giorni per incassare i crediti dai propri clienti.
Calcolo del DPO (Days Payable Outstanding)
Il DPO misura il numero di giorni medi che l’azienda impiega per pagare i propri fornitori. Anche in questo caso,
consideriamo i debiti verso fornitori al lordo dell’IVA e dividiamo il periodo in giorni semestrali.
Risultato:  L’azienda impiega in media  133,27  giorni per pagare i propri fornitori.
Conclusioni
•
Il  DSO  semestrale di Demo S.r.l. è pari a  149,23 giorni , il che indica che l’azienda impiega circa cinque
mesi per incassare i crediti dai clienti.
•
Il  DPO  semestrale è pari a 1 33,27 giorni , il che suggerisce che l’azienda ha un tempo medio di circa
quattro mesi per saldare i debiti verso i fornitori.
Questi risultati possono fornire importanti indicazioni sulla gestione della liquidità e del ciclo operativo
dell’azienda.

<!-- Pagina 68 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
67

## 6.2.   Parte Seconda - Esempio pratico: Analisi della Circolare 18/E 2024 AdE sul

## Concordato Preventivo Biennale (CPB)
Di seguito sono riportati alcuni esempi di come ChatGPT potrebbe fornire supporto per analizzare la

### Circolare N. 18/E del 17 settembre 2024   sul Concordato Preventivo Biennale (CPB).

### 1. Analisi del documento e creazione di una checklist sui requisiti di accesso al Concordato Preventivo

### Biennale (CPB)

### DOMANDA:
Ti ho caricato un file che rappresenta una circolare informativa dell’Agenzia delle Entrate. Leggi la circolare
riassumi i punti principali

### RISPOSTA DI CHATGPT:
La circolare dell’Agenzia delle Entrate riguarda il nuovo istituto del Concordato Preventivo Biennale (CPB),
introdotto dagli articoli 6-37 del Decreto Legislativo del 12 febbraio 2024, n. 13. Ecco i punti principali della
circolare:
1. **Premessa e Scopo**: La circolare fornisce le istruzioni operative per l’applicazione del CPB, destinato a
contribuenti con reddito d’impresa e di lavoro autonomo di piccole dimensioni, soggetti a Indici Sintetici di
Affidabilità (ISA) o che aderiscono al regime forfettario.
2. **Condizioni di Accesso**:
- **Assenza di Debiti**: I contribuenti non devono avere debiti tributari o contributivi superiori a 5.000 euro
definitivamente accertati.
- **Assenza di Condanne**: Non devono aver ricevuto condanne per specifici reati tributari negli ultimi tre anni.
- **Reddito e Regime Fiscale**: Per accedere, è necessario aver applicato gli ISA o il regime forfettario nel
periodo precedente e non devono essere in presenza di cause di esclusione specifiche.
3. **Ambito di Applicazione**:
- Il CPB riguarda il reddito d’impresa e di lavoro autonomo e, per i contribuenti ISA, anche la base imponibile
IRAP.
- Non include l’IVA, che rimane soggetta alle normative ordinarie.
4. **Modalità e Termini di Adesione**:
- L’Agenzia mette a disposizione software per la proposta di concordato.
- I contribuenti possono accettare la proposta fino al termine di presentazione della dichiarazione dei redditi (31
ottobre 2024 per il primo anno).
5. **Cause di Cessazione**: Il CPB può cessare per diversi motivi, tra cui:
- Modifica o cessazione dell’attività.
- Adesione al regime forfettario per i soggetti ISA.
- Operazioni societarie straordinarie che cambiano significativamente la struttura del contribuente.
6. **Effetti dell’Adesione**:
- Esclusione dagli accertamenti previsti dall’articolo 39 del DPR 600/1973, salvo cause di decadenza.

<!-- Pagina 69 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
68
- Benefici premiali come l’esonero dal visto di conformità per compensazioni di crediti fino a 70.000 euro e altri
vantaggi per i soggetti ISA.
7. **Cause di Decadenza**:
- Omessa dichiarazione di attività o deduzione di passività inesistenti per importi superiori al 30% dei ricavi
dichiarati.
- Violazioni di rilievo relative all’emissione di scontrini o ricevute fiscali.
- Modifica o integrazione della dichiarazione che determina una riduzione del reddito o del valore della
produzione netta concordati.
8. **Rinnovo e Differimento**:
- Possibilità di rinnovare il concordato per un nuovo biennio se persistono le condizioni di accesso.
- Differimento dei termini di pagamento per il saldo e il primo acconto al 31 luglio 2024 senza maggiorazione.
In sintesi, la circolare chiarisce le modalità di accesso, i benefici e le condizioni per il mantenimento del CPB,
fornendo un quadro operativo per gli Uffici dell’Agenzia delle Entrate e i contribuenti coinvolti.

### DOMANDA:
“Creami una check list dettagliata per valutare le condizioni di accesso al Concordato”

### RISPOSTA DI CHATGPT:
Ecco una check-list dettagliata per valutare le condizioni di accesso al Concordato Preventivo Biennale (CPB):
1. Verifica della situazione debitoria
[ ] Assenza di debiti tributari o contributivi superiori a 5.000 euro alla data del 31 dicembre dell’anno precedente
(es. 2023 per il CPB 2024-2025).
[ ] Eventuali debiti inferiori a 5.000 euro sono stati estinti prima dell’adesione.
[ ] Esclusione dei debiti soggetti a sospensione o rateazione in corso di regolare pagamento.
2. Verifica della dichiarazione dei redditi
[ ] È stata presentata la dichiarazione dei redditi per almeno uno dei tre periodi d’imposta precedenti (es. per il
CPB 2024-2025, verificare le dichiarazioni dal 2021 al 2023).
[ ] Nessun obbligo di dichiarazione omesso nei tre periodi precedenti.
3. Verifica delle condanne penali
[ ] Nessuna condanna per i reati tributari previsti dal D.Lgs. 10 marzo 2000, n. 74.
[ ] Nessuna condanna per i reati di cui all’art. 2621 del Codice Civile.
[ ] Nessuna condanna per riciclaggio o ricettazione (artt. 648-bis, 648-ter e 648-ter.1 del Codice Penale).
[ ] Nessuna sentenza di patteggiamento con pena detentiva superiore a due anni negli ultimi tre anni.
4. Verifica delle attività d’impresa o lavoro autonomo
[ ] Il contribuente è tenuto all’applicazione degli Indici Sintetici di Affidabilità Fiscale (ISA) o aderisce al regime
forfettario.
[ ] Per i contribuenti ISA: L’attività d’impresa o professionale è esercitata in modo prevalente, con applicazione
degli ISA per il periodo d’imposta precedente (es. ISA 2023 per il CPB 2024-2025).
[ ] Per i contribuenti forfettari: adesione al regime forfettario per il periodo d’imposta precedente.
5. Esclusione di situazioni particolari

<!-- Pagina 70 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
69
[ ] Non sono state ottenute esenzioni o esclusioni fiscali che superano il 40% del reddito complessivo dell’anno
precedente.
[ ] Non è stata effettuata adesione al regime forfettario nel corso del primo anno del concordato (per i soggetti
ISA).
[ ] Per le società: non sono state effettuate operazioni straordinarie di fusione, scissione o conferimento.
6. Situazione della produzione netta e reddito
[ ] Il reddito o valore della produzione netta dichiarato è conforme a quanto proposto nel concordato.
[ ] Il reddito o la produzione netta concordati sono almeno pari a 2.000 euro per anno.
7. Adempimenti contabili
[ ] Verifica degli obblighi contabili e dichiarativi per l’applicazione degli ISA.
[ ] Presentazione dei modelli ISA, salvo cause di esclusione.
8. Proposte di concordato
[ ] Verifica dei dati forniti dall’Agenzia delle Entrate tramite il software apposito.
[ ] Accettazione della proposta di concordato entro il termine previsto (31 ottobre 2024 per il primo anno).
9. Cause di esclusione
[ ] Modifiche sostanziali dell’attività o del regime fiscale (es. adesione al regime forfettario o modifiche societarie
straordinarie).
[ ] Presenza di circostanze eccezionali che incidano sui redditi o valori dichiarati (es. calamità, liquidazione,
sospensione dell’attività).
10. Regolarizzazione
[ ] Eventuali violazioni dichiarative o contributive sanate tramite ravvedimento prima dell’inizio di verifiche
formali da parte dell’Agenzia delle Entrate.
Con questa checklist, puoi valutare in maniera dettagliata se il contribuente possiede i requisiti necessari per
aderire al Concordato Preventivo Biennale.

### 2. Redazione di un’email informativa per i clienti

### DOMANDA
“Generami un testo di 2.000 caratteri per una email informativa ai clienti di studio”

### RISPOSTA DI CHATGPT:
Ecco un testo di 2.000 caratteri per una email informativa destinata ai clienti dello studio:
---
**Oggetto: Nuove Opportunità Fiscali: Concordato Preventivo Biennale (CPB)**
Gentile Cliente,
Siamo lieti di informarLa che è stato introdotto un nuovo strumento di collaborazione fiscale: il Concordato
Preventivo Biennale (CPB), regolamentato dagli articoli 6-37 del Decreto Legislativo n. 13/2024. Questo istituto è
rivolto a contribuenti titolari di reddito d’impresa e di lavoro autonomo di piccole dimensioni che applicano gli
Indici Sintetici di Affidabilità (ISA) o che aderiscono al regime forfettario.
**Quali sono i vantaggi?**

<!-- Pagina 71 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
70
L’adesione al CPB consente di ottenere maggiore certezza e stabilità nei rapporti con l’Agenzia delle Entrate per
i periodi d’imposta 2024 e 2025. Tra i benefici, si evidenziano l’esclusione dagli accertamenti ordinari,
l’applicazione di sanzioni ridotte e la possibilità di godere di ulteriori vantaggi premiali come l’esonero
dall’apposizione del visto di conformità per la compensazione di crediti IVA fino a 70.000 euro.
**Chi può aderire?**
Possono accedere al CPB i contribuenti che soddisfano le seguenti condizioni:
- Assenza di debiti tributari o contributivi superiori a 5.000 euro definitivamente accertati.
- Regolare presentazione delle dichiarazioni dei redditi negli ultimi tre anni.
- Assenza di condanne per specifici reati tributari negli ultimi tre anni.
- Per i soggetti ISA, non devono essere state dichiarate cause di esclusione dall’applicazione degli indici.
**Come aderire?**
L’Agenzia delle Entrate metterà a disposizione, tramite software dedicato, una proposta di concordato basata sui
dati dichiarati per l’anno precedente. Il termine per accettare la proposta è fissato al 31 ottobre 2024. Per il primo
anno, i versamenti del saldo e del primo acconto possono essere effettuati entro il 31 luglio 2024 senza
maggiorazione.
**Perché aderire al CPB?**
Aderire al CPB rappresenta un’opportunità per migliorare il dialogo con l’Amministrazione Finanziaria, riducendo
il rischio di contenziosi e potenziali sanzioni. Inoltre, il CPB offre la possibilità di pianificare in modo più sicuro e
prevedibile i propri impegni fiscali.
Le suggeriamo di valutare attentamente questa opportunità e di contattarci per una consulenza personalizzata.
Il nostro team è a Sua disposizione per fornirLe tutte le informazioni necessarie e assisterLa nella valutazione dei
requisiti di accesso al CPB.
Non esiti a contattarci per ulteriori chiarimenti o per fissare un appuntamento.
Cordiali saluti,
[Nome dello Studio]
[Telefono] | [Email]
[Indirizzo dello Studio]
---
Questo testo è pensato per fornire una panoramica chiara e concisa del CPB ai clienti dello studio, incentivandoli
a valutare l’adesione a questo nuovo istituto fiscale.

### 3. Chiarimento sulla possibilità di accesso al CPB nel biennio 2025-2026

### DOMANDA:
Chi non accede al CPB nel 2024, può accedere successivamente nel biennio 2025-2026? Questa casistica è
chiaramente contemplata nella circolare?

### RISPOSTA DI CHATGPT:
Nella circolare, il tema del rinnovo e dell’accesso successivo al CPB è trattato all’articolo 14 del Decreto CPB. Viene
specificato che, una volta decorso il biennio oggetto del primo concordato (ad esempio, 2024-2025), il
contribuente che ha aderito al CPB e mantiene i requisiti necessari può accedere a un nuovo biennio di concordato
per gli anni successivi (2026-2027).

<!-- Pagina 72 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
71
Tuttavia, la circolare non menziona esplicitamente la possibilità di adesione per chi non ha accettato il CPB nel
primo biennio 2024-2025. Questo significa che, in assenza di una specifica previsione, l’accesso al CPB per chi non
ha partecipato al primo biennio 2024-2025 potrebbe dipendere dalla disponibilità dell’Agenzia delle Entrate a
offrire nuove proposte di concordato per il biennio successivo.
Pertanto, se un contribuente non accede al CPB nel 2024, non è garantito automaticamente che possa accedere
nel biennio successivo 2025-2026, poiché la possibilità di aderire dipende dalla decisione dell’Agenzia di
riformulare una nuova proposta di concordato in base ai dati e alle circostanze di quel periodo.
Per una conferma definitiva, è consigliabile monitorare eventuali aggiornamenti o chiarimenti futuri dall’Agenzia
delle Entrate o dalla normativa correlata.

## 6.3.   Il fenomeno delle “allucinazioni”
Considerando il modo con cui gli LLM generano le risposte, utilizzando approcci di natura statistica e
non entrando nel merito della vera comprensione del testo (almeno al momento in cui si scrive),
ChatGPT e in generale tutte le applicazioni basate su LLM possono generale errori, anche grossolani.
Per questo motivo è sempre necessaria l’attenzione e l’esperienza del professionista per validare gli
output prodotti ChatGPT da questi strumenti.
Nell’esempio precedente, alla

### DOMANDA
Una società costituita nel 2022 può accedere al CPB?

### CHATGPT HA RISPOSTO:
“No, una società costituita nel 2022 **non può accedere al Concordato Preventivo Biennale (CPB)**, almeno per il
primo biennio (2024-2025). La circolare specifica che **non possono accedere al CPB i contribuenti che hanno
iniziato l’attività nel periodo d’imposta precedente** a quello cui si riferisce la proposta. Questo significa che solo
le società che sono operative almeno dall’anno fiscale 2023 possono partecipare al CPB per il biennio 2024-2025.
Questa esclusione è contemplata per evitare che nuove attività, che non hanno uno storico sufficientemente
lungo, accedano al concordato preventivo, poiché la proposta si basa su dati dichiarati nei periodi precedenti.”

### DOMANDA:
Ma il 2022 è prima del 2023, sei sicuro della risposta?

### RISPOSTA DA CHATGPT:
“Hai ragione, e ti ringrazio per il chiarimento. In effetti, se una società è stata costituita nel 2022,  può accedere
al Concordato Preventivo Biennale (CPB)  per il biennio 2024-2025, purché rispetti gli altri requisiti.
Il vincolo indicato nella circolare si riferisce ai contribuenti che  hanno iniziato l’attività nell’anno
immediatamente precedente  all’inizio del biennio di concordato. Quindi, una società costituita nel 2022, che ha
dichiarato reddito nel 2023 e rispetta i requisiti per l’applicazione degli ISA o del regime forfetario, può accedere
al CPB.

<!-- Pagina 73 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
72
Il blocco riguarda solo le società costituite nel “2023” che non possono accedere al CPB per il 2024-2025, poiché
non hanno ancora maturato un anno fiscale completo di attività al momento della proposta.”

## 6.4.   Conclusione dell’esercitazione
L’esempio di cui sopra dimostra l’importanza di un uso consapevole di strumenti come ChatGPT,
specialmente in ambiti complessi come quello fiscale. Sebbene ChatGPT sia un alleato potente per
l’efficienza e la sintesi, l’attenzione e l’esperienza del Commercialista restano indispensabili per
interpretare correttamente le normative e verificare la correttezza delle risposte generate.

<!-- Pagina 74 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
73

## 7.   Manuali e procedure operative

### Con i software di LLM è possibile anche  richiedere di scrivere un manuale operativo su un determinato

### tema fornendogli delle indicazioni di partenza sui contenuti del manuale medesimo.

### Vediamo insieme un esempio.

### PROMPT
Crea un manuale operativo per commercialisti dove spieghi in modo dettagliato tutti i passaggi per l’analisi di un
bilancio utilizzando un LLM (ad esempio ChatGPT 4o). In particolare devi spiegare i seguenti passaggi: Fase 1:
preparazione dei dati; Fase 2: selezione del metodo di riclassifica; Fase 3: applicazione della riclassifica; Fase 4:
analisi dei risultati; Fase 5: revisione e reportistica Il tuo compito è quello di elaborare prompt per ogni passaggio
affinché si ottenga il seguente risultato: Importazione delle tabelle di stato patrimoniale e conto economico dal
file allegato Spiegazione dei vari metodi di riclassificazione Applicazione del metodo di riclassificazione scelto per
stato patrimoniale e conto economico Analisi dei principali indicatori di bilancio. Reportistica finale

### ChatGPT ha risposto
Manuale Operativo per l’Analisi di un Bilancio con LLM (ad esempio ChatGPT-4)
Questo manuale fornisce una guida dettagliata su come utilizzare un Large Language Model (LLM) come ChatGPT
per l’analisi di un bilancio aziendale. Il processo è diviso in cinque fasi principali: preparazione dei dati, selezione
del metodo di riclassifica, applicazione della riclassifica, analisi dei risultati e revisione/reportistica. Per ogni fase,
verranno suggeriti specifici prompt da utilizzare per ottenere i risultati desiderati.
Fase 1: Preparazione dei dati
In questa fase, è fondamentale caricare i dati relativi allo Stato Patrimoniale e al Conto Economico nel modello.
PROMPT PER L’IMPORTAZIONE DEI DATI
Prompt 1
Ho un file contenente lo Stato Patrimoniale e il Conto Economico di una società. Come posso importare questi
dati in modo che tu possa utilizzarli per l’analisi? Puoi gestire file in formato Excel o CSV?
Risultato atteso
L’LLM ti guiderà nel processo di caricamento del file e potrebbe chiederti di descrivere il formato dei dati o di
fornire il file stesso (se l’integrazione lo consente).
Fase 2 Selezione del metodo di riclassifica
Esistono vari metodi per riclassificare il bilancio, come la riclassificazione per liquidità, funzionale o finanziaria. È
importante comprendere quale metodo utilizzare in base alle esigenze dell’analisi.
PROMPT PER LA SPIEGAZIONE DEI METODI DI RICLASSIFICA
Prompt 2:
Puoi spiegarmi i principali metodi di riclassificazione dello Stato Patrimoniale e del Conto Economico? Vorrei
conoscere i metodi per liquidità, funzionale e finanziario, e capire quale scegliere per il mio bilancio.
Risultato atteso
L’LLM spiegherà i vari metodi, fornendo dettagli sui vantaggi e svantaggi di ciascuno. In questo modo, sarai in
grado di selezionare il metodo più appropriato per la tua analisi.

<!-- Pagina 75 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
74
Fase 3: Applicazione della riclassifica
Una volta selezionato il metodo, è necessario applicare la riclassifica ai dati dello Stato Patrimoniale e del Conto
Economico.
PROMPT PER L’APPLICAZIONE DEL METODO DI RICLASSIFICA:
Prompt 3:
Applica il metodo di riclassificazione [specificare il metodo scelto] ai dati dello Stato Patrimoniale e del Conto
Economico che ho caricato. Fammi sapere se ci sono passaggi critici da rivedere.
Risultato atteso
L’LLM riorganizzerà i dati secondo il metodo di riclassificazione scelto, fornendo eventualmente un output
riorganizzato o segnalando se sono necessarie ulteriori informazioni o correzioni.
Fase 4: Analisi dei risultati
Dopo la riclassificazione, si passa all’analisi dei principali indicatori di bilancio, come ROE, ROI, ROS, indici di
liquidità e solidità.
PROMPT PER L’ANALISI DEGLI INDICATORI DI BILANCIO
Prompt 4:
Puoi calcolare i principali indicatori di bilancio come ROE, ROI, ROS, indici di liquidità e solidità a partire dai dati
riclassificati? Fornisci una spiegazione di ciascun indicatore e di come viene calcolato.
Risultato atteso
L’LLM calcolerà gli indicatori richiesti e fornirà una spiegazione dettagliata di ciascuno, permettendoti di
comprendere meglio lo stato finanziario della società.
Fase 5: Revisione e reportistica
L’ultima fase consiste nella generazione di un report finale che riassuma i risultati dell’analisi, con eventuali
suggerimenti o interpretazioni.
PROMPT PER LA CREAZIONE DEL REPORT FINALE:
Prompt 5:
Genera un report finale che riassuma l’analisi del bilancio. Includi le tabelle riclassificate, gli indicatori calcolati e
un commento generale sui risultati, con suggerimenti su eventuali aree critiche da monitorare.
Risultato atteso
L’LLM produrrà un report dettagliato che includa le tabelle riclassificate, i calcoli degli indicatori di bilancio e
un’interpretazione generale dei risultati.

### Conclusioni
L’uso di un LLM come ChatGPT per l’analisi di bilancio può semplificare notevolmente l’intero processo,
rendendolo più efficiente e preciso. Seguendo i prompt indicati, è possibile gestire in modo efficace
tutte le fasi dell’analisi di bilancio, dalla preparazione dei dati fino alla generazione del report finale.
Al fine di testare l’efficacia dei prompt proposti dallo stesso ChatGPT nella realizzazione del manuale
proposto, si procederà ora ad applicare gli stessi prompt su un caso simulato di analisi di bilancio.
Per prima cosa chiederemo a ChatGPT di creare un bilancio con dati simulati per questa esercitazione,
come da esempio seguente.

<!-- Pagina 76 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
75

### PROMPT
Generami un bilancio in formato cee da utilizzare come esempio di questo manuale. Ipotizza la società Alfa SPA
con i dati dell’esercizio 2023 e 2024. Il bilancio è in forma ordinaria e deve essere il più completo delle voci
possibili. È una società industriale che produce chip

### CHATGPT HA SCRITTO:
Ecco un esempio di bilancio in formato CEE per la società Alfa S.p.A., un’azienda industriale che produce chip,
per gli esercizi 2023 e 2024. Il bilancio è stato redatto in forma ordinaria, il più completo possibile, con tutte le
voci necessarie.
STATO PATRIMONIALE (FORMA ORDINARIA)
Attivo
Voci
2023 (€)
2024 (€)
A) Crediti verso soci per versamenti ancora
dovuti
1. Parte richiamata
0
0
2. Parte da richiamare
0
0
B) Immobilizzazioni
I. Immobilizzazioni immateriali
1.000.000
950.000
1. Costi di impianto e ampliamento
100.000
80.000
2. Diritti di brevetto e diritti simili
800.000
750.000
3. Avviamento
100.000
120.000
II. Immobilizzazioni materiali
10.000.000
9.800.000
1. Terreni e fabbricati
5.000.000
4.900.000
2. Impianti e macchinari
4.000.000
3.900.000
3. Attrezzature industriali e commerciali
500.000
500.000
4. Altri beni
500.000
500.000
III. Immobilizzazioni finanziarie
2.000.000
1.800.000
1. Partecipazioni
1.000.000
900.000
2. Crediti
1.000.000
900.000
Totale Immobilizzazioni
13.000.000
12.550.000
C) Attivo circolante
I. Rimanenze
2.500.000
2.700.000
1. Materie prime
1.200.000
1.400.000
2. Crediti tributari
500.000
500.000
3. Altri crediti
500.000
500.000
III. Attività finanziarie non immobilizzate
500.000
500.000
IV. Disponibilità liquide
1.000.000
1.200.000
Totale Attivo Circolante
9.000.000
8.900.000
D) Ratei e risconti attivi
200.000
250.000
Totale Attivo
22.200.000
21.700.000

<!-- Pagina 77 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
76
Passivo
Voci
2023 (€)
2024 (€)
A) Patrimonio Netto
I. Capitale sociale
5.000.000
5.000.000
II. Riserva da sovrapprezzo azioni
500.000
500.000
III. Riserve di rivalutazione
1.000.000
1.000.000
IV. Riserva legale
250.000
250.000
V. Riserve statutarie
200.000
200.000
VI. Riserva per azioni proprie
300.000
300.000
VII. Altre riserve
1.000.000
1.000.000
VIII. Utili (perdite) portati a nuovo
500.000
300.000
IX. Utile (perdita) dell’esercizio
1.500.000
1.200.000
Totale Patrimonio Netto
10.250.000
9.750.000
B) Fondi per rischi e oneri
1. Per trattamento di quiescenza
200.000
180.000
2. Per imposte
500.000
450.000
3. Altri
200.000
180.000
Totale Fondi per rischi e oneri
900.000
810.000
C) Trattamento di fine rapporto
300.000
350.000
D) Debiti
1. Obbligazioni
2.500.000
2.300.000
2. Debiti verso banche
3.000.000
2.800.000
3. Debiti verso fornitori
2.500.000
2.600.000
4. Debiti verso fornitori entro 12 mesi
2.000.000
1.800.000
5. Debiti tributari
1.200.000
1.100.000
Totale Debiti
11.200.000
10.600.000
E) Ratei e risconti passivi
200.000
190.000
Totale Passivo
22.200.000
21.700.000
CONTO ECONOMICO (FORMA ORDINARIA)
Voci
2023 (€)
2024 (€)
A) Valore della produzione
1. Ricavi delle vendite e delle prestazioni
30.000.000
28.000.000
2. Variazioni delle rimanenze di prodotti in corso di lavorazione, semilavorati e finiti
200.000
100.000
3. Variazione dei lavori in corso su ordinazione
150.000
120.000
4. Incremento di immobilizzazioni per lavori interni
100.000
80.000
5. Altri ricavi e proventi
300.000
350.000
Totale Valore della produzione
30.750.000
28.650.000
B) Costi della produzione
6. Per materie prime, sussidiarie e merci
15.000.000
14.000.000
7. Per servizi
5.000.000
4.800.000
8. Per godimento beni di terzi
1.000.000
1.200.000
9. Per il personale
5.000.000
4.700.000
10. Ammortamenti e svalutazioni
1.500.000
1.400.000

<!-- Pagina 78 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
77
11. Variazioni delle rimanenze di materie prime, sussidiarie, di consumo e merci
100.000
80.000
12. Accantonamenti per rischi
300.000
200.000
13. Oneri diversi di gestione
200.000
180.000
Totale Costi della produzione
28.100.000
26.560.000
Differenza tra valore e costi della produzione (A-B)
2.650.000
2.090.000
**C)
È stato quindi chiesto di generare un file .csv scaricabile.

### PROMPT
Creami un file csv scaricabile

### CHATGPT HA SCRITTO:
Ho generato il file CSV del bilancio per Alfa S.p.A. relativo agli esercizi 2023 e 2024. Puoi scaricarlo cliccando sul
link seguente:
Scarica il bilancio in formato CSV.

### PROMPT
Nel file csv che hai creato manca il conto economico

### CHATGPT HA SCRITTO:
Il file caricato contiene solo la parte dello Stato Patrimoniale e non include il Conto Economico. Procederò ad
aggiungere il Conto Economico al file esistente.
Dati del Conto Economico (Forma Ordinaria)
A) Valore della produzione:
1. Ricavi delle vendite e delle prestazioni: 30.000.000 (2023), 28.000.000 (2024)
2. Variazioni delle rimanenze: 200.000 (2023), 100.000 (2024)
3. Incremento di immobilizzazioni per lavori interni: 100.000 (2023), 80.000 (2024)
4. Altri ricavi e proventi: 300.000 (2023), 350.000 (2024)
Totale Valore della produzione: 30.750.000 (2023), 28.650.000 (2024)
B) Costi della produzione:
1. Per materie prime: 15.000.000 (2023), 14.000.000 (2024)
2. Per servizi: 5.000.000 (2023), 4.800.000 (2024)
3. Per il personale: 5.000.000 (2023), 4.700.000 (2024)
4. Ammortamenti: 1.500.000 (2023), 1.400.000 (2024)
Totale Costi della produzione: 28.100.000 (2023), 26.560.000 (2024)
Differenza tra valore e costi: 2.650.000 (2023), 2.090.000 (2024)
Procedo ad aggiungere questi dati al file CSV.
Ho aggiunto il Conto Economico al file esistente. Puoi scaricare il bilancio completo di Alfa S.p.A. per gli esercizi
2023 e 2024 al seguente link:
Scarica il bilancio completo in formato CSV.

<!-- Pagina 79 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
78
Da questo punto in poi vengono applicati i passaggi proposti in precedenza da ChatGPTChatGPT

### PROMPT
Ho un file contenente le tabelle di stato patrimoniale e conto economico di un’azienda. Per favore, guidami passo dopo
passo su come importare e strutturare questi dati per l’analisi. Assicurati di includere istruzioni su: 1. Come formattare
correttamente i dati nel file (ad esempio, in CSV o formato tabulare) 2. Come inserire i dati nel prompt in modo che tu
possa elaborarli 3. Quali informazioni aggiuntive potrebbero essere necessarie per una completa analisi

### CHATGPT HA SCRITTO:
Ecco i passaggi dettagliati su come importare e strutturare i dati del bilancio per un’analisi completa, a partire
dal file contenente le tabelle di Stato Patrimoniale e Conto Economico.
Passo 1: Formattazione corretta dei dati
Prima di importare i dati per l’analisi, assicurati che il file sia formattato correttamente, idealmente in formato
CSV. Se il file è già in formato CSV, ecco cosa verificare:
• Intestazioni chiare: Ogni colonna dovrebbe avere un’intestazione chiara, ad esempio: “Voci”, “2023 (€)”,
“2024 (€)”.
• Valori numerici: Verifica che tutti i valori siano espressi in formato numerico, senza caratteri speciali (ad
esempio, evita il separatore di migliaia come il punto o la virgola per i decimali).
• Voci distinte: Assicurati che ogni riga contenga una voce distinta del bilancio, come “Immobilizzazioni”,
“Crediti”, ecc.
Ecco un esempio di come il file CSV dovrebbe apparire:
Voci,2023 (€),2024 (€)
A) Crediti verso soci per versamenti ancora dovuti,,
B) Immobilizzazioni,,
I. Immobilizzazioni immateriali,1.000.000,950.000
1. Costi di impianto e ampliamento,100.000,80.000
...
Passo 2: Inserimento dei dati nel prompt
Una volta verificato che il file è formattato correttamente, segui questi passaggi per caricare i dati nel modello
per l’analisi:
1. Carica il file in CSV: Dovrai caricare il file CSV o incollare i dati in un formato tabulare nel prompt.
Esempio di prompt per il caricamento del file: “Ho un file CSV con le tabelle di Stato Patrimoniale e Conto
Economico. Posso fornirti i dati per l’analisi?”
2. Struttura i dati nel prompt: Se non puoi caricare direttamente il file, puoi fornire i dati manualmente,
seguendo una struttura ordinata come l’esempio mostrato sopra.
Esempio di prompt per inserimento manuale dei dati:
Stato Patrimoniale 2023 e 2024:
Voci,2023 (€),2024 (€)
I. Immobilizzazioni immateriali,1.000.000,950.000
1. Costi di impianto e ampliamento,100.000,80.000
...

<!-- Pagina 80 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
79
3.
Fornisci entrambi gli esercizi: Se il file include bilanci per più esercizi (es. 2023 e 2024), assicurati di
fornire i dati per ogni anno separatamente, ma mantenendo la stessa struttura.
Passo 3: Informazioni aggiuntive per l’analisi
Oltre ai dati di bilancio, potresti dover fornire ulteriori informazioni per un’analisi più completa:
1. Settore dell’azienda: Fornire informazioni sull’industria in cui opera l’azienda (ad esempio, produzione di
chip) aiuta a contestualizzare l’analisi.
2. Obiettivi dell’analisi: Definisci cosa desideri ottenere dall’analisi del bilancio. Alcuni esempi possono essere:
o   Calcolo degli indicatori finanziari (ROE, ROI, ROS).
o   Analisi della liquidità e solidità patrimoniale.
o   Confronto delle performance tra anni diversi.
3. Particolari economici: Includi eventuali note su eventi straordinari o cambiamenti economici significativi
che possono influenzare i risultati finanziari (ad esempio, ristrutturazioni aziendali, nuove acquisizioni, ecc.).
Conclusione
Seguendo questi passaggi, potrai importare e strutturare correttamente i dati del bilancio per l’analisi con un
modello di linguaggio come ChatGPT. Se desideri procedere con l’analisi del file che hai caricato, fammi sapere,
e lo esaminerò per estrarne i dati necessari.

### PROMPT
Ho scelto di utilizzare la riclassificazione dello Stato Patrimoniale secondo il criterio finanziario e la
riclassificazione del Conto Economico a valore aggiunto. Utilizzando i dati che ti ho fornito nella Fase 1, per favore:
1. Applica questi metodi di riclassificazione ai dati del bilancio 2. Mostra il risultato della riclassificazione in un
formato chiaro e leggibile 3. Evidenzia eventuali voci o calcoli particolari che hai dovuto effettuare durante il
processo di riclassificazione 4. Spiega brevemente il significato delle principali sezioni del bilancio riclassificato

### CHATGPT HA SCRITTO:
Attivo Corrente
Voci
2023 (€)
2024 (€)
0
A) Crediti verso soci per versamenti ancora dovuti
13
2. Crediti
1.000.000
900.000
15
I. Rimanenze
2.500.000
2.700.000
19
II. Crediti
5.000.000
4.500.000
20
1. Crediti verso clienti
4.000.000
3.500.000
21
2. Crediti tributari
500.000
500.000
24
IV. Disponibilità liquide
1.000.000
1.200.000
Passivo Corrente
Voci
2023 (€)
2024 (€)
46
2. Debiti verso banche
3.000.000
2.800.000
47
3. Debiti verso fornitori
2.500.000
2.600.000
48
4. Debiti tributari
1.200.000
1.100.000

<!-- Pagina 81 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
80
Attivo Fisso
Voci
2023 (€)
2024 (€)
1
B) Immobilizzazioni
2
I. Immobilizzazioni immateriali
1.000.000
950.000
6
II. Immobilizzazioni materiali
10.000.000
9.800.000
11
III. Immobilizzazioni finanziarie
2.000.000
1.800.000
Passivo Consolidato
Voci
2023 (€)
2024 (€)
45
1. Obbligazioni
2.500.000
2.300.000
Conto Economico Riclassificato
Voci
2023 (€)
2024 (€)
51
A) Valore della produzione
56
Totale Valore della produzione
30.750.000
28.650.000
57
B) Costi della produzione
62
Totale Costi della produzione
28.100.000
26.560.000
Ecco il risultato della riclassificazione dello Stato Patrimoniale e del Conto Economico che hai richiesto. Ora ti
fornirò un riepilogo del significato delle principali sezioni e calcoli effettuati:
Stato Patrimoniale Riclassificato (Criterio Finanziario)
1.   Attivo Corrente :
o   Comprende le voci che indicano le risorse finanziarie a breve termine dell’azienda, come le  Rimanenze ,
i  Crediti  verso clienti e le  Disponibilità liquide . Questi rappresentano gli asset liquidi o facilmente
liquidabili che l’azienda utilizza per finanziare le operazioni quotidiane.
2.   Passivo Corrente:
o   Includono i  Debiti verso fornitori ,  Debiti verso banche  e  Debiti tributari . Questi sono obblighi finanziari
a breve termine che l’azienda deve pagare entro l’anno successivo.
3.   Attivo Fisso:
o   Composto dalle  Immobilizzazioni  (materiali, immateriali e finanziarie), rappresenta gli investimenti a
lungo termine dell’azienda, come impianti, macchinari, brevetti e partecipazioni.
4.   Passivo Consolidato:
o   In questa sezione rientrano le  Obbligazioni  e altri debiti a lungo termine. Si tratta di passività finanziarie
che non devono essere rimborsate immediatamente, ma nel medio-lungo termine.
Conto Economico Riclassificato (Valore Aggiunto)
1.   Valore della Produzione :
o   Rappresenta i ricavi generati dalle vendite di beni e servizi, più eventuali incrementi di rimanenze e
immobilizzazioni per lavori interni. In questo caso, include le voci come  Ricavi delle vendite ,  Variazioni
delle rimanenze  e  Altri ricavi e proventi .
2.   Costi della Produzione :
o   Includono i  costi per materie prime ,  costi per servizi ,  costi del personale  e  ammortamenti . Questi
rappresentano le spese sostenute per produrre i beni o servizi venduti.
Calcoli particolari:

<!-- Pagina 82 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
81
•
Valore Aggiunto : Nella riclassificazione a valore aggiunto, il “Valore Aggiunto” si ottiene sottraendo i
costi variabili (come quelli per materie prime e servizi) dal  Valore della Produzione . Questo valore indica
quanto l’azienda ha contribuito alla produzione con le proprie risorse interne, come il lavoro e
l’organizzazione.
Se desideri approfondire ulteriormente o hai bisogno di aggiustamenti, fammi sapere!

### PROMPT
Esegui il calcolo del valore aggiunto, dell’EBITDA e dell’EBIT

### ChatGPT ha scritto:
Calcolo Valore Aggiunto, EBITDA e EBIT
Indicatori
2023 (€)
2024 (€)
Valore Aggiunto
10750000
9850000
EBITDA
5750000
5150000
EBIT
4250000
3750000
Ho eseguito i calcoli del  Valore Aggiunto ,  EBITDA  e  EBIT  per gli esercizi 2023 e 2024. Puoi visualizzare i risultati
nella tabella che ho mostrato. Se hai bisogno di ulteriori chiarimenti o di altri calcoli, fammi sapere!

### PROMPT
Basandoti sul bilancio riclassificato 2023 e 2024, per favore calcola e interpreta i seguenti indicatori di bilancio
per singolo anno 2023 e 2024, indicando anche le formule di calcolo: 1. Indici di liquidità: * Indice di liquidità
corrente * Indice di liquidità immediata (Quick Ratio) 2. Indici di solidità patrimoniale: * Indice di indebitamento
(Leverage) * Indice di copertura delle immobilizzazioni 3. Indici di redditività: * ROE (Return on   Equity) * ROI
(Return on Investment) * ROS (Return on Sales) 4. Indici di efficienza: * Rotazione del capitale investito * Giorni
medi di incasso dei crediti * Giorni medi di pagamento dei debiti Per ciascun indicatore, fornisci: * Il valore
calcolato * Una breve spiegazione del suo significato * Un’interpretazione nel contesto dell’azienda analizzata *
Eventuali soglie o valori di riferimento per l’industria, se applicabili

### ChatGPT ha scritto:
Indicatori di Bilancio 2023 e 2024
Indicatori
2023 (€)
2024 (€)
Indice di liquidità corrente
0.8035714285714286
0.839622641509434
Indice di liquidità immediata (Quick Ratio)
0.5803571428571429
0.5849056603773585
Indice di indebitamento (Leverage)
1.3365853658536586
1.323076923076923
Indice di copertura delle immobilizzazioni
0.7884615384615384
0.7768924302788844
ROE
0.14634146341463414
0.12307692307692308
ROI
0.19318181818181818
0.17482517482517482
ROS
0.14166666666666666
0.13392857142857142
Rotazione del capitale investito
1.3636363636363635
1.3053613053613053
Giorni medi di incasso dei crediti
60.83333333333333
58.66071428571429
Giorni medi di pagamento dei debiti
60.83333333333333
67.78571428571429

<!-- Pagina 83 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
82
Ho calcolato gli indicatori di bilancio per gli esercizi 2023 e 2024. Ecco una breve spiegazione e interpretazione
per ciascun indicatore:
1. Indici di liquidità
•
Indice di liquidità corrente (2023: 0.80, 2024: 0.84) : Misura la capacità dell’azienda di coprire i debiti a
breve termine con le attività correnti. Un valore inferiore a 1 indica una potenziale difficoltà nel
soddisfare gli impegni a breve termine.
•
Quick Ratio (2023: 0.58, 2024: 0.58) : Valuta la liquidità immediata dell’azienda, escludendo le
rimanenze. Anche qui, valori inferiori a 1 suggeriscono una possibile tensione di liquidità.
2. Indici di solidità patrimoniale
•
Indice di indebitamento (Leverage) (2023: 1.34, 2024: 1.32) : Esprime il rapporto tra il totale dei debiti
e il patrimonio netto. Valori intorno a 1 indicano una situazione equilibrata, mentre valori più alti
segnalano un utilizzo più intensivo del debito.
•
Indice di copertura delle immobilizzazioni (2023: 0.79, 2024: 0.78) : Misura la capacità del patrimonio
netto di coprire le immobilizzazioni. Valori inferiori a 1 indicano che l’azienda si affida anche a fonti di
finanziamento esterne per le immobilizzazioni.
3. Indici di redditività
•
ROE (2023: 14.6%, 2024: 12.3%) : Indica la redditività del patrimonio netto. Valori positivi suggeriscono
una buona performance, con un leggero calo nel 2024.
•
ROI (2023: 13.3%, 2024: 11.5%) : Misura la redditività degli investimenti totali dell’azienda. Anche in
questo caso, c’è un leggero calo nel 2024.
•
ROS (2023: 14.2%, 2024: 13.4%) : Indica il margine operativo lordo rispetto ai ricavi di vendita. Un ROS
costante suggerisce una gestione operativa stabile.
4. Indici di efficienza
•
Rotazione del capitale investito (2023: 1.37, 2024: 1.36) : Valuta l’efficienza con cui l’azienda utilizza il
capitale investito per generare ricavi. Un valore sopra 1 è considerato positivo.
•
Giorni medi di incasso dei crediti (2023: 60.8, 2024: 58.7) : Mostra la velocità con cui l’azienda riscuote
i crediti. Valori tra 60 e 90 giorni sono comuni nel settore.
•
Giorni medi di pagamento dei debiti (2023: 60.8, 2024: 67.7) : Indica il tempo medio di pagamento dei
debiti verso i fornitori. Un incremento può segnalare una gestione più dilatata dei pagamenti.
Se desideri ulteriori dettagli o chiarimenti su uno specifico indicatore, fammi sapere!

### PROMPT
Basandoti sull’analisi effettuata nelle fasi precedenti, genera un report finale che includa: 1. Un riepilogo esecutivo
(massimo 250 parole) che evidenzi i principali risultati dell’analisi e le conclusioni chiave 2. Una sezione dedicata
alla presentazione dei bilanci riclassificati, con brevi commenti sulle principali voci e variazioni 3. Un’analisi
dettagliata degli indicatori calcolati nella Fase 4, includendo grafici o tabelle comparative per facilitare la
comprensione 4. Una sezione di “Punti di forza e aree di miglioramento” che identifichi: * I principali punti di
forza dell’azienda emersi dall’analisi * Le aree che potrebbero richiedere attenzione o miglioramento * Eventuali
rischi o opportunità future basate sui trend identificati 5. Raccomandazioni: * Suggerimenti specifici per
migliorare la performance finanziaria * Possibili strategie per affrontare le criticità identificate * Aree che
potrebbero richiedere un’analisi più approfondita 6. Una conclusione che riassuma i punti chiave e fornisca una
prospettiva generale sulla salute finanziaria dell’azienda Assicurati che il report sia scritto in un linguaggio chiaro
e professionale, adatto sia per esperti finanziari che per manager non specializzati in finanza

### CHATGPT HA SCRITTO:
Report Finale di Analisi Finanziaria per Alfa S.p.A.

<!-- Pagina 84 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
83
1. Riepilogo Esecutivo
L’analisi finanziaria di Alfa S.p.A. per gli anni 2023 e 2024 ha evidenziato una solida struttura patrimoniale, con
indici di liquidità e indebitamento relativamente stabili nel tempo. Tuttavia, l’azienda presenta una leggera
flessione nella redditività e alcuni segnali di potenziale tensione finanziaria, soprattutto nella gestione della
liquidità immediata. Nonostante ciò, Alfa S.p.A. ha dimostrato di mantenere una buona efficienza operativa,
come dimostrato dalla rotazione del capitale investito e dai margini di redditività stabili. È fondamentale
monitorare da vicino il ciclo di incasso e pagamento, poiché un aumento del tempo medio di pagamento
potrebbe indicare difficoltà nel far fronte alle obbligazioni. Nel complesso, l’azienda si trova in una posizione
solida, con margini di miglioramento nelle aree di gestione del capitale circolante e di contenimento dei costi.
2. Bilanci Riclassificati
Stato Patrimoniale (Riclassificato - Criterio Finanziario)
•   Attivo Corrente  (2023: €9M, 2024: €8.9M): Le disponibilità liquide sono aumentate nel 2024, segnalando
una maggiore capacità di copertura immediata dei debiti.
•   Attivo Fisso  (2023: €13M, 2024: €12.55M): Leggera riduzione delle immobilizzazioni, possibile effetto di
disinvestimenti o minore crescita negli investimenti a lungo termine.
•   Passivo Corrente  (2023: €11.2M, 2024: €10.6M): Riduzione dei debiti a breve termine, segnale positivo per
la gestione delle obbligazioni correnti.
Conto Economico (Riclassificato - Valore Aggiunto)
•   Valore della Produzione  (2023: €30.75M, 2024: €28.65M): Leggera contrazione dei ricavi nel 2024,
probabilmente dovuta a fluttuazioni di mercato o riduzione della domanda.
•   EBITDA  (2023: €5.75M, 2024: €5.15M): La redditività operativa si mantiene su livelli buoni, ma in calo,
richiedendo attenzione alla gestione dei costi.
3. Analisi degli Indicatori di Bilancio
Indicatore
2023
2024
Indice di liquidità corrente
0.80
0.84
Quick Ratio
0.58
0.58
Leverage
1.34
1.32
Copertura Immobilizzazioni
0.79
0.78
ROE
14.6%
12.3%
ROI
13.3%
11.5%
ROS
14.2%
13.4%
Rotazione Capitale Investito
1.37
1.36
Giorni medi di incasso crediti
60.8 giorni
58.7 giorni
Giorni medi di pagamento debiti
60.8 giorni
67.7 giorni
Interpretazione :
•
Liquidità : Gli indici di liquidità corrente e Quick Ratio segnalano la necessità di migliorare la gestione
del capitale circolante, specialmente per aumentare la liquidità immediata.
•
Indebitamento : Il leverage è stabile, indicando un buon equilibrio tra debiti e patrimonio netto.
•
Redditività : Nonostante il calo dei margini, l’azienda resta sufficientemente redditizia con un ROE e ROI
che rimangono sopra la media industriale.
•
Efficienza : Il ciclo di incasso è ben gestito, ma i giorni medi di pagamento dei debiti sono in aumento,
suggerendo una gestione più prolungata dei debiti.
4. Punti di Forza e Aree di Miglioramento
Punti di Forza:

<!-- Pagina 85 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
84
•
Redditività Operativa Stabile : Nonostante la lieve contrazione del 2024, Alfa S.p.A. continua a generare
buoni margini operativi.
•
Efficienza nella gestione dei crediti : Il ciclo di incasso è migliorato, riducendo i giorni medi di riscossione
dei crediti.
Aree di Miglioramento:
•
Liquidità Immediata : L’indice di liquidità immediata è basso, segnalando il bisogno di aumentare le
riserve liquide o ridurre le passività a breve termine.
•
Gestione dei Debiti : L’aumento dei giorni medi di pagamento potrebbe essere un segnale di difficoltà
nel gestire i flussi di cassa a breve termine.
Rischi e Opportunità:
•
Rischi : Se non controllata, la diminuzione dei margini e l’aumento dei tempi di pagamento potrebbero
ridurre la capacità dell’azienda di onorare i propri debiti.
•
Opportunità : Un miglioramento nella gestione del capitale circolante potrebbe sbloccare liquidità e
ridurre il rischio di insolvenza.
5. Raccomandazioni
•
Migliorare la gestione della liquidità : Ridurre l’accumulo di rimanenze e incrementare le disponibilità
liquide.
•
Ottimizzare i costi operativi : Identificare aree in cui ridurre le spese generali, come i costi di servizi e
materie prime, per mantenere i margini.
•
Strategie di finanziamento : Esplorare finanziamenti a lungo termine per ridurre la pressione sui debiti a
breve termine.
6. Conclusione
Alfa S.p.A. si presenta come un’azienda solida con buoni livelli di efficienza e redditività. Tuttavia, ci sono aree di
miglioramento, specialmente nella gestione della liquidità e del capitale circolante. Se affrontati correttamente,
questi aspetti permetteranno all’azienda di migliorare ulteriormente la sua posizione finanziaria nel lungo
termine.

## 7.1.   Conclusione dell’esercitazione
In conclusione, il software di AI, seguendo le richieste dell’utente ha generato una guida passo passo,
completa anche di prompt da utilizzare in tutte le fasi, per impostare una analisi di bilancio. I prompt
suggeriti nell’esempio da ChatGPT nelle varie fasi di elaborazione si sono rilevati essere efficaci. Tuttavia,
rimane sempre da considerare la regola di base, vale a dire che le risposte fornite da una AI possono
essere soggette a errori ed è quindi compito dell’utente/professionista verificarne il contenuto.

<!-- Pagina 86 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
85

## 8.   Formazione

## 8.1.   La Ricerca in manuali
L’obiettivo di questa esercitazione è di dimostrare come sia possibile estrarre informazioni da manuali
o guide operative.

### Esempio: Manuale operativo per il deposito dei bilanci al registro delle imprese
In questo caso d’uso ci facciamo aiutare da ChatGPT nella versione 4o per ricercare informazioni
all’interno del Manuale operativo per il deposito dei bilanci al registro delle imprese.
Come possiamo vedere sotto ho caricato nella chat di ChatGPT il file pdf del Manuale e gli ho chiesto
di spiegarmi cosa avessi caricato. Questo serve per avere conferma che il file fosse stato correttamente
caricato e “letto” da ChatGPT.

### PROMPT
Ho caricato un file. Sai dirmi in estrema sintesi cosa ho caricato?

### La risposta di ChatGPT è stata quella riportata qui sotto:
Hai caricato il “Manuale operativo per il deposito dei bilanci al registro delle imprese per l’anno 2024” pubblicato
da Unioncamere. Questo documento è una guida dettagliata per le imprese italiane su come compilare e
depositare i bilanci e gli elenchi soci presso il registro delle imprese. Il manuale copre vari aspetti tra cui:
1.   Formati di bilancio : ordinario, abbreviato e delle micro-imprese.
2.   Tassonomia XBRL : istruzioni per la redazione, validazione e firma dell’istanza XBRL.
3.   Termini e modalità di presentazione : quali moduli utilizzare, predisposizione dei documenti, dichiarazioni
di conformità e sottoscrizione.
4.   Particolarità per specifici tipi di imprese : società quotate, cooperative, società benefit, consorzi, start-up
innovative, ecc.
5.   Diritti di segreteria e imposta di bollo : informazioni sui costi legati al deposito.
6.   Sanzioni : penalità per mancata conformità.
7.   Qualità della banca dati bilanci : indicazioni per garantire la precisione e l’affidabilità dei dati depositati.
Questo documento è essenziale per garantire che le imprese seguano le corrette procedure legali e tecniche per
il deposito dei bilanci, assicurando conformità alle normative vigenti.
A questo punto è stato chiesto a ChatGPT:

### PROMPT
Mi servono delle informazioni specifiche sul deposito bilancio di una startup, puoi darmi indicazioni precise?
Verifica la risposta prima di darmela per essere sicuro sia esatta.

<!-- Pagina 87 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
86

### LA RISPOSTA DI CHATGPT È STATA QUELLA RIPORTATA SOTTO:
Ecco le informazioni specifiche sul deposito del bilancio di una startup innovativa, estratte dal manuale operativo
di Unioncamere:
Esenzione da Diritti di Segreteria e Imposta di Bollo
Le startup innovative, iscritte nella sezione speciale del Registro delle Imprese, sono esenti dal pagamento dei
diritti di segreteria e dell’imposta di bollo per il deposito dei bilanci. Questa esenzione dura fino al quinto anno
dalla costituzione della startup. Le startup che beneficiano di una proroga di dodici mesi del diritto di permanenza
nella sezione speciale (come previsto dall’art. 38 co. 5 del D.L. 34/2020) possono continuare a godere di questa
esenzione fino al sessantesimo mese dalla costituzione .
Termini e Documentazione Necessaria
Il bilancio di esercizio deve essere depositato entro 30 giorni dalla data del verbale di approvazione. La
documentazione richiesta per il deposito include:
1.   Una copia del bilancio composta da:
o   Stato Patrimoniale
o   Conto Economico
o   Rendiconto Finanziario (obbligatorio solo per il bilancio ordinario)
o   Nota Integrativa (esclusi i bilanci delle micro-imprese) .
2.   Relazione sulla gestione (obbligatoria per il bilancio ordinario, non necessaria per il bilancio abbreviato e
per le micro-imprese) .
3.   Verbale di assemblea che ha approvato il bilancio o, in caso di decisione scritta, il verbale della
deliberazione di approvazione del bilancio .
4.   Relazione del Collegio Sindacale o del soggetto incaricato della revisione legale dei conti, se esistente .
Certificazione Legale del Bilancio
Le PMI innovative devono depositare la certificazione legale del bilancio d’esercizio e dell’eventuale bilancio
consolidato secondo le regole del D.Lgs. 39/2010. Questa certificazione, redatta da un revisore contabile o da una
società di revisione, costituisce parte integrante del bilancio e deve essere presentata congiuntamente al bilancio
all’assemblea.
Mantenimento dei Requisiti
Le startup innovative devono aggiornare le informazioni e mantenere i requisiti almeno una volta all’anno entro
30 giorni dall’approvazione del bilancio e comunque entro sei mesi dalla chiusura di ciascun esercizio. Questi
adempimenti devono essere effettuati tramite una pratica di Comunicazione Unica e non possono essere allegati
al bilancio .
Tassonomia XBRL
Per documentare i requisiti relativi alle spese di ricerca e sviluppo, le startup innovative devono utilizzare il campo
testuale “Informazioni relative a startup, anche a vocazione sociale, e PMI innovative” presente nella sezione
“Bilancio micro, altre informazioni” della tassonomia XBRL.
Queste informazioni coprono i principali aspetti del deposito bilancio per una startup innovativa, come descritto
nel manuale operativo Unioncamere per il 2024.
Come avrete letto sopra nella domanda a ChatGPT, per avere maggiore sicurezza nella correttezza della

### risposta, gli è stato chiesto espressamente di verificare la risposta prima di fornirla.  Questo è un primo

### metodo, molto semplice, per evitare le così dette “allucinazioni”

<!-- Pagina 88 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
87

### Ricerca su manuali “riservati”
La ricerca sopra illustrata è sicuramente il modo più semplice e veloce per fare ricerche all’interno di
un manuale. Il problema che pone, però, è che in questo modo il file caricato in ChatGPT resta nella
memoria dello stesso e non è più riservato.
Per ovviare a questo inconveniente esistono vari metodi. Eccone alcuni:
-   Eliminare nelle impostazioni di ChatGPT – controlli dati -- Migliora il modello per tutti, la possibilità
per ChatGPT di conservare i dati che gli vengono forniti
-   Sottoscrivere la versione Team di ChatGPT che ha maggiori controlli sulla sicurezza e sulla privacy
-   utilizzare delle applicazioni specifiche che funzionano come ChatGPT ma lavorano in locale senza
che i dati vengano immessi nella rete.

## 8.2.   Creazione di Piani di formazione personalizzati
La presente analisi affronta un argomento di facile comprensione e accessibile ad una vasta platea di
utenti. Programmare un corso su un software così ampiamente diffuso a livello internazionale come
Excel ha permesso alle IA consultate di disporre di un’enorme quantità di materiale di supporto e
documentazione, reperibile su tutti i supporti divulgativi oggi utilizzati.
Questa ampia disponibilità di risorse consente all’I.A. la risposta non solo agevole, ma anche
ampiamente supportata da fonti aggiornate e affidabili, facilitando la redazione di testo comprensibile
e coerente con quanto domandato.
Le domande sono state rivolte alle 2 I.A. di maggiore diffusione (ChatGPT 4o a pagamento e Gemini
versione gratuita). Sono state utilizzate due tra i maggiori competitor sia per testare sia per verificare
la differenza tra i risultati delle versioni a pagamento o a titolo gratuito.
Di seguito sono riportate le domande (i prompt) con le risposte dei due software di LLM raffrontate in
colonne affiancate.

### 1^ Domanda

### PROMPT

### Crea un programma di formazione in 10 lezioni sul software Excel con esercizi e test di valutazione
CHAT GPT RISPOSTA:
Creare un programma di formazione su Excel in 10
lezioni, completo di esercizi e test di valutazione, è
un’ottima idea per fornire una solida base su questo
potente strumento. Di seguito trovi un programma
strutturato che copre dalle basi fino a concetti più
avanzati.
GEMINI RISPOSTA:
Assolutamente! Ecco una proposta di programma di
formazione su Excel, suddiviso in 10 lezioni, con
esercizi e test di valutazione:
Programma di Formazione Excel
Livello:  Base (adattare in base al pubblico)

<!-- Pagina 89 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
88
Lezione 1: Introduzione a Excel
●   Obiettivi:
o   Familiarizzare con l’interfaccia di Excel.
o   Comprendere il concetto di celle, colonne,
righe e fogli di lavoro.
o   Inserimento e modifica dei dati.
o   Salvare e aprire file.
●   Esercizi:
o   Creare un nuovo foglio di lavoro e inserire
dati semplici (nomi e numeri).
o   Salvare il foglio di lavoro con un nome specifico.
●   Test di valutazione:
o   Domande a scelta multipla sull’interfaccia di
Excel e semplici esercizi pratici di inserimento
e modifica dei dati.
Lezione 2: Formattazione di Base
●   Obiettivi:
o   Applicare formattazioni base (grassetto,
corsivo, colore delle celle).
o   Formattare numeri, date e testi.
o   Allineamento delle celle e formattazione
condizionale semplice.
●   Esercizi:
o   Formattare un foglio di lavoro con testo,
numeri e date in modo ordinato e leggibile.
o   Applicare una formattazione condizionale
semplice.
●   Test di valutazione:
o   Esercizi di formattazione su un foglio
predefinito.
Lezione 3: Funzioni e Formule di Base
●   Obiettivi:
o   Comprendere l’uso delle formule e delle
funzioni.
o   Utilizzo di funzioni aritmetiche di base
(SOMMA, MEDIA, MIN, MAX).
o   Utilizzare riferimenti relativi e assoluti.
●   Esercizi:
o   Creare un semplice foglio di calcolo con
formule per calcolare il totale, la media e il
massimo dei dati inseriti.
●   Test di valutazione:
o   Risoluzione di problemi con l’uso di formule
di base in Excel.
Obiettivo:  Acquisire le competenze di base per
utilizzare Excel in modo efficace per l’analisi dei dati e
la creazione di report.
Lezione 1: Introduzione a Excel
●   Argomenti:  Interfaccia, fogli di lavoro, celle,
righe e colonne, formati di file.
●   Esercizi:  Creazione di un nuovo foglio di lavoro,
formattazione delle celle, inserimento di dati.
●   Test:  Domande a scelta multipla sull’interfaccia
e le funzionalità di base.
Lezione 2: Formule e Funzioni di Base
●   Argomenti:  Operatori aritmetici, formule di
base, funzioni SUM, AVERAGE, COUNT.
●   Esercizi:  Calcolo di somme, medie, conteggi su
range di dati.
●   Test:  Esercizi pratici sulla creazione di formule
semplici.
Lezione 3: Formattazione Condizionale
●   Argomenti:  Evidenziazione di celle in base a
criteri, scale di colore, icone.
●   Esercizi:  Formattazione di dati in base a valori,
creazione di regole personalizzate.
●   Test:
Domande
a
scelta
multipla
sulla
formattazione condizionale.
Lezione 4: Grafici
●   Argomenti:  Tipi di grafici, creazione di grafici,
personalizzazione.
●   Esercizi:  Creazione di grafici a barre, a linee, a
torta.
●   Test:  Esercizi pratici sulla creazione di grafici.
Lezione 5: Tabelle Pivot
●   Argomenti:  Creazione di tabelle pivot, analisi dei
dati aggregati.
●   Esercizi:  Creazione di tabelle pivot semplici e
complesse.
●   Test:  Domande a scelta multipla sulle tabelle pivot.
Lezione 6: Funzioni LOGICHE (SE, E, O) e VLOOKUP
●   Argomenti:  Funzioni logiche, ricerca di valori.
●   Esercizi:  Creazione di formule logiche, ricerca di
dati in tabelle.
●   Test:  Esercizi pratici sull’utilizzo delle funzioni
logiche e VLOOKUP.

<!-- Pagina 90 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
89
Lezione 4: Gestione dei Dati
●   Obiettivi:
o   Ordinare e filtrare i dati.
o   Creare e utilizzare tabelle.
o   Inserire e gestire semplici grafici (tabelle
pivot introdotte).
●   Esercizi:
o   Creare un elenco di dati, ordinarli e applicare
filtri.
o   Creare una tabella e inserire un grafico base.
●   Test di valutazione:
o   Domande teoriche e pratiche sulla gestione
dei dati in Excel.
Lezione 5: Funzioni Logiche
●   Obiettivi:
o   Comprendere e utilizzare funzioni logiche
(SE, E, O).
o   Annidare funzioni logiche.
●   Esercizi:
o   Creare un foglio di lavoro che utilizzi la
funzione SE per determinare se un valore
soddisfa certe condizioni.
o   Annidare funzioni logiche per risolvere
problemi complessi.
●   Test di valutazione:
o   Esercizi sull’uso di funzioni logiche per creare
soluzioni dinamiche.
Lezione 6: Funzioni di Ricerca e Riferimento
●   Obiettivi:
o   Utilizzare le funzioni di ricerca e riferimento
(CERCA.VERT,
CERCA.ORIZZ,
INDICE,
CONFRONTA).
o   Capire l’importanza di questi strumenti nel
lavoro con grandi quantità di dati.
●   Esercizi:
o   Creare un elenco di dati e utilizzare
CERCA.VERT per recuperare informazioni
specifiche.
o   Esercizi su INDICE e CONFRONTA.
●
Test di valutazione:
o   Problemi pratici che richiedono l’uso di
funzioni di ricerca.
Lezione 7: Grafici e Visualizzazioni Avanzate
●   Obiettivi:
Lezione 7: Gestione dei Dati
●   Argomenti:  Ordinamento, filtraggio, convalida
dei dati.
●   Esercizi:  Ordinamento di dati, creazione di filtri
personalizzati.
●   Test:  Domande a scelta multipla sulla gestione
dei dati.
Lezione 8: Creazione di Report
●   Argomenti:
Formattazione
di
report,
intestazioni, piè di pagina.
●   Esercizi:  Creazione di report professionali.
●   Test:  Valutazione della capacità di creare report
ben strutturati.
Lezione 9: Introduzione a Power Query
●   Argomenti:
Connessione
a
dati
esterni,
trasformazione dei dati.
●   Esercizi:  Importazione di dati da diversi formati.
●   Test:  Domande a scelta multipla su Power
Query.
Lezione 10: Progetto Finale
●   Argomento:  Applicazione delle conoscenze
acquisite per risolvere un problema reale.
●   Esercizi:  Sviluppo di un progetto completo
utilizzando Excel.
●   Valutazione:  Valutazione del progetto finale
sulla base di criteri predefiniti.
Note:
●   Materiale didattico:  Presentazioni, esercitazioni
pratiche, casi studio.
●   Modalità:
Lezioni
frontali,
esercitazioni
individuali e di gruppo.
●   Valutazione:  Test a metà corso e esame finale.
●   Personalizzazione:  Adattare il programma in
base al livello degli allievi e alle loro esigenze
specifiche.
Strumenti utili:
●   Microsoft Excel:  Versione più recente.
●   Piattaforme e-learning:  Per erogare il corso
online.
●   Software di creazione di presentazioni:  Per
creare il materiale didattico.
Questo è solo un esempio, il programma può essere
personalizzato in base alle tue esigenze specifiche.

<!-- Pagina 91 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
90
o   Creare grafici avanzati (a torta, a barre, a
dispersione).
o   Personalizzare grafici per migliorare la
leggibilità.
●   Esercizi:
o   Creare
diversi
tipi
di
grafici
per
rappresentare dati complessi.
o   Personalizzare un grafico esistente con titoli,
legende e etichette dati.
●   Test di valutazione:
o   Creazione e personalizzazione di grafici
basati su un set di dati fornito.
Lezione 8: Tabelle Pivot e Analisi dei Dati
●   Obiettivi:
o   Creare e utilizzare tabelle pivot per l’analisi
dei dati.
o   Raggruppare e filtrare i dati nelle tabelle
pivot.
o   Utilizzare le funzionalità di calcolo avanzate
nelle tabelle pivot.
●   Esercizi:
o   Creare  una tabella pivot da un set di dati e
analizzare i risultati.
o   Applicare filtri e gruppi sui dati di una tabella
pivot.
●   Test di valutazione:
o   Esercizi di analisi dei dati con tabelle pivot.
Lezione 9: Automazione con Macro
●   Obiettivi:
o   Registrare e riprodurre macro semplici.
o   Modificare macro base con l’editor di VBA.
o   Comprendere le basi della programmazione
VBA.
●   Esercizi :
o   Registrare una macro per automatizzare una
serie di operazioni ripetitive.
o   Modificare una macro per includere logiche
condizionali.
●   Test di valutazione:
o   Creare e modificare una macro per eseguire
un compito specifico.
Lezione 10: Integrazione e Funzioni Avanzate
●   Obiettivi:
Vuoi che mi concentri su un aspetto specifico di
questo programma, come ad esempio gli esercizi o i
test di valutazione?
Inoltre, posso aiutarti a creare materiale didattico

### più specifico, come presentazioni o esercitazioni.

<!-- Pagina 92 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
91
o   Importare ed esportare dati da e verso altri
software (ad esempio, Access, Word, etc.).
o   Utilizzare
funzioni
avanzate
come
SOMMA.SE, CONTA.SE e formule array.
o   Creare modelli di Excel personalizzati.
●   Esercizi:
o   Importare un set di dati da un file CSV e
creare un modello di analisi.
o   Utilizzare funzioni avanzate per analizzare
dati complessi.
●   Test di valutazione:
o   Esercizi di integrazione dei dati e utilizzo di
funzioni avanzate per risolvere un problema
reale.
Considerazioni Finali
Ogni lezione dovrebbe includere una breve parte
teorica, seguita da esercizi pratici. Il test di valutazione
dovrebbe combinare domande teoriche con esercizi
pratici che coprano i concetti appresi durante la
lezione. Dopo l’ultima lezione, è possibile effettuare
un test finale che valuti l’apprendimento complessivo

### dell’intero corso.
Le due risposte come si può notare risultano complete e strutturate in maniera similare; Gemini - anche
se gratuito - in questo caso ha aggiunto del suo proponendo un programma di lezioni di Livello “Base
(adattare in base al pubblico)”
Prima di approfondire e sviluppare almeno una singola lezione proviamo a far sviluppare alle due IA
un programma di formazione avanzato in 10 lezioni sempre su Excel:

### 2^ Domanda

### PROMPT
Mi proponi il programma di formazione in 10 lezioni a livello Avanzato
CHAT GPT RISPOSTA:
Ecco un programma di formazione in 10 lezioni su
Excel a livello avanzato. Questo programma è pensato
per utenti che hanno già una solida comprensione
delle basi di Excel e desiderano approfondire le
funzionalità avanzate e le tecniche di automazione.
GEMINI RISPOSTA:
Assolutamente! Ecco una proposta di programma di
formazione su Excel a livello avanzato, pensato per chi
ha già una buona padronanza delle funzionalità di
base:

<!-- Pagina 93 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
92
Lezione 1: Funzioni Avanzate di Ricerca e Riferimento
●   Obiettivi:
o   Approfondire
l’uso
di
CERCA.VERT,
CERCA.ORIZZ, INDICE e CONFRONTA.
o   Utilizzare
funzioni
come
CERCA.X,
SE.ERRORE per gestire errori nelle ricerche.
o   Implementare ricerche dinamiche usando
formule combinate.
●   Esercizi:
o   Creare  formule avanzate utilizzando CERCA.X
e INDICE + CONFRONTA in combinazione.
o   Gestire errori di ricerca con SE.ERRORE.
●   Test di valutazione:
o   Problemi complessi che richiedono l’uso di
funzioni avanzate di ricerca e gestione degli
errori.
Lezione 2: Funzioni di Matrice e Formule Array
●   Obiettivi:
o   Comprendere e utilizzare formule array.
o   Implementare funzioni come SOMMA.SE,
CONTA.PIÙ.SE con matrici.
o   Creare formule dinamiche che restituiscono
più risultati.
●   Esercizi:
o   Utilizzare formule array per risolvere
problemi di calcolo complessi.
o   Applicare
SOMMA.PRODOTTO
con
condizioni multiple.
●   Test di valutazione:
o   Esercizi sull’uso di formule array in scenari reali.
Lezione 3: Automazione Avanzata con Macro e VBA
●   Obiettivi:
o   Registrare macro avanzate e modificarle in
VBA.
o   Creare macro per automazione complessa e
ripetitiva.
o   Introduzione
a
VBA:
cicli,
condizioni,
gestione degli errori.
●   Esercizi:
o   Scrivere una macro per automatizzare un
report complesso.
o   Modificare macro esistenti per includere
logiche condizionali e cicli.
●   Test di valutazione:
o   Creare una macro VBA che automatizzi un
compito specifico con controllo degli errori.
Programma di Formazione Excel Avanzato
Obiettivo:  Acquisire competenze avanzate per
utilizzare Excel come strumento potente per l’analisi
dei dati, la creazione di modelli complessi e
l’automazione di processi.
Lezione 1: Funzioni Avanzate e Array
●   Argomenti:
Funzioni
statistiche
avanzate
(STDEV, VAR, CORREL), funzioni di data e ora,
funzioni di ricerca e riferimento (INDEX,
MATCH), matrici e operazioni su array.
●   Esercizi:
Calcolo
di
deviazioni
standard,
correlazioni, creazione di tabelle dinamiche con
array.
Lezione 2: Tabelle Pivot Dinamiche Avanzate
●   Argomenti:
Creazione
di
tabelle
pivot
multidimensionali, calcoli personalizzati, filtri
avanzati, slicers.
●   Esercizi:  Analisi di grandi dataset, creazione di
report interattivi.
Lezione 3: Power Query
●   Argomenti:  Trasformazione avanzata dei dati,
unione
di
tabelle,
creazione
di
query
personalizzate, pulizia dei dati.
●   Esercizi:  Connessione a diverse fonti dati (SQL,
Web), pulizia e trasformazione di dati disordinati.
Lezione 4: Power Pivot
●   Argomenti:
Modellazione
dati
relazionali,
creazione di misure DAX, relazioni tra tabelle.
●   Esercizi:
Creazione
di
modelli
dati
multidimensionali, calcolo di KPI.
Lezione 5: VBA (Visual Basic for Applications)
●   Argomenti:  Introduzione a VBA, registrazione di
macro, creazione di moduli, controllo di flusso.
●   Esercizi:
Automazione
di
task
ripetitivi,
creazione di funzioni personalizzate.
Lezione 6: Analisi What-If e Scenari
●   Argomenti:  Tabella dati, Goal Seek, Solver,
analisi degli scenari.
●   Esercizi:
Simulazione
di
diversi
scenari,
ottimizzazione di modelli.
Lezione 7: Creazione di Dashboard Interattivi
●   Argomenti:
Slicer,
filtri,
formattazione
condizionale, controllo degli utenti.

<!-- Pagina 94 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
93
Lezione 4: Analisi dei Dati con Tabelle Pivot Avanzate
●   Obiettivi:
o   Approfondire l’uso delle tabelle pivot per
l’analisi avanzata.
o   Utilizzare calcoli personalizzati e campi
calcolati nelle tabelle pivot.
o   Creare tabelle pivot connessi a più fonti di dati.
●   Esercizi:
o   Creare
tabelle
pivot
complesse
che
includono calcoli personalizzati.
o   Utilizzare tabelle pivot per analizzare dati
provenienti da più fogli di lavoro.
●   Test di valutazione:
o   Risoluzione di casi studio di analisi dati
complessa con tabelle pivot.
Lezione 5: Dashboard Interattive e Visualizzazione
Avanzata
●   Obiettivi:
o   Creare dashboard interattivi utilizzando
strumenti di visualizzazione avanzata.
o   Utilizzare
controlli
come
barre
di
scorrimento, pulsanti e convalida dei dati.
o   Creare grafici avanzati e personalizzati
(grafici combinati, sparklines).
●   Esercizi:
o   Creare un dashboard interattivo che includa
grafici dinamici e filtri.
o   Personalizzare
grafici
per
migliorare
l’efficacia visiva della dashboard.
●   Test di valutazione:
o   Progettazione di un dashboard completo per
la visualizzazione dei KPI.
Lezione 6: Power Query e Power Pivot
●   Obiettivi:
o   Introduzione a
Power Query per la
trasformazione e manipolazione dei dati.
o   Utilizzare Power Pivot per creare modelli di
dati complessi.
o   Implementare
relazioni
tra
tabelle
e
utilizzare DAX (Data Analysis Expressions).
●   Esercizi:
o   Importare, pulire e trasformare dati con
Power Query.
o   Creare un modello di dati con Power Pivot e
scrivere formule DAX.
●   Test di valutazione:
●   Esercizi:  Creazione di dashboard personalizzati
per monitorare i KPI.
Lezione 8: Protezione dei Dati e Condivisione
●   Argomenti:  Protezione delle cartelle di lavoro,
condivisione di file, collaborazione in tempo reale.
●   Esercizi:
Configurazione
di
permessi,
condivisione di file su OneDrive.
Lezione 9: Geostatistica e Mappe
●   Argomenti:  Creazione di mappe, analisi spaziale
dei dati.
●   Esercizi:  Visualizzazione di dati geografici, analisi
di cluster.
Lezione 10: Progetto Finale
●   Argomento:  Applicazione delle conoscenze
acquisite per risolvere un problema complesso.
●   Esercizi:  Sviluppo di un progetto completo
utilizzando tutte le funzionalità avanzate di Excel.
Esercizi e Test:
●   Esercizi pratici:  Verranno proposti esercizi
sempre più complessi per consolidare le
competenze acquisite.
●   Casi studio:  Analisi di casi reali per applicare le
conoscenze teoriche.
●   Progetti:  Sviluppo di progetti individuali o di
gruppo per valutare la capacità di risolvere
problemi complessi.
Strumenti utili:
●   Microsoft Excel:  Versione più recente con
Power Pivot e Power Query.
●   Altre fonti dati:  Database SQL, file CSV, fogli di
calcolo esterni.
●   Software di controllo di versione:  Per gestire le
modifiche ai file.
Personalizzazione:
●   Il
programma
può
essere
ulteriormente
personalizzato in base alle esigenze specifiche
dei partecipanti, ad esempio focalizzandosi su
settori particolari (finanza, marketing, ecc.) o su
funzionalità
specifiche
(analisi
statistica,
simulazione).
Note:
●   Prerequisiti:
Ottima
conoscenza
delle
funzionalità di base di Excel.

<!-- Pagina 95 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
94
o   Esercizi complessi di manipolazione dati e
creazione di modelli con Power Query e
Power Pivot.
Lezione 7: Sicurezza e Condivisione di Documenti
●   Obiettivi:
o   Proteggere file Excel con password e
impostare livelli di accesso.
o   Condividere file Excel in modo sicuro e
collaborare in tempo reale.
o   Utilizzare strumenti di audit e controllo delle
modifiche.
●   Esercizi:
o   Configurare la protezione di un foglio di
lavoro con diversi livelli di accesso.
o   Creare  un file Excel collaborativo con
controllo delle modifiche.
●   Test di valutazione:
o   Test pratici sulla protezione, condivisione e
gestione delle modifiche di file Excel.
Lezione 8: Integrazione con Altri Software e
Automazione di Processi
●   Obiettivi:
o   Importare ed esportare dati tra Excel e altri
software (Access, SQL Server, Word).
o   Automatizzare processi utilizzando Excel in
combinazione con altri strumenti (ad esempio,
automatizzare l’invio di email con Outlook).
o   Integrare Excel con Power BI per analisi e
visualizzazioni avanzate.
●   Esercizi:
o   Creare un processo di importazione ed
esportazione dati tra Excel e un database SQL.
o   Automatizzare l’invio di report Excel via
email con VBA.
●   Test di valutazione:
o   Progettare un flusso di lavoro integrato tra
Excel e altri strumenti software.
Lezione 9: Modellazione e Previsioni con Excel
●   Obiettivi:
o   Creare modelli di previsione avanzati
utilizzando funzioni statistiche.
o   Utilizzare strumenti come la regressione
lineare, il forecast e l’analisi dei trend.
o   Implementare scenari what-if e analisi di
sensibilità.
●   Esercizi:
●   Materiale
didattico:
Presentazioni,
esercitazioni pratiche, casi studio, tutorial video.
●   Modalità:
Lezioni
frontali,
esercitazioni
individuali e di gruppo, laboratori pratici.
●   Valutazione:  Test intermedi, valutazione dei
progetti finali.
Questo programma è pensato per fornire una solida
base
nelle
funzionalità
avanzate
di
Excel,
preparando gli utenti a utilizzare il software in modo
professionale per l’analisi dei dati e la creazione di
modelli complessi.
Vuoi
approfondire
qualche
argomento
in
particolare?

<!-- Pagina 96 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
95
o   Creare un modello di previsione delle
vendite utilizzando dati storici.
o   Eseguire un’analisi di sensibilità per diversi
scenari di business.
●   Test di valutazione:
o   Realizzazione di previsioni accurate e analisi
di scenari complessi.
Lezione 10: Ottimizzazione e Soluzione di Problemi
con Solver
●   Obiettivi:
o   Utilizzare il componente aggiuntivo Solver
per risolvere problemi di ottimizzazione.
o   Creare modelli di ottimizzazione lineare e
non lineare.
o   Applicare Solver in contesti reali, come la
gestione delle risorse o la pianificazione
della produzione.
●   Esercizi:
o   Creare un modello di ottimizzazione dei costi
utilizzando Solver.
o   Risolvere un problema di allocazione delle
risorse con vincoli specifici.
●   Test di valutazione:
o   Problemi di ottimizzazione da risolvere con
Solver in scenari aziendali complessi.
Considerazioni Finali
Al termine del corso, è possibile prevedere un test finale
complesso che copra tutti gli argomenti trattati, con un
mix di domande teoriche e esercizi pratici. Questo
aiuterà a consolidare l’apprendimento e a verificare la
padronanza delle tecniche avanzate di Excel.
Come si può notare, entrambe sviluppano una risposta coerente e valida e per la quale richiedendo un
livello avanzato si propongono programmi differenti vista la numerosità di funzioni esistente nel
software EXCEL.
Proviamo ora ad approfondire una lezione di base prendendo ad esempio la lezione sui grafici proposte
da entrambe le IA nel programma di base.

### 3^ Domanda

### PROMPT
Mi sviluppi una lezione sul software Excel con argomento “Grafici e Visualizzazioni Avanzate” completa di
esercizi e test di valutazione finali

<!-- Pagina 97 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
96
CHAT GPT RISPOSTA:
Lezione: Grafici e Visualizzazioni Avanzate in Excel
Obiettivi della Lezione:
●   Creare grafici avanzati e personalizzati.
●   Comprendere l’utilizzo di grafici combinati per
rappresentare dati complessi.
●   Sviluppare dashboard interattive utilizzando
strumenti avanzati di visualizzazione.
●   Imparare a utilizzare le “Sparklines” per
visualizzazioni rapide e intuitive.
Struttura della Lezione:
1. Introduzione ai Grafici Avanzati
●   Tipi di Grafici Avanzati:
o   Grafici combinati (ad esempio, colonna +
linea).
o   Grafici a dispersione (Scatter Plot) e bolle.
o   Istogrammi e grafici a cascata (Waterfall).
o   Grafici a radar e ad area.
●   Personalizzazione dei Grafici:
o   Modifica degli assi (scala logaritmica, asse
secondario).
o   Aggiunta di linee di tendenza e barre di
errore.
o   Personalizzazione di colori, stili, e serie di
dati.
o   Inserimento di etichette personalizzate e
formattazione avanzata.
2. Creazione di Grafici Combinati
●   Creazione di un Grafico Combinato:
o   Passaggi per combinare grafici a colonne e
grafici a linee.
o   Utilizzo dell’asse secondario per dati con
scale diverse.
o   Personalizzazione delle serie di dati e
formattazione delle linee.
●   Esempio Pratico:
o   Creare un grafico che mostra le vendite
mensili
come
colonne
e
la
crescita
percentuale rispetto all’anno precedente
come linea.
3.
Visualizzazioni
Avanzate
con
Dashboard
Interattive
●   Introduzione  ai Dashboard:
GEMINI RISPOSTA:
Assolutamente! Ecco una lezione completa su “Grafici
e Visualizzazioni Avanzate” in Excel, con esercizi e test
di valutazione:
Lezione: Grafici e Visualizzazioni Avanzate in Excel
Obiettivi:
●   Esplorare i tipi di grafici avanzati disponibili in
Excel.
●   Personalizzare i grafici per una migliore
comprensione dei dati.
●   Creare
visualizzazioni
interattive
per
presentazioni efficaci.
Contenuti:
1. Introduzione ai Grafici Avanzati
●   Oltre i grafici di base:  Histograms, box plots,
scatter plots con linee di tendenza, grafici a
bolle.
●   Quando usarli:  Scenari adatti per ogni tipo di
grafico.
●   Personalizzazione:  Elementi grafici, etichette
dati, linee di griglia, colori.
2. Creazione di Grafici Avanzati
●   Step-by-step:  Procedura dettagliata per creare
diversi tipi di grafici.
●   Tipi di dati:  Come scegliere il tipo di grafico in
base ai dati.
●   Formule e funzioni:  Utilizzo di formule per
calcolare dati da visualizzare.
3. Personalizzazione dei Grafici
●   Stili  e formati:  Applicazione di stili predefiniti e
creazione di stili personalizzati.
●   Elementi  grafici:  Aggiunta di elementi come
immagini, forme e testo.
●   Etichette dati:  Formattazione delle etichette
per una migliore leggibilità.
4. Grafici Interattivi
●   Slicer e filtri:  Creazione di grafici interattivi con
slicer e filtri.
●   Dashboard:  Combinazione di più grafici in un
unico dashboard.
●   Power  View:  Creazione di visualizzazioni
interattive più complesse.

<!-- Pagina 98 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
97
o   Creazione di layout per dashboard in Excel.
o   Utilizzo
di
controlli
come
barre
di
scorrimento, pulsanti e convalida dei dati per
interattività.
●   Costruzione di un Dashboard:
o   Raccolta e preparazione dei dati per la
visualizzazione.
o   Creazione di un dashboard con grafici
dinamici collegati a filtri e controlli.
o   Personalizzazione della dashboard per una
presentazione professionale.
4. Sparklines e Visualizzazioni Compatte
●   Creazione di Sparklines:
o   Inserimento di Sparklines per rappresentare
tendenze all’interno di una singola cella.
o   Tipi
di
Sparklines:
linee,
colonne
e
vincitori/perdenti.
o   Personalizzazione e utilizzo delle Sparklines
per riepiloghi rapidi.
●   Esempio Pratico:
o   Aggiungere Sparklines a una tabella di dati
per mostrare l’andamento delle vendite per
ciascun prodotto.
Esercizi Pratici
Esercizio 1: Creazione di un Grafico Combinato
●   Obiettivo:  Creare un grafico combinato che
rappresenti i ricavi e il margine di profitto di
un’azienda per gli ultimi 12 mesi.
●   Istruzioni:
o   Inserisci i dati di ricavo mensile e margine di
profitto in un foglio di lavoro.
o   Crea un grafico a colonne per i ricavi.
o   Aggiungi una serie di dati per il margine di
profitto e rappresentala come linea.
o   Personalizza
il
grafico
con
un
asse
secondario per la serie di margine di profitto.
Esercizio 2: Costruzione di una Dashboard
●   Obiettivo :  Creare un dashboard interattivo che
permetta di visualizzare i dati di vendita per
regione e per prodotto.
●   Istruzioni:
o   Prepara i dati di vendita per regione e
prodotto in una tabella.
o   Crea grafici per le vendite per regione e per
prodotto.
Esercizi:
1.   Creazione di un istogramma:  Analizzare la
distribuzione dei salari in un’azienda.
2.   Box plot:  Confrontare la distribuzione dei prezzi
di diversi prodotti.
3.   Scatter plot con linea di tendenza:  Analizzare la
correlazione tra due variabili (es. vendite vs
spese pubblicitarie).
4.   Grafico a bolle:  Visualizzare tre variabili
contemporaneamente (es. vendite, profitti,
numero di clienti).
5.   Dashboard interattivo:  Creare un dashboard
per monitorare le vendite mensili di un
prodotto, con filtri per regione e categoria.
Test di Valutazione:
1.   Domande a scelta multipla:
o   Qual è il grafico più adatto per visualizzare la
distribuzione di una variabile continua?
o   Come si aggiunge una linea di tendenza a un
grafico a dispersione?
o   Qual è la funzione di un slicer in un grafico?
2.   Esercizio pratico:
o   Fornire un dataset e chiedere di creare un grafico
specifico con determinate caratteristiche.
o   Valutare la capacità di:
▪   Scegliere il grafico corretto.
▪   Personalizzare il grafico.
▪   Interpretare i risultati.
Materiali Aggiuntivi:
●   Esempi pratici:  Fornire esempi reali di utilizzo
dei grafici avanzati in diversi settori.
●   Tutorial video:  Creare tutorial dettagliati per
ogni tipo di grafico.
●   Risorse online:  Indicare risorse utili per
approfondire l’argomento.
Suggerimenti per l’insegnante:
●   Partecipazione  attiva:  Incoraggiare gli studenti
a sperimentare e creare i propri grafici.
●   Feedback
costruttivo:
Fornire
feedback
individuali per migliorare le competenze degli
studenti.

<!-- Pagina 99 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
98
o   Aggiungi un filtro per la selezione della
regione e collega il filtro ai grafici.
o   Personalizza la dashboard per presentare i
dati in modo chiaro e interattivo.
Esercizio 3: Utilizzo di Sparklines
●   Obiettivo:  Aggiungere Sparklines a una tabella
di dati per visualizzare l’andamento delle
vendite trimestrali.
●   Istruzioni:
o   Inserisci i dati di vendita trimestrale per
diversi prodotti.
o   Aggiungi Sparklines per ogni prodotto per
visualizzare l’andamento delle vendite.
o   Personalizza le Sparklines per migliorare la
leggibilità e l’efficacia visiva.
Test di Valutazione Finale
1.   Domande a Scelta Multipla:
o   Qual è il vantaggio principale dell’uso di un
grafico combinato rispetto a un grafico singolo?
o   Quale tipo di grafico è più adatto per
rappresentare la distribuzione di una
variabile continua?
o   Quando è utile utilizzare un asse secondario
in un grafico?
2.   Domanda Aperta:
o   Descrivi il processo per creare un dashboard
interattivo in Excel. Quali sono gli elementi
essenziali
e
come
possono
essere
personalizzati?
3.   Esercizio Pratico:
o   Crea un grafico avanzato per un dataset
fornito (ad esempio, un dataset che contiene
le vendite e i costi operativi di un’azienda su
base mensile). Aggiungi una linea di
tendenza e personalizza il grafico per
presentare i risultati in modo chiaro.
Consegna il file Excel con il grafico creato.
Materiali di Supporto
●   Foglio di lavoro Excel con i dati per gli esercizi.
●   Video tutorial (opzionale) che mostra passo per
passo come creare grafici avanzati e dashboard.
●   Documentazione PDF con i passaggi e i
suggerimenti per gli esercizi.
Conclusione
Questa lezione su “Grafici e Visualizzazioni Avanzate”
fornisce agli utenti le competenze necessarie per
●   Relazione con il mondo reale:  Collegare gli
esercizi
a
situazioni
reali
per
rendere
l’apprendimento più significativo.
Osservazioni:
●   Livello:  Adattare il livello di difficoltà degli
esercizi al livello di preparazione degli studenti.
●   Software:  Assicurarsi che gli studenti abbiano
accesso alla versione di Excel con le funzionalità
necessarie.
●   Tempo:  Prevedere un tempo adeguato per ogni
attività.
Questo è solo un esempio di lezione. Può essere
personalizzato e ampliato in base alle esigenze
specifiche del corso e degli studenti.
Vuoi che mi concentri su un aspetto specifico di
questa lezione, come ad esempio un tipo di grafico
particolare o la creazione di dashboard interattivi?

<!-- Pagina 100 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
99
rappresentare e analizzare dati complessi in Excel. Gli
esercizi pratici e il test di valutazione finale aiutano a
consolidare l’apprendimento e a verificare la
comprensione dei concetti trattati.
Anche in questo caso risposte accettabili da entrambe.
Ma tentiamo di approfondire un argomento specifico.

### 4^ Domanda

### PROMPT
Lezione Excel su Grafici combinati (ad esempio, colonna + linea) con dati di esempio
Chat GPT RISPOSTA:
Lezione: Grafici Combinati in Excel
Obiettivi della Lezione:
●   Imparare a creare grafici combinati in Excel,
come grafici a colonne + linea.
●   Comprendere l’utilizzo degli assi secondari per
rappresentare dati con scale diverse.
●   Personalizzare i grafici combinati per una
presentazione efficace.
1. Introduzione ai Grafici Combinati
●   Cos’è un Grafico Combinato?
o   Un grafico combinato in Excel è un grafico
che utilizza più tipi di grafici (come colonne e
linee) nello stesso spazio grafico per
rappresentare
dati
diversi.
Questo
è
particolarmente utile quando si vuole
mostrare dati che hanno diverse unità di
misura o range di valori.
●   Quando Utilizzare i Grafici Combinati?
o   Per confrontare serie di dati con scale
diverse.
o   Per visualizzare una serie di dati (ad esempio,
ricavi) come colonne e un’altra serie (ad
esempio, crescita percentuale) come linee.
2. Creazione di un Grafico Combinato
Esempio Pratico:
Supponiamo di avere i dati di un’azienda che includono
il fatturato mensile e il margine di profitto percentuale
Gemini RISPOSTA:
Lezione: Grafici Combinati in Excel (Colonna + Linea)
Obiettivi:
●   Comprendere l’utilità dei grafici combinati.
●   Creare grafici combinati colonna e linea in Excel.
●   Interpretare correttamente i dati rappresentati.
●   Personalizzare i grafici per una migliore
visualizzazione.
Perché i grafici combinati?
I grafici combinati sono particolarmente utili quando
si vogliono confrontare due serie di dati con scale di
misura diverse, o quando si vuole mostrare una
tendenza generale insieme a dei valori puntuali. Ad
esempio, si può usare un grafico combinato per
visualizzare sia il volume delle vendite (colonne) sia il
prezzo medio (linea) nel tempo.
Creazione di un grafico combinato (Colonna + Linea)
Esempio:  Supponiamo di avere i dati mensili delle
vendite di un prodotto (in unità) e il prezzo medio
unitario. Vogliamo visualizzare entrambe le serie di
dati in un unico grafico.
1.   Inserisci i dati:  Crea un foglio di calcolo con due
colonne: una per i mesi e una per le vendite.
Aggiungi una terza colonna per i prezzi medi.
2.   Seleziona i dati:  Seleziona tutte le celle
contenenti i dati (compresi i nomi delle colonne).
3.   Inserisci il grafico:  Vai alla scheda “Inserisci” e
scegli il tipo di grafico “Combinato”.

<!-- Pagina 101 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
100
per l’anno 2023. Vogliamo creare un grafico
combinato che mostri entrambi i dati in modo efficace.
Dati di Esempio:
Mese
Fatturato (€) Margine di Profitto (%)
Gennaio
50,000
20%
Febbraio
55,000
18%
Marzo
60,000
22%
Aprile
65,000
19%
Maggio
70,000
25%
Giugno
75,000
23%
Luglio
80,000
24%
Agosto
85,000
26%
Settembre 90,000
22%
Ottobre
95,000
27%
Novembre 100,000
29%
Dicembre
110,000
30%
Passaggi per Creare il Grafico Combinato:
1.   Inserimento dei Dati in Excel:
o   Apri un nuovo foglio di lavoro Excel.
o   Inserisci i dati di esempio nelle celle come
mostrato sopra.
2.   Creazione del Grafico:
o   Seleziona l’intervallo di dati (incluse le
etichette di mese, fatturato e margine di
profitto).
o   Vai alla scheda “Inserisci” sulla barra
multifunzione.
o   Nella sezione “Grafici”, scegli “Grafico
Combinato”.
o   Seleziona “Grafico a Colonne Raggruppate -
Linea su Asse Secondario”.
3.   Personalizzazione del Grafico:
o   Asse Secondario:  Assicurati che la serie del
“Margine di Profitto” sia rappresentata come
linea e sia assegnata all’asse secondario.
o   Modifica del Colore e Stile:  Personalizza i
colori delle colonne e della linea per
migliorare la leggibilità.
o   Etichette e Titoli:  Aggiungi un titolo al grafico
e etichette agli assi. Ad esempio, “Fatturato e
Margine di Profitto Mensile - 2023”.
4.   Aggiungere  Linee di Tendenza (Opzionale):
o   Per
evidenziare
una
tendenza,
puoi
aggiungere una linea di tendenza al margine
4.   Personalizza il grafico:
o   Scegli i tipi di grafico:  Nel riquadro di
dialogo, seleziona “Colonna raggruppata”
per le vendite e “Linea” per i prezzi medi.
o   Assi:  Assicurati che l’asse secondario sia
attivo per il prezzo medio (clicca con il destro
sull’asse del prezzo e seleziona “Formatta
asse”).
o   Legenda:  Personalizza la legenda per una
migliore comprensione.
o   Titoli:  Aggiungi un titolo al grafico e ai due
assi.
Interpretazione del grafico
Un grafico combinato colonna e linea ci permette di:
●   Confrontare le tendenze:  Osservare come le
vendite evolvono nel tempo rispetto ai prezzi
medi.
●   Identificare correlazioni:  Verificare se esiste
una relazione tra le due serie di dati (ad
esempio, se un aumento del prezzo corrisponde
a una diminuzione delle vendite).
●   Evidenziare eventi:  Identificare eventi particolari
che hanno influenzato le vendite o i prezzi.
Esercizio
Dataset:
Mese
Vendite
Prezzo medio
Gennaio
1000
10
Febbraio
1200
12
Marzo
800
11
...
...
...
Esporta in Fogli
Compito:
1.   Crea un foglio di calcolo con i dati sopra riportati.
2.   Crea un grafico combinato colonna e linea per
visualizzare le vendite e i prezzi medi nel tempo.
3.   Personalizza il grafico aggiungendo un titolo,
modificando i colori e le etichette.
4.   Analizza il grafico e cerca di individuare eventuali
trend o correlazioni.
Test di valutazione
1.   Domande a scelta multipla:
o   Qual è l’utilità principale di un grafico
combinato?

<!-- Pagina 102 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
101
di profitto. Fai clic con il tasto destro sulla
linea del margine di profitto, scegli “Aggiungi
Linea di Tendenza” e seleziona il tipo di linea
di tendenza desiderato (ad esempio, lineare).
3. Esercizi Pratici
Esercizio 1: Creazione di un Grafico Combinato
●   Obiettivo:
Creare
un
grafico
combinato
utilizzando i dati di esempio forniti sopra.
●   Istruzioni:
o   Inserisci i dati nel foglio di lavoro.
o   Crea un grafico combinato con le colonne per
il fatturato e la linea per il margine di profitto.
o   Personalizza il grafico aggiungendo un asse
secondario e modifica colori e stili per una
migliore presentazione.
Esercizio 2: Personalizzazione Avanzata del Grafico
●   Obiettivo:  Personalizzare ulteriormente il grafico
creato nel primo esercizio.
●   Istruzioni:
o   Aggiungi etichette dati alla linea del margine
di profitto.
o   Modifica il formato dell’asse secondario per
visualizzare
i
valori
percentuali
correttamente.
o   Aggiungi una linea di tendenza al margine di
profitto e personalizzane l’aspetto.
4. Test di Valutazione Finale
1. Domande a Scelta Multipla:
●
Quando è consigliabile utilizzare un grafico
combinato in Excel?
a)   Quando tutti i dati sono dello stesso tipo.
b)   Quando si vuole confrontare due serie di
dati con unità di misura o scale diverse.
c)   Quando si lavora con un solo tipo di dati.
d)   Quando non si vuole mostrare dati
complessi.
●
Quale tipo di grafico combinato permette di
visualizzare una serie di dati come colonna e
un’altra come linea?
a)   Colonna empilata
b)   Grafico a barre
c)   Colonna + Linea su asse secondario
d)   Grafico a dispersione
o   Come si aggiunge un secondo asse a un
grafico in Excel?
o   Quali tipi di grafici si possono combinare?
2.   Esercizio pratico:
o   Fornire un nuovo dataset e chiedere di
creare un grafico combinato appropriato.
Suggerimenti aggiuntivi
●   Formule:  Utilizza formule per calcolare nuovi
dati da visualizzare (es. variazione percentuale
delle vendite).
●   Formattazione condizionale:  Evidenzia i punti
dati più importanti.
●   Tendenze:  Aggiungi linee di tendenza per
visualizzare l’andamento generale dei dati.
●   Power Pivot:  Per analisi più complesse, utilizza
Power Pivot per creare modelli dati e
visualizzazioni interattive.
Con questo esercizio e le informazioni fornite, sarai
in grado di creare grafici combinati efficaci per
visualizzare e analizzare i tuoi dati in modo più
approfondito.
Vuoi approfondire altri aspetti dei grafici combinati,
come ad esempio la creazione di dashboard
interattivi o l’utilizzo di Power BI?
Potresti essere interessato ad altri tipi di grafici
combinati, come ad esempio:
●   Colonna e area:  Per mostrare una parte di un
totale rispetto a un valore assoluto.
●   Linea e dispersione:  Per combinare una
tendenza generale con dei punti dati individuali.
Fammi
sapere
quale
argomento
preferisci
approfondire!

<!-- Pagina 103 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
102
2. Domanda Aperta:
●
Spiega come l’uso dell’asse secondario in un
grafico combinato migliora la leggibilità dei
dati e descrivi un esempio in cui potrebbe
essere necessario.
3. Esercizio Pratico:
●
Utilizzando i dati di esempio, crea un grafico
combinato che rappresenti il fatturato annuale
totale e il margine di profitto mensile. Assicurati
di utilizzare l’asse secondario e personalizzare il
grafico
per
una
presentazione
efficace.
Consegna il file Excel con il grafico creato.
Conclusione
Al termine di questa lezione, gli utenti dovrebbero
essere in grado di creare e personalizzare grafici
combinati in Excel, utilizzando l’asse secondario per
visualizzare dati con scale diverse e migliorare la
comunicazione visiva delle informazioni.
Lo sviluppo delle risposte segue una struttura similare, ma in questo caso si iniziano ad evidenziare le
differenze tra le due IA:
-   la tabella proposta:
o   Gemini - mette a disposizione un pulsante per esportare la tabella creata in un nuovo file
“Fogli” (EXCEL di Google)
o   Chat GPT - crea un’intera tabella che si può copiare e incollare agevolmente in un foglio Excel
-   I test:
o   Gemini - sviluppa parzialmente i test di valutazione
o   Chat GPT – sviluppa il test di valutazione proponendo domande e risposte
Entrambi gli aspetti sono superabili continuando a fare domande all’IA; nel nostro caso Gemini non ha
sviluppato le risposte e quindi gli domanderemo:

### 5^ Domanda

### PROMPT
Proponi i test di valutazione delle domande a scelta multipla completo di risposte

### GEMINI RISPOSTA:
Assolutamente! Ecco un esempio di domande a scelta multipla per valutare la comprensione degli studenti sui
grafici combinati in Excel, completo delle risposte:

<!-- Pagina 104 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
103
Domande a scelta multipla sui grafici combinati in Excel
1.   Qual è la principale utilità di un grafico combinato?  a) Confrontare serie di dati con unità di misura diverse.
b) Visualizzare solo dati di tipo numerico. c) Rappresentare solo trend nel tempo.  Risposta corretta: a)
2.   Quale combinazione di tipi di grafici è più comune in un grafico combinato?  a) Linea e torta b) Colonna e
linea c) A barre e a dispersione  Risposta corretta: b)
3.   Perché si utilizza un secondo asse in un grafico combinato?  a) Per visualizzare dati con scale diverse. b) Per
rendere il grafico più colorato. c) Per separare le serie di dati. Risposta corretta: a)
4.   Quale elemento grafico è utile per evidenziare punti specifici in un grafico combinato?  a) Legenda b)
Etichette dati c) Titolo  Risposta corretta: b)
5.   Qual è il vantaggio di utilizzare un grafico combinato rispetto a due grafici separati?  a) Occupa meno
spazio. b) Permette di confrontare facilmente le serie di dati. c) È più esteticamente piacevole. Risposta
corretta: b)
Esercizio pratico (con dataset di esempio)
Dataset:
Mese
Vendite (unità)
Prezzo medio (€) Spese marketing (€)
Gennaio
1000
10
5000
Febbraio
1200
12
6000
Marzo
800
11
4000
...
...
...
...
Esporta in Fogli
Compito:
●   Crea un grafico combinato che visualizzi:
o   Le vendite (colonne)
o   Il prezzo medio (linea)
o   Le spese marketing (area)
●   Personalizza il grafico aggiungendo un titolo, modificando i colori e le etichette.
●   Analizza il grafico e cerca di individuare eventuali correlazioni tra le serie di dati.
Valutazione:
●   Corretta scelta dei tipi di grafici.
●   Corretta configurazione degli assi e delle leggende.
●   Personalizzazione efficace del grafico.
●   Capacità di interpretare e commentare i risultati.
Come si può osservare Gemini nel rispondere ha creato le risposte ai test a domanda multipla
inserendo anche qual è la risposta esatta; Quest’ultima informazione mancava alla risposta
precedentemente fornita “chat GPT”.

### Considerazioni conclusive
I software di intelligenza Artificiale attualmente, sia a pagamento che gratuiti, riescono a sviluppare
validamente programmi su argomenti di facile comprensione ed accessibili ad una vasta platea di
utenti.
Confrontando invece l’I.A. a pagamento (ChatGPT) con quella Gratuita (Gemini) l’unica sostanziale
differenza, che si può notare in tutte le risposte, è che la I.A. a pagamento fornisce risposte con un

<!-- Pagina 105 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
104
numero di caratteri (Lunghezza) superiore, rispetto alla versione I.A. Gratuita (c.d. “finestra di
contesto” 2 ).

## 8.3.   Supporto nell’utilizzo del software
In non rari casi  ci siamo trovati bloccati nell’utilizzare un software perché non sapevamo come svolgere
una determinata operazione. Spesso gli aiuti del software non danno una soluzione e finora l’unico
modo di risolvere il problema era cercarlo su Google, leggere la spiegazione e provare a implementarla.
Oggi con ChatGPT questo diventa molto più facile.
Di seguito, viene proposto un esempio di richiesta a ChatGPT di fornire istruzioni su come creare una
tabella pivot in Excel. Nella domanda si nota che è stato detto a ChatGPT di immedesimarsi in un
esperto di Excel; questa istruzione preliminare è molto utile perché prepara l’AI a dare una risposta più
“tecnica”.

### ECCO IL PRIMO PROMPT IN CHAT:
Sei un esperto di Excel. Ho bisogno che mi spieghi come posso creare una tabella pivot

### RISPOSTA DI CHATGPT:
Certo! Creare una tabella pivot in Excel è un ottimo modo per riassumere e analizzare grandi quantità di dati.
Ecco una guida passo-passo per aiutarti a creare una tabella pivot:
Passaggi per Creare una Tabella Pivot in Excel
1. Preparazione dei Dati
Assicurati che i tuoi dati siano organizzati in un formato tabellare, con intestazioni di colonna univoche. Ogni
colonna dovrebbe contenere un solo tipo di dati (ad esempio, numeri, testo, date).
2. Selezione dei Dati
Evidenzia l’intervallo di celle che contiene i dati che vuoi analizzare. Puoi includere anche l’intestazione delle
colonne.
3. Inserimento della Tabella Pivot
•   Vai alla scheda  “Inserisci”  nella barra degli strumenti di Excel.
•   Clicca su  “Tabella Pivot” .
•   Apparirà una finestra di dialogo “Crea Tabella Pivot”.
4. Impostazioni della Tabella Pivot
•   Assicurati che l’intervallo dei dati sia corretto nella sezione  “Seleziona tabella o intervallo” .
•   Scegli dove vuoi posizionare la tabella pivot: puoi creare un nuovo foglio di lavoro o inserirla in un foglio di
lavoro esistente.
5. Creazione della Tabella Pivot
•   Clicca su  “OK” .
•   Apparirà un riquadro di  “Campi Tabella Pivot”  sulla destra.
2  Una finestra di contesto rappresenta una quantità limitata di dati che un algoritmo può considerare in un dato momento.
Per esempio, in modelli linguistici come GPT, la finestra di contesto è la quantità di testo (o token) che il modello può prendere
in considerazione per generare una risposta. Se la finestra di contesto è limitata, l’algoritmo può “vedere” solo un numero
limitato di parole o frasi precedenti.

<!-- Pagina 106 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
105
6. Organizzazione dei Dati nella Tabella Pivot
•   Filtri:  Trascina un campo qui per filtrare i dati della tabella pivot.
•   Righe:  Trascina un campo qui per suddividere i dati in righe.
•   Colonne:  Trascina un campo qui per suddividere i dati in colonne.
•   Valori:  Trascina un campo qui per eseguire calcoli o aggregazioni sui dati. Puoi sommare, contare, calcolare
la media, ecc.
Esempio Pratico
Supponiamo di avere un elenco di vendite con le seguenti colonne:  Data, Cliente, Prodotto, Quantità, Prezzo .
•   Trascina il campo  “Prodotto”  nell’area  “Righe”  per visualizzare i dati per prodotto.
•   Trascina il campo  “Quantità”  nell’area  “Valori”  per sommare le quantità vendute di ogni prodotto.
•   Trascina il campo  “Cliente”  nell’area  “Colonne”  per vedere quali clienti hanno acquistato ogni prodotto.
Suggerimenti Utili
•   Aggiornamento:  Se i dati originali cambiano, aggiorna la tabella pivot cliccando su  “Aggiorna”  nella scheda
“Analizza” .
•   Raggruppamento:  Puoi raggruppare i dati, ad esempio per data, cliccando con il tasto destro su una data e
selezionando  “Raggruppa” .
•   Filtri e Slicer:  Usa i filtri e i slicer (affettatrici) per analizzare meglio i dati.
Spero che queste istruzioni ti siano utili per creare la tua tabella pivot in Excel. Se hai altre domande o hai bisogno
di ulteriori chiarimenti, non esitare a chiedere!
Si propone, di seguito, un altro esempio per il programma word.

### PROMPT CHIESTO A CHATGPT:
Ho bisogno di cambiare il colore dello sfondo di un testo selezionato, come faccio?

### RISPOSTA DI CHATGPT:
Per cambiare il colore dello sfondo del testo selezionato in Microsoft Word, puoi utilizzare l’opzione di
evidenziazione del testo. Ecco i passaggi dettagliati su come fare:
Cambiare il Colore dello Sfondo del Testo in Word
1.   Seleziona il Testo:
o   Usa il mouse per evidenziare il testo a cui desideri cambiare il colore dello sfondo.
2.   Usa lo Strumento Evidenziatore:
o   Vai alla scheda  “Home”  nella barra degli strumenti di Word.
o   Cerca l’icona dell’evidenziatore, che sembra una penna con un tratto sotto di essa. Solitamente si
trova accanto alle opzioni di colore del testo.
o   Clicca sulla freccia accanto all’icona per aprire il menu a tendina dei colori.
3.   Seleziona il Colore:
o   Scegli il colore che desideri applicare come sfondo al testo selezionato. Quando selezioni un colore,
lo sfondo del testo cambierà immediatamente al colore scelto.
4.   Rimuovere o Cambiare l’Evidenziazione:
o   Per rimuovere l’evidenziazione, seleziona di nuovo il testo e clicca sull’opzione “Nessun colore” nel
menu dell’evidenziatore.
o   Per cambiare colore, semplicemente seleziona un nuovo colore dal menu a tendina.

<!-- Pagina 107 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
106
Suggerimenti Utili
•
Colore del Testo e dello Sfondo:  Assicurati che il colore del testo e lo sfondo siano sufficientemente
contrastanti per mantenere una buona leggibilità.
•
Utilizzo dell’Evidenziatore per Note:  L’evidenziatore può essere particolarmente utile per sottolineare
o marcare parti importanti del documento per una lettura successiva.
Alternative per Cambiare lo Sfondo (Intero Paragrafo)
Se desideri cambiare il colore di sfondo di un intero paragrafo o di una sezione del documento, puoi utilizzare le
opzioni di  “Riempimento del Paragrafo” :
1.   Seleziona il Paragrafo:
o   Posiziona il cursore nel paragrafo o seleziona i paragrafi che desideri formattare.
2.   Apri il Menu Colore Sfondo:
o   Nella scheda  “Home” , clicca sulla freccia accanto all’icona del secchiello di vernice, situata vicino alle
opzioni di allineamento.
3.   Scegli il Colore:
o   Seleziona il colore desiderato dal menu. Questo applicherà il colore di sfondo all’intero paragrafo.
Seguendo questi passaggi, potrai personalizzare lo sfondo del testo nei tuoi documenti Word in base alle tue
esigenze. Se hai bisogno di ulteriori chiarimenti o di altre informazioni, sentiti libero di chiedere!
Ovviamente, domande simili possono essere fatte per altri software di uso comune.
Per i software Microsoft, inoltre, ricordiamo che risultati simili se non migliori possono essere ottenuti con
Copilot, lo strumento di AI che Microsoft sta introducendo in Windows e nella sua suite di Microsoft 365.
Un’alternativa interessante all’utilizzo di ChatGPT può essere Perplexity.ai che permette di chattare in
modo similare a ChatGPT ma utilizzando come base dati i video di Youtube.
Ecco il prompt e la risposta dove vedete anche i video Youtube che Perplexity suggerisce:

### PROMPT CHIESTO A PERPLEXITY:
Ho bisogno che mi spieghi come posso creare una tabella pivot

### RISPOSTA DI PERPLEXITY
Creare una tabella pivot in Excel è un processo semplice che ti permette di sintetizzare e analizzare grandi
quantità di dati in modo efficace. Ecco una guida passo-passo su come procedere:
1.   Preparazione dei Dati
Assicurati che i tuoi dati siano ben strutturati, con intestazioni di colonna chiare e senza righe o colonne vuote
2.   Selezionare i Dati
•   Seleziona l’intervallo di dati : Clicca su una qualsiasi cella all’interno del tuo intervallo di dati.
•   Vai alla scheda “Inserisci” : Nella barra multifunzione in alto, clicca su “Inserisci” e poi su “Tabella Pivot”
3.   Creazione della Tabella Pivot
•   Finestra di dialogo : Si aprirà una finestra di dialogo in cui puoi selezionare l’intervallo di dati da utilizzare.
Di solito, Excel rileva automaticamente l’intervallo corretto, ma puoi modificarlo se necessario.
•   Scegli dove posizionare la tabella pivot : Puoi decidere se creare la tabella pivot in un nuovo foglio di
lavoro o in uno esistente
4.   Strutturare la Tabella Pivot

<!-- Pagina 108 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
107
•   Elenco Campi Pivot : Una volta creata la tabella pivot, vedrai un elenco di campi sulla destra. Questi campi
rappresentano le colonne del tuo intervallo di dati originale.
•   Trascina i campi : Trascina i campi nelle aree “Filtri”, “Colonne”, “Righe” e “Valori” per strutturare la tua
tabella pivot. Ad esempio, puoi trascinare il campo “Data” nell’area “Righe” e il campo “Vendite” nell’area
“Valori” per vedere le vendite per data
5.   Analizzare i Dati
•   Raggruppare i dati : Puoi raggruppare i dati per mesi, trimestri o anni, cliccando con il tasto destro su una
data nella tabella pivot e selezionando “Raggruppa”
•   Filtrare i dati : Usa i filtri per visualizzare solo i dati di interesse. Puoi aggiungere campi all’area “Filtri” per
creare filtri a livello di rapporto
6.   Formattare la Tabella Pivot
•   Stili PivotTable : Nella scheda “Progettazione” puoi scegliere diversi stili per la tua tabella pivot per
migliorarne l’aspetto visivo.
•   Aggiungere totali e subtotali : Puoi personalizzare la visualizzazione dei totali e subtotali attraverso le
opzioni di progettazione
7.   Creare Grafici Pivot
•   Grafici Pivot : Puoi creare grafici pivot per visualizzare i tuoi dati in modo ancora più intuitivo. Basta
selezionare la tabella pivot e andare su “Inserisci” > “Grafico Pivot”
Esempio Pratico
Supponiamo di avere un database con le vendite di libri in diverse città italiane. Per creare una tabella pivot
che riassuma le vendite per genere e città:
1.   Seleziona l’intervallo di dati.
2.   Inserisci una tabella pivot.
3.   Trascina il campo “Genere” nell’area “Righe”.
4.   Trascina il campo “Città” nell’area “Colonne”.
5.   Trascina il campo “Vendite” nell’area “Valori”
Seguendo questi passaggi, potrai creare e personalizzare una tabella pivot per analizzare i tuoi dati in modo
efficace.
Nelle risposte del software di motore di ricerca LLM è associato anche il link del video da cui la risposta
è stata tratta in modo da poter verificare il contenuto.
Ovviamente Perplexity può essere usato anche per una ricerca più generale non limitata solo ai video
di Youtube. Interessante è il fatto che viene sempre indicata la fonte della risposta per poterla
verificare.

<!-- Pagina 109 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
108

## 9.   Potenziamento delle tecniche di ricerca web tramite AI

### Le caratteristiche della ricerca tramite i  Motori di Ricerca Tradizionali  sono note:
•   la ricerca avviene tramite query molto precise;
•   occorre molto tempo per leggere, selezionare ed interpretare i risultati;
•   pertanto, la ripetizione e l’affinamento della ricerca sono vincolate dal tempo necessario
/disponibile ad eseguire l’operazione;
•   ogni ricerca restituisce sempre lo stesso risultato, pertanto gli affinamenti successivi possono
essere poco produttivi.

### L’utilizzo dei software di AI (LLM)  come ChatGPT, CLAUDE AI, GEMINI invece, generano risposte alle
domande poste tramite un meccanismo di tipo statistico. La riposta è basata sui pattern e sulle
conoscenze acquisite durante l'addestramento.
Tali sistemi possono rispondere a domande, fornire spiegazioni dettagliate e creare testi coerenti in
modo simile a una conversazione umana. Interagire con essi è simile a condurre una conversazione
con un essere umano: le domande possono essere poste in linguaggio naturale e le risposte sono veloci
e contestuali. È possibile chiedere, inoltre, verifiche e approfondimenti, completando l’informazione
per interazioni successive. Occorre ricordare però che l’output della macchina è “una risposta
formalmente corretta” ma non vi è una comprensione profonda del quesito: si tratta semplicemente
“generato” statisticamente.
Questo metodo di indagine è comunque molto utile quando si cerca di comprendere argomenti dei
quali non si conoscono parole chiave, concetti complessi da approfondire progressivamente, o quando
si ha bisogno di spiegazioni dettagliate di concetti di uso comune.
Una particolarità che vale la pena citare è che all’interno di una sessione di utilizzo, lo strumento LLM
acquisisce “il contesto” di una conversazione, e permette all’utente di approfondire l’argomento
affrontato senza dover ripetere le informazioni di base ogni volta.
Riepilogando le caratteristiche:
•   la ricerca può partire da interrogazioni molto generiche, da perfezionare tramite le interazioni
conversazionali successive;
•   il responso, pur non essendo perfettamente affidabile è molto chiaro, e restituisce un valore
informativo fruibile immediatamente;
•   il tempo per selezionare e capire se la domanda posta è giusta, è sbagliata o deve essere affinata
è molto breve, non occorre spulciare fra migliaia di risultati;
•   la medesima ricerca non restituisce sempre lo stesso risultato, pertanto la ripetizione, la richiesta
di precisazione o di fonti è molto utile.

<!-- Pagina 110 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
109

### Accuratezza, affidabilità e aggiornamento
Gli LLM come ChatGPT / CLAUDE AI ecc. possono fornire risposte rapide e dettagliate, ma la loro
accuratezza dipende dalla qualità e dalla quantità dei dati con cui sono stati addestrati e dal modo di
porre le domande. Poiché molti modelli non hanno accesso diretto a internet o a fonti aggiornate in
tempo reale, possono generare risposte basate su informazioni obsolete o incomplete. Inoltre, la base
informativa spesso è generalista, e costituita dal web con ulteriore limite temporale (“ informazioni
aggiornate fino alla data di termine dell’addestramento ”).
I motori di ricerca “tradizionali” forniscono accesso diretto a una vasta gamma di fonti aggiornate,
incluse pagine web, articoli, documenti ufficiali e altro sempre aggiornati.
Tuttavia, la qualità dei risultati può variare e gli utenti devono essere in grado di valutare criticamente
le fonti per distinguere informazioni affidabili da quelle meno attendibili. La possibilità di accedere a
fonti primarie e ufficiali rende i motori di ricerca particolarmente utili per ricerche che richiedono dati
precisi e aggiornati a discapito però del tempo: gli utenti devono spesso vagliare una grande quantità
di risultati per trovare ciò di cui hanno bisogno.

### Esempio pratico
È stato condotto un test su una questione professionale estremamente rilevante. È in corso la modifica
dell’art. 2407 c.c. in tema responsabilità del collegio sindacale. Alla data di stesura di questo articolo,
la proposta di modifica è stata approvata dalla Camera e deve essere esaminata dal Senato, come si
evince dall’ iter  descritto dai siti dei due rami del Parlamento.
A diversi LLM è stato posto lo stesso quesito:
“È stata recentemente modificata la responsabilità del collegio sindacale disciplinata dall’art. 2407 c.c.? A quando
risale l’ultima modifica e cosa prevede? Esistono progetti di riforma della disciplina?” 3
3  La domanda è posta in modo volutamente generico. Siccome l’iter di riforma non é ancora concluso perché il disegno di
legge è stato approvato solo da un ramo del Parlamento, la modifica dell’art. 2407 c.c. allo stato non esiste.

<!-- Pagina 111 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
110
Quello sotto riportato è l’ iter  legislativo edotto dai siti web di Camera e Senato.
Estratto dal sito della camera dei deputati
Estratto dal sito senato della repubblica
Si riportano di seguito i test eseguiti con i diversi sistemi basati su AI e LLM.

### ChatGPT versione 4o by OpenAI: RISPOSTA NON AGGIORNATA E NON DEL TUTTO CORRETTA (NON

### SONO CITATE LE MODIFICHE IN CORSO)

<!-- Pagina 112 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
111

### Claude 3.5 Sonnet by Anthropic: RISPOSTA NON DEL TUTTO CORRETTA E AGGIORNATA (CON

### LIMITAZIONI ESPLICITATE)

### GEMINI (agg. 12/09/2024) By GOOGLE: LA RISPOSTA TIENE CONTO DELLE MODIFICHE IN CORSO, MA

### NON È CORRETTA
Si noti:
-   che la risposta tiene conto delle modifiche in corso, ma l’esposizione è parzialmente incoerente;
-   che la risposta è stata fornita utilizzando risorse web che sono citate come approfondimenti;
-   che in calce è esposto una avvertenza / limitazione significativa in relazione alla natura della
informazione prodotta.

<!-- Pagina 113 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
112

### Microsoft Copilot (integrato in EDGE e basato sull’architettura GPT-4 di OpenAI): LA RISPOSTA TIENE

### CONTO DELLE MODIFICHE IN CORSO, MA NON È TOTALMENTE CORRETTA
Si noti:
•   che la risposta tiene conto delle modifiche in corso, ma le affermazioni sono corrette solo in parte;
•   che la data citata del 31 agosto 2024 è apparsa nella prima interazione, mentre nelle successive è
stata corretta con 30 maggio;
•   che la risposta è stata fornita “USANDO IL WEB”;
•   che sono citate le fonti consultate (ritenute sufficientemente affidabili).

### PERPLEXITY (agg. 5/10/2024) : RISPOSTA CORRETTA CON APPROFONDIMENTO

<!-- Pagina 114 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
113
Si noti:
-   che la risposta fornita contiene una affermazione che contrasta con il paragrafo “ultima modifica”,
pertanto a scopo di maggior cautela è stato richiesto un approfondimento (si veda il prompt di
approfondimento riportato successivamente);
-   che la risposta cita le fonti;

### -   che Perplexity a differenza degli altri LLM, è un  motore di ricerca conversazionale  e  chatbot
basato su AI, progettato per fornire risposte dirette e pertinenti alle domande degli utenti
attingendo a un vasto database di informazioni aggiornate.
Si noti:
-
che grazie alle differenti tecniche di ricerca rispetto ai motori di ricerca tradizionali, è possibile
approfondire la ricerca e chiedere conferme allo strumento impiegato.

### Conclusioni
È stato richiesto un compito molto complesso ai diversi sistemi in relazione alle loro potenzialità poiché
le informazioni richieste sono sia tecniche, che soggette ad aggiornamento recentissimo.
Le ricerche condotte con gli strumenti innovativi si sono rivelate molto veloci da eseguire e le risposte
sufficientemente precise quando si utilizzano strumenti con accesso al web (GEMINI, COPILOT,
PERPLEXITY).
È chiaro che l’esempio proposto è una argomentazione particolarmente delicata, e che per ottenere
certezze ferme l’unica strada è consultare la pagina web del Parlamento. E’ però che evidenze che
l’indicazione fornita dai più precisi LLM (e i link di supporto quando presenti) hanno accelerato molto
l’accesso all’informazione.

<!-- Pagina 115 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
114
La conferma dei risultati ottenuti è poi stata eseguita facendo ricerche di controllo su Google, Bing ecc.

### coniugando velocità e accuratezza.

## 9.1.   Conclusione dell’esercitazione
Sia la ricerca condotta tramite motori di ricerca tradizionali che tramite AI ha punti di forza e debolezza.
Potremmo sintetizzare le caratteristiche dei due sistemi di ricerca con il noto controverso rapporto
Efficacia vs Efficienza:

### •   EFFICACIA : come capacità di raggiungere un obiettivo prefissato. (carattere facilmente
riscontrabile dei motori di ricerca).

### •   EFFICIENZA : come la capacità di raggiungere un obiettivo con la minore quantità di risorse, tempo
ed energia possibili (caratteristica riconoscibile negli LLM di AI).

### L’uso combinato di entrambi gli strumenti può offrire il miglior risultato : la ricerca tramite AI può
fornire un supporto immediato e contestuale, mentre i motori di ricerca possono essere utilizzati per
verificare le informazioni e accedere a documenti specifici e aggiornati.
La scelta dello strumento dipende dalle esigenze specifiche del contesto. Per ottenere risposte rapide
in modo conversazionale, i modelli di intelligenza artificiale orientati al dialogo sono molto efficaci.
Tuttavia, per ricerche approfondite e altamente dettagliate, i tradizionali motori di ricerca rimangono
attualmente indispensabili. Integrare entrambi gli strumenti nella routine lavorativa può migliorare
notevolmente l'efficienza e la precisione nel lavoro del Commercialista

<!-- Pagina 116 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
115

## 10.   Analisi delle condizioni di trattamento dati dei principali

## software AI

### Premessa
L’obiettivo del presente approfondimento è quello di evidenziare le principali clausole contrattuali in
tema di trattamento e protezione nonché sicurezza dei dati dei principali strumenti di intelligenza
artificiale generativa.
Per questo fine sono state prese in considerazione le privacy policy dei seguenti strumenti di
intelligenza artificiale:
1.   ChatGPT – Openai ( https://openai.com/it-IT/policies/eu-privacy-policy/ )
2.   Claude – Sonnet ( Privacy Policy \ Anthropic )
3.   Microsoft Copilot ( https://learn.microsoft.com/it-it/copilot/microsoft-365/microsoft-365-
copilot-privacy )
4.   Google Gemini
( https://support.google.com/gemini/answer/13594961?sjid=14797734831315783999-
EU&visit_id=638611419640664925-4142049551&rd=1#gemini_apps )
I parametri di valutazione sono i seguenti:
1.   Chi è il titolare del trattamento?
2.   Quali dati personali raccoglie?
3.   Quali sono le finalità del trattamento
4.   Rispetto dei requisiti dell’articolo 5 del GDPR
5.   Dove sono conservati i dati
6.   Tempi di conservazione
7.   Misure di sicurezza adottate
8.   Nomina di eventuali sub responsabili e/o responsabili esterni
9.   Rispetto dei diritti degli interessati indicati nel GDPR
L’analisi è stata condotta anche con l’ausilio di ChatGPT e Google NotebookLM.

## 10.1.   ChatGPT

### 1.   Titolare del trattamento:  Per gli utenti residenti nello Spazio Economico Europeo (SEE) o in
Svizzera, il titolare del trattamento è OpenAI Ireland Limited, con sede legale al 1st Floor, The
Liffey Trust Centre, 117-126 Sheriff Street Upper, Dublino 1, D01 YC43, Irlanda.

<!-- Pagina 117 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
116

### 2.   Dati personali raccolti:
Dati forniti direttamente dall’utente:
-   Informazioni sull’account: nome, informazioni di contatto, credenziali dell’account, dati della carta
di pagamento e cronologia delle transazioni.
-   Contenuti dell’utente: input forniti, file caricati e feedback.
-   Informazioni sulle comunicazioni: nome, informazioni di contatto e contenuto dei messaggi.
-   Informazioni sui social media: dati di contatto e informazioni aggregate e analitiche sull’attività sui
social media fornite dalle piattaforme.
-   Altre informazioni fornite dall’utente: informazioni fornite durante eventi, sondaggi o per la
verifica dell’età o dell’identità.
Dati raccolti automaticamente durante l’utilizzo dei servizi:
-   Dati di log: indirizzo IP, tipo e impostazioni del browser, data e ora della richiesta e modalità di
interazione con i servizi.
-   Dati di utilizzo: tipi di contenuti visualizzati o utilizzati, funzionalità utilizzate, azioni intraprese,
fuso orario, paese, date e orari di accesso, user agent e versione, tipo di dispositivo e dati sulla
connessione.
-   Informazioni sul dispositivo: nome del dispositivo, sistema operativo, identificatori del dispositivo
e browser utilizzato.
-   Cookie e tecnologie simili: utilizzati per gestire i servizi e migliorare l’esperienza utente.
Dati ottenuti da altre fonti:
-   Informazioni pubblicamente disponibili su Internet: utilizzate principalmente per sviluppare modelli.
-   Informazioni dai partner: inclusi partner per la sicurezza e la prevenzione delle frodi e fornitori di
servizi di marketing.

### 3.   Finalità del trattamento:
-   Fornire e gestire i servizi.
-   Migliorare e sviluppare i servizi, comprese nuove funzionalità, e condurre ricerche.
-   Comunicare con gli utenti, ad esempio fornendo informazioni o comunicazioni di marketing sui
servizi ed eventi.
-   Prevenire frodi, attività criminali o abusi e proteggere i sistemi e i servizi.
-   Rispettare gli obblighi di legge e proteggere i diritti, la privacy, la sicurezza o la proprietà degli
utenti, di OpenAI, delle sue affiliate o di terzi.

### 4.   Rispetto dei requisiti dell’articolo 5 del GDPR:  Le fonti non forniscono dettagli specifici sulle
misure adottate da OpenAI per garantire la conformità a ciascun principio dell’articolo 5 del GDPR.
Affermano che OpenAI implementa misure tecniche, amministrative e organizzative

<!-- Pagina 118 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
117
commercialmente ragionevoli per proteggere i dati personali. Tuttavia, non approfondiscono in
dettaglio come ciò venga effettivamente realizzato.

### 5.   Dove sono conservati i dati:  I dati personali sono elaborati e conservati nelle strutture e nei server
di OpenAI negli Stati Uniti. Possono anche essere condivisi con fornitori di servizi e affiliati in altre
giurisdizioni.

### 6.   Tempi di conservazione:  OpenAI conserva i dati personali per il tempo necessario a fornire i propri
servizi o per altri scopi commerciali legittimi, come la risoluzione di controversie, la sicurezza e la
protezione o il rispetto degli obblighi di legge. La durata specifica dipende da diversi fattori, tra
cui la finalità del trattamento, la quantità, la natura e la sensibilità dei dati, il rischio potenziale di
danni derivanti da un uso o una divulgazione non autorizzati e gli eventuali requisiti di legge. Le
impostazioni utente possono anche influenzare la durata della conservazione, come la
disattivazione della cronologia delle chat in ChatGPT.

### 7.   Misure di sicurezza adottate:  Le fonti menzionano l’implementazione di misure tecniche,
amministrative e organizzative commercialmente ragionevoli per proteggere i dati personali, ma
non forniscono dettagli specifici.

### 8.   Nomina di eventuali sub-responsabili e/o responsabili esterni:  Le fonti indicano che OpenAI
condivide i dati personali con fornitori e fornitori di servizi per supportare le proprie operazioni
commerciali. Questi includono fornitori di servizi di hosting, assistenza clienti, cloud, fornitura di
contenuti, data warehouse, supporto e monitoraggio della sicurezza, software di comunicazione
via e-mail, analisi web, pagamenti e transazioni e altri fornitori di servizi IT. Tuttavia, le fonti non
menzionano specificamente se questi fornitori sono considerati sub-responsabili o responsabili
esterni ai sensi del GDPR.

### 9.   Rispetto dei diritti degli interessati indicati nel GDPR:
-   Diritto di accesso: gli utenti hanno il diritto di accedere ai propri dati personali e alle informazioni
relative al loro trattamento.
-   Diritto alla cancellazione: gli utenti possono richiedere la cancellazione dei propri dati personali
dagli archivi di OpenAI.
-   Diritto di rettifica: gli utenti possono richiedere la rettifica o l’aggiornamento dei propri dati
personali.
-   Diritto alla portabilità dei dati: gli utenti possono richiedere il trasferimento dei propri dati
personali a terzi.
-   Diritto alla limitazione del trattamento: gli utenti possono richiedere la limitazione del trattamento
dei propri dati personali.
-   Diritto di revoca del consenso: gli utenti possono revocare il consenso al trattamento dei propri
dati personali, laddove il consenso sia la base giuridica del trattamento.

<!-- Pagina 119 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
118
-   Diritto di opposizione: gli utenti hanno il diritto di opporsi al trattamento dei propri dati personali
per finalità di marketing diretto o quando il trattamento si basa su interessi legittimi.
-   Diritto di presentare un reclamo all’autorità di controllo: gli utenti possono presentare un reclamo
all’autorità di controllo competente per la protezione dei dati.
Le fonti sottolineano che questi diritti possono essere limitati in determinate circostanze, ad esempio
quando l’adempimento della richiesta rivelerebbe i dati personali di un’altra persona o quando OpenAI
è legalmente obbligata a conservare le informazioni.

## 10.2.   Claude – Sonet

### 1.   Titolare del trattamento:  Per i residenti nello Spazio Economico Europeo (SEE), nel Regno Unito

### o in Svizzera, il titolare del trattamento è  Anthropic Ireland, Limited .

### 2.   Dati personali raccolti:  Anthropic raccoglie diverse categorie di dati personali, tra cui:
-   Dati di identità e contatto: come nome, indirizzo email e numero di telefono, raccolti al
momento della registrazione di un account Anthropic o per ricevere informazioni sui servizi.
-   Informazioni sul pagamento: raccolte se si sceglie di acquistare l’accesso ai prodotti e ai servizi
Anthropic.
-   Input e Output: i prompt o input (inclusi testo, file, documenti, foto, immagini e altri materiali)
forniti ai servizi di intelligenza artificiale di Anthropic e le risposte o completamenti generati in
base a tali input. Se includi dati personali nei tuoi input, Anthropic li raccoglierà e queste
informazioni potrebbero essere riprodotte negli output.
-   Feedback sull’utilizzo dei servizi: incluso qualsiasi feedback, idee, suggerimenti per migliorare
o valutazioni forniti in merito agli output, ad esempio utilizzando l’icona con il pollice in alto/in
basso. Le conversazioni correlate alle valutazioni degli output verranno archiviate come parte
del feedback.
-   Informazioni sulla comunicazione: raccolte quando si comunica con Anthropic, ad esempio
tramite i suoi account sui social media, inclusi nome, informazioni di contatto e il contenuto
dei messaggi inviati.
-   Informazioni tecniche: raccolte automaticamente quando si utilizzano i servizi, inclusi dati sul
dispositivo e sulla connessione (come tipo di dispositivo, informazioni sul sistema operativo,
informazioni sul browser, referenti delle pagine Web, rete mobile, informazioni sulla
connessione, operatore di telefonia mobile o provider di servizi Internet, impostazione del fuso
orario, indirizzo IP), informazioni sull’utilizzo (come date e orari di accesso, cronologia di
navigazione, ricerche, collegamenti cliccati, pagine visualizzate), informazioni su registri ed
errori.

<!-- Pagina 120 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
119
-   Cookie e tecnologie simili: Anthropic e i suoi fornitori di servizi utilizzano cookie, script e
tecnologie simili per gestire i servizi e raccogliere informazioni sull’utente e sull’utilizzo dei
servizi.
-   Dati per l’addestramento dei modelli: Anthropic ottiene dati personali da fonti terze per
addestrare i suoi modelli. Queste fonti includono informazioni disponibili pubblicamente su
Internet, set di dati concessi in licenza da aziende terze e dati forniti da utenti o crowd worker.

### 3.   Finalità del trattamento:
-   Fornire, mantenere e facilitare i prodotti e i servizi offerti in relazione all’account Anthropic,
inclusi l’elaborazione di dati di identità e contatto, informazioni di pagamento, feedback, input
e output.
-   Comunicare con l’utente per scopi non di marketing, inclusi l’invio di email relative ai servizi,
notifiche push e altri messaggi.
-   Inviare comunicazioni di marketing, se l’utente ha acconsentito a riceverle.
-   Creare e amministrare l’account Anthropic.
-   Facilitare i pagamenti per i prodotti e i servizi forniti da Anthropic.
-   Prevenire e indagare su frodi, abusi e violazioni delle Norme di utilizzo, attività illegali o
criminali, accesso o utilizzo non autorizzati di dati personali o dei sistemi e delle reti di
Anthropic, per proteggere i diritti di Anthropic e di altri e per adempiere agli obblighi legali,
governativi e istituzionali.
-   Indagare e risolvere controversie.
-   Indagare e risolvere problemi di sicurezza.
-   Eseguire il debug e identificare e riparare gli errori che compromettono le funzionalità esistenti.
-   Migliorare i servizi e condurre ricerche.
-   Identificare i dati personali e addestrare i modelli di intelligenza artificiale.
-   Far rispettare i Termini di servizio e termini e accordi simili, incluse le Norme di utilizzo.

### 4.   Rispetto dei requisiti dell’articolo 5 del GDPR:  Le fonti non forniscono dettagli specifici su come
Anthropic garantisca la conformità a ciascun principio dell’articolo 5 del GDPR. Tuttavia,
affermano che Anthropic utilizza i dati personali solo in conformità con le leggi applicabili e si basa
su basi giuridiche come contratto, interessi legittimi, consenso e obblighi legali per l’elaborazione
dei dati.

### 5.   Dove sono conservati i dati:  Quando si accede al sito Web o ai servizi di Anthropic, i dati personali
possono essere trasferiti ai server di Anthropic negli Stati Uniti o in altri paesi al di fuori dello
Spazio Economico Europeo (SEE) e del Regno Unito.

### 6.   Tempi di conservazione:  Anthropic conserva i dati personali per il tempo ragionevolmente
necessario per le finalità descritte nella sua Informativa sulla privacy. Quando i dati personali

<!-- Pagina 121 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
120
raccolti non sono più necessari, Anthropic e i suoi fornitori di servizi eseguiranno le procedure
necessarie per distruggerli, eliminarli, cancellarli o convertirli in forma anonima, come consentito
o richiesto dalle leggi applicabili.

### 7.   Misure di sicurezza adottate:  Le fonti non forniscono dettagli specifici sulle misure di sicurezza
adottate da Anthropic. Tuttavia, menzionano che Anthropic implementa misure tecniche,
amministrative e organizzative commercialmente ragionevoli per proteggere i dati personali.

### 8.   Nomina di eventuali sub-responsabili e/o responsabili esterni:  Anthropic divulga i dati personali
alle seguenti categorie di terze parti:
-   Affiliate e partner aziendali.
-   Fornitori di servizi e partner commerciali: Anthropic può condividere i dati personali con
fornitori di servizi e partner commerciali per una serie di scopi commerciali, tra cui l’hosting di
siti Web e dati, la garanzia della conformità agli standard del settore, la ricerca, l’auditing e
l’elaborazione dei dati.
-   Come parte di un evento aziendale significativo: in caso di fusione, transazione aziendale,
fallimento o altra situazione che comporti il trasferimento di attività aziendali.
-   Siti Web e servizi di terze parti: i servizi di Anthropic possono prevedere integrazioni con o
indirizzare l’utente a siti Web, app e servizi gestiti da terze parti. L’interazione con queste terze
parti è soggetta alle loro informative sulla privacy.
-   In ottemperanza a requisiti normativi o legali, sicurezza, diritti di terzi e per far valere i diritti o i
termini di Anthropic: Anthropic può divulgare i dati personali alle autorità di regolamentazione
governative come richiesto dalla legge, anche per scopi legali, fiscali o contabili, in risposta alle
loro richieste di tali informazioni o per assistere nelle indagini. Possono anche divulgare i dati
personali a terzi in relazione a reclami, controversie o contenziosi, quando altrimenti consentito
o richiesto dalla legge, o se determinano che la divulgazione è necessaria per proteggere la salute
e la sicurezza dell’utente o di qualsiasi altra persona, per proteggersi da frodi o rischi di credito,
per far valere i propri diritti legali o i diritti legali di altri, per far valere gli impegni contrattuali
assunti dall’utente o come altrimenti consentito o richiesto dalla legge applicabile.
-   Con il consenso dell’individuo: Anthropic divulgherà i dati personali quando un individuo
fornisce il proprio permesso o ordina di divulgare tali informazioni.

### 9.   Rispetto dei diritti degli interessati indicati nel GDPR:  Anthropic riconosce e afferma di rispettare
i diritti degli interessati ai sensi del GDPR, tra cui:
-   Diritto di sapere: l’utente ha il diritto di sapere quali dati personali Anthropic elabora su di lui,
comprese le categorie di dati personali, le categorie di fonti da cui vengono raccolti, le finalità
aziendali o commerciali della raccolta e le categorie di terzi a cui vengono comunicati.
-   Accesso e portabilità dei dati: l’utente può avere il diritto di richiedere una copia dei dati
personali che Anthropic elabora su di lui, fatte salve determinate eccezioni e condizioni. In

<!-- Pagina 122 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
121
alcuni casi e in base alla legge applicabile, l’utente ha il diritto di trasferire le proprie
informazioni.
-   Cancellazione: l’utente può avere il diritto di richiedere la cancellazione dei dati personali
raccolti da Anthropic durante l’utilizzo dei suoi servizi, fatte salve determinate eccezioni.
L’utente può anche eliminare singole conversazioni, che verranno rimosse immediatamente
dalla cronologia delle conversazioni ed eliminate automaticamente dal back-end di Anthropic
entro 30 giorni.
-   Rettifica: l’utente può avere il diritto di richiedere la correzione dei dati personali inesatti che
Anthropic conserva su di lui, fatte salve determinate eccezioni. Anthropic non può garantire
l’accuratezza fattuale degli output. Se gli output contengono dati personali inesatti relativi
all’utente, è possibile inviare una richiesta di correzione e Anthropic farà uno sforzo ragionevole
per correggere tali informazioni.
-   Opposizione: l’utente può avere il diritto di opporsi al trattamento dei propri dati personali,
inclusa la profilazione effettuata per motivi di interesse pubblico o legittimo. Nei luoghi in cui
tale diritto è applicabile, Anthropic cesserà di elaborare i dati personali in caso di opposizione,
a meno che non dimostri motivi legittimi cogenti per il trattamento che prevalgono sugli
interessi, i diritti e le libertà dell’utente o per l’accertamento, l’esercizio o la difesa di
rivendicazioni legali. Se Anthropic utilizza le informazioni dell’utente per il marketing diretto,
l’utente può opporsi e rinunciare a ricevere futuri messaggi di marketing diretto utilizzando il
collegamento per annullare l’iscrizione presente in tali comunicazioni.
-   Limitazione: l’utente ha il diritto di limitare il trattamento dei propri dati personali in
determinate circostanze.
-   Revoca del consenso: laddove il trattamento dei dati personali da parte di Anthropic si basi sul
consenso, l’utente ha il diritto di revocare il proprio consenso. La revoca del consenso non
pregiudica la liceità del trattamento basata sul consenso prima della revoca.
L’utente può esercitare i propri diritti inviando una richiesta via email a Anthropic all’indirizzo
privacy@anthropic.com.

## 10.3.   Microsoft Copilot

### 1.   Titolare del trattamento:  Microsoft

### 2.   Dati personali raccolti:  Microsoft Copilot per Microsoft 365 accede ai contenuti e al contesto
attraverso Microsoft Graph, inclusi documenti, messaggi di posta elettronica, calendario, chat,
riunioni e contatti. Raccoglie anche le richieste degli utenti, le risposte generate da Copilot e le
citazioni a tutte le informazioni utilizzate come base per la risposta. Inoltre, quando si utilizzano
plug-in di terze parti, questi potrebbero raccogliere dati aggiuntivi in base alle proprie informative
sulla privacy.

<!-- Pagina 123 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
122

### 3.   Finalità del trattamento:
-   Fornire funzionalità di produttività basate sull’intelligenza artificiale.
-   Generare risposte accurate, pertinenti e contestuali alle richieste degli utenti.
-   Archiviare la cronologia delle interazioni Copilot con l’utente.
-   Consentire agli amministratori di visualizzare e gestire i dati archiviati.
-   Migliorare Microsoft Copilot per Microsoft 365 con il feedback facoltativo dei clienti.
-   Fornire informazioni più rilevanti tramite plug-in di terze parti.

### 4.   Rispetto dei requisiti dell’articolo 5 del GDPR:  Le fonti affermano che Microsoft Copilot per
Microsoft 365 è conforme agli impegni esistenti in materia di privacy, sicurezza e conformità per
i clienti commerciali di Microsoft 365, tra cui il Regolamento generale sulla protezione dei dati
(GDPR). Tuttavia, non vengono forniti dettagli specifici su come Microsoft garantisca la conformità
a ciascun principio dell’articolo 5 del GDPR.

### 5.   Dove sono conservati i dati:  Le fonti indicano che i dati elaborati da Microsoft Copilot per
Microsoft 365 rimangono all’interno del perimetro del servizio Microsoft 365. Per gli utenti
dell’Unione Europea (UE), il traffico dei dati rimane all’interno del Confine dei dati dell’Europa.
Tuttavia, durante i periodi di utilizzo elevato, il sistema può chiamare anche altre aree in cui sia
disponibile capacità. Le query dei clienti al di fuori dell’UE possono essere elaborate negli Stati
Uniti, nell’UE o in altre aree.

### 6.   Tempi di conservazione:  Le fonti non specificano i tempi di conservazione per i dati elaborati da
Microsoft Copilot per Microsoft 365. Tuttavia, gli amministratori possono impostare i criteri di
conservazione per i dati correlati alle interazioni tramite chat con Copilot utilizzando Microsoft
Purview.

### 7.   Misure di sicurezza adottate:
-   Isolamento logico dei contenuti dei clienti all’interno di ciascun tenant.
-   Sicurezza fisica rigorosa, screening in background e crittografia a più livelli.
-   Crittografia dei dati in transito e inattivi.
-   Conformità a normative sulla privacy ampiamente applicabili e standard di privacy diffusi.

### 8.   Nomina di eventuali sub responsabili e/o responsabili esterni:  Le fonti menzionano che
Microsoft Copilot per Microsoft 365 può utilizzare plug-in o connettori di terze parti. Tuttavia, non
forniscono un elenco specifico di questi sub responsabili o responsabili esterni. Gli amministratori
possono visualizzare le autorizzazioni, l’accesso ai dati, le condizioni per l’utilizzo e l’informativa
sulla privacy dei plug-in nella sezione “App integrate” dell’interfaccia di amministrazione di
Microsoft 365.

<!-- Pagina 124 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
123

### 9.   Rispetto dei diritti degli interessati indicati nel GDPR:  Le fonti non descrivono in dettaglio come
gli utenti possano esercitare i propri diritti ai sensi del GDPR in relazione a Microsoft Copilot per
Microsoft 365. Tuttavia, dato che il servizio è soggetto al GDPR, si può presumere che gli utenti
abbiano il diritto di accedere, rettificare, cancellare, limitare e opporsi al trattamento dei propri
dati personali. Per ottenere informazioni specifiche su come esercitare tali diritti, è consigliabile
contattare Microsoft direttamente.

## 10.4.   Google Gemini

### 1. Titolare del trattamento  Il titolare del trattamento dei dati relativi a Gemini è  Google LLC . In
quanto tale, Google è responsabile di garantire la conformità al GDPR per tutti i dati personali
raccolti e trattati attraverso il suo servizio.

### 2. Dati personali raccolti
-   Dati forniti dall’utente: Testi, comandi, domande, informazioni personali incluse nelle richieste.
Dati di utilizzo: Informazioni sull’utilizzo del servizio, come data e ora di accesso, frequenza di

### utilizzo, funzionalità utilizzate.

### -   Dati tecnici: Indirizzo IP, tipo di dispositivo, sistema operativo, browser.
-   Dati biometrici: In alcuni casi, potrebbero essere raccolti dati biometrici per scopi di

### autenticazione o personalizzazione.

### 3. Finalità del trattamento
-   Rispondere alle richieste degli utenti, tradurre testi, generare contenuti creativi.
-   Migliorare il modello: Addestrare e perfezionare il modello di linguaggio per ottenere risultati
sempre più accurati e pertinenti.
-   Personalizzare l’esperienza utente: Adattare le risposte e i suggerimenti alle preferenze e alle
abitudini dell’utente.
-   Analizzare l’utilizzo: Comprendere come gli utenti utilizzano il servizio per identificare
opportunità di miglioramento e sviluppare nuove funzionalità.

### 4. Rispetto dei requisiti dell’articolo 5 del GDPR
Google, in quanto azienda leader nel settore tecnologico, ha implementato numerose misure per
garantire la conformità ai principi stabiliti dall’articolo 5 del GDPR. Tuttavia, una valutazione
dettagliata richiederebbe l’accesso a informazioni tecniche e legali specifiche.

### 5. Dove sono conservati i dati
Non vengono forniti dettagli specifici su come Microsoft garantisca la conformità a ciascun principio
dell’articolo 5 del GDPR.

<!-- Pagina 125 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
124

### 6. Tempi di conservazione
I tempi di conservazione dei dati variano a seconda del tipo di dato e della finalità del trattamento.
Tuttavia, non vengono forniti dettagli specifici

### 7. Misure di sicurezza adottate
-   Crittografia: I dati sono crittografati sia durante la trasmissione che durante la conservazione.
-   Controllo degli accessi: L’accesso ai dati è limitato al personale autorizzato.
-   Monitoraggio continuo: Vengono effettuati controlli regolari per identificare e mitigare
eventuali minacce.
-   Compliance certificata

### 8. Nomina di sub responsabili e/o responsabili esterni
Google stipula accordi contrattuali che impongono ai fornitori di rispettare le norme sulla protezione
dei dati personali.

### 9. Rispetto dei diritti degli interessati
-   Diritto di accesso: Gli utenti possono richiedere una copia dei propri dati.
-   Diritto di rettifica: Gli utenti possono richiedere la correzione di dati errati.
-   Diritto alla cancellazione: Gli utenti possono richiedere la cancellazione dei propri dati in
determinate circostanze.
-   Diritto di opposizione: Gli utenti possono opporsi al trattamento dei loro dati per particolari finalità

## 10.5.   Sintesi
Parametro di
Valutazione/AI
ChatGPT
Claude Sonet
Microsoft Copilot
Gemini
Chi è il titolare del
trattamento?
OpenAI Ireland Limited
Anthropic Ireland Limited
Microsoft
Google LLC
Quali dati personali
raccoglie?
Dati di contatto, input
utente, informazioni
social, dati di log e
utilizzo, informazioni sul
dispositivo, cookie
Dati di identità,
informazioni di
pagamento, input e
output, feedback,
informazioni tecniche
Contenuti Microsoft 365,
richieste utenti, risposte
generate, dati da plug-in
di terze parti
Testi, comandi, dati di
utilizzo, dati tecnici, dati
biometrici
Quali sono le finalità
del trattamento
Fornire servizi, migliorare
i servizi, prevenire frodi,
rispettare obblighi legali
Fornire servizi,
comunicare con gli utenti,
prevenire frodi, migliorare
i servizi
Fornire funzionalità AI,
migliorare i servizi, fornire
informazioni più
pertinenti
Rispondere a richieste,
migliorare modelli,
personalizzare esperienze
Rispetto dei requisiti
dell’articolo 5 del
GDPR
Non specificato in
dettaglio
Non specificato in
dettaglio
Conforme a GDPR, ma
non specificato in
dettaglio
Misure implementate, ma
non descritte in dettaglio
Dove sono conservati i
dati
Stati Uniti, condivisi con
fornitori di servizi e
affiliati in altre
giurisdizioni
Stati Uniti o altri paesi al
di fuori del SEE e Regno
Unito
All’interno del perimetro
Microsoft 365, con
eccezioni per capacità
Non specificato

<!-- Pagina 126 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
125
Tempi di
conservazione
Variabile, in base a finalità
e impostazioni utente
come disattivazione
cronologia
Tempo ragionevolmente
necessario per le finalità
descritte
Non specificato, criteri
impostati dagli
amministratori con
Microsoft Purview
Variabile in base alla
finalità, non specificato
Misure di sicurezza
adottate
Misure tecniche,
amministrative e
organizzative
Misure tecniche,
amministrative e
organizzative
Crittografia, sicurezza
fisica, isolamenti logici
Crittografia, controllo
accessi, monitoraggio
continuo
Nomina di eventuali
sub responsabili e/o
responsabili esterni
Fornitori di servizi di
hosting, sicurezza,
marketing
Affiliate, fornitori di
servizi, partner
commerciali
Non specificato, ma
include plug-in di terze
parti
Sub-responsabili con
accordi di protezione dati
Rispetto dei diritti
degli interessati
indicati nel GDPR
Accesso, rettifica,
cancellazione, limitazione,
opposizione, portabilità,
reclamo
Accesso, rettifica,
cancellazione, limitazione,
opposizione, portabilità,
revoca consenso
Non specificato in
dettaglio, soggetto ai
diritti GDPR
Accesso, rettifica,
cancellazione,
opposizione

<!-- Pagina 127 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
126

## 11.   Considerazioni conclusive
L’obiettivo di questo elaborato è incoraggiare i colleghi a sperimentare in prima persona le soluzioni di
AI già disponibili sul web e facilmente accessibili, in particolare quelle di AI generativa. L'Intelligenza
Artificiale sta diventando parte integrante di molte attività quotidiane, e la sua integrazione nei processi
operativi degli studi professionali sarà imprescindibile per garantire il mantenimento di efficienza e
competitività.
Numerose software house stanno già implementando soluzioni di Intelligenza Artificiale nei gestionali
utilizzati dagli studi, in particolare per le attività contabili. Tuttavia, spetta a noi professionisti
immaginare e capire come impiegare i nuovi strumenti e sfruttarli al meglio per tutte le attività della
vita professionale quotidiana, dalle più semplici alle più complesse.
L'adozione dell'Intelligenza Artificiale è inevitabile, e l'invito è quello di agire proattivamente,
sperimentando questi strumenti per comprendere come possano potenziare le nostre attività. È
importante ricordare che l'Intelligenza Artificiale non è una soluzione universale, ma un potente
strumento che richiede un'implementazione attenta e una profonda comprensione: il suo corretto
impiego permetterà agli studi di alleggerirsi dalle attività più routinarie per concentrare le forze sugli
aspetti più altamente professionali.
È essenziale accogliere queste innovazioni con un approccio equilibrato, integrando gradualmente nella
pratica professionale. Questo non solo garantirà la nostra competitività in un mercato in rapida
trasformazione, ma ci permetterà anche di ridefinire il valore e l'impatto della nostra professione
nell'era digitale.
Rimanere passivi o attendere soluzioni su misura potrebbe compromettere la nostra capacità di
affrontare le sfide del nuovo mercato. È quindi fondamentale sviluppare competenze specifiche
nell'utilizzo dell'Intelligenza Artificiale per integrarla strategicamente nei nostri processi.
La nostra esperienza, etica e professionalità sono fondamentali per costruire lo studio del futuro,
sempre attento agli interessi e ai diritti della clientela. In questo contesto, la sicurezza e la protezione
dei dati assumono un'importanza cruciale per garantire l'affidabilità del nostro operato e la tutela di
chi si affida alla nostra professionalità.
In conclusione, l'obiettivo è rimanere all'avanguardia in un panorama professionale sempre più digitale,
a beneficio dei clienti e della società nel suo complesso. L'Intelligenza Artificiale rappresenta una
straordinaria opportunità di crescita e innovazione per la nostra professione, purché sia adottata con
consapevolezza, competenza e responsabilità.

<!-- Pagina 128 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
127

## 12.   Limitazioni al lavoro
L’adozione dell’AI generativa all’interno di uno studio professionale offre una vasta gamma di
applicazioni, grazie alla diversità di soluzioni disponibili sul mercato, come emerso nel corso del
presente lavoro. Oggi i modelli di AI più avanzati, definiti “di frontiera”, dimostrano elevate
performance in una serie di compiti, che spaziano dal ragionamento e la conoscenza di base, fino alla
generazione di codice informatico, comunicazione, analisi dati e calcoli matematici. Le prestazioni di
questi modelli possono essere valutate tramite  benchmark  e test indipendenti, come quelli consultabili
su piattaforme specializzate come  https://artificialanalysis.ai . Tuttavia, il modello con i migliori risultati
nei test potrebbe non essere sempre quello più adatto alle specifiche esigenze di uno studio. Infatti,
nella scelta del modello giusto entrano in gioco fattori soggettivi rilevanti, poiché i modelli possono
essere addestrati e personalizzati per svolgere compiti specifici, rispondendo a necessità operative
particolari. Inoltre, l’evoluzione tecnologica è così rapida che modelli oggi considerati all’avanguardia
potrebbero essere presto superati da nuove soluzioni, rendendo la scelta e l’aggiornamento costante
una parte cruciale della strategia tecnologica di uno studio.
Tali considerazioni fanno sì che anche il presente lavoro corra il rischio di essere superato nel giro di
pochi mesi (o settimane) dalla sua pubblicazione. Con questa consapevolezza abbiamo comunque
voluto mettere a disposizione un primo vademecum operativo (una specie di punto di partenza) per
iniziare a testare e far propri gli utilizzi di questi nuovi strumenti.
Le risposte elaborate dai modelli LLM nella presente guida hanno esclusivamente scopo dimostrativo
e sono volte a illustrare le capacità e i limiti degli strumenti di intelligenza artificiale. Si precisa che tali
risposte potrebbero contenere errori, imprecisioni o allucinazioni, fenomeno noto nell'ambito dell'AI
in cui il sistema genera informazioni non accurate o fuorvianti. Pertanto, si raccomanda all'utente di
verificare sempre l'accuratezza delle informazioni ottenute prima di prenderle come base per decisioni
operative o professionali. Gli autori non si assumono alcuna responsabilità per eventuali danni o
conseguenze derivanti dall'uso delle informazioni fornite.

<!-- Pagina 129 -->
GUIDA OPERATIVA DI INTELLIGENZA ARTIFICIALE
L’aiuto intelligente al Commercialista
128

## 13.   Appendice
Link ai vari software di LLM richiamati:

### 1.   OpenAI GPT-4 : OpenAI -  https://openai.com/index/gpt-4

### 2.   Google Gemini :  Google AI  -  https://ai.google/

### 3.   Anthropic Claude :  Anthropic  -  https://www.anthropic.com/

### 4.   Copilot :  Microsoft Copilot  -  https://www.microsoft.com/en-us/microsoft-365/copilot

### 5.   Perplexity AI :  Perplexity AI  -  https://www.perplexity.ai/

<!-- Pagina 130 -->
Fondazione Nazionale di Ricerca dei Commercialisti E.T.S.
Piazza della Repubblica, 68 00185 Roma
