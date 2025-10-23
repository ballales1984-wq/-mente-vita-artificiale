#!/usr/bin/env python3
"""
🧠 MENTE ARTIFICIALE UNIFICATA - Versione Finale Completa v4.0
===============================================================

Sistema cognitivo unificato con:
✅ Tutti i 11 moduli cerebrali
✅ Narrazione cognitiva in linguaggio naturale
✅ Memoria permanente 2GB con consolidamento
✅ Cicli estesi (fino a 1000+)
✅ Hardware reale (camera + microfono)
✅ Ottimizzazione automatica memoria
✅ Salvataggio progressivo

Autore: Alessio + Cursor AI
Data: 22 Ottobre 2025
"""

import os
import sys
import time
import json
from datetime import datetime
from pathlib import Path

# Moduli core
from moduli import visione, udito, prefrontale, motoria, emozione
from moduli.biosegnale import InterfacciaCoerenzaCerebrale
from moduli.memoria_permanente import MemoriaPermanente

# Moduli avanzati (Fase 2 - Espansione Cognitiva)
from moduli.pianificazione import Pianificatore
from moduli.attenzione import AttenzionSelettiva
from moduli.teoria_mente import TeoriaDellaMente
from moduli.linguaggio import SistemaLinguaggio
from moduli.creativita import SistemaCreativita

# Opzionali
try:
    import cv2
    CV2_OK = True
except:
    CV2_OK = False

try:
    import sounddevice as sd
    from scipy.io import wavfile
    AUDIO_OK = True
except:
    AUDIO_OK = False


class ConfigurazioneUnificata:
    """Configurazione sistema unificato"""
    
    def __init__(self):
        # Cicli
        self.num_cicli = 1000  # Cicli da eseguire (0 = infinito)
        self.delay_tra_cicli = 2.0  # Secondi tra cicli
        
        # Hardware
        self.usa_camera = True
        self.usa_microfono = True
        self.durata_ascolto = 4.0  # Secondi
        
        # Memoria
        self.memoria_max_gb = 2  # Limite memoria permanente
        self.auto_consolidamento = True
        self.intervallo_consolidamento = 50  # Ogni 50 cicli
        
        # Narrazione
        self.mostra_narrazione = True
        self.salva_narrazione_file = True
        
        # Salvataggio
        self.salva_ogni_n_cicli = 10  # Salva stato ogni 10 cicli
        self.cartella_output = Path("output_unificato")


