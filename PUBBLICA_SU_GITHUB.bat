@echo off
echo ================================================================================
echo   PUBBLICAZIONE SU GITHUB - Mente Vita Artificiale
echo ================================================================================
echo.

echo [STEP 1] Verifica git...
git --version >nul 2>&1
if errorlevel 1 (
    echo ERRORE: Git non installato!
    echo Scarica da: https://git-scm.com/
    pause
    exit /b 1
)
echo   OK Git installato
echo.

echo [STEP 2] Inizializza repository (se non ancora fatto)...
if not exist ".git" (
    git init
    echo   OK Repository inizializzato
) else (
    echo   OK Repository già esistente
)
echo.

echo [STEP 3] Aggiungi file...
git add .
echo   OK File aggiunti
echo.

echo [STEP 4] Commit...
git commit -m "Release v7.0 - Artificial Life System (28 modules, 7 phases)"
echo   OK Commit creato
echo.

echo [STEP 5] Crea repository su GitHub...
echo.
echo   MANUALE: Vai su https://github.com/new
echo            Nome: mente-vita-artificiale
echo            Descrizione: Artificial Life System - 28 brain modules, 7 phases
echo            Pubblico: SI
echo            README: NO (ce l'hai già)
echo            .gitignore: NO (ce l'hai già)
echo            License: Apache 2.0 (ce l'hai già)
echo.
echo   Premi un tasto quando hai creato il repository...
pause >nul
echo.

echo [STEP 6] Inserisci URL repository...
echo   Esempio: https://github.com/TUO_USERNAME/mente-vita-artificiale.git
echo.
set /p REPO_URL="URL Repository: "
echo.

echo [STEP 7] Connetti repository remoto...
git remote add origin %REPO_URL%
echo   OK Remote configurato
echo.

echo [STEP 8] Push su GitHub...
git branch -M main
git push -u origin main
echo.

if errorlevel 0 (
    echo ================================================================================
    echo   SUCCESSO! Progetto pubblicato su GitHub!
    echo ================================================================================
    echo.
    echo   Repository: %REPO_URL%
    echo.
    echo   Prossimi passi:
    echo   1. Aggiungi topics: ai, agi, consciousness, artificial-life
    echo   2. Aggiungi descrizione dettagliata
    echo   3. Crea release v7.0
    echo   4. Condividi sui social!
    echo.
) else (
    echo.
    echo ================================================================================
    echo   ERRORE durante il push
    echo ================================================================================
    echo.
    echo   Verifica:
    echo   - URL repository corretto
    echo   - Permessi di accesso
    echo   - Connessione internet
    echo.
)

echo.
pause


