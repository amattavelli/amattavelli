# =============================================================================
# Copia-Corsi-Nel-Repo.ps1
# Copia i PPTX da OneDrive/Corsi nelle directory giuste del repo git
# =============================================================================
# USO:
#   1. Clona il repo: git clone https://github.com/amattavelli/amattavelli.git
#      e fai checkout del branch corretto
#   2. Modifica le due variabili $SourceRoot e $DestRoot qui sotto
#   3. Prima esecuzione: lascia $DryRun = $true  → solo anteprima, nessuna copia
#   4. Se l'anteprima è ok: metti $DryRun = $false e riesegui
# =============================================================================

$SourceRoot = "C:\Users\AlessandroMattavelli\OneDrive - MATTAVELLI AMODEO COMMERCIALISTI ASSOCIATI\Corsi"
$DestRoot   = "C:\Users\AlessandroMattavelli\OneDrive - MATTAVELLI AMODEO COMMERCIALISTI ASSOCIATI\amattavelli\Formazione"
$DryRun     = $true   # <-- metti $false per copiare davvero

# =============================================================================
# MAPPING: parole chiave nel nome cartella → subdirectory di destinazione
# Le regole vengono valutate IN ORDINE: vince la prima che fa match
# =============================================================================
$Mapping = @(

    # ── EXCEL / BI / AI ──────────────────────────────────────────────────────

    @{ Keys = @("CHAT GPT","CHATGPT","COPILOT","RATIO AI","RATIO COPILOT","RATIO HR",
                "MASTER AI","CORSO AI","DIGITAL","COMPETENZ.*AI","COME OTTENERE",
                "METODO CIAO","COMMERCIALISTA 4.0","AI PER I DIPENDENTI",
                "DIPENDENTI AI","AI E PRATICHE") ;  Dest = "Excel-BI-AI\AI-Strumenti" },

    @{ Keys = @("AI PER.*FINANZ","FINANZ.*AI","AI PER ANALISI","ANALISI.*AI",
                "BANKING AI","INTELLIGENZA ARTIFICIALE","RISORSA UMANA.*AI",
                "CREDITO.*AI","AI.*COMMERCIALI","BP AI","CESI.*AI","GIUFFRÈ.*AI",
                "GIUFFRE.*AI","IA E BUSINESS","IA.*CONTROLLO","AI.*CDG",
                "CT BUSINESS PLAN.*AI","API MANTOVA AI","ALI AI") ; Dest = "Excel-BI-AI\AI-Finance" },

    @{ Keys = @("POWER BI","POWERBI","PBI","BUSINESS INTELLIGENCE","ROVEDA BI",
                "PERFORMANCE MANAGER","INFINANCE") ;                 Dest = "Excel-BI-AI\Power-BI" },

    @{ Keys = @("MI CHIAMO EXCEL","EXCEL.*RISOLVO","EXCEL ESTREMO","EXCEL.*IA",
                "UTILIZ.*EXCEL","EXCEL.*AVANZ","POWER QUERY","DAX") ; Dest = "Excel-BI-AI\Excel-Avanzato" },

    @{ Keys = @("EXCEL DA 0","EXCEL.*PRINCIPIANTE","EXCEL.*ESPERTO",
                "CORSO EXCEL","ESINEXCEL","CORSOEXCEL","EXCEL.*DATI",
                "EXCEL.*IMPRES","EVENTO.*EXCEL","API.*EXCEL") ;       Dest = "Excel-BI-AI\Excel-Base" },

    # ── CONTROLLO DI GESTIONE ─────────────────────────────────────────────────

    @{ Keys = @("BUDGET","SCOSTAMENT","ODCEC ANALISI SCOSTAMENTI",
                "DRC -BUDGET","DRC - SCOSTAMENTI","VERIFICA REDDITIVIT") ; Dest = "Controllo-di-Gestione\Budget" },

    @{ Keys = @("BALANCED","BALANCE SCORECARD","BSC","SCORECARD",
                "LIUC.*BSC","LIUC CFO") ;                              Dest = "Controllo-di-Gestione\Balanced-Scorecard" },

    @{ Keys = @("BUSINESS PLAN","BUSINESS IDEA","BP.*AQUILA","BP.*HOLDING",
                "BPLAN","ODCEC.*ATTEND","IL SOLE 24.*BP","BUSINESS PLAN.*ASSILEA",
                "ILLIMITY","DALLA.*IDEA","CT.*BUSINESS PLAN","CESI.*BUSINESS PLAN",
                "LE INFO.*BPLAN","MASTER.*LUISS","SIMULAZIONE PIANO",
                "PIANO.*SOSTENIB") ;                                   Dest = "Controllo-di-Gestione\Business-Plan" },

    @{ Keys = @("RENDICONTO","TESORERIA","CASH FLOW","DSCR","PIANO FIN",
                "PIANO ECONOMICO FINANZIARIO","IL PIANO FINANZIARIO",
                "DAL BILANCIO AL RENDICONTO","CORSO DI TESORERIA",
                "DRC.*RENDICONTO","BP HOLDING RENDICONTO") ;           Dest = "Controllo-di-Gestione\Rendiconto-Tesoreria" },

    @{ Keys = @("CONTABILIT.*ANALITICA","CENTRI.*COSTO","COSTO.*CENTRI",
                "COANA","ABC.*COST","DRC.*ESERCITAZIONI","ALI.*CONTROLLO") ; Dest = "Controllo-di-Gestione\Contabilita-Analitica" },

    @{ Keys = @("CONTROLLO.*ECONOMICO","ECONOMICO.*FINANZIARIO",
                "CONTROLLO DI GESTIONE","CONTROLLO.*GESTIONE",
                "CONTROLL.*AZIENDA","ADEGUATO ASSETTO","ANCE.*CONTROLLO",
                "ORDINE.*CONTROLLO","RISTORAZIONE.*CONTROLLO",
                "API MANTOVA.*CONTROLLO","PRICING","GESTIONE.*IMPRESA",
                "PIANIFICAZIONE.*AZIENDALE") ;                         Dest = "Controllo-di-Gestione\Controllo-Economico" },

    # ── BANCHE / RATING / LEASING ─────────────────────────────────────────────

    @{ Keys = @("CRISI","RISANAMENTO","OCC ","OCC$","COMPOSIZIONE NEGOZIATA",
                "COMP.*NEGOZI","CURATORI","ALLERTA","CODICE.*CRISI",
                "ATTESTAZ","AIRCES","ORDINE AVVOCATI","STAV",
                "BUSINESS INTERNATIONAL.*CRISI") ;                     Dest = "Banche-Rating-Advisory\Crisi-e-Risanamento" },

    @{ Keys = @("LEASING","ASSILEA","MATEMATICA FINANZ","PRINCIPI.*LEASING",
                "FONDAMENTI.*LEASING","SG LEASING","ANALISI.*LEASING") ; Dest = "Banche-Rating-Advisory\Leasing" },

    @{ Keys = @("CENTRALE RISCHI","CR FIRENZE","CR$","^CR ") ;         Dest = "Banche-Rating-Advisory\Centrale-Rischi" },

    @{ Keys = @("RISCHIO DEFAULT","STRUMENTI.*PREVENI","PREVENI.*DEFAULT",
                "SCORING","ALTMAN","ALLERTA.*DEFAULT") ;               Dest = "Banche-Rating-Advisory\Rischio-Default" },

    @{ Keys = @("RATING","MERITO CREDITIZIO","BANCA.*IMPRESA","IMPRESA.*BANCA",
                "MCC ","MCC$","COFACE","HYPO","NOKIA","FINANZA.*NON FINANCE",
                "NITREX","DRC.*PIANO DI RISANAMENTO","INTERVENTO.*ATTESTAZ",
                "FINANZA.*IMPRESA","FINANCE","ILLIMITY","CREDITNEWS","SAF") ; Dest = "Banche-Rating-Advisory\Rating-Advisory" },

    # ── CONTABILITÀ ───────────────────────────────────────────────────────────

    @{ Keys = @("BILANCI IRREGOLARI","INDAGINE.*BILANCIO","BILANCIO.*INDAGINE",
                "BILANCIO.*RAGGI","BILANCIO.*SOSPETT","ASSILEA.*BILANCIO.*IRREGOL",
                "DRC.*INDAGINE") ;                                     Dest = "Contabilita\Bilanci-Irregolari" },

    @{ Keys = @("ANALISI.*BILANCIO","BILANCIO.*ANALISI","INDICI.*BILANCIO",
                "BILANCIO.*INDICI","MASTER BILANCIO","ODCEC.*INDICI",
                "ASSILEA.*MERITO","DRC.*ANALISI DI BILANCIO",
                "BP HOLDING.*ANALISI","ASSILEA.*BILANCIO") ;           Dest = "Contabilita\Analisi-di-Bilancio" },

    @{ Keys = @("MAGAZZINO") ;                                         Dest = "Contabilita\Contabilita-Impresa" },

    @{ Keys = @("BILANCIO","DAL BILANCIO","DALLA CONTABILITA",
                "COGE.*BILANCIO","CORSO COGE","COGECOMPTECH",
                "LEGGERE.*CAPIRE","COSTRUZIONE.*BILANCIO") ;           Dest = "Contabilita\Bilancio-Esercizio" },

    @{ Keys = @("CONTABILITA","COGE","PARTITA DOPPIA","SCRITTURE") ;   Dest = "Contabilita\Contabilita-Impresa" },

    # ── GESTIONE FISCALE ──────────────────────────────────────────────────────

    @{ Keys = @("IVA","TRIANGOLAZ","OPERAZIONI.*ESTERO") ;             Dest = "Gestione-Fiscale\IVA" },

    @{ Keys = @("ROTTAMAZIONE","ACCERTAMENTO","REDDITOMETRO",
                "DAL BILANCIO.*DICHIARAZ","DICHIARAZIONE.*REDDITI",
                "UTILE.*BILANCIO.*IMPONIBILE","ASSEGNAZIONE") ;        Dest = "Gestione-Fiscale\Accertamento" },

    @{ Keys = @("LEGGE.*BILANCIO","MANOVRA","FINANZIARIA 20",
                "FDCEC","ODCEC.*LECCO","CONVEGNO.*LEGGE") ;            Dest = "Gestione-Fiscale\Legge-Bilancio" }
)