class MenteUnificata:
    """Sistema unificato completo"""
    
    def __init__(self, config: ConfigurazioneUnificata):
        self.config = config
        
        # Crea cartelle
        config.cartella_output.mkdir(exist_ok=True)
        
        print("\n" + "="*70)
        print("  🧠 MENTE ARTIFICIALE UNIFICATA v4.0")
        print("="*70)
        print(f"\n[CONFIG]")
        print(f"  • Cicli configurati: {config.num_cicli if config.num_cicli > 0 else 'INFINITI'}")
        print(f"  • Memoria disponibile: {config.memoria_max_gb}GB")
        print(f"  • Ascolto: {config.durata_ascolto}s")
        print(f"  • Consolidamento: Ogni {config.intervallo_consolidamento} cicli")
        
        # Inizializza moduli
        print(f"\n[INIT] Caricamento moduli...")
        
        self.visione = visione.CortecciaVisiva()
        self.udito = udito.CortecciaUditiva()
        self.biosegnali = InterfacciaCoerenzaCerebrale()
        self.emozione = emozione.Amigdala()
        self.emozione.inizializza()
        self.prefrontale = prefrontale.CortecciaPrefrontale()
        self.prefrontale.inizializza()
        self.motoria = motoria.CortecciaMotoria()
        self.memoria = MemoriaPermanente(max_size_gb=config.memoria_max_gb)
        
        # Moduli avanzati (Fase 2)
        print(f"\n[AVANZATI] Caricamento moduli cognitivi superiori...")
        self.pianificatore = Pianificatore()
        self.attenzione = AttenzionSelettiva()
        self.teoria_mente = TeoriaDellaMente()
        self.linguaggio = SistemaLinguaggio()
        self.creativita = SistemaCreativita()
        print("  ✅ 5 moduli avanzati attivi!")
        
        # Camera
        self.camera = None
        if config.usa_camera and CV2_OK:
            try:
                self.camera = cv2.VideoCapture(0)
                if self.camera.isOpened():
                    print("  ✅ Camera attiva")
                else:
                    config.usa_camera = False
            except:
                config.usa_camera = False
        
        # Stats
        self.stats = {
            'cicli_eseguiti': 0,
            'successi': 0,
            'fallimenti': 0,
            'inizio': datetime.now().isoformat(),
            'memorie_salvate': 0
        }
        
        # Log narrazione
        if config.salva_narrazione_file:
            self.log_file = open(config.cartella_output / "log_completo.txt", "w", encoding="utf-8")
            self.log_file.write("="*70 + "\n")
            self.log_file.write("  🧠 LOG COMPLETO MENTE UNIFICATA\n")
            self.log_file.write("="*70 + "\n")
            self.log_file.write(f"Inizio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            self.log_file.write(f"Cicli previsti: {config.num_cicli}\n")
            self.log_file.write("="*70 + "\n\n")
        else:
            self.log_file = None
        
        print("\n[OK] Sistema pronto!\n")
    
    def genera_narrazione(self, vis, audio_text, valenza, pattern, azione, successo):
        """Genera narrazione cognitiva"""
        lines = []
        
        # Header
        lines.append("\n" + "="*70)
        lines.append("  💭 NARRAZIONE COGNITIVA")
        lines.append("="*70)
        
        # Vista
        emo = "[++]" if valenza > 0.5 else ("[+]" if valenza > 0 else ("[-]" if valenza < 0 else "[=]"))
        lines.append(f"\n[VISTA] {emo}")
        desc = vis.get('descrizione', 'nulla')
        lines.append(f'   "Vedo: {desc}"')
        if vis.get('num_oggetti', 0) > 0:
            lines.append(f'   "Ho rilevato {vis["num_oggetti"]} oggetti."')
        
        # Udito
        lines.append(f"\n[UDITO]")
        if audio_text:
            lines.append(f'   "Ho sentito: \'{audio_text}\'"')
        else:
            lines.append(f'   "Silenzio o rumore di fondo."')
        
        # Emozioni
        if valenza > 0.5:
            stato = "positivo e fiducioso"
        elif valenza > 0:
            stato = "leggermente positivo"
        else:
            stato = "neutro e calmo"
        
        neuroni = pattern.count('█')
        lines.append(f"\n[EMOZIONI] {emo}")
        lines.append(f'   "Mi sento {stato} (valenza: {valenza:+.2f})."')
        lines.append(f'   "Attività neurale: {neuroni} neuroni attivi su {len(pattern)}."')
        
        # Pensieri
        lines.append(f"\n[PENSIERI]")
        if audio_text:
            if any(w in audio_text.lower() for w in ['ciao', 'salve']):
                lines.append(f'   "Saluto rilevato. Rispondo cordialmente."')
            if any(w in audio_text.lower() for w in ['vieni', 'avvicinati']):
                lines.append(f'   "Richiesta di avvicinamento. Valuto sicurezza."')
        lines.append(f'   "Situazione analizzata e valutata."')
        
        # Decisione
        lines.append(f"\n[DECISIONE]")
        lines.append(f'   "Ho deciso di: {azione.upper().replace("_", " ")}"')
        
        # Motivazione
        motivazioni = {
            'avvicinati': "Richiesta diretta, situazione sicura.",
            'allontanati': "Situazione incerta, prendo distanza.",
            'fermati': "Comando stop ricevuto.",
            'mantieni_distanza': "Osservazione prudente.",
            'monitora': "Continuo analisi senza intervenire.",
            'esegui_comando': "Comando ricevuto, eseguo.",
        }
        lines.append(f"\n[MOTIVAZIONE]")
        lines.append(f'   "{motivazioni.get(azione, "Azione appropriata.")}"')
        
        # Esito
        lines.append(f"\n[ESITO]")
        if successo:
            lines.append(f'   "Azione eseguita con successo."')
        else:
            lines.append(f'   "Azione non riuscita, mi adatto."')
        
        # Apprendimento
        lines.append(f"\n[APPRENDIMENTO]")
        if valenza > 0 and successo:
            lines.append(f'   "Esperienza positiva, rafforzo comportamento."')
        elif valenza < 0:
            lines.append(f'   "Memorizzo per evitarla in futuro."')
        else:
            lines.append(f'   "Aggiungo esperienza alla memoria."')
        
        lines.append("\n" + "="*70)
        
        return "\n".join(lines)
    
    def ciclo_cognitivo(self, num_ciclo):
        """Esegue un ciclo cognitivo completo"""
        
        print(f"\n{'╔'+'═'*68+'╗'}")
        print(f"║ CICLO #{num_ciclo:04d}{' '*58}║")
        print(f"{'╚'+'═'*68+'╝'}")
        
        # 1. Visione
        print("\n[1/7] 👁️  VISIONE")
        vis = self.visione.elabora(None)
        print(f"       {vis['descrizione']}")
        
        # 2. Udito
        print("\n[2/7] 👂 UDITO")
        aud = self.udito.ascolta(None)
        audio_text = aud.get('testo', aud.get('trascrizione', ''))
        if audio_text:
            print(f"       '{audio_text}'")
        else:
            print(f"       Silenzio")
        
        # 3. Biosegnali
        print("\n[3/7] ⚡ BIOSEGNALI")
        onda = self.biosegnali.percepisce_segnale([vis, aud])
        pattern = onda.pattern.replace('1', '█').replace('0', '░')
        print(f"       {pattern}")
        
        # 4. Emozione
        print("\n[4/7] ❤️  EMOZIONE")
        stato = self.emozione.elabora({'percezioni': [vis, aud]})
        valenza = stato.dati.get('valenza', 0)
        print(f"       {valenza:+.2f}")
        
        # 5. Decisione
        print("\n[5/7] 🧠 DECISIONE")
        dec = self.prefrontale.ragiona({
            'percezioni_visive': vis,
            'percezioni_uditive': aud
        })
        azione = dec.get('azione', 'monitora')
        print(f"       {azione.upper()}")
        
        # 6. Azione
        print("\n[6/7] 🦾 AZIONE")
        successo = self.motoria.agisci({'azione': azione})
        print(f"       {'✅ Successo' if successo else '❌ Fallito'}")
        
        # 7. Narrazione
        if self.config.mostra_narrazione:
            narrazione = self.genera_narrazione(vis, audio_text, valenza, pattern, azione, successo)
            print(narrazione)
            
            # Salva in file
            if self.log_file:
                self.log_file.write(f"\n{'='*70}\n")
                self.log_file.write(f"CICLO #{num_ciclo:04d}\n")
                self.log_file.write(narrazione + "\n")
                self.log_file.flush()
        
        # 8. Memoria
        memoria_episodio = {
            'ciclo': num_ciclo,
            'descrizione': vis.get('descrizione', ''),
            'audio': audio_text,
            'emozione': 'positivo' if valenza > 0 else 'neutro',
            'valenza': valenza,
            'azione': azione,
            'successo': successo,
            'pattern': pattern
        }
        self.memoria.aggiungi_memoria(memoria_episodio)
        
        # Stats
        self.stats['cicli_eseguiti'] = num_ciclo
        if successo:
            self.stats['successi'] += 1
        else:
            self.stats['fallimenti'] += 1
        self.stats['memorie_salvate'] = self.memoria.get_statistiche()['totale_memorie']
        
        return successo
    
    def consolidamento_memoria(self, num_ciclo):
        """Consolida memoria ogni N cicli"""
        print(f"\n[CONSOLIDAMENTO] Ottimizzazione memoria al ciclo {num_ciclo}...")
        
        stats_pre = self.memoria.get_statistiche()
        pre_mb = stats_pre['spazio_usato_mb']
        
        # Se memoria > 80% del limite, comprimi
        if stats_pre['percentuale_usata'] > 80:
            print(f"  ⚠️  Memoria al {stats_pre['percentuale_usata']:.1f}%, comprimo...")
            self.memoria._comprimi_vecchie()
        
        stats_post = self.memoria.get_statistiche()
        post_mb = stats_post['spazio_usato_mb']
        
        print(f"  ✅ Memoria: {pre_mb:.2f}MB → {post_mb:.2f}MB")
        print(f"  📊 Memorie totali: {stats_post['totale_memorie']}")
    
    def salva_checkpoint(self, num_ciclo):
        """Salva stato sistema"""
        checkpoint = {
            'ciclo': num_ciclo,
            'timestamp': datetime.now().isoformat(),
            'stats': self.stats,
            'memoria_stats': self.memoria.get_statistiche()
        }
        
        path = self.config.cartella_output / f"checkpoint_{num_ciclo:04d}.json"
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(checkpoint, f, indent=2)
        
        print(f"[CHECKPOINT] Salvato: {path.name}")
    
    def report_progresso(self, num_ciclo):
        """Report periodico"""
        print(f"\n{'='*70}")
        print(f"  📊 REPORT PROGRESSO - Ciclo {num_ciclo}")
        print(f"{'='*70}")
        print(f"  • Cicli completati: {self.stats['cicli_eseguiti']}")
        print(f"  • Successi: {self.stats['successi']}")
        print(f"  • Fallimenti: {self.stats['fallimenti']}")
        print(f"  • Tasso successo: {self.stats['successi']/num_ciclo*100:.1f}%")
        
        mem_stats = self.memoria.get_statistiche()
        print(f"\n  💾 MEMORIA:")
        print(f"  • Episodi salvati: {mem_stats['totale_memorie']}")
        print(f"  • Spazio usato: {mem_stats['spazio_usato_mb']:.2f}MB / {self.config.memoria_max_gb*1024}MB")
        print(f"  • Percentuale: {mem_stats['percentuale_usata']:.1f}%")
        print(f"  • Rimanente: {mem_stats['spazio_rimanente_gb']:.3f}GB")
        print(f"{'='*70}\n")
    
    def esegui_sessione(self):
        """Esegue sessione completa"""
        print(f"\n[SESSIONE] Inizio esecuzione")
        print(f"  • Cicli: {self.config.num_cicli if self.config.num_cicli > 0 else 'INFINITI'}")
        print(f"  • Delay: {self.config.delay_tra_cicli}s")
        print(f"\n[!] Premi CTRL+C per interrompere\n")
        
        ciclo = 1
        
        try:
            while True:
                # Esegui ciclo
                successo = self.ciclo_cognitivo(ciclo)
                
                # Consolidamento periodico
                if self.config.auto_consolidamento and ciclo % self.config.intervallo_consolidamento == 0:
                    self.consolidamento_memoria(ciclo)
                
                # Salvataggio checkpoint
                if ciclo % self.config.salva_ogni_n_cicli == 0:
                    self.salva_checkpoint(ciclo)
                
                # Report progresso
                if ciclo % 50 == 0:
                    self.report_progresso(ciclo)
                
                # Check limite cicli
                if self.config.num_cicli > 0 and ciclo >= self.config.num_cicli:
                    print(f"\n[FINE] Raggiunto limite di {self.config.num_cicli} cicli")
                    break
                
                # Pausa
                time.sleep(self.config.delay_tra_cicli)
                ciclo += 1
        
        except KeyboardInterrupt:
            print(f"\n\n[!] Interruzione utente al ciclo {ciclo}")
        
        finally:
            self.chiudi(ciclo)
    
    def chiudi(self, ciclo_finale):
        """Chiude sistema e salva finale"""
        print(f"\n[SHUTDOWN] Chiusura sistema...")
        
        # Chiudi camera
        if self.camera:
            self.camera.release()
            if CV2_OK:
                cv2.destroyAllWindows()
        
        # Salva stats finali
        self.stats['fine'] = datetime.now().isoformat()
        self.stats['cicli_finali'] = ciclo_finale
        
        stats_path = self.config.cartella_output / "stats_finali.json"
        with open(stats_path, 'w', encoding='utf-8') as f:
            json.dump(self.stats, f, indent=2)
        
        # Chiudi log
        if self.log_file:
            self.log_file.write(f"\n{'='*70}\n")
            self.log_file.write(f"Fine: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            self.log_file.write(f"Cicli completati: {ciclo_finale}\n")
            self.log_file.write(f"{'='*70}\n")
            self.log_file.close()
        
        # Report finale
        print(f"\n{'='*70}")
        print(f"  🎉 SESSIONE COMPLETATA")
        print(f"{'='*70}")
        print(f"\n[RISULTATI]")
        print(f"  • Cicli eseguiti: {ciclo_finale}")
        print(f"  • Successi: {self.stats['successi']}")
        print(f"  • Tasso successo: {self.stats['successi']/ciclo_finale*100:.1f}%")
        
        mem_stats = self.memoria.get_statistiche()
        print(f"\n[MEMORIA]")
        print(f"  • Episodi salvati: {mem_stats['totale_memorie']}")
        print(f"  • Spazio usato: {mem_stats['spazio_usato_mb']:.2f}MB")
        
        print(f"\n[FILE SALVATI]")
        print(f"  • Log completo: {self.config.cartella_output}/log_completo.txt")
        print(f"  • Stats finali: {self.config.cartella_output}/stats_finali.json")
        print(f"  • Memoria: memoria_permanente/")
        print(f"{'='*70}\n")


# ==================== MENU ====================

def menu():
    """Menu interattivo"""
    print("""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║        🧠 MENTE ARTIFICIALE UNIFICATA v4.0                      ║
║                                                                  ║
║    Sistema completo con memoria 2GB e cicli estesi              ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
    """)
    
    print("\n[MENU] Scegli configurazione:\n")
    print("  1. Test rapido (10 cicli)")
    print("  2. Sessione media (100 cicli)")
    print("  3. Sessione lunga (1000 cicli)")
    print("  4. Sessione infinita (CTRL+C per fermare)")
    print("  5. Personalizzato")
    print("\n  9. Esci")
    
    scelta = input("\n>> Scelta: ").strip()
    
    config = ConfigurazioneUnificata()
    
    if scelta == "1":
        config.num_cicli = 10
    elif scelta == "2":
        config.num_cicli = 100
    elif scelta == "3":
        config.num_cicli = 1000
    elif scelta == "4":
        config.num_cicli = 0  # Infinito
    elif scelta == "5":
        try:
            num = int(input("Numero cicli (0=infinito): ").strip())
            config.num_cicli = num
        except:
            print("\n❌ Valore non valido, uso 10")
            config.num_cicli = 10
    elif scelta == "9":
        print("\n✅ Uscita\n")
        return
    else:
        print("\n❌ Scelta non valida\n")
        return menu()
    
    # Avvia
    mente = MenteUnificata(config)
    mente.esegui_sessione()


# ==================== ENTRY POINT ====================

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\n\n✅ Interruzione utente\n")
    except Exception as e:
        print(f"\n❌ Errore: {e}\n")
        import traceback
        traceback.print_exc()

