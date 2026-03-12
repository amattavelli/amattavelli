# Excellere in Studio4

# Excellere in Studio 4: Collegare i dati tra loro (II parte)
## INTRODUZIONE
Nella scorsa puntata abbiamo cominciato ad apprezzare l’importanza di poter collegare tra loro i dati, trattandoli come oggetti ricchi di informazioni da scambiare e condividere. Oggi compiremo un passo decisivo: cercheremo di sintetizzare e sommare i dati tra loro per ottenere veri e propri report.
Se avete seguito e provato a ripetere gli esercizi proposti nella prima parte di questo intervento, pubblicata nel numero di aprile, dovreste ormai avere familiarità con le tabelle e con i concetti di chiave e di condizione.
Ora si tratta di applicare tali concetti anche alle somme condizionali e poi estenderli alle Query che occuperanno l’ultima parte di questo intervento.
Oggi impareremo a raggruppare e sintetizzare i dati a filtrarli e a calcolarne le somma o la media o il conteggio utilizzando sia le formule che le Power Query, funzione recentemente rinominata Get and Transform e tradotta nella versione Italiana Recupera e Trasforma.
Le applicazioni sono innumerevoli: contabilità, bilancio, report di vendita e di produzione, solo per citare le più comuni. Ma potremmo dire serenamente che unendo le funzionalità delle funzioni di ricerca e di somma condizionale è possibile realizzare pressoché qualsiasi operazione di analisi dati.
Come sempre tutti gli esempi e anche alcuni esercizi sono scaricabili nel foglio ExcellereInStudio4.xlsx.
## CHIAVI E CRITERI
Quando abbiamo affrontato per la prima volta il tema del collegamento tra dati e tabelle è emersa l’esigenza di disporre di un campo comune, che abbiamo definito chiave. Una volta individuata la chiave, non è stato difficile correlare i movimenti al piano dei conti, per mezzo del codice conto o aggiungere la nazione alle vendite richiamando il codice cliente. Un concetto del tutto simile è il criterio: il criterio è la condizione in base alla quale una determinata operazione deve essere eseguita oppure non eseguita. A differenza della chiave, il criterio non è necessario che esista e sia verificato: mentre cercare di ottenere le informazioni del cliente ROSSI in una tabella che non contiene il cliente ROSSI restituisce un errore, la somma del fatturato del cliente ROSSI da una tabella che non riporta ROSSI avrà come risultato 0; Le chiavi sono univoche i criteri possono essere multipli.
L’uso più comune dei criteri è rappresentato dalla somma e il conteggio condizionale che in Excel si traduce nelle funzioni: CONTA.SE(), SOMMA.SE(), CONTA.PIÙ.SE(), SOMMA.PIÙ.SE() e altrettanto utili anche se meno utilizzate: MEDIA.SE() e MEDIA. PIÙ.SE() e MAX. PIÙ.SE(). Potremmo dire che le funzioni di aggregazione si distinguono per il tipo di operazione e il numero di condizioni utilizzate: il prefisso indica il tipo di operazione, la locuzione PIÙ indica la possibilità di utilizzare più di un criterio.
## SOMMA.SE() e CONTA.SE()
La funzione SOMMA.SE() si presenta composta da tre argomenti con la seguente sintassi:
SOMMA.SE(INTERVALLO; Criterio; INT_SOMMA)
che possiamo tradurre in somma nell’INT_SOMMA tutto ciò che rispetta il CRITERIO nell’INTERVALLO (che chiameremo anche intervallo_criteri). Appare evidente come l’intervallo_criteri e l’int_somma debbano avere lo stesso numero di righe.
In pratica è come se Excel leggesse ogni riga dell’intervallo selezionato e procedesse a sommare i numeri dell’int_somma per ciascuna riga che soddisfa il criterio, secondo questo schema:
Vediamo gli argomenti della funzione uno alla volta:
- Intervallo: può trattarsi di un gruppo di celle, di una colonna, di un nome o più raramente di una formula. È il “luogo” in cui è contenuta e va verificata la condizione. Le celle dell’intervallo possono contenere testo o numeri
- Criterio: è un’espressione che contempla gli operatori = (che può essere omesso) >, >=, <, <=. Gli operatori vanno sempre posti tra virgolette;
- Int_SOMMA: può trattarsi di un gruppo di celle, di una colonna, di un nome o più raramente di una formula. È il “luogo” in cui sono contenuti i valori da sommare, qualora la condizione sia verificata. Le celle che compongono l’intervallo possono contenere sia numeri che testo (quest’ultimo sarà considerato alla stregua di uno 0 nella somma).
La funzione CONTA.SE() ragiona in maniera analoga, solo che al posto di sommare i valori dell’int_somma, conta i valori dell’intervallo che soddisfano le condizioni.
Gli esempi come sempre chiariscono i concetti e data la parentela stretta tra le funzioni di ricerca quali il CERCA.VERT() e quelle di aggregazione (somma, media e conteggio condizionale), riprenderemo da qui in avanti alcuni degli esempi trattati nella scorsa puntata, e li completeremo sommando e conteggiando i dati.
Cominceremo con un semplice conteggio e via via saliremo di complessità, proprio come accade quando si affronta una vetta.
Nel primo esempio abbiamo una tabella clienti, ci interessa conoscere il numero di clienti per nazione e per tipo.
Cominciamo col riportare le tipologie di cliente e le nazioni sul foglio di lavoro.
In colonna B dovranno apparire il numero di Rivenditori e Utilizzatori, nella colonna D il numero di clienti per ogni nazione. Utilizzeremo la funzione CONTA.SE() indicando quale intervallo, rispettivamente le colonne Nome Cliente e Tipo Cliente.
In B31 potremo scrivere:
+CONTA.SE(Tabella2[Tipo Cliente];A31)
La sintassi di queste formule può sembrare complicata ma se si utilizzano mouse e tastiera invece che digitare, la formula si compila da sola.
Ecco il procedimento, come spesso accade, la descrizione è molto più lunga dell’esecuzione.
- In B31 cominciamo con lo scrivere +CONTA, man mano che scriviamo il TAG sottostante ci mostra le funzioni che corrispondono a quanto stiamo scrivendo, restringendo via via l’elenco. Selezioniamo con i tasti cursore CONTA.SE e premiamo il tasto TAB.
- La formula si completerà diventando +CONTA.SE(
- Per inserire l’intervallo_criteri selezioniamo la colonna Tipo Cliente
- La formula si completerà diventando +CONTA.SE(Tabella2[Tipo Cliente] aggiungiamo un punto e virgola per terminare l’argomento
- Ora dobbiamo inserire il criterio per il quale basterà cliccare sul campo A31 infine chiudiamo la parentesi
Oppure, se non vogliamo utilizzare i riferimenti di tabella:
=CONTA.SE($G$19:$G$28;A31)
O ancora:
=CONTA.SE(G:G;A31)
In tutte e tre le formule, che portano agli stessi risultati, si sta chiedendo ad Excel di contare solo gli elementi nella colonna G o nel campo Tipo Cliente che sono uguali al contenuto della cella A31; il criterio è quindi: =A31, che diventa A31, poiché il segno “=” può essere omesso. Copiando la formula nella cella sottostante si ottiene il conteggio degli utilizzatori.
Con procedimento analogo calcoliamo il numero di clienti per nazione a partire dalla cella D31. Il criterio questa volta sarà contenuto nella colonna C e dovrà essere confrontato con il campo Nazione contenuto nella colonna F.
La soluzione sarà: CONTA.SE(Tabella2[Nazione];C31)
Oppure, se non vogliamo utilizzare i riferimenti di tabella:
=CONTA.SE($F$19:$F$28;C31)
O ancora:
=CONTA.SE(F:F;C31)
Nelle formule appena viste e in quelle che seguiranno viene fatto largo uso dei riferimenti assoluti, che abbiamo già trattato nel numero di febbraio.
Introduciamo una tecnica al riguardo molto utile: per trasformare un riferimento relativo in assoluto è sufficiente premere il tasto F4 mentre si digita il riferimento, se si preme nuovamente F4 il riferimento diventa relativo sulla colonna e assoluto sulla riga, se si preme ancora F4 il riferimento diventa relativo sulla riga e assoluto sulla colonna, se si preme ancora un’ultima volta, il riferimento torna interamente relativo e così via in maniera ciclica. Provate a scrivere +A1 in una cella poi premete a ripetizione F4 e sperimenterete quanto appena descritto.
Compreso il concetto di intervallo e criterio e dell’uso dei riferimenti assoluti e relativi per indicarli, possiamo affrontare la più utilizzata tra le funzioni di aggregazioni, SOMMA.SE().
Con il SOMMA.SE() la logica permane la medesima, ma abbiamo la compresenza di un intervallo e di un int_somma, la funzione esegue una data operazione, la somma dell’intervallo, solo quando la cella contenuta nell’intervallo_criteri soddisfa il criterio.
Per vedere una prima applicazione, riprendiamo l’esempio contabile della prima parte.
Abbiamo un’estrazione da un bilancio di verifica TAB_1 che vogliamo riclassificare secondo lo schema della TAB_2 in cui è stata aggiunta una colonna Riclass, che riporta la riclassificazione in un bilancio riclassificato. Alcune voci appartengono alle immobilizzazioni mentre altre attengono alla liquidità.
In B55 dovrà apparire il totale delle Immobilizzazioni e in B56 il totale della Liquidità. I criteri sono da ricercarsi nella colonna A alle righe 55 e seguenti, mentre l’intervallo in cui va verificato il criterio per ogni riga della tabella è da individuarsi nella colonna Riclass della TAB_2 e la colonna da sommare è l’Importo della TAB_1. Qualcosa non torna… Intervallo_criterio e Int_somma appartengono a due tabelle differenti non ancora legate tra loro. Osserviamo però, forti dell’esperienza maturata nella prima parte di questo intervento, che le due tabelle hanno una chiave comune il CODICE/Cod. Basterà allora collegare le due tabelle per mezzo della chiave comune e riportare in TAB_1 il campo Riclass.
Ancora una volta notiamo che SOMMA.SE() mostra ancora di più le sue potenzialità quando è utilizzato insieme al CERCA.VERT(). In pratica prima collego poi sintetizzo e sommo.
Cominciamo col collegare per mezzo del CERCA.VERT().
In D38 scriviamo RICLASS, grazie alle caratteristiche delle Tabelle, verrà creata direttamente la colonna pronta ad accogliere la seguente formula:
=+CERCA.VERT([@Descrizione];TAB_2[[DESCRIZION]:[Riclass]];2;0)
Anche in questo caso descriviamo la procedura per utilizzare mouse e tastiera per compilare da sola la formula invece che digitare complicate sintassi.
- In una cella qualsiasi del campo Riclass cominciamo con lo scrivere +CE, il TAG sottostante mostra le funzioni , Selezioniamo con i tasti cursore CERCA.VERT e premiamo il tasto TAB.
- La formula si completerà diventando +CERCA.VERT(
- Per inserire la chiave posizioniamoci sul campo Descrizione restando nella stessa riga è sufficiente premere due volte il tasto freccia a sinistra oppure cliccare col mouse ricordiamoci di chiudere sempre l’argomento con un “;”
- La formula si completerà diventando +CERCA.VERT([@Descrizione];
- Ora dobbiamo inserire la matrice_tabella, che abbiamo definito come quell’insieme di celle o colonne o campi che hanno quale prima colonna il campo in cui è presente la chiave, selezioniamo con tastiera o mouse il campo DESCRIZION e il campo RICLASS e poniamo il consueto punto e virgola finale. La formula si completerà diventando:
- +CERCA.VERT([@Descrizione]; TAB_2[[DESCRIZION]:[Riclass]];
- Abbiamo selezionato due colonne e ci interessa riportare il contenuto della seconda colonna quando corrispondente alla chiave e non siamo interessati ad alcuna approssimazione, quindi completiamo la formula aggiungendo 2;0, chiudiamo la parentesi e abbiamo finito.
Abbiamo ottenuto la compresenza dell’intervallo_criteri e dell’intervallo; ora non ci resta che sommare tutti gli importi ogniqualvolta vi sia corrispondenza tra criterio e intervallo.
In B55 scriveremo, utilizzando mouse e tastiera per la compilazione automatica:
=+SOMMA.SE(TAB_1[Riclass];A55;TAB_1[Importo])
Che si traduce in: somma l’importo di tutte le righe in cui il codice di riclassificazione è uguale al contenuto di A55. Copiando la formula nella cella sottostante si ottiene la somma anche della liquidità.
Comprendere e mettere in pratica ciò che abbiamo appena visto, apre la strada a possibilità di risparmi di tempo veramente rilevanti (ve l’avevo promesso) in moltissime attività tipiche dell’attività professionale.
Fino a che non ho appreso l’uso del CERCA.VERT() e del SOMMA.SE(), ho sempre riclassificato i bilanci con la “tecnica della spunta”: leggevo un elenco e riportavo le cifre nella voce corrispondente sommandole manualmente, regolarmente dimenticavo o duplicavo qualche voce, per non parlare degli errori di battitura…
Oggi invece per qualsiasi riclassificazione debba realizzare utilizzo la seguente procedura:
- Numero a piacere (solitamente salto di 5 in 5 per consentire l’inserimento di nuove voci) le voci del Bilancio (ma potrebbe trattarsi anche di un quadro RF, di un questionario ISTAT, etc…)
- Nell’elenco da riclassificare aggiungo due colonne che nomino codvoce e descrizione
- Per ogni riga dell’elenco da riclassificare, compilo la colonna codvoce e ottengo, grazie al CERCA.VERT(), la corrispondente descrizione, così facendo sono sicuro di riclassificare tutte le voci una sola volta attribuendo una voce dell’elenco obiettivo
- Nell’elenco obiettivo utilizzo la funzione SOMMA.SE() ottengo i totali e il gioco è fatto!
Non solo il procedimento appena descritto è più veloce e privo di errori (provare per credere!), ma presenta vantaggi non trascurabili: consente la ricostruzione e disaggregazione immediata di ogni voce riclassificata e rende agevole ogni successiva modifica alla riclassificazione.
Saggiamo con ulteriori esempi la potenza degli strumenti di aggregazione e somma ripercorrendo sempre gli esempi del numero di maggio.
Prendiamo il caso di una procedura concorsuale che presenta il seguente elenco creditori
Vogliamo i totali crediti ammessi e non ammessi per categoria.
Avremo quindi un unico intervallo che dovrà corrispondere a C68, “Privilegio” e C69, “Chirografo” con due differenti int_somma.
Per sfruttare meglio la situazione e ridurre al minimo la digitazione spostiamo la colonna Importo accanto alla colonna Non ammesso, per farlo collochiamoci in C61 e cliccando sul tasto sinistro del mouse, poco sotto selezioniamo l’intera colonna, trasciniamo la colonna dopo la colonna tipo.
Ora in D68 scriveremo la formula una sola volta che poi copieremo in E68, D69, E69; per riuscirci dovremo sfruttare bene i riferimenti assoluti e relativi.
La formula in D68 corrisponde a
+SOMMA.SE($C$62:$C$65;$C68;D$62:D$65)
Osserviamo l’uso del “$” e proviamo a tradurre la funzione in linguaggio comune. Stiamo chiedendo a Excel di sommare tutti gli elementi che nella colonna C uguali alla cella corrispondente nella medesima riga posta nella colonna C utilizzando come somma l’intervallo dalla riga 62 alla riga 65, nella colonna corrispondente.
Copiando la formula, l’intervallo_criteri resterà costante, il criterio manterrà sempre la colonna C e varierà di riga mentre l’int_somma manterrà costante le righe di riferimento ma modificherà la colonna.
Ora copiamo la cella D68 nell’intervallo D68:E69 e otterremo la soluzione dell’esercizio con un solo passaggio.
I più attenti avranno notato che per far funzionare la formula abbiamo dovuto modificare “Privilegiato” in “Privilegio”, altrimenti il criterio non avrebbe trovato alcuna corrispondenza in int_criterio.
Facile no? E sarebbe stato ugualmente facile qualora avessimo avuto 30 colonne e 300.000,00 righe, i passaggi sarebbero stati esattamente gli stessi e anche i tempi di esecuzione!
Anche nel caso delle assemblee il SOMMA.SE() può tornare utile.
Nella tabella abbiamo una situazione piuttosto comune: 4 partecipanti di cui uno presente in delega; vogliamo sapere ogni presente quanti diritti rappresenta e quanto peserà il suo voto. La soluzione è il calcolo dei diritti rappresentati. Identifichiamo l’intervallo_criteri: poiché ci interessa verificare la somma dei voti dei delegati, dovremo esaminare le righe del campo Delega a e verificare l’uguaglianza con quanto riportato nel campo Presenti. In una cella qualsiasi del campo Diritti rappresentati comporremo la seguente espressione:
=+SOMMA.SE([[Delega a ]];[@Presenti];[Diritti di voto])
E otterremo così:
Per il campo Totale abbiamo utilizzato la formula
=+[@[Diritti rapprensentati]]+[@[Diritti di voto]]*([@[Delega a ]]="")
Che corrisponde a dire somma i diritti rappresentati ai diritti di voto in tutti quei casi non c’è un delegato.
Un’operazione molto frequente, che solitamente richiede molto tempo se eseguita manualmente, è proprio la riconciliazione contabile.
Ricordo ancora che, la prima volta che sono entrato in uno studio di commercialisti, ero rimasto affascinato da due giovani professionisti che si ripetevano l’un l’altro cifre apparentemente senza un senso compiuto, non sapendo ancora allora quante volte avrei dovuto ripetere quel rituale! Così è stato fino a che non ho incontrato sulla mia strada il CERCA.VERT() e il SOMMA.SE() e compreso le potenzialità. Già nella scorsa puntata abbiamo avuto modo di apprezzare l’uso del CERCA.VERT() per trovare cifre che non trovano corrispondenza.
Tuttavia la funzione CERCA.VERT() è in grado di identificare solo le cifre presenti in un conto e assenti nell’altro, mentre non serve per individuare cifre ripetute un numero di volte differente.
Si coglie come il controllo con il CERCA.VERT() individui l’operazione del 21/02/2018 per Euro 165,00 come non riportata nel Conto_2 ma “non si accorga” del fatto che il movimento di Euro 921,00 è sì presente in entrambi i conti ma nel Conto_2 è riportata due volte e così pure il movimento di Euro 894,00 è presente due volte nel Conto_1 e una sola volta nel Conto_2.
La formula in colonna D dovrà quindi sommare tutti gli importi del Conto_1 che corrispondono all’importo corrente (quello collocato sulla medesima riga nella colonna B) e confrontarli con gli importi del Conto_2.
Viceversa la formula in colonna H dovrà sommare tutti gli importi del Conto_2 che corrispondono all’importo corrente (quello collocato sulla medesima riga nella colonna F) e confrontarli con gli importi del Conto_1.
In D119 scriveremo quindi
=+SOMMA.SE($B$119:$B$128;B119)-SOMMA.SE($F$119:$F$128;B119)
che copiato e incollato nella cella H119 diventa:
=+SOMMA.SE($B$119:$B$128;F119)-SOMMA.SE($F$119:$F$128;F119)
Si noti che quando l’int_somma coincide con l’intervallo, l’int_somma può essere omesso.
Dal confronto della colonna D e della colonna H emergono chiaramente le poste da porre in riconciliazione: la duplicazione in Conto_2 di 921, l’assenza in Conto_2 di 165, la duplicazione in Conto_1 di 894 e l’assenza in Conto_1 di 169.
Per trovare quante volte una cifra è ripetuta si può utilizzare anche il CONTA.SE(), lascio ai più diligenti di voi l’applicazione al caso di questa funzione.
## SOMMA.PIÙ.SE()
La funzione SOMMA.PIÙ.SE() ha fatto la sua comparsa la prima volta con Excel 2007 ed è stata subito salutata da un deciso entusiasmo dagli utenti Excel che già avevano avuto modo di sperimentare la funzione SOMMA.SE().
Fino a quel momento e ancora oggi per chi possiede versioni ante 2007 per sommare intervalli rispondenti a criteri multipli occorreva creare una colonna criterio composta.
Per chiarire e per dare una chance anche ai lettori con versioni obsolete (che sarebbe ora di cambiare se intendete fare di Excel un vostro alleato) risolveremo il prossimo esempio con entrambi i metodi.
La tabella, che abbiamo rinominato Fat, riporta le vendite di 4 linee di prodotti su tre esercizi, siamo interessati a conoscere il fatturato di ciascun prodotto in ogni esercizio.
Se non vogliamo o possiamo utilizzare la funzione SOMMA.PIÙ.SE(), dobbiamo ricorrere ad un artifizio, creando una colonna che concatena il campo Anno con il campo Linea e che chiameremo AnnoLinea.
Per compilare l’AnnoLinea abbiamo due strade:
- possiamo utilizzare la funzione CONCATENA() inserendo negli argomenti gli elementi da concatenare ad esempio in C33 scriveremo CONCATENA(A133;B133) oppure =+CONCATENA([@Anno];[@Linea]) o ancora, ma solo nella versione 2016/Office365 CONCAT([@Anno]:[@Linea])
- possiamo concatenare direttamente gli elementi usando l’operatore “&” e pertanto scriveremo A133&B133 o [@Anno]&[@Linea]
Così facendo le nostre condizioni multiple sono state unificate in un’unica condizione ed è pertanto possibile utilizzare la funzione SOMMA.SE() avendo cura di impostare anche il criterio come concatenamento di due criteri.
Il criterio diviene infatti G$132&$F133, assolutizzando il riferimento di riga per l’anno e il riferimento di colonna per la linea.
Con la funzione SOMMA.PIÙ.SE() tutto diventa più semplice.
La funzione SOMMA.PIÙ.SE() consente di combinare fino a 127 criteri con altrettanti intervalli_criteri , anche se normalmente se ne usano molti meno e di inserire criteri con operatori >, <, >=, <= combinandoli tra loro.
La sintassi ricalca quella del SOMMA.SE() ma l’int_somma occupa la posizione del primo argomento e le coppie di intervallo_criteri e criterio, il cui ordine è irrilevante, occupano gli argomenti successivi.
Vediamo l’applicazione al caso appena trattato:
int_somma corrisponde al campo Fatturato, qualsiasi saranno le condizioni, occorrerà sommare il contenuto della colonna Fatturato avente corrispondenza tra criteri e intervalli
int_criteri1 può indifferentemente essere o il campo Anno, in tal caso il criterio andrà ricercato nelle intestazioni di colonna della tabella di sintesi, oppure nel campo Linea e in tal caso il criterio andrà ricercato nelle intestazioni di linea della tabella di sintesi.
Ecco quindi la formula da inserire in una cella qualsiasi della tabella soluzione.
=+SOMMA.PIÙ.SE(Fat[Fatturato];Fat[Linea];[@Linea];Fat[Anno];G$133)
Che tradotta in linguaggio comune significa: somma la colonna fatturato se il campo Linea della Fat è uguale alla Linea corrente e se l’Anno è uguale alla colonna corrispondente al riferimento. Come di consueto abbiamo utilizzato i riferimenti assoluti e relativi per ottimizzare i tempi nei successivi copia e incolla.
Vediamo un ultimo esempio, ancora più significativo.
Abbiamo quattro tabelle. Nella scorsa puntata avevamo utilizzato la funzione CERCA.VERT() per completare la tabella Vendite con i dati provenienti dalle tabelle AnClienti, Aree e Prodotti ora vogliamo i totali per Categoria/Area e per Categoria/Mkt con possibilità di scegliere una Zona.
Nel primo caso avremo due condizioni, nel secondo tre.
Previa creazione della colonna Fatturato, prodotto di prezzo e Qta, in B24 comporremo, con tastiera e mouse e un sapiente uso del tasto funzione F4, la seguente funzione:
=+SOMMA.PIÙ.SE(Vendite[Fatturato];Vendite[Categoria];$A24;Vendite[Area];B$23)
Lasceremo libero il riferimento riga della Categoria e bloccheremo la colonna e lasceremo libero il riferimento di colonna dell’Area e bloccheremo il riferimento di riga e così potremo copiare la cella B24 nelle altre.
In F24 invece la formula diventa:
=+SOMMA.PIÙ.SE(Vendite[Fatturato];Vendite[Area];$F$22;Vendite[Categoria];$E24;Vendite[Mkt];F$23)
Che si traduce in somma il fatturato per l’AREA corrispondente a F22 (in qualsiasi cella venga copiata la formula) con categoria corrispondente a quanto riportato nella colonna E e con Mkt corrispondente a quanto riportato in riga 23.
Nel foglio Excellere in Studio4.xlsx sono riportati oltre a tutti gli esempi dell’articolo anche alcuni esercizi per fare pratica con questa importantissima funzione, provate a completarli sia con l’uso del SOMMA.SE() e SOMMA.PIÙ.SE(), sia con le Query che tratteremo nel prossimo paragrafo.
## POWER QUERY E GET & TRANSFORM (RECUPERA E TRASFORMA)
Sebbene all’apparenza non sembra cambiato molto, Excel 2016 o Excel365 rappresenta una vera e propria rivoluzione per gli utilizzatori di Excel grazie all’introduzione dell’interfaccia RECUPERA E TRASFORMA e la comparsa delle Power Pivot. In realtà uno strumento analogo, le Power Query, aveva fatto già la sua apparizione un po’ in sordina con un componente aggiuntivo, con GET & TRANSFORM, tradotto in RECUPERA E TRASFORMA nella versione Italiana, la funzionalità è ricompresa nel pacchetto Excel2016 o Excel365. Per chi non avesse l’ultima versione di Excel, le Power Query sono disponibili all’indirizzo https://www.microsoft.com/it-it/download/details.aspx?id=39379,
RECUPERA E TRASFORMA, come la stessa parola indica, è stato introdotto per recuperare e trasformare i dati in modo semplice e immediato e consente di connettere, combinare e perfezionare le origini dati in base a specifiche esigenze di analisi.
In pratica potremo importare dati anche da fonti differenti, collegarli tra loro sostituendo di fatto la funzione CERCA.VERT() e sintetizzarli calcolando somme e altri subtotali, facendo a meno delle funzioni di aggregazione SOMMA.SE(), CONTA.SE(), SOMMA.PIÙ.SE() …
In questo articolo ci limiteremo ad introdurre l’argomento e a risolvere l’ultimo esempio affrontato, ottenendo gli stessi risultati. Più avanti, quando affronteremo il discorso delle tabelle PIVOT, torneremo ad occuparci di questa funzionalità che sta sconvolgendo il modo di fare analisi dati e non solo con Excel.
Riprendiamo allora le nostre tabelle Vendite, AnClienti, Aree e Prodotti che abbiamo rinominato TabVendite, TabAnClienti, TabAree e TabProdotti e a cui abbiamo rimosso tutti i campi calcolati in precedenza.
I passaggi da seguire per l’utilizzo della funzionalità RECUPERA E TRASFORMA sono i seguenti
- Individuare e caricare la base dati o meglio il modello dati (RECUPERA)
- Selezionare le informazioni rilevanti collegando tra loro eventualmente le tabelle (TRASFORMA)
- Sintetizzare i dati (ANALIZZA), questa fase può essere eseguita anche mediante l’utilizzo di Tabelle Pivot o strumenti di Business Intelligence quali le PowerBi.
Nel nostro esempio la fase denominata RECUPERA è molto semplice; come indicato in figura, basterà accedere alla scheda DATI (POWER QUERY per le versioni precedenti) e posizionandosi su una cella qualsiasi della tabella che si intende caricare nel modello dati cliccare sul comando . Impartito il comando, apparirà un’interfaccia completamente diversa da quella a cui siamo abituati con cinque schede e tre aree di lavoro.
Partendo da sinistra a destra troviamo infatti:
- l’area Query in cui sono presenti le Tabelle che compongono il Modello dati
- L’area Dati che mostra i dati importati ed eventualmente trasformati
- L’area Proprietà che mostra oltre al nome della Query i passaggi di trasformazione che sono stati eseguiti sui dati; sarà così facile ripercorrere e modificare in qualsiasi momento le operazioni eseguite.
Per ritornare ad Excel occorre cliccare sul comando ; Excel a questo punto creerà una tabella collegata alla principale che riporta tutti i dati della Query eseguita in base alle trasformazioni eseguite.
Nel nostro caso dobbiamo importare quattro tabelle, quindi ripeteremo l’operazione eseguita per la TabVendite per le altre tabelle. Otterremo il seguente risultato
L’area Query ora contiene le quattro tabelle che possono essere collegate tra loro.
Prima però occorre calcolare il fatturato mediante il comando Aggiungi colonna/Colonna personalizzata
Si accede alla finestra di dialogo Colonna personalizzata in cui è possibile inserire la nostra formula richiamando i campi con un semplice click e collegandoli con l’operatore “*”.
Il risultato sarà la compilazione della colonna Fatturato. Ora occorre importare nella TabVendite:
- Il nome del cliente e la nazione utilizzando come chiave il campo Cliente della TabVendite e il campo IdCliente della tabella TabAnClienti
- L’Area collegando la TabAnClienti con la TabAree
- Il nome pdt, la Categoria e il Mercato (Mkt) utilizzando come chiave il campo Prodotto della TabVendite e della TabProdotti
Il metodo più veloce è cliccare sul tasto Merge di query posto nella scheda Home dell’interfaccia Recupera e trasforma.
La finestra di dialogo successiva è molto intuitiva e richiede semplicemente di indicare le tabelle da collegare e le chiavi da utilizzare. Nell’area Dati ora appare una colonna in più, denominata appunto TabAnClienti che può essere espansa mediante il tasto  posto a destra dell’intestazione consentendo di selezionare gli elementi di nostro interesse della tabella collegata, nel nostro caso il Nome Cliente e il Paese.
Ripeteremo il procedimento anche per importare l’Area e i campi relativi ai prodotti
Espandendo i campi otterremo la tabella che segue
Ora non ci resta che raggruppare i dati e sommarli attraverso il comando  Nella scheda Home.
Il nostro obiettivo è ottenere una tabella così strutturata
Avremo allora bisogno di raggruppare per Area e Categoria e sommare per importo. Cliccando sul comando Raggruppa per, appare una finestra di dialogo che compileremo come segue:
- Sceglieremo l’opzione Avanzate per poter inserire più raggruppamenti (ce ne servono due)
- Raggrupperemo per Area e Categoria
- Chiameremo la nuova colonna TotFatt (o altro nome a piacere)
- Utilizzeremo l’operatore Somma
- Opereremo la somma sulla colonna Fatturato
È possibile mediante il tasto Aggiungi aggregazione utilizzare contemporaneamente altri operatori e quindi calcolare la media, il conteggio, etc…
Confermando la finestra con in tasto OK si otterrà la seguente area dati. Il Fatturato è stato raggruppato secondo i criteri impartiti ma la tabella è diversa rispetto a quella che ci eravano prefissati. Possiamo innanzi tutto ordinarla per Categoria; a tal fine basterà posizionarsi sul campo Categoria e utilizzare il consueto comando
Se vogliamo portare le categorie in colonna possiamo utilizzare un comando posto nella scheda trasforma: Colonna Pivot.
Il Funzionamento è semplice: è sufficiente selezionare sia la colonna che si intende far diventare intestazione di riga, sia la colonna valori e cliccare sul comando. Confermando la finestra di dialogo successiva si otterrà il risultato finale.
Si noti che nell’area Impostazioni Query sono riportati tutti i passaggi applicati consentendo così di tornare su ogni operazione eseguita, il funzionamento è del tutto simile ad una riga di programma, eliminarla o modificarne il contenuto, si tratta di una caratteristica molto preziosa come vedremo in seguito.
Ad esempio, per ottenere anche le tabelle Area/Categoria o Zona/Categoria, potremmo duplicare la Query che abbiamo appena creato, sarà sufficiente eliminare gli ultimi tre passaggi, inserendo nuovi raggruppamenti e nuove colonne pivot.
Provate da soli e vedrete come è semplice e immediato, ve lo lascio come compito, avete tempo fino al numero di luglio (tanto è un periodo tranquillo questo, vero?) quando sveleremo i segreti di una funzione che molti considerano troppo complicata, quasi un tabù, ma che in realtà è molto più semplice di quanto non si creda, le tabelle PIVOT che se usate con il Recupera e Trasforma, diventano una miscela esplosiva.
Alla prossima!