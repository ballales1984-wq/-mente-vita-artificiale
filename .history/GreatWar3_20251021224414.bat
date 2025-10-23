@echo off
title GreatWar3 - Gioco di Guerra Strategico
echo ============================================
echo    GREATWAR3 - AVVIO IN CORSO...
echo ============================================
echo.

cd /d "%~dp0greatwar3"
python gioco_avanzato.py

if errorlevel 1 (
    echo.
    echo ============================================
    echo    ERRORE: Il gioco si e' chiuso con errori
    echo ============================================
    pause
)

