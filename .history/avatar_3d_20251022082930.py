"""
🤖 AVATAR 3D - Omino Interattivo
=================================
Visualizzazione 3D che reagisce alle decisioni della mente artificiale.

Funzionalità:
- Omino 3D con testa, corpo, braccia, gambe
- Espressioni facciali (emozioni)
- Movimenti basati su azioni
- Indicatori stati mentali
- Real-time updates

Autore: Alessio + Cursor AI
"""

import pygame
import math
import time
import json
import os
from typing import Dict, Tuple, Optional
from dataclasses import dataclass

# Colori
BIANCO = (255, 255, 255)
NERO = (0, 0, 0)
GRIGIO = (128, 128, 128)
ROSSO = (255, 0, 0)
VERDE = (0, 255, 0)
BLU = (0, 0, 255)
GIALLO = (255, 255, 0)
ARANCIONE = (255, 165, 0)
AZZURRO = (0, 200, 255)


@dataclass
class StatoAvatar:
    """Stato dell'avatar"""
    emozione: str = "neutro"  # felice, triste, arrabbiato, neutro
    azione: str = "idle"  # idle, cammina, guarda, pensa
    energia: float = 1.0  # 0-1
    attenzione: float = 0.5  # 0-1
    arousal: float = 0.5  # 0-1
    pattern_neurale: str = "0000000000"