# Cartelle da ignorare (meta-cartelle, non contengono corsi veri)
$Skip = @("CATALOGO CORSI","Programmi","Verbali corsi vari","Corsi","Praticanti","ANCDL VDbis")

# =============================================================================
# ESECUZIONE
# =============================================================================
$unmapped  = @()
$copied    = 0
$skipped   = 0

Write-Host "`n$(if ($DryRun) {'[DRY RUN - nessuna copia]'} else {'[ESECUZIONE REALE]'})" -ForegroundColor Cyan
Write-Host "Source : $SourceRoot"
Write-Host "Dest   : $DestRoot`n"

$sourceFolders = Get-ChildItem -Path $SourceRoot -Directory

foreach ($folder in $sourceFolders) {
    $name = $folder.Name

    # Salta cartelle meta
    if ($Skip -contains $name) {
        Write-Host "  SKIP  $name" -ForegroundColor DarkGray
        $skipped++
        continue
    }

    # Cerca tutti i PPTX nella cartella (incluse sottocartelle)
    $pptxFiles = Get-ChildItem -Path $folder.FullName -Recurse -Filter "*.pptx"
    if ($pptxFiles.Count -eq 0) {
        Write-Host "  VUOTA $name" -ForegroundColor DarkGray
        $skipped++
        continue
    }

    # Trova la destinazione tramite keyword matching
    $destSubDir = $null
    $nameUpper  = $name.ToUpper()

    foreach ($rule in $Mapping) {
        foreach ($key in $rule.Keys) {
            if ($nameUpper -match $key) {
                $destSubDir = $rule.Dest
                break
            }
        }
        if ($destSubDir) { break }
    }

    if (-not $destSubDir) {
        $unmapped += $name
        Write-Host "  ???   $name" -ForegroundColor Yellow
        continue
    }

    # Copia i file
    $destPath = Join-Path $DestRoot $destSubDir
    foreach ($file in $pptxFiles) {
        $destFile = Join-Path $destPath $file.Name
        Write-Host "  OK    $($file.Name)" -ForegroundColor Green
        Write-Host "        → $destSubDir\"

        if (-not $DryRun) {
            if (-not (Test-Path $destPath)) { New-Item -ItemType Directory -Path $destPath -Force | Out-Null }
            Copy-Item -Path $file.FullName -Destination $destFile -Force
        }
        $copied++
    }
}

# Riepilogo
Write-Host "`n─────────────────────────────────" -ForegroundColor Cyan
Write-Host "File $(if ($DryRun) {'da copiare'} else {'copiati'}): $copied"
Write-Host "Cartelle saltate: $skipped"

if ($unmapped.Count -gt 0) {
    Write-Host "`nCARTELLE NON CLASSIFICATE ($($unmapped.Count)) — da mappare manualmente:" -ForegroundColor Yellow
    $unmapped | ForEach-Object { Write-Host "  - $_" -ForegroundColor Yellow }
    # Salva anche su file per comodità
    $unmapped | Out-File -FilePath "$PSScriptRoot\cartelle-non-classificate.txt" -Encoding utf8
    Write-Host "`n  → Lista salvata in: cartelle-non-classificate.txt"
}

if ($DryRun) {
    Write-Host "`n  Per eseguire davvero: cambia `$DryRun = `$false e riesegui" -ForegroundColor Cyan
}
