# Dazi e BEP

### Lo studio del punto di pareggio per compensare i dazi
L’articolo esamina l'impatto dei dazi doganali sul punto di pareggio e sulla sostenibilità economica delle imprese esportatrici europee. In un contesto di tensioni geopolitiche e politiche protezionistiche, l'introduzione o l'aumento dei dazi può influenzare significativamente i margini aziendali e la competitività. L'analisi proposta utilizza un modello semplificato, basato su formule parametriche e un tool specifico, per valutare e simulare l'effetto dei dazi sul conto economico aziendale. Per comprendere gli effetti, occorre formulare scenari e l’articolo ne delinea due: da un lato illustra come un venditore italiano potrebbe adattarsi all'introduzione di un dazio del 20% sulle esportazioni negli Stati Uniti per rimanere competitivo, dall’altro come potrebbe reagire qualora dovesse sopportare dazi in entrata, esplorando le implicazioni per i costi, la domanda e i margini di profitto.
### I Dazi come componente del modello di margine
Le tensioni geopolitiche e le politiche protezionistiche adottate da alcuni Paesi, in particolare dagli Stati Uniti, hanno riportato al centro del dibattito economico il tema dei dazi doganali. Questi strumenti, utilizzati per tutelare la produzione interna o per ragioni strategiche, impongono una tassa sulle merci importate e hanno un effetto diretto sulle dinamiche di prezzo, competitività e margini aziendali. Per le imprese europee esportatrici, l’introduzione o l’aumento di un dazio può trasformarsi in un fattore critico di vulnerabilità economica, in quanto incide sull’equilibrio finanziario e sulla sostenibilità delle vendite all’estero.
L’obiettivo di questo contributo è duplice: da un lato, comprendere come il dazio agisca sui parametri economici chiave, in particolare sul punto di pareggio; dall’altro, offrire uno strumento analitico e operativo per valutare e simulare l’impatto di diverse ipotesi di dazio sul conto economico aziendale. La trattazione si concentra su un modello semplificato ma efficace, basato su formule parametriche e su un’applicazione pratica tramite un tool specificamente progettato per rappresentare in sintesi le simulazioni del punto di pareggio, Break Even Point_24.
Supponiamo che un venditore italiano esporti un macchinario negli Stati Uniti al prezzo di 10.000 euro. Con l'introduzione di un dazio del 20% all'importazione, l'acquirente statunitense dovrà pagare un dazio di 2.000 euro (cioè il 20% di 10.000 euro) al momento dell'importazione.​
Questo aumento dei costi può portare a diverse conseguenze:​ Per l'acquirente statunitense: Il costo totale del macchinario sale a 12.000 euro (10.000 euro di prezzo base più 2.000 euro di dazio). Questo potrebbe indurlo a cercare fornitori alternativi, magari locali, per ridurre le spese.​
Per il venditore italiano: Di fronte a una possibile diminuzione della domanda dovuta all'aumento dei prezzi per l'acquirente, il venditore potrebbe decidere di ridurre il prezzo di vendita per mantenere la competitività. Ad esempio, potrebbe offrire il macchinario a 8.500 euro. In questo caso, l'acquirente pagherebbe 8.500 euro più un dazio di 1.700 euro (il 20% di 8.500 euro), per un totale di 10.200 euro. Il venditore, tuttavia, vedrebbe ridursi il proprio margine di profitto.​
Un aspetto cruciale da considerare nell'ambito dei modelli di margine riguarda l'incidenza del dazio sulle strutture di prezzo e sui costi aziendali.
Cominciamo col comprenderne gli effetti sul margine di contribuzione (Ricavi – Costi Variabili) e sul reddito netto (Ricavi – Costi Variabili – Costi Fissi) per il venditore.
In presenza di uno sconto (s) a seguito di un dazio la formula del margine di contribuzione per il venditore diventa
Se consideriamo
La formula diventa
Se vogliamo calcolare la differenza in percentuale del margine di contribuzione scriveremo
Poiché   abbiamo:
Dal momento che  altro non è che la marginalità percentuale che chiameremo m possiamo affermare che:
Dove s è la percentuale di sconto e m il margine percentuale ante sconto.
Figura : Relazione sconto 20% e perdita di Mdc
Dalla figura e dalla formula si intuisce che l’effetto sul reddito è tanto più pronunciato quanto più il margine di partenza è basso e come per non azzerare completamente il margine di contribuzione (∆Mdc = -100%) occorre che il margine di partenza non sia inferiore allo sconto applicato.
Con il medesimo procedimento si può calcolare l’effetto sul reddito netto, basterà aggiungere CF alla nostra formula.
Poiché    altro non è che la redditività netta delle vendite possiamo riscrivere la formula in
Che con un rappresentazione grafica diventa
Figura : La perdita sul reddito netto derivante da uno sconto del 20%
Anche in questo caso il punto di sostenibilità dello sconto è pari ad una redditività delle vendite pari al 20%.
Per gli allergici alla matematica, proviamo a vedere nella pratica un esempio numerico sviluppato grazie al tool Break Even Point_24, un tool per simulare azioni sulle variabili del punto di pareggio.
### La simulazione di un caso aziendale: gli effetti sulle esportazioni
Supponiamo che un’azienda abbia venduto negli USA fino ad oggi 10.000 prodotti con un prezzo unitario medio di  100,00, un costo variabile unitario di  70,00 e costi fissi 50.000,00. In assenza di sconti la situazione potrebbe essere così rappresentata.
Figura : Calcolo reddito e valori di pareggio in caso di dazi
Se l’azienda propone uno sconto al cliente americano poniamo del 10% il cliente vedrà il proprio prezzo finale diventare
Nel caso il venditore volesse mantenere inalterato il costo per l’acquirente americano dovrebbe applicare uno sconto così calcolato
Che nel caso di dazio al 20% è pari al 16,67%
Infatti
Ma uno sconto del genere rischia, come abbiamo visto, di compromettere l’intera marginalità; da qui l’utilità del tool di simulazione.
Partiamo da questa rappresentazione grafica.
Figura : Lo sconto cambia l'inclinazione della linea dei ricavi
Come si nota la riduzione di prezzo del 16,67% porta ad uno spostamento del punto di pareggio verso destra.
La figura seguente spiega meglio quali interventi potrebbero essere necessari in caso di sconto
Figura : Le manovre per il recupero del margine
Come si nota lo sconto ha portato una diminuzione del risultato calcolato del 66,67% inferiore all’obiettivo, pari ai 250.000,00 iniziali. Le frecce riportano le manovre che da sole sarebbero sufficienti per il recupero del margine: un aumento della quantità del 125% o una riduzione del 23,81% dei costi variabili.
Alcune delle manovre sono oggettivamente non perseguibili. Raddoppiare le vendite sarebbe pressoché impossibile.
È curioso notare che, se per assurdo le imprese esportatrici scegliessero la brillante strategia di aumentare le quantità vendute per compensare la perdita di margine causata dalla riduzione dei prezzi per assorbire i dazi, si troverebbero di fronte a un magnifico effetto boomerang. Infatti, incrementare le esportazioni significherebbe ampliare ulteriormente quel deficit della bilancia commerciale che, con un semplicismo davvero ammirevole, è stato indicato come motivo principale per introdurre i dazi stessi.
La soluzione per recuperare i maggiori costi derivanti dai dazi, quindi, può essere soltanto un equilibrato cocktail di interventi su tutti i fattori coinvolti
Il tool assiste l'utente nel processo di analisi delle variazioni di una variabile, considerando le altre variabili coinvolte e le modifiche già apportate.
Ipotizziamo che il massimo dell’incremento delle quantità vendute sia il 10%, le soluzioni sulle altre variabili diventano:
Figura : Le manovre in caso di aumento del 10% delle quantità
Supponiamo che si riesca a ottenere una riduzione dei costi variabili del 18% agendo ad esempio su materiali, provvigioni e trasporti il quadro diventa
Figura : La situazione a seguito della riduzione dei costi variabili
Ora la riduzione dei costi fissi del 29,5% appare una scelta obbligata se si vuole il raggiungimento dell’obiettivo. Tuttavia tale taglio potrebbe essere eccessivo o non perseguibile; se ipotizziamo una riduzione dei costi fissi del 10%, possiamo riconsiderare, cancellando il valore precedentemente inserito, le quantità di pareggio.
Figura : Situazione finale e pieno recupero del margine
Nell’ipotesi che fosse possibile ridurre i costi variabili del 18% e i costi fissi del 10% e il cliente fosse disposto ad aumentare le quantità acquistate del 13,75% sarebbe possibile garantire uno sconto per azzerare l’effetto dazi sull’acquirente.
Ovviamente l’esempio è del tutto indicativo e volutamente semplificato ma non è da escludere che i grossi esportatori facciano ragionamenti simili a quelli esposti per mantenere il mercato statunitense, con buona pace delle intenzioni di riduzione delle importazioni.
### La simulazione di un caso aziendale: gli effetti sulle importazioni
Il tool ha una terza parte che consente anche di calcolare gli effetti di un incremento dei costi variabili qualora si volesse simulare l’effetto contrario a quello fin qui descritto: la presenza di un dazio all’importazione.
Poniamo che, in uno scenario di guerra commerciale che ci auguriamo rappresenti un’ipotesi remota, quale reazione ai dazi in uscita, si stabilisca un dazio in entrata del 20% sulle importazioni. In quel caso il tool consente di calcolare l’aumento di prezzo per compensare. Si noti che la compensazione può avere due distinti obiettivi: il recupero del margine assoluto e quello del margine percentuale.
L’incremento di un costo variabile “i”  può essere compensato mediante un aumento di prezzo pari a
Da cui si ottiene
Figura : L'aumento di prezzo per mantenere il margine a fronte di un dazio in entrata del 20%
Come si vede, nonostante il margine resti invariato per effetto dell’incremento di prezzo, la marginalità scende dal 25% al 20,83% per effetto del maggior fatturato.
Laddove si volesse puntare al mantenimento della marginalità, si dovrebbe optare per un aumento di prezzo pari a
Da cui si ottiene
L’aumento del 28,57% di prezzo avrebbe quindi questi effetti
Figura : L'aumento di prezzo per mantenere la marginalità invariata a fronte di un dazio in entrata del 20%
Nel caso il mercato fosse in grado di assorbire l’aumento di prezzo del 28,57% la marginalità dell’azienda rimarrebbe invariata.
Il filo rosso che unisce tutti gli esempi trattati è l’effetto dei dazi sulla variazione potenziale aumento di prezzi e di conseguenza l’emergere dell'inflazione.
I dazi, infatti, incrementano i costi di produzione, spingeranno le aziende ad alzare i prezzi. Questo aumento dei prezzi può portare a una riduzione del potere d'acquisto dei consumatori e a un incremento generale dei costi, contribuendo allo scenario della “tempesta perfetta”. A meno che non si tratti della nota tecnica negoziale della “porta in faccia” che consiste nell’avanzare che consiste nel fare inizialmente una richiesta esagerata o eccessiva, per poi avanzare una richiesta più ragionevole (quella che si desiderava realmente ottenere). In pratica un bluff molto pericoloso.