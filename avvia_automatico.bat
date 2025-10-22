@echo off
echo ================================================================
echo    AVVIO AUTOMATICO - Sistema Completo
echo ================================================================
echo.
echo [1/3] Avatar 3D...
start /MIN python avatar_3d.py
timeout /t 1 /nobreak > nul
echo [OK]
echo.
echo [2/3] Dashboard Web...
start /MIN streamlit run dashboard.py
timeout /t 2 /nobreak > nul
echo [OK] Apri: http://localhost:8501
echo.
echo [3/3] Simulazione...
start python mente_ai_demo.py
echo [OK]
echo.
echo ================================================================
echo    TUTTO AVVIATO!
echo ================================================================
echo.
echo Apri browser su: http://localhost:8501
echo.


