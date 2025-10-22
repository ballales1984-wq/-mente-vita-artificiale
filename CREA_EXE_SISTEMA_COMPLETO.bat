@echo off
chcp 65001 > nul
echo ================================================================
echo    CREAZIONE ESEGUIBILI - Sistema Completo v3.0
echo ================================================================
echo.

REM Controlla PyInstaller
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
echo [2/5] Creazione MenteAI_SistemaCompleto.exe
echo ================================================================
echo.

pyinstaller --onefile --name="MenteAI_SistemaCompleto" --console --add-data "moduli;moduli" --add-data "data;data" --hidden-import="moduli.visione" --hidden-import="moduli.udito" --hidden-import="moduli.motoria" --hidden-import="moduli.prefrontale" --hidden-import="moduli.memoria" --hidden-import="moduli.emozione" --hidden-import="moduli.talamo" --hidden-import="moduli.tronco" --hidden-import="moduli.base" --hidden-import="moduli.biosegnale" --hidden-import="moduli.segnali_neurali" --hidden-import="moduli.apprendimento_online" mente_artificiale_completa.py

echo.
echo [OK] MenteAI_SistemaCompleto.exe creato!
echo.

echo ================================================================
echo [3/5] Creazione Avatar3D.exe
echo ================================================================
echo.

pyinstaller --onefile --name="Avatar3D" --console --noconsole --add-data "data;data" avatar_3d.py

echo.
echo [OK] Avatar3D.exe creato!
echo.

echo ================================================================
echo [4/5] Creazione Launcher.exe
echo ================================================================
echo.

pyinstaller --onefile --name="Launcher_SistemaCompleto" --console --add-data "moduli;moduli" --add-data "data;data" --hidden-import="moduli.visione" --hidden-import="moduli.udito" --hidden-import="moduli.motoria" --hidden-import="moduli.prefrontale" --hidden-import="moduli.memoria" --hidden-import="moduli.emozione" --hidden-import="moduli.biosegnale" --hidden-import="moduli.apprendimento_online" avvia_sistema_completo.py

echo.
echo [OK] Launcher_SistemaCompleto.exe creato!
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
echo   - MenteAI_SistemaCompleto.exe (sistema completo)
echo   - Avatar3D.exe (avatar 3D standalone)
echo   - Launcher_SistemaCompleto.exe (avvia tutto)
echo.
echo NUOVO TOTALE: 6 eseguibili
echo   (3 vecchi + 3 nuovi)
echo.
echo ================================================================
echo.
echo [INFO] Per creare release:
echo   1. Vai in dist\
echo   2. Seleziona tutti gli .exe
echo   3. Crea ZIP: MenteAI_v3.0_Release.zip
echo   4. Upload su GitHub
echo.
pause



