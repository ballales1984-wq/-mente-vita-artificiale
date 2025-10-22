@echo off
echo ================================================================
echo    CREAZIONE EXE - MENTE ARTIFICIALE MODULARE
echo ================================================================
echo.

REM Controlla se PyInstaller è installato
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo [*] Installazione PyInstaller...
    pip install pyinstaller
    echo.
)

echo [*] Creazione eseguibile in corso...
echo.

REM Crea EXE con PyInstaller
pyinstaller --onefile ^
    --name="MenteArtificiale" ^
    --icon=NONE ^
    --console ^
    --add-data "moduli;moduli" ^
    --hidden-import="moduli.visione" ^
    --hidden-import="moduli.udito" ^
    --hidden-import="moduli.motoria" ^
    --hidden-import="moduli.prefrontale" ^
    --hidden-import="moduli.memoria" ^
    --hidden-import="moduli.emozione" ^
    --hidden-import="moduli.talamo" ^
    --hidden-import="moduli.tronco" ^
    --hidden-import="moduli.base" ^
    esempio_semplice.py

echo.
echo ================================================================
echo    FATTO! Eseguibile creato in: dist\MenteArtificiale.exe
echo ================================================================
echo.
pause

