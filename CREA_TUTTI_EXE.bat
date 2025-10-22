@echo off
chcp 65001 > nul
echo ================================================================
echo    CREAZIONE ESEGUIBILI - MENTE ARTIFICIALE v3.0
echo ================================================================
echo.

REM Controlla se PyInstaller è installato
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo [1/5] Installazione PyInstaller...
    pip install pyinstaller
    echo.
) else (
    echo [OK] PyInstaller già installato
    echo.
)

echo ================================================================
echo [2/5] Creazione MenteAI_Semplice.exe
echo ================================================================
echo.

pyinstaller --onefile --name="MenteAI_Semplice" --console --add-data "moduli;moduli" --hidden-import="moduli.visione" --hidden-import="moduli.udito" --hidden-import="moduli.motoria" --hidden-import="moduli.prefrontale" --hidden-import="moduli.memoria" --hidden-import="moduli.emozione" --hidden-import="moduli.talamo" --hidden-import="moduli.tronco" --hidden-import="moduli.base" esempio_semplice.py

echo.
echo [OK] MenteAI_Semplice.exe creato!
echo.

echo ================================================================
echo [3/5] Creazione MenteAI_Cicli.exe (con memoria)
echo ================================================================
echo.

pyinstaller --onefile --name="MenteAI_Cicli" --console --add-data "moduli;moduli" --add-data "data;data" --hidden-import="moduli.visione" --hidden-import="moduli.udito" --hidden-import="moduli.motoria" --hidden-import="moduli.prefrontale" --hidden-import="moduli.memoria" --hidden-import="moduli.emozione" --hidden-import="moduli.talamo" --hidden-import="moduli.tronco" --hidden-import="moduli.base" --hidden-import="moduli.biosegnale" --hidden-import="moduli.segnali_neurali" mente_ai_cicli.py

echo.
echo [OK] MenteAI_Cicli.exe creato!
echo.

echo ================================================================
echo [4/5] Creazione MenteAI_Camera.exe
echo ================================================================
echo.

pyinstaller --onefile --name="MenteAI_Camera" --console --add-data "moduli;moduli" --add-data "data;data" --hidden-import="moduli.visione" --hidden-import="moduli.udito" --hidden-import="moduli.motoria" --hidden-import="moduli.prefrontale" --hidden-import="moduli.memoria" --hidden-import="moduli.emozione" --hidden-import="moduli.talamo" --hidden-import="moduli.tronco" --hidden-import="moduli.base" --hidden-import="cv2" mente_con_camera.py

echo.
echo [OK] MenteAI_Camera.exe creato!
echo.

echo ================================================================
echo [5/5] Pulizia file temporanei
echo ================================================================
echo.

REM Rimuovi file .spec
del /Q *.spec 2>nul

echo [OK] Pulizia completata
echo.

echo ================================================================
echo    TUTTI GLI ESEGUIBILI CREATI CON SUCCESSO!
echo ================================================================
echo.
echo Eseguibili disponibili in: dist\
echo.
echo   - MenteAI_Semplice.exe (demo rapida)
echo   - MenteAI_Cicli.exe (con memoria)
echo   - MenteAI_Camera.exe (con camera)
echo.
echo ================================================================
echo.
echo [INFO] Per creare release GitHub:
echo   1. Copia tutti gli .exe in una cartella
echo   2. Crea ZIP: release_v3.0.zip
echo   3. Upload su GitHub release
echo.
pause

