"""
Quattro articoli Ratio -- 18 settembre 2026

1. 2026-09-18_unioncamere-195-imprese-ai-divario-pmi.docx
2. 2026-09-18_dati-aziendali-ai-gdpr-chatgpt-rischi.docx
3. 2026-09-18_ai-literacy-obbligo-scattato-cosa-documentare.docx
4. 2026-09-18_codice-deontologico-ingegneri-ai-professionisti.docx
"""

from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BASE = "/home/user/amattavelli/Ratio/articoli/"

BLU_SCURO = RGBColor(0x1F, 0x49, 0x7D)
BLU_MEDIO = RGBColor(0x2E, 0x74, 0xB5)
GRIGIO    = RGBColor(0x60, 0x60, 0x60)
GRIGIO_CH = RGBColor(0x80, 0x80, 0x80)
GRIGIO_PI = RGBColor(0xA0, 0xA0, 0xA0)


def new_doc():
    doc = Document()
    s = doc.sections[0]
    s.page_width    = Cm(21)
    s.page_height   = Cm(29.7)
    s.left_margin   = Cm(3)
    s.right_margin  = Cm(3)
    s.top_margin    = Cm(2.5)
    s.bottom_margin = Cm(2.5)
    sn = doc.styles["Normal"]
    sn.font.name = "Calibri"
    sn.font.size = Pt(11)
    return doc


