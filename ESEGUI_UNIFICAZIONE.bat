@echo off
chcp 65001 > nul
echo ================================================================
echo    UNIFICAZIONE PROGETTO - Mente Artificiale v3.0
echo ================================================================
echo.

echo [1/6] Backup file importanti...
if not exist backup mkdir backup
copy README.md backup\README_old.md > nul 2>&1
copy README_GITHUB.md backup\ > nul 2>&1
copy README_MENTE_AI.md backup\ > nul 2>&1
echo [OK] Backup creato in: backup\
echo.

echo [2/6] Sostituisco README con versione unificata...
copy /Y README_UNIFICATO.md README.md > nul
echo [OK] README.md aggiornato
echo.

echo [3/6] Elimino README duplicati...
del README_GITHUB.md 2>nul
del README_MENTE_AI.md 2>nul
echo [OK] README duplicati eliminati
echo.

echo [4/6] Elimino documentazione duplicata...
del COMPLETATO.md 2>nul
del TUTTO_COMPLETATO.md 2>nul
del PROGETTO_COMPLETO_FINALE.md 2>nul
del PROGETTO_FINALE_COMPLETO.txt 2>nul
echo [OK] Mantieni solo: TUTTO_COMPLETATO_FINALE.md
echo.

echo [5/6] Elimino programmi obsoleti...
del mente_artificiale_modulare.py 2>nul
del mente_inizializzazione_completa.py 2>nul
echo [OK] Programmi obsoleti eliminati
echo.

echo [6/6] Pulizia file temporanei...
del /Q *.spec 2>nul
del "Perfetto. Creiamo ora l'architettur.txt" 2>nul
del test_consolidamento.json 2>nul
del test_richiamo.json 2>nul
del test_integrato.json 2>nul
echo [OK] File temporanei eliminati
echo.

echo ================================================================
echo    UNIFICAZIONE COMPLETATA!
echo ================================================================
echo.
echo File principali:
echo   [OK] README.md (unificato)
echo   [OK] mente_completa_finale.py (sistema completo)
echo   [OK] dashboard.py (visualizzazione)
echo   [OK] TUTTO_COMPLETATO_FINALE.md (achievement)
echo   [OK] 3 eseguibili in dist\
echo.
echo Backup salvato in: backup\
echo.
echo ================================================================
echo    PRONTO PER GITHUB!
echo ================================================================
echo.
pause

