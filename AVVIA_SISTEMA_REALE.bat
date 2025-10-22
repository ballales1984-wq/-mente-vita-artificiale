@echo off
chcp 65001 > nul
cls
echo ================================================================
echo        AVVIO SISTEMA REALE - Con Camera e Microfono
echo ================================================================
echo.

echo [INFO] Questo script avvia:
echo   1. Avatar 3D (omino che reagisce)
echo   2. Dashboard Web (visualizzazione)
echo   3. Mente REALE (con camera + microfono)
echo.
echo [IMPORTANTE] Assicurati di avere:
echo   - Webcam collegata
echo   - Microfono funzionante
echo.
pause
cls

echo ================================================================
echo [1/3] Avvio Avatar 3D...
echo ================================================================
start "Avatar 3D" python avatar_3d.py
timeout /t 2 /nobreak > nul
echo [OK] Avatar avviato
echo.

echo ================================================================
echo [2/3] Avvio Dashboard Web...
echo ================================================================
start "Dashboard" streamlit run dashboard.py
timeout /t 3 /nobreak > nul
echo [OK] Dashboard: http://localhost:8501
echo.

echo ================================================================
echo [3/3] Avvio Mente Artificiale REALE...
echo ================================================================
echo.
echo [ATTENZIONE] Nella finestra che si apre:
echo   - Scegli opzione 1, 2 o 3
echo   - Quando chiede "PARLA ORA", usa il microfono
echo   - La mente userà la CAMERA REALE
echo.
timeout /t 2 /nobreak > nul

python mente_artificiale_completa.py

echo.
echo ================================================================
echo [FINE] Mente terminata
echo ================================================================
echo.
echo [INFO] Avatar e Dashboard sono ancora aperti
echo [INFO] Chiudi le finestre manualmente o premi un tasto
echo.
pause > nul

echo.
echo [SHUTDOWN] Chiusura componenti...
taskkill /F /FI "WINDOWTITLE eq Avatar 3D*" > nul 2>&1
taskkill /F /FI "WINDOWTITLE eq Dashboard*" > nul 2>&1
echo [OK] Sistema spento
echo.