def sep(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_after  = Pt(2)
    p.paragraph_format.space_before = Pt(2)
    pPr  = p._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bot  = OxmlElement("w:bottom")
    bot.set(qn("w:val"),   "single")
    bot.set(qn("w:sz"),    "6")
    bot.set(qn("w:space"), "1")
    bot.set(qn("w:color"), "1F497D")
    pBdr.append(bot)
    pPr.append(pBdr)


def heading(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after  = Pt(6)
    r = p.add_run(text)
    r.font.name  = "Calibri"
    r.font.size  = Pt(12)
    r.font.bold  = True
    r.font.color.rgb = BLU_SCURO


def para(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after  = Pt(8)
    p.paragraph_format.line_spacing = Pt(16)
    r = p.add_run(text)
    r.font.name = "Calibri"
    r.font.size = Pt(11)


def testata(doc, mese_anno, categoria):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("RATIO  •  Approfondimenti per Professionisti e Imprese")
    r.font.name = "Calibri"; r.font.size = Pt(9)
    r.font.color.rgb = BLU_SCURO
    r.font.bold = True; r.font.all_caps = True
    sep(doc)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = p.add_run(f"{mese_anno}  |  {categoria}")
    r.font.name = "Calibri"; r.font.size = Pt(8.5)
    r.font.italic = True; r.font.color.rgb = GRIGIO
    doc.add_paragraph()


def titolo(doc, titolo_testo, occhiello, data_autore):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run(titolo_testo)
    r.font.name = "Calibri"; r.font.size = Pt(24)
    r.font.bold = True; r.font.color.rgb = BLU_SCURO
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_after = Pt(10)
    r = p.add_run(occhiello)
    r.font.name = "Calibri"; r.font.size = Pt(13)
    r.font.italic = True; r.font.color.rgb = BLU_MEDIO
    sep(doc)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_after = Pt(16)
    r = p.add_run(data_autore)
    r.font.name = "Calibri"; r.font.size = Pt(9)
    r.font.color.rgb = GRIGIO_CH


def riferimenti(doc, fonti):
    sep(doc)
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    r = p.add_run("Riferimenti")
    r.font.name = "Calibri"; r.font.size = Pt(9)
    r.font.bold = True; r.font.color.rgb = GRIGIO
    for s in fonti:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(f"• {s}")
        r.font.name = "Calibri"; r.font.size = Pt(8.5)
        r.font.color.rgb = GRIGIO
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(16)
    r = p.add_run(
        "© 2026 Mattavelli Amodeo — Commercialisti Associati  •  "
        "Riproduzione consentita con citazione della fonte"
    )
    r.font.name = "Calibri"; r.font.size = Pt(8)
    r.font.color.rgb = GRIGIO_PI; r.font.italic = True


# ============================================================
# ARTICOLO 1
# Il 19,5% di Unioncamere: il raddoppio che non convince
# ============================================================

doc = new_doc()
testata(doc, "Settembre 2026", "Mercato AI e Adozione nelle Imprese")
titolo(
    doc,
    "Il raddoppio che non convince. Un'impresa su cinque usa l'AI, le altre quattro aspettano.",
    "Il rapporto Unioncamere-Dintec del 17 settembre 2026 certifica che le imprese italiane "
    "che usano l'AI sono passate dal 13,1% al 19,5% in un anno. "
    "Nelle grandi aziende siamo oltre il 50%. Nelle piccole, al 15%. "
    "Il professionista che segue PMI dovrebbe leggere questo dato non come una notizia positiva, "
    "ma come una mappa di dove si concentra il lavoro da fare.",
    "A cura della Redazione Ratio  •  18 settembre 2026"
)

para(doc,
    "Se chiedete a un titolare di PMI italiana se usa l'intelligenza artificiale in azienda, "
    "la risposta più frequente è no. Se poi gli chiedete se usa ChatGPT, Copilot o strumenti "
    "simili per preparare offerte, rispondere a email, riassumere contratti o fare ricerche, "
    "la risposta spesso cambia. Il dato Unioncamere-Dintec pubblicato il 17 settembre 2026, "
    "che certifica il 19,5% di imprese italiane che usano l'AI, va letto con questa premessa: "
    "misura le imprese che hanno dichiarato un uso strutturato di tecnologie AI in almeno uno "
    "dei loro processi, attraverso il questionario Selfi4.0 somministrato dai Punti Impresa "
    "Digitale delle Camere di commercio, su un campione di oltre 20.000 rilevazioni effettuate "
    "negli ultimi due anni. Non misura l'uso informale, individuale, non dichiarato, che nelle "
    "PMI italiane è probabilmente molto più diffuso. Il 19,5% è quindi il pavimento, "
    "non il soffitto. La crescita però è reale: dal 13,1% del 2024 al 19,5% del 2025 "
    "è quasi un raddoppio in dodici mesi, e la direzione è inequivocabile."
)

para(doc,
    "La scomposizione del dato è quella che dovrebbe preoccupare chiunque lavori con le "
    "piccole imprese. Nelle grandi aziende, quelle con più di 250 dipendenti, "
    "la quota di adozione supera il 50%: più di una su due ha già integrato l'AI in qualche "
    "forma strutturata nei propri processi. Nelle imprese con meno di 50 dipendenti, "
    "la quota scende al 15%. Questo divario non è una curiosità statistica: "
    "è un divario competitivo che si allarga ogni anno. "
    "La grande azienda che ottimizza la gestione documentale con l'AI nel 2025 riduce i costi, "
    "accelera i cicli, risponde meglio ai clienti. La PMI che aspetta accumula uno svantaggio "
    "che con il tempo diventa strutturale, non recuperabile con un singolo investimento futuro. "
    "Il mercato non aspetta chi si prepara a distanza: si sposta mentre ci si prepara."
)

heading(doc, "Il freno che nessuno vuole affrontare davvero")

para(doc,
    "Il dato più rilevante del rapporto Unioncamere non è la percentuale di chi usa l'AI: "
    "è la percentuale di chi non la usa pur dichiarando di volerlo fare. "
    "Il 58,6% delle PMI italiane indica la mancanza di competenze digitali come primo ostacolo "
    "all'adozione dell'intelligenza artificiale. Solo il 7% ha avviato percorsi formativi "
    "strutturati sul tema. Questo squilibrio ha una logica solo apparente: "
    "le PMI percepiscono il problema come tecnologico, non come umano. "
    "Comprano software, sottoscrivono abbonamenti, implementano strumenti nuovi. "
    "Poi scoprono che i dipendenti non sanno usarli in modo produttivo, "
    "che i processi non sono stati ridisegnati per accoglierli, "
    "che i risultati promessi non arrivano. "
    "Il software non è il problema. "
    "La preparazione delle persone che lo usano è il problema. "
    "La tecnologia, nel 2026, costa poco. "
    "La competenza per usarla bene è la risorsa scarsa."
)

heading(doc, "Cosa stanno adottando le imprese")

para(doc,
    "La tecnologia AI più diffusa nelle imprese italiane con almeno dieci addetti è il text mining, "
    "adottato dall'11,6% del totale: la capacità di estrarre informazioni strutturate "
    "da testi non strutturati, applicata a contratti, email, documenti, feedback. "
    "Seguono i sistemi di recommendation, i chatbot e le interfacce conversazionali, "
    "i sistemi di riconoscimento automatico di immagini. "
    "Questi numeri descrivono un'adozione ancora concentrata sui processi più standardizzabili: "
    "quelli con dati abbondanti, formati prevedibili, operazioni ripetitive ad alto volume. "
    "L'AI generativa, quella che produce testi, analisi e codice, "
    "è sottorappresentata nelle rilevazioni Unioncamere perché viene usata spesso in modo "
    "informale, individuale, non integrato nei processi ufficiali dell'impresa. "
    "La sua diffusione reale è quasi certamente superiore a quanto le statistiche catturano, "
    "e la distanza tra uso dichiarato e uso effettivo è probabilmente l'area "
    "dove le imprese corrono i rischi maggiori senza saperlo."
)

para(doc,
    "Il professionista che segue una PMI italiana nel 2026 si trova di fronte a una domanda "
    "che un anno fa non aveva ancora una risposta operativa chiara. "
    "La domanda non è 'se usare l'AI', perché quella risposta è già data dal mercato. "
    "La domanda è 'perché questa impresa specifica non la usa ancora in modo strutturato, "
    "e cosa la tiene ferma'. "
    "La risposta quasi mai è il costo degli strumenti, che nel 2026 sono accessibili "
    "a qualunque dimensione di impresa. "
    "La risposta è quasi sempre la mancanza di qualcuno che aiuti l'imprenditore "
    "a capire da dove si inizia, su quale processo, con quale obiettivo misurabile. "
    "Il commercialista o il consulente che conosce i numeri dell'azienda, "
    "i suoi processi, i suoi punti di inefficienza, "
    "è nella posizione migliore per dare questa risposta. "
    "Il 19,5% delle imprese ci sta arrivando da sola. "
    "Il restante 80,5% aspetta ancora qualcuno che le aiuti a entrare dalla porta giusta."
)

riferimenti(doc, [
    "Unioncamere-Dintec — 'Il 19,5% delle imprese italiane usa l'Intelligenza artificiale' (17 settembre 2026)",
    "ANSA — 'Unioncamere-Dintec, 19,5% imprese italiane usa l'Intelligenza artificiale' (17 settembre 2026)",
    "Teleborsa — 'Intelligenza artificiale al 19,5% nelle imprese, ma deficit competenze agisce da freno' (17 settembre 2026)",
    "BusinessPeople — 'Intelligenza artificiale: il 19,5% delle imprese italiane usa l'AI' (2026)",
    "Edunews24 — 'Adozione IA in Italia al 19,5%, ma le PMI restano ferme al 15%' (2026)",
    "Unioncamere — Selfi4.0: strumento di rilevazione della maturità digitale delle imprese",
    "Osservatorio AI del Politecnico di Milano — Rapporto mercato AI Italia 2025-2026",
])
doc.save(BASE + "2026-09-18_unioncamere-195-imprese-ai-divario-pmi.docx")
print("Salvato: articolo 1")


# ============================================================
# ARTICOLO 2
# I dati aziendali nell'AI: GDPR e rischi concreti
# ============================================================

doc = new_doc()
testata(doc, "Settembre 2026", "Privacy, GDPR e Strumenti AI")
titolo(
    doc,
    "Il documento che hai caricato su ChatGPT. Dove va, chi lo legge, cosa dice la legge.",
    "Ogni prompt è un trasferimento di dati. "
    "Quando un professionista o un dipendente carica una fattura, un contratto "
    "o una busta paga su uno strumento AI consumer, "
    "non sta solo usando uno strumento: sta eseguendo un trattamento di dati personali. "
    "Le conseguenze sul piano GDPR sono concrete, spesso ignorate "
    "e difficili da sanare dopo il fatto.",
    "A cura della Redazione Ratio  •  18 settembre 2026"
)

para(doc,
    "Uno studio professionale riceve un contratto di fornitura da revisionare per un cliente. "
    "Il collaboratore apre ChatGPT, copia il testo nel campo del prompt e chiede "
    "un'analisi delle clausole più critiche. "
    "L'operazione dura trenta secondi e produce un output utile. "
    "Ciò che non si vede dura molto di più: "
    "il testo del contratto, con i dati del cliente, della controparte, "
    "i termini economici, le condizioni riservate, "
    "è stato trasmesso ai server di OpenAI negli Stati Uniti "
    "senza che esista un contratto di trattamento dati ai sensi dell'articolo 28 del GDPR, "
    "senza che il cliente sia stato informato, "
    "e su un piano di abbonamento che per impostazione predefinita "
    "usa gli input degli utenti per addestrare i modelli futuri. "
    "Questo non è un caso di scuola. "
    "Avviene ogni giorno in studi professionali e uffici aziendali di tutta Italia."
)

para(doc,
    "Il nodo giuridico è netto. "
    "La lavorazione di informazioni tramite prompt, "
    "quando queste informazioni contengono dati di persone fisiche identificabili, "
    "costituisce un trattamento di dati personali ai sensi dell'articolo 4 del GDPR. "
    "Il titolare del trattamento è l'impresa o lo studio che usa lo strumento, "
    "non il fornitore della piattaforma AI. "
    "Se il trattamento coinvolge un fornitore esterno che elabora dati "
    "per conto del titolare, si applica l'obbligo di stipulare "
    "un Data Processing Agreement conforme all'articolo 28, "
    "che disciplini finalità, modalità, misure di sicurezza, "
    "trasferimenti extra-UE e obblighi del responsabile. "
    "La maggior parte dei piani consumer dei principali strumenti AI "
    "— ChatGPT Plus, Microsoft Copilot personale, Claude.ai standard — "
    "non fornisce questi accordi contrattuali per impostazione predefinita."
)

heading(doc, "La differenza tra piano consumer e piano enterprise")

para(doc,
    "Sulla stessa piattaforma possono coesistere due prodotti radicalmente diversi "
    "dal punto di vista della conformità GDPR. "
    "ChatGPT Plus, il piano da 20 euro al mese, "
    "usa gli input per il miglioramento del modello salvo opt-out esplicito, "
    "non prevede un DPA e trasmette i dati a server statunitensi "
    "senza garantie contrattuali specifiche per i trasferimenti extra-UE. "
    "ChatGPT Enterprise e ChatGPT Team, i piani aziendali, "
    "non usano gli input per addestrare i modelli, "
    "includono un Data Processing Agreement conforme al GDPR "
    "con clausole contrattuali standard per i trasferimenti extra-UE "
    "e offrono controlli aggiuntivi sulla residenza dei dati. "
    "La differenza di prezzo tra i due piani è nell'ordine di 3-5 volte. "
    "La differenza di esposizione legale è molto maggiore. "
    "Uno studio professionale che usa ChatGPT Plus per elaborare dati dei clienti "
    "non sta risparmiando sui costi IT: "
    "sta trasferendo sul cliente un rischio che il cliente non conosce."
)

heading(doc, "Il problema specifico dei professionisti")

para(doc,
    "Per gli studi professionali, la questione assume una dimensione aggiuntiva. "
    "La Legge 23 settembre 2025 n. 132 all'articolo 13 "
    "prevede che il professionista che usa sistemi AI nell'erogazione della prestazione "
    "debba comunicarlo al cliente con linguaggio chiaro. "
    "Ma questa comunicazione, che riguarda l'uso dello strumento, "
    "non esaurisce l'obbligo sulla protezione dei dati. "
    "La comunicazione dice 'ho usato l'AI'. "
    "Il GDPR richiede che il cliente sappia anche 'quali dati sono stati trattati, "
    "da chi, con quali garanzie'. "
    "Un'informativa generica sull'uso dell'AI non sostituisce "
    "un'adeguata disclosure sul trattamento dei dati personali del cliente "
    "tramite strumenti di terze parti. "
    "Chi ha preparato la clausola contrattuale tipo per l'informativa AI "
    "pubblicata dal CNDCEC ha fatto un passo nella direzione giusta, "
    "ma il pezzo sulla protezione dei dati rimane separato "
    "e richiede un aggiornamento dell'informativa privacy dello studio."
)

para(doc,
    "Il Garante per la Protezione dei Dati Personali ha già segnalato "
    "il tema dell'AI generativa e del trattamento dei dati negli ultimi anni, "
    "con ammonimenti a provider e utenti. "
    "Nel 2026, con i poteri di vigilanza pienamente operativi "
    "e la combinazione AI Act più GDPR come quadro di riferimento, "
    "il rischio per chi usa strumenti AI consumer su dati di clienti "
    "è concreto e crescente. "
    "Il passaggio pratico non è complesso: "
    "identificare quali strumenti AI si usano in studio, "
    "verificare se esistono DPA con i fornitori, "
    "e dove non esistono valutare se passare ai piani aziendali "
    "o se smettere di usare quelli strumenti per i dati dei clienti. "
    "Non è una questione di tecnologia. "
    "La stessa piattaforma, lo stesso modello, un piano diverso: "
    "il problema si risolve con una decisione amministrativa, "
    "non con un investimento tecnologico."
)

riferimenti(doc, [
    "Garante per la Protezione dei Dati Personali — ammonimento su AI generativa (2023-2026)",
    "Regolamento UE 2016/679 (GDPR), articoli 4, 13, 28, 44-49",
    "Legge 23 settembre 2025, n. 132, articolo 13 — uso AI nelle professioni intellettuali",
    "AI4Business — 'Privacy e AI: come proteggere i dati e la proprietà intellettuale in azienda' (2026)",
    "TECH.TEAM Lab — 'IA generativa in azienda: cosa nessun fornitore ti dice sul GDPR' (2026)",
    "Aipolicy.it — 'Deepfake AI generativa: rischi GDPR e AI Act per PMI italiane' (maggio 2026)",
    "OpenAI — Enterprise Privacy Policy e Data Processing Agreement (aggiornamento 2026)",
    "CNDCEC — Clausola contrattuale tipo per l'informativa AI ai clienti dello studio (2026)",
])
doc.save(BASE + "2026-09-18_dati-aziendali-ai-gdpr-chatgpt-rischi.docx")
print("Salvato: articolo 2")


# ============================================================
# ARTICOLO 3
# AI literacy: l'obbligo è scattato, come si documenta
# ============================================================

doc = new_doc()
testata(doc, "Settembre 2026", "Compliance AI Act e Obblighi Formativi")
titolo(
    doc,
    "L'obbligo di formazione AI è scattato il 2 agosto. Cosa conta come prova, cosa no.",
    "L'articolo 4 del Regolamento AI Act impone alle organizzazioni di adottare misure "
    "per lo sviluppo dell'AI literacy del personale. "
    "Le autorità di vigilanza italiane hanno avviato le attività di sorveglianza dal 3 agosto. "
    "Solo il 7% delle PMI ha avviato percorsi strutturati. "
    "Il problema, per molti, non è fare la formazione: è dimostrare di averla fatta.",
    "A cura della Redazione Ratio  •  18 settembre 2026"
)

para(doc,
    "Un ispettore dell'Agenzia per la Cybersicurezza Nazionale chiede all'azienda "
    "di mostrare la documentazione relativa alla formazione AI del personale, "
    "come previsto dall'articolo 4 del Regolamento UE 2024/1689. "
    "L'azienda usa strumenti AI da mesi: il titolare ha comprato un abbonamento Copilot, "
    "ha fatto una riunione con i dipendenti per spiegarne l'uso, "
    "ha risposto alle loro domande. "
    "Niente è stato trascritto, registrato, attestato. "
    "Nessuno ha firmato un foglio presenze. "
    "Il materiale della riunione non esiste come documento. "
    "Questa è esattamente la situazione in cui si trovano la maggior parte delle PMI italiane "
    "nel settembre 2026: l'AI è in uso, la formazione è avvenuta in qualche forma, "
    "ma la documentazione che serve a dimostrarlo non c'è."
)

para(doc,
    "L'obbligo di AI literacy introdotto dall'articolo 4 dell'AI Act "
    "è in vigore dal 2 agosto 2026. "
    "Non è un obbligo astratto: le autorità nazionali di vigilanza italiane, "
    "ACN e AgID, hanno avviato le attività di sorveglianza dal 3 agosto. "
    "Il testo dell'articolo 4, come modificato dal Regolamento Digital Omnibus "
    "(UE 2026/1744), richiede che i fornitori e i deployer di sistemi AI "
    "'adottino misure a supporto dello sviluppo della competenza sull'AI "
    "del proprio personale e delle altre persone che operano per loro conto'. "
    "La modifica introdotta dal Digital Omnibus ha chiarito un punto cruciale: "
    "l'obbligo non impone di garantire un livello specifico di AI literacy "
    "per ogni singolo dipendente. "
    "Impone di adottare misure — e di poterle documentare."
)

heading(doc, "Cosa conta come documentazione valida")

para(doc,
    "La differenza tra una formazione AI che soddisfa l'obbligo "
    "e una che non lo soddisfa non sta nel contenuto: "
    "sta nella traccia che lascia. "
    "Sono accettabili come documentazione i corsi e-learning con tracciamento "
    "della completamento, con attestato nominativo e data, "
    "anche se erogati su piattaforme esterne all'impresa. "
    "Sono accettabili i workshop interni con materiali distribuiti, "
    "foglio presenze firmato, verbale sintetico con data e argomenti trattati. "
    "Sono accettabili i percorsi formativi erogati da enti di formazione accreditati, "
    "con emissione di certificato e relativa conservazione nel fascicolo del dipendente. "
    "Non sono accettabili le riunioni di aggiornamento senza documentazione, "
    "le policy generali sull'uso degli strumenti IT che nominano l'AI en passant, "
    "i messaggi email o le comunicazioni Slack in cui si parla di AI senza attestazione formale. "
    "La logica è la stessa che si applica alla formazione sulla sicurezza sul lavoro: "
    "se non è documentata, per l'autorità di vigilanza non è avvenuta."
)

heading(doc, "Il gap che i dati Unioncamere confermano")

para(doc,
    "Il rapporto Unioncamere-Dintec del 17 settembre 2026 "
    "fornisce una misura indiretta della distanza che separa le imprese italiane "
    "dalla compliance AI literacy. "
    "Il 58,6% delle PMI dichiara la mancanza di competenze digitali "
    "come primo ostacolo all'adozione dell'AI. "
    "Solo il 7% ha avviato percorsi formativi strutturati. "
    "L'obbligo di AI literacy è già in vigore. "
    "Questo significa che, sulla base dei soli dati disponibili, "
    "almeno nove PMI su dieci che usano sistemi AI nei loro processi "
    "sono esposte a una contestazione in caso di ispezione, "
    "non perché non abbiano fatto formazione, "
    "ma perché non possono documentarla in modo adeguato. "
    "La sanzione prevista dall'AI Act per le violazioni degli obblighi "
    "di cui all'articolo 4 rientra nella categoria generale "
    "fino al 3% del fatturato mondiale o 15 milioni di euro. "
    "Per una PMI con 2 milioni di fatturato, "
    "il 3% sono 60.000 euro di esposizione teorica "
    "per un problema che si risolve con un pomeriggio di formazione documentata."
)

para(doc,
    "Il professionista che aiuta un cliente a strutturare la documentazione AI literacy "
    "non sta facendo consulenza tecnologica: "
    "sta riducendo un rischio di compliance concreto e misurabile. "
    "Il percorso non deve essere lungo o costoso: "
    "tre ore di formazione strutturata con un fornitore accreditato, "
    "un attestato nominativo per ogni dipendente che usa strumenti AI, "
    "una procedura interna che descrive quali strumenti sono in uso e con quali regole, "
    "aggiornata almeno una volta all'anno. "
    "Chi ha già fatto la formazione sulla sicurezza sul lavoro "
    "sa esattamente come funziona questo processo. "
    "La struttura è la stessa. "
    "La novità è solo l'argomento."
)

riferimenti(doc, [
    "Regolamento UE 2024/1689 (AI Act), articolo 4 — AI literacy",
    "Regolamento UE 2026/1744 (Digital Omnibus on AI) — modifica articolo 4",
    "Legge 23 settembre 2025, n. 132 — designazione ACN e AgID come autorità di vigilanza",
    "Randstad — 'AI literacy e obbligo di formazione nelle aziende: come muoversi?' (2026)",
    "Agenda Digitale — 'Formazione AI obbligatoria per le imprese: guida completa' (2026)",
    "Eclogaitalia — 'Formazione IA obbligatoria: cosa impone l'AI Act e come adeguarsi' (2026)",
    "Unioncamere-Dintec — Rapporto adozione AI nelle imprese italiane (settembre 2026)",
    "Il Sole 24 Ore — 'AI literacy, in vigore i nuovi obblighi formativi introdotti dall'AI Act' (2026)",
])
doc.save(BASE + "2026-09-18_ai-literacy-obbligo-scattato-cosa-documentare.docx")
print("Salvato: articolo 3")


# ============================================================
# ARTICOLO 4
# Il codice deontologico degli Ingegneri e l'AI: cosa cambia per gli altri ordini
# ============================================================

doc = new_doc()
testata(doc, "Settembre 2026", "Professioni e Regolamentazione AI")
titolo(
    doc,
    "Gli Ingegneri hanno già riscritto le regole sull'AI. Gli altri ordini hanno sei mesi.",
    "Con delibera del 23 giugno 2026, il Consiglio Nazionale degli Ingegneri "
    "ha aggiornato il Codice deontologico per recepire la Legge 132/2025 sull'AI. "
    "La legge impone a tutti gli ordini professionali di fare lo stesso entro sei mesi. "
    "Per commercialisti, avvocati e consulenti del lavoro la scadenza si avvicina. "
    "Le nuove regole ridefiniscono cosa significa 'responsabilità professionale' "
    "quando parte del lavoro la fa un sistema AI.",
    "A cura della Redazione Ratio  •  18 settembre 2026"
)

para(doc,
    "Un ingegnere strutturale usa un software AI per verificare i calcoli "
    "di un progetto di ristrutturazione. "
    "Il software produce un output che l'ingegnere controlla, "
    "integra con le proprie valutazioni e inserisce nella relazione tecnica finale. "
    "Il cliente, in fase di consegna del progetto, chiede: "
    "'questi calcoli li ha fatti lei o il software?' "
    "Fino al 22 giugno 2026, la domanda non aveva una risposta codificata. "
    "Dal 23 giugno, il Codice deontologico degli Ingegneri italiani "
    "aggiornato con delibera del Consiglio Nazionale risponde in modo preciso: "
    "li ha fatti l'ingegnere, con il supporto di strumenti AI, "
    "e la responsabilità è esclusivamente sua. "
    "La dichiarazione di uso dell'AI nella prestazione non trasferisce responsabilità: "
    "la formalizza in capo al professionista, con obblighi di supervisione espliciti."
)

para(doc,
    "L'aggiornamento del codice deontologico degli Ingegneri non è una scelta discrezionale "
    "dell'ordine: è l'adempimento di un obbligo introdotto dall'articolo 13 "
    "della Legge 23 settembre 2025 n. 132. "
    "Questa norma, dedicata espressamente alle 'Disposizioni in materia di professioni intellettuali', "
    "stabilisce che i sistemi AI sono consentiti nell'esercizio delle professioni "
    "solo come strumenti di supporto, "
    "che il professionista deve comunicare al cliente l'utilizzo di sistemi AI "
    "con linguaggio chiaro e comprensibile, "
    "e che la responsabilità professionale per le prestazioni rese "
    "con il supporto di AI rimane interamente in capo al professionista. "
    "La legge impone poi agli ordini e collegi professionali "
    "di adeguare i propri regolamenti entro sei mesi dall'entrata in vigore "
    "dei decreti attuativi, approvati il 4 agosto 2026. "
    "La scadenza per gli adeguamenti è quindi intorno a febbraio 2027, "
    "ma il Consiglio Nazionale degli Ingegneri ha anticipato i tempi di oltre sei mesi."
)

heading(doc, "Tre livelli di formazione che la legge richiede agli ordini")

para(doc,
    "L'articolo 13 della Legge 132/2025 non si limita a imporre aggiornamenti deontologici: "
    "struttura i percorsi formativi che gli ordini devono erogare su tre livelli distinti. "
    "Il primo è il livello tecnico: comprensione del funzionamento dei sistemi AI "
    "usati nella professione specifica, delle loro capacità e dei loro limiti, "
    "con particolare attenzione ai rischi di errore non rilevabile senza supervisione umana. "
    "Il secondo è il livello giuridico: conoscenza del quadro normativo applicabile, "
    "dall'AI Act alla Legge 132, agli obblighi di disclosure al cliente "
    "e alle implicazioni sulla responsabilità professionale. "
    "Il terzo è il livello deontologico: comprensione di come l'uso dell'AI "
    "si integra con i principi di autonomia professionale, indipendenza di giudizio "
    "e dovere di cura verso il cliente. "
    "Questi tre livelli si intrecciano: "
    "un professionista che conosce la legge ma non capisce i limiti tecnici dello strumento "
    "non è in grado di supervisionarne l'output in modo adeguato."
)

heading(doc, "Cosa cambia concretamente per i commercialisti")

para(doc,
    "Per il Consiglio Nazionale dei Dottori Commercialisti e degli Esperti Contabili, "
    "l'adeguamento del Codice deontologico è un processo in corso. "
    "Il CNDCEC ha già pubblicato la clausola contrattuale tipo per l'informativa AI ai clienti, "
    "ma l'aggiornamento del codice deontologico vero e proprio "
    "— quello che stabilisce obblighi, divieti e responsabilità per il singolo iscritto — "
    "deve ancora essere formalizzato. "
    "La scadenza normativa a febbraio 2027 lascia tempo, "
    "ma i comportamenti che il codice codificherà sono già obbligatori per legge: "
    "la disclosure dell'uso dell'AI al cliente, "
    "il mantenimento della supervisione professionale sull'output dei sistemi AI, "
    "la documentazione dei controlli effettuati. "
    "Il commercialista che aspetta che il codice deontologico venga aggiornato "
    "prima di adeguare i propri comportamenti "
    "sta misurando la propria responsabilità con lo strumento sbagliato: "
    "la legge è già in vigore, l'obbligo è già operativo, "
    "il codice deontologico non farà che recepire ciò che la legge già prevede."
)

para(doc,
    "La norma più rilevante per il futuro delle professioni intellettuali italiane "
    "nell'articolo 13 della Legge 132/2025 è quella sui compensi: "
    "entro dodici mesi dall'entrata in vigore dei decreti attuativi, "
    "i sistemi tariffari professionali devono essere aggiornati "
    "per tener conto della classificazione di rischio del sistema AI impiegato. "
    "La logica è che l'automazione non deve svalutare il lavoro intellettuale: "
    "se un sistema AI a rischio elevato assiste il professionista in una valutazione critica, "
    "il compenso deve riflettere la responsabilità aggiuntiva di supervisione, "
    "non ridursi perché 'lo ha fatto il software'. "
    "Questa è la trasformazione più profonda che la legge introduce nelle professioni: "
    "non la sostituzione del professionista, ma la ridefinizione del valore "
    "di ciò che il professionista fa quando l'AI lo affianca."
)

riferimenti(doc, [
    "Consiglio Nazionale degli Ingegneri — delibera di aggiornamento Codice deontologico (23 giugno 2026)",
    "Legge 23 settembre 2025, n. 132, articolo 13 — Disposizioni in materia di professioni intellettuali",
    "LavoriPubblici — 'Codice deontologico Ingegneri: nuove regole per l'IA' (2026)",
    "Ordine degli Ingegneri della Provincia di Palermo — 'Nuovo Codice deontologico adottato' (14 settembre 2026)",
    "Ordine dei Giornalisti — 'Riforma professioni su Deontologia e AI: il Consiglio ha anticipato i tempi' (2026)",
    "Ingenio-web — 'Riforma professioni 2026: formazione, deontologia, disciplina e compensi' (2026)",
    "CNDCEC — Clausola contrattuale tipo per l'informativa AI ai clienti dello studio (2026)",
    "Dirittoaldigitale.com — 'Decreti attuativi AI Act Italia 2026: cosa cambia' (2026)",
])
doc.save(BASE + "2026-09-18_codice-deontologico-ingegneri-ai-professionisti.docx")
print("Salvato: articolo 4")

print("\nTutti e 4 gli articoli generati in:", BASE)
