@echo off
title Creazione EXE per Desktop
echo.
echo ======================================================================
echo   📦 CREAZIONE EXE PER DESKTOP
echo ======================================================================
echo.
echo [INFO] Creazione eseguibili Windows...
echo [INFO] Questo può richiedere 5-10 minuti
echo.
pause

echo.
echo [1/3] 📺 Creazione: MenteAI_Video_Narrazione.exe
echo ======================================================================
pyinstaller --onefile --noconsole --name "MenteAI_Video_Narrazione" --icon=NONE ^
    --add-data "moduli;moduli" ^
    mente_video_narrazione.py

if %ERRORLEVEL% NEQ 0 (
    echo ❌ Errore creazione MenteAI_Video_Narrazione.exe
    pause
    exit /b 1
)
echo ✅ MenteAI_Video_Narrazione.exe creato!
echo.

echo [2/3] 🎭 Creazione: MenteAI_Demo_Narrazione.exe
echo ======================================================================
pyinstaller --onefile --console --name "MenteAI_Demo_Narrazione" --icon=NONE ^
    --add-data "moduli;moduli" ^
    mente_demo_con_narrazione.py

if %ERRORLEVEL% NEQ 0 (
    echo ❌ Errore creazione MenteAI_Demo_Narrazione.exe
    pause
    exit /b 1
)
echo ✅ MenteAI_Demo_Narrazione.exe creato!
echo.

echo [3/3] 🧠 Creazione: MenteAI_Buffer.exe
echo ======================================================================
pyinstaller --onefile --console --name "MenteAI_Buffer" --icon=NONE ^
    --add-data "moduli;moduli" ^
    mente_buffer_temp.py

if %ERRORLEVEL% NEQ 0 (
    echo ❌ Errore creazione MenteAI_Buffer.exe
    pause
    exit /b 1
)
echo ✅ MenteAI_Buffer.exe creato!
echo.

echo ======================================================================
echo   ✅ TUTTI GLI EXE CREATI CON SUCCESSO!
echo ======================================================================
echo.
echo [POSIZIONE] Gli EXE sono in: dist\
echo.
dir dist\*.exe /B
echo.
echo [COPIA] Copiando sul Desktop...
copy dist\MenteAI_Video_Narrazione.exe "%USERPROFILE%\Desktop\" >nul 2>&1
copy dist\MenteAI_Demo_Narrazione.exe "%USERPROFILE%\Desktop\" >nul 2>&1
copy dist\MenteAI_Buffer.exe "%USERPROFILE%\Desktop\" >nul 2>&1
echo ✅ File copiati sul Desktop!
echo.
echo ======================================================================
echo   🎉 FATTO! Controlla il tuo Desktop
echo ======================================================================
echo.
echo [EXE DISPONIBILI]
echo   • MenteAI_Video_Narrazione.exe  ← Video + Narrazione (Consigliato!)
echo   • MenteAI_Demo_Narrazione.exe   ← Demo con narrazione
echo   • MenteAI_Buffer.exe            ← Sistema completo
echo.
echo [NOTA] Al primo avvio Windows potrebbe chiedere conferma sicurezza
echo        Clicca "Ulteriori informazioni" → "Esegui comunque"
echo.
pause