class Avatar3D:
    """
    Avatar 3D interattivo controllato dalla mente artificiale
    """
    
    def __init__(self, larghezza: int = 800, altezza: int = 600):
        pygame.init()
        
        self.larghezza = larghezza
        self.altezza = altezza
        self.screen = pygame.display.set_mode((larghezza, altezza))
        pygame.display.set_caption("🤖 Avatar - Mente Artificiale")
        
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)
        self.font_grande = pygame.font.Font(None, 36)
        
        # Stato
        self.stato = StatoAvatar()
        
        # Posizione centrale
        self.centro_x = larghezza // 2
        self.centro_y = altezza // 2
        
        # Animazioni
        self.tempo = 0
        self.angolo_braccio = 0
        self.angolo_testa = 0
        self.offset_corpo = 0
        
        # File di comunicazione con la mente
        self.path_stato = "data/avatar_stato.json"
        self.ultimo_aggiornamento = 0
        
        print("[Avatar 3D] ✅ Inizializzato")
    
    def aggiorna_da_file(self):
        """Legge stato dalla mente artificiale"""
        if not os.path.exists(self.path_stato):
            return
        
        try:
            # Controlla se file è stato modificato
            mod_time = os.path.getmtime(self.path_stato)
            if mod_time == self.ultimo_aggiornamento:
                return
            
            self.ultimo_aggiornamento = mod_time
            
            # Leggi stato
            with open(self.path_stato, 'r', encoding='utf-8') as f:
                dati = json.load(f)
            
            # Aggiorna stato
            self.stato.emozione = dati.get('emozione', 'neutro')
            self.stato.azione = dati.get('azione', 'idle')
            self.stato.energia = dati.get('energia', 1.0)
            self.stato.attenzione = dati.get('attenzione', 0.5)
            self.stato.arousal = dati.get('arousal', 0.5)
            self.stato.pattern_neurale = dati.get('pattern_neurale', '0000000000')
            
            print(f"[Avatar] Aggiornato: {self.stato.emozione} - {self.stato.azione}")
        
        except Exception as e:
            pass
    
    def aggiorna_animazioni(self, dt: float):
        """Aggiorna animazioni temporali"""
        self.tempo += dt
        
        # Animazioni basate su azione
        if self.stato.azione == "cammina":
            # Dondolio braccia
            self.angolo_braccio = math.sin(self.tempo * 3) * 30
            self.offset_corpo = abs(math.sin(self.tempo * 3)) * 5
        
        elif self.stato.azione == "guarda":
            # Testa che si muove
            self.angolo_testa = math.sin(self.tempo * 2) * 20
        
        elif self.stato.azione == "pensa":
            # Testa leggermente inclinata
            self.angolo_testa = 15
        
        else:  # idle
            # Respiro lento
            self.offset_corpo = math.sin(self.tempo * 0.5) * 2
            self.angolo_braccio = math.sin(self.tempo * 0.5) * 5
            self.angolo_testa = 0
    
    def disegna_testa(self, x: int, y: int):
        """Disegna testa con espressione"""
        raggio = 40
        
        # Testa (cerchio)
        pygame.draw.circle(self.screen, AZZURRO, (x, y), raggio)
        pygame.draw.circle(self.screen, NERO, (x, y), raggio, 2)
        
        # Occhi
        occhio_offset = 12
        occhio_raggio = 6
        
        # Occhio sinistro
        pygame.draw.circle(self.screen, BIANCO, 
                         (x - occhio_offset, y - 10), occhio_raggio)
        pygame.draw.circle(self.screen, NERO, 
                         (x - occhio_offset, y - 10), occhio_raggio, 1)
        pygame.draw.circle(self.screen, NERO, 
                         (x - occhio_offset, y - 10), 3)
        
        # Occhio destro
        pygame.draw.circle(self.screen, BIANCO, 
                         (x + occhio_offset, y - 10), occhio_raggio)
        pygame.draw.circle(self.screen, NERO, 
                         (x + occhio_offset, y - 10), occhio_raggio, 1)
        pygame.draw.circle(self.screen, NERO, 
                         (x + occhio_offset, y - 10), 3)
        
        # Bocca (varia con emozione)
        if self.stato.emozione == "felice":
            # Sorriso
            pygame.draw.arc(self.screen, NERO, 
                          (x - 20, y, 40, 30), 
                          math.pi, 0, 3)
        
        elif self.stato.emozione == "triste":
            # Bocca all'ingiù
            pygame.draw.arc(self.screen, NERO, 
                          (x - 20, y + 20, 40, 20), 
                          0, math.pi, 3)
        
        elif self.stato.emozione == "arrabbiato":
            # Linea dritta
            pygame.draw.line(self.screen, NERO, 
                           (x - 15, y + 20), 
                           (x + 15, y + 20), 3)
            # Sopracciglia aggrottate
            pygame.draw.line(self.screen, NERO, 
                           (x - 20, y - 20), 
                           (x - 10, y - 25), 2)
            pygame.draw.line(self.screen, NERO, 
                           (x + 10, y - 25), 
                           (x + 20, y - 20), 2)
        
        else:  # neutro
            # Linea
            pygame.draw.line(self.screen, NERO, 
                           (x - 15, y + 20), 
                           (x + 15, y + 20), 2)
    
    def disegna_corpo(self, x: int, y: int):
        """Disegna corpo"""
        # Torso (rettangolo)
        larghezza = 50
        altezza = 80
        pygame.draw.rect(self.screen, AZZURRO, 
                        (x - larghezza//2, y, larghezza, altezza))
        pygame.draw.rect(self.screen, NERO, 
                        (x - larghezza//2, y, larghezza, altezza), 2)
    
    def disegna_braccio(self, x: int, y: int, angolo: float, sinistro: bool = True):
        """Disegna braccio"""
        lunghezza = 50
        spessore = 8
        
        # Calcola posizione finale
        rad = math.radians(angolo)
        if sinistro:
            start_x = x - 25
            end_x = start_x - lunghezza * math.sin(rad)
            end_y = y + lunghezza * math.cos(rad)
        else:
            start_x = x + 25
            end_x = start_x + lunghezza * math.sin(rad)
            end_y = y + lunghezza * math.cos(rad)
        
        # Disegna
        pygame.draw.line(self.screen, AZZURRO, 
                        (start_x, y + 10), 
                        (int(end_x), int(end_y)), spessore)
        
        # Mano (cerchietto)
        pygame.draw.circle(self.screen, AZZURRO, 
                          (int(end_x), int(end_y)), 6)
        pygame.draw.circle(self.screen, NERO, 
                          (int(end_x), int(end_y)), 6, 1)
    
    def disegna_gamba(self, x: int, y: int, offset: float, sinistra: bool = True):
        """Disegna gamba"""
        lunghezza = 60
        spessore = 10
        
        if sinistra:
            start_x = x - 12
            end_x = start_x - offset * 10
        else:
            start_x = x + 12
            end_x = start_x + offset * 10
        
        end_y = y + lunghezza
        
        # Disegna
        pygame.draw.line(self.screen, AZZURRO, 
                        (start_x, y), 
                        (int(end_x), int(end_y)), spessore)
        
        # Piede (cerchietto)
        pygame.draw.circle(self.screen, AZZURRO, 
                          (int(end_x), int(end_y)), 8)
        pygame.draw.circle(self.screen, NERO, 
                          (int(end_x), int(end_y)), 8, 1)
    
    def disegna_omino(self):
        """Disegna omino completo"""
        # Centro con offset corpo
        cx = self.centro_x
        cy = self.centro_y + int(self.offset_corpo)
        
        # Collo
        collo_y = cy - 60
        
        # Gambe
        gambe_y = cy + 80
        offset_gamba = math.sin(self.tempo * 3) * 0.5 if self.stato.azione == "cammina" else 0
        self.disegna_gamba(cx, gambe_y, offset_gamba, sinistra=True)
        self.disegna_gamba(cx, gambe_y, -offset_gamba, sinistra=False)
        
        # Corpo
        self.disegna_corpo(cx, cy)
        
        # Braccia
        self.disegna_braccio(cx, cy, self.angolo_braccio, sinistro=True)
        self.disegna_braccio(cx, cy, -self.angolo_braccio, sinistro=False)
        
        # Testa (con rotazione)
        testa_x = cx + int(math.sin(math.radians(self.angolo_testa)) * 10)
        self.disegna_testa(testa_x, collo_y)
    
    def disegna_hud(self):
        """Disegna HUD con informazioni"""
        # Pannello in alto
        pygame.draw.rect(self.screen, (50, 50, 50), (0, 0, self.larghezza, 60))
        
        # Emozione
        testo_emozione = self.font_grande.render(
            f"😊 {self.stato.emozione.upper()}", True, GIALLO)
        self.screen.blit(testo_emozione, (20, 15))
        
        # Azione
        testo_azione = self.font.render(
            f"Azione: {self.stato.azione}", True, BIANCO)
        self.screen.blit(testo_azione, (250, 20))
        
        # Energia
        self.disegna_barra(450, 20, 150, 20, self.stato.energia, VERDE, "Energia")
        
        # Pannello in basso
        pygame.draw.rect(self.screen, (50, 50, 50), 
                        (0, self.altezza - 80, self.larghezza, 80))
        
        # Pattern neurale
        testo_pattern = self.font.render("Pattern Neurale:", True, BIANCO)
        self.screen.blit(testo_pattern, (20, self.altezza - 70))
        
        # Visualizza pattern
        pattern_visual = self.stato.pattern_neurale.replace('1', '█').replace('0', '░')
        testo_neural = self.font_grande.render(pattern_visual, True, AZZURRO)
        self.screen.blit(testo_neural, (20, self.altezza - 45))
        
        # Attenzione e Arousal
        self.disegna_barra(450, self.altezza - 65, 150, 15, 
                          self.stato.attenzione, GIALLO, "Attenzione")
        self.disegna_barra(450, self.altezza - 40, 150, 15, 
                          self.stato.arousal, ARANCIONE, "Arousal")
    
    def disegna_barra(self, x: int, y: int, larghezza: int, altezza: int, 
                     valore: float, colore: Tuple, label: str = ""):
        """Disegna barra indicatore"""
        # Sfondo
        pygame.draw.rect(self.screen, GRIGIO, (x, y, larghezza, altezza))
        
        # Riempimento
        fill_width = int(larghezza * valore)
        pygame.draw.rect(self.screen, colore, (x, y, fill_width, altezza))
        
        # Bordo
        pygame.draw.rect(self.screen, NERO, (x, y, larghezza, altezza), 2)
        
        # Label
        if label:
            testo = self.font.render(label, True, BIANCO)
            self.screen.blit(testo, (x, y - 18))
        
        # Valore
        testo_val = self.font.render(f"{int(valore*100)}%", True, BIANCO)
        self.screen.blit(testo_val, (x + larghezza + 5, y))
    
    def disegna_sfondo(self):
        """Disegna sfondo"""
        # Gradiente semplice
        for y in range(self.altezza):
            r = 200 - int(y / self.altezza * 100)
            g = 220 - int(y / self.altezza * 120)
            b = 255 - int(y / self.altezza * 100)
            pygame.draw.line(self.screen, (r, g, b), (0, y), (self.larghezza, y))
        
        # Pavimento
        pygame.draw.rect(self.screen, (100, 150, 100), 
                        (0, self.centro_y + 150, self.larghezza, self.altezza))
    
    def run(self):
        """Loop principale"""
        running = True
        
        print("[Avatar] Loop avviato")
        print("[Avatar] La finestra reagirà alle decisioni della mente")
        print("[Avatar] Chiudi finestra per uscire")
        
        while running:
            dt = self.clock.tick(60) / 1000.0  # 60 FPS
            
            # Eventi
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.KEYDOWN:
                    # Comandi manuali per test
                    if event.key == pygame.K_1:
                        self.stato.emozione = "felice"
                    elif event.key == pygame.K_2:
                        self.stato.emozione = "triste"
                    elif event.key == pygame.K_3:
                        self.stato.emozione = "arrabbiato"
                    elif event.key == pygame.K_4:
                        self.stato.emozione = "neutro"
                    
                    elif event.key == pygame.K_w:
                        self.stato.azione = "cammina"
                    elif event.key == pygame.K_g:
                        self.stato.azione = "guarda"
                    elif event.key == pygame.K_p:
                        self.stato.azione = "pensa"
                    elif event.key == pygame.K_SPACE:
                        self.stato.azione = "idle"
            
            # Aggiorna da file
            self.aggiorna_da_file()
            
            # Aggiorna animazioni
            self.aggiorna_animazioni(dt)
            
            # Disegna
            self.disegna_sfondo()
            self.disegna_omino()
            self.disegna_hud()
            
            # Aggiorna schermo
            pygame.display.flip()
        
        pygame.quit()
        print("[Avatar] Chiuso")


# ==================== TEST ====================

if __name__ == "__main__":
    print("="*70)
    print("  🤖 AVATAR 3D - Test")
    print("="*70)
    print()
    print("[INFO] Comandi tastiera:")
    print("  1-4: Cambia emozione (1=felice, 2=triste, 3=arrabbiato, 4=neutro)")
    print("  W: Cammina")
    print("  G: Guarda")
    print("  P: Pensa")
    print("  SPACE: Idle")
    print()
    print("[INFO] L'avatar legge automaticamente da: data/avatar_stato.json")
    print("[INFO] La mente artificiale aggiornerà questo file ad ogni ciclo")
    print()
    
    avatar = Avatar3D()
    avatar.run()

