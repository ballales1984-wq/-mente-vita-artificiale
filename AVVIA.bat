@echo off
chcp 65001 > nul
cls
echo ================================================================
echo           MENTE ARTIFICIALE MODULARE v3.0
echo ================================================================
echo.
echo Scegli cosa avviare:
echo.
echo   1. Demo rapida (10 secondi)
echo   2. Sistema completo (tutte le funzioni)
echo   3. Dashboard web (visualizzazione)
echo   4. Dashboard + Demo (test senza hardware)
echo   5. Simulazione demo (genera episodi)
echo.
echo   9. Esci
echo.
set /p scelta="Scelta (1-5): "

if "%scelta%"=="1" (
    echo.
    echo [Avvio demo rapida...]
    python esempio_semplice.py
    goto fine
)

if "%scelta%"=="2" (
    echo.
    echo [Avvio sistema completo...]
    python mente_completa_finale.py
    goto fine
)

if "%scelta%"=="3" (
    echo.
    echo [Avvio dashboard web...]
    echo [INFO] Apri browser su: http://localhost:8501
    streamlit run dashboard.py
    goto fine
)

if "%scelta%"=="4" (
    echo.
    echo [Avvio dashboard + demo...]
    echo.
    echo [1/2] Avvio simulazione demo...
    start /B python mente_ai_demo.py
    timeout /t 2 /nobreak > nul
    echo [2/2] Avvio dashboard...
    echo [INFO] Apri browser su: http://localhost:8501
    streamlit run dashboard.py
    goto fine
)

if "%scelta%"=="5" (
    echo.
    echo [Avvio simulazione demo...]
    echo [INFO] Genera episodi simulati
    echo [INFO] Premi CTRL+C per fermare
    python mente_ai_demo.py
    goto fine
)

if "%scelta%"=="9" (
    echo.
    echo [Uscita]
    goto fine
)

echo.
echo [ERRORE] Scelta non valida!
pause
goto fine

:fine
echo.
pause



