@echo off
chcp 65001 > nul
cls
echo ================================================================
echo           AVVIO SISTEMA COMPLETO
echo    Mente + Avatar + Dashboard + Demo
echo ================================================================
echo.

echo [1/5] Preparazione ambiente...
if not exist data mkdir data
echo [OK] Directory data\ pronta
echo.

echo [2/5] Avvio Avatar 3D (omino)...
start "Avatar 3D" python avatar_3d.py
timeout /t 2 /nobreak > nul
echo [OK] Avatar avviato
echo.

echo [3/5] Avvio Dashboard Web...
start "Dashboard" streamlit run dashboard.py
timeout /t 3 /nobreak > nul
echo [OK] Dashboard avviata su http://localhost:8501
echo.

echo [4/5] Avvio Simulazione Demo (dati)...
start "Demo" python mente_ai_demo.py
timeout /t 2 /nobreak > nul
echo [OK] Demo avviata (genera episodi)
echo.

echo ================================================================
echo           SISTEMA COMPLETO ATTIVO!
echo ================================================================
echo.
echo Finestre aperte:
echo   [1] Avatar 3D (omino che reagisce)
echo   [2] Dashboard Web (http://localhost:8501)
echo   [3] Simulazione Demo (genera dati)
echo.
echo [INFO] L'omino reagisce automaticamente ai dati!
echo [INFO] La dashboard si aggiorna in tempo reale!
echo.
echo ================================================================
echo.
echo Premi un tasto per TERMINARE tutto...
pause > nul

echo.
echo [SHUTDOWN] Chiusura componenti...
taskkill /F /FI "WINDOWTITLE eq Avatar 3D*" > nul 2>&1
taskkill /F /FI "WINDOWTITLE eq Dashboard*" > nul 2>&1
taskkill /F /FI "WINDOWTITLE eq Demo*" > nul 2>&1
echo [OK] Sistema spento
echo.



