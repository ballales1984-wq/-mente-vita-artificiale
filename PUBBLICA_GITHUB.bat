@echo off
echo ================================================================
echo           PUBBLICAZIONE SU GITHUB - Automatica
echo           Mente Artificiale Modulare v2.0
echo ================================================================
echo.

REM Controlla se Git è installato
git --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Git non installato!
    echo.
    echo Scarica da: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo [OK] Git trovato
echo.

REM Chiedi conferma
echo ATTENZIONE: Questo script:
echo   1. Inizializza repository Git
echo   2. Aggiunge tutti i file
echo   3. Crea commit iniziale
echo   4. Ti chiederà URL del repository GitHub
echo.
set /p conferma="Continuare? (s/n): "

if /i not "%conferma%"=="s" (
    echo Operazione annullata
    pause
    exit /b 0
)

echo.
echo ================================================================
echo STEP 1: Inizializzazione Repository
echo ================================================================

REM Inizializza Git (se non già fatto)
if not exist .git (
    echo [*] Inizializzazione Git...
    git init
    echo [OK] Repository inizializzato
) else (
    echo [!] Repository già inizializzato
)

echo.
echo ================================================================
echo STEP 2: Aggiungi File
echo ================================================================

echo [*] Aggiunta file al repository...
git add .
echo [OK] File aggiunti

echo.
echo ================================================================
echo STEP 3: Primo Commit
echo ================================================================

echo [*] Creazione commit iniziale...
git commit -m "feat: Initial release v2.0 - Mente Artificiale con Memoria Intelligente e Biosegnali Neurali"
echo [OK] Commit creato

echo.
echo ================================================================
echo STEP 4: Collegamento a GitHub
echo ================================================================

echo.
echo Hai già creato il repository su GitHub?
echo.
echo Se NO:
echo   1. Vai su https://github.com
echo   2. Click [+] -^> New repository
echo   3. Nome: mente-artificiale-modulare
echo   4. NON aggiungere README/License (già presenti)
echo   5. Copia URL del repository
echo.

set /p repo_url="Inserisci URL repository GitHub (es. https://github.com/user/repo.git): "

if "%repo_url%"=="" (
    echo [ERROR] URL non fornito
    pause
    exit /b 1
)

echo.
echo [*] Collegamento a: %repo_url%
git remote add origin %repo_url% 2>nul

if errorlevel 1 (
    echo [!] Remote già esistente, aggiornamento...
    git remote set-url origin %repo_url%
)

echo [OK] Repository collegato

echo.
echo ================================================================
echo STEP 5: Push su GitHub
echo ================================================================

echo [*] Creazione branch main...
git branch -M main

echo [*] Push su GitHub...
echo.
git push -u origin main

if errorlevel 1 (
    echo.
    echo [!] Push fallito. Possibili cause:
    echo   - Autenticazione richiesta
    echo   - Repository non esistente
    echo   - Problemi connessione
    echo.
    echo Prova manualmente:
    echo   git push -u origin main
    pause
    exit /b 1
)

echo.
echo ================================================================
echo           PUBBLICAZIONE COMPLETATA! 
echo ================================================================
echo.
echo [OK] Repository pubblicato su GitHub!
echo.
echo Apri nel browser:
echo   %repo_url:.git=%
echo.
echo Prossimi step:
echo   1. Verifica file su GitHub
echo   2. Aggiungi topics (Settings -^> About)
echo   3. Abilita Discussions/Issues
echo   4. (Opzionale) Crea Release v2.0.0
echo.
echo ================================================================
pause

