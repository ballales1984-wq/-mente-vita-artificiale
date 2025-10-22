@echo off
title Mente Artificiale - Launcher
color 0A

:menu
cls
echo ================================================================
echo           MENTE ARTIFICIALE MODULARE - LAUNCHER
echo ================================================================
echo.
echo Scegli quale versione avviare:
echo.
echo   [1] Ciclo Singolo (Demo veloce)
echo   [2] Cicli Continui (30 cicli con menu)
echo   [3] Apri cartella eseguibili
echo   [4] Esci
echo.
echo ================================================================
echo.

choice /c 1234 /n /m "Scelta: "

if errorlevel 4 goto :eof
if errorlevel 3 goto opendir
if errorlevel 2 goto cicli
if errorlevel 1 goto singolo

:singolo
cls
echo Avvio ciclo singolo...
echo.
dist\MenteArtificiale.exe
pause
goto menu

:cicli
cls
echo Avvio versione con cicli continui...
echo.
dist\MenteAI_Cicli.exe
pause
goto menu

:opendir
explorer dist
goto menu

