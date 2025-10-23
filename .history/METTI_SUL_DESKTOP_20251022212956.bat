@echo off
title Collegamenti Desktop
cls
echo.
echo ======================================================================
echo   🖥️  CREAZIONE COLLEGAMENTI SUL DESKTOP
echo ======================================================================
echo.
echo [INFO] Creazione collegamenti rapidi (10 secondi)
echo.

set DESKTOP=%USERPROFILE%\Desktop
set PROGETTO=%CD%

echo [1/4] 🧠 Collegamento: Mente Unificata
powershell -Command "$WS = New-Object -ComObject WScript.Shell; $SC = $WS.CreateShortcut('%DESKTOP%\🧠 Mente Unificata.lnk'); $SC.TargetPath = 'python'; $SC.Arguments = '%PROGETTO%\MENTE_UNIFICATA.py'; $SC.WorkingDirectory = '%PROGETTO%'; $SC.Description = 'Sistema Unificato Completo con Narrazione'; $SC.Save()"
if %ERRORLEVEL% EQU 0 (echo       ✅ Creato) else (echo       ❌ Errore)

echo [2/4] 📺 Collegamento: Video + Narrazione
powershell -Command "$WS = New-Object -ComObject WScript.Shell; $SC = $WS.CreateShortcut('%DESKTOP%\📺 Video Narrazione.lnk'); $SC.TargetPath = 'python'; $SC.Arguments = '%PROGETTO%\mente_video_narrazione.py'; $SC.WorkingDirectory = '%PROGETTO%'; $SC.Description = 'Video Camera + Narrazione Real-Time'; $SC.Save()"
if %ERRORLEVEL% EQU 0 (echo       ✅ Creato) else (echo       ❌ Errore)

echo [3/4] 🎭 Collegamento: Dashboard Demo
powershell -Command "$WS = New-Object -ComObject WScript.Shell; $SC = $WS.CreateShortcut('%DESKTOP%\🎭 Dashboard Demo.lnk'); $SC.TargetPath = '%PROGETTO%\AVVIA_AUTOMATICO.bat'; $SC.WorkingDirectory = '%PROGETTO%'; $SC.Description = 'Dashboard Web con Avatar 3D'; $SC.Save()"
if %ERRORLEVEL% EQU 0 (echo       ✅ Creato) else (echo       ❌ Errore)

echo [4/4] 📖 Collegamento: Log Narrazione
powershell -Command "$WS = New-Object -ComObject WScript.Shell; $SC = $WS.CreateShortcut('%DESKTOP%\📖 Log Narrazione.lnk'); $SC.TargetPath = 'notepad.exe'; $SC.Arguments = '%PROGETTO%\output_unificato\log_completo.txt'; $SC.WorkingDirectory = '%PROGETTO%'; $SC.Description = 'Leggi Log Narrazioni Complete'; $SC.Save()"
if %ERRORLEVEL% EQU 0 (echo       ✅ Creato) else (echo       ❌ Errore)

echo.
echo ======================================================================
echo   ✅ COLLEGAMENTI CREATI SUL DESKTOP!
echo ======================================================================
echo.
echo [DESKTOP] Controlla il desktop, troverai:
echo.
echo   🧠 Mente Unificata.lnk         ← Sistema completo (1000+ cicli)
echo   📺 Video Narrazione.lnk        ← Video + narrazione live
echo   🎭 Dashboard Demo.lnk          ← Dashboard web
echo   📖 Log Narrazione.lnk          ← Leggi log completo
echo.
echo [USO] Doppio click per avviare!
echo.
echo ======================================================================
echo.
pause

