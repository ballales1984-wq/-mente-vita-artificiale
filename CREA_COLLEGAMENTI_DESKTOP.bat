@echo off
title Creazione Collegamenti Desktop
echo.
echo ======================================================================
echo   🔗 CREAZIONE COLLEGAMENTI SUL DESKTOP
echo ======================================================================
echo.
echo [INFO] Creazione collegamenti rapidi (molto più veloce degli EXE!)
echo.

set DESKTOP=%USERPROFILE%\Desktop
set PROGETTO=%CD%

echo [1/3] 📺 Collegamento: MenteAI Video+Narrazione
powershell -Command "$WS = New-Object -ComObject WScript.Shell; $SC = $WS.CreateShortcut('%DESKTOP%\🧠 MenteAI Video Narrazione.lnk'); $SC.TargetPath = 'python'; $SC.Arguments = '%PROGETTO%\mente_video_narrazione.py'; $SC.WorkingDirectory = '%PROGETTO%'; $SC.Description = 'Mente AI con Video e Narrazione Real-Time'; $SC.Save()"
echo       ✅ Creato

echo [2/3] 🎭 Collegamento: MenteAI Demo
powershell -Command "$WS = New-Object -ComObject WScript.Shell; $SC = $WS.CreateShortcut('%DESKTOP%\🎭 MenteAI Demo.lnk'); $SC.TargetPath = '%PROGETTO%\AVVIA_AUTOMATICO.bat'; $SC.WorkingDirectory = '%PROGETTO%'; $SC.Description = 'Demo Automatica con Dashboard'; $SC.Save()"
echo       ✅ Creato

echo [3/3] 🧠 Collegamento: MenteAI Buffer
powershell -Command "$WS = New-Object -ComAPI WScript.Shell; $SC = $WS.CreateShortcut('%DESKTOP%\💾 MenteAI Buffer.lnk'); $SC.TargetPath = 'python'; $SC.Arguments = '%PROGETTO%\mente_buffer_temp.py'; $SC.WorkingDirectory = '%PROGETTO%'; $SC.Description = 'Sistema con Buffer Temporaneo'; $SC.Save()"
echo       ✅ Creato

echo.
echo ======================================================================
echo   ✅ COLLEGAMENTI CREATI SUL DESKTOP!
echo ======================================================================
echo.
echo [DESKTOP] Controlla il tuo desktop, troverai:
echo.
echo   🧠 MenteAI Video Narrazione.lnk  ← Video + Narrazione Real-Time
echo   🎭 MenteAI Demo.lnk              ← Demo Automatica
echo   💾 MenteAI Buffer.lnk            ← Sistema Buffer
echo.
echo [USO] Doppio click sul collegamento per avviare!
echo.
echo ======================================================================
echo.
pause

