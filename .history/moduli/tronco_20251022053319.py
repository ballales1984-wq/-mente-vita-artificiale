"""
🌙 MODULO TRONCO - Sistema Reticolare e Funzioni Vitali
========================================================
Monitoraggio stato interno e autoregolazione sistema.
Equivalente: Tronco encefalico e sistema reticolare

Funzioni principali:
- Monitoraggio energia/batteria
- Gestione stato sistema (arousal, vigilanza)
- Watchdog e recovery da errori
- Heartbeat e health checks
- Load balancing risorse
"""

import time
import psutil
from typing import Dict, Any, Optional
from dataclasses import dataclass
from .base import ModuloCerebrale, TipoModulo, RisultatoElaborazione
from .base import richiede_inizializzazione


@dataclass
class StatoInterno:
    """Stato interno del sistema"""
    energia: float  # % batteria (0-100)
    temperatura: float  # Temperatura CPU °C
    carico_cpu: float  # % utilizzo CPU
    carico_memoria: float  # % utilizzo RAM
    arousal: float  # Livello vigilanza (0-1)
    errori_recenti: int  # Numero errori ultimi cicli
    uptime: float  # Tempo accensione (secondi)
    cicli_cognitivi: int  # Cicli completati


class TroncoEncefalico(ModuloCerebrale):
    """
    Sistema di monitoraggio e regolazione vitale
    
    Funzionalità:
    - Monitora risorse sistema (CPU, RAM, energia)
    - Gestisce stato arousal/vigilanza
    - Watchdog per recovery da errori
    - Health checks continui
    - Suggerisce modalità risparmio energetico
    """
    
    def __init__(self):
        """Inizializza tronco encefalico"""
        super().__init__("Tronco Encefalico", TipoModulo.REGOLAZIONE)
        
        # Stato interno
        self.energia_iniziale = 100.0
        self.energia_corrente = 100.0
        self.drain_rate_base = 0.3  # % per ciclo
        
        self.temperatura_corrente = 45.0
        self.temperatura_max = 85.0
        self.temperatura_warning = 75.0
        
        self.arousal = 0.8  # Livello vigilanza iniziale
        self.arousal_min = 0.3
        self.arousal_max = 1.0
        
        # Statistiche
        self.tempo_avvio = time.time()
        self.cicli_completati = 0
        self.errori_totali = 0
        self.errori_recenti = []
        
        # Soglie allerta
        self.soglia_energia_critica = 15.0
        self.soglia_energia_bassa = 25.0
        self.soglia_cpu_alta = 80.0
        self.soglia_memoria_alta = 85.0
        
        # Watchdog
        self.ultimo_heartbeat = time.time()
        self.timeout_heartbeat = 30.0  # secondi
    
    def inizializza(self) -> bool:
        """Inizializza monitoraggio sistema"""
        print(f"[{self.nome}] Inizializzazione sistema vitale...")
        
        try:
            # Test accesso info sistema
            cpu_percent = psutil.cpu_percent(interval=0.1)
            mem_info = psutil.virtual_memory()
            
            print(f"[{self.nome}] ✅ Accesso info sistema OK")
            print(f"  • CPU: {cpu_percent:.1f}%")
            print(f"  • RAM: {mem_info.percent:.1f}%")
            
            self.attivo = True
            self.modalita_reale = True
            
            # Primo heartbeat
            self.heartbeat()
            
            return True
            
        except Exception as e:
            print(f"[{self.nome}] ⚠️ Errore: {e}")
            print(f"[{self.nome}] Modalità simulata")
            self.attivo = True
            self.modalita_reale = False
            return True
    
    @richiede_inizializzazione
    def elabora(self, input_data: Dict[str, Any]) -> RisultatoElaborazione:
        """
        Monitora e regola stato interno
        
        Args:
            input_data: Dict con:
                - ciclo_completato: Se ciclo cognitivo completato
                - errore_occorso: Se errore nel ciclo
                - carico_cognitivo: Stima carico (0-1)
                
        Returns:
            RisultatoElaborazione con stato e raccomandazioni
        """
        # Aggiorna contatori
        if input_data.get('ciclo_completato', False):
            self.cicli_completati += 1
        
        if input_data.get('errore_occorso', False):
            self.errori_totali += 1
            self.errori_recenti.append(time.time())
            # Mantieni solo ultimi 10 errori
            if len(self.errori_recenti) > 10:
                self.errori_recenti = self.errori_recenti[-10:]
        
        # Leggi stato sistema
        stato = self._leggi_stato_sistema(input_data)
        
        # Aggiorna energia
        self._aggiorna_energia(input_data.get('carico_cognitivo', 0.5))
        
        # Aggiorna arousal
        self._aggiorna_arousal(stato)
        
        # Check allerte
        allerte = self._check_allerte(stato)
        
        # Genera raccomandazioni
        raccomandazioni = self._genera_raccomandazioni(stato, allerte)
        
        # Heartbeat
        self.heartbeat()
        
        return RisultatoElaborazione(
            tipo="reale" if self.modalita_reale else "simulato",
            successo=True,
            dati={
                'stato': stato,
                'allerte': allerte,
                'raccomandazioni': raccomandazioni
            }
        )
    
    def _leggi_stato_sistema(self, input_data: Dict) -> StatoInterno:
        """
        Leggi stato corrente del sistema
        
        Args:
            input_data: Dati addizionali
            
        Returns:
            StatoInterno con metriche correnti
        """
        if self.modalita_reale:
            try:
                # Metriche reali da psutil
                cpu = psutil.cpu_percent(interval=0.1)
                mem = psutil.virtual_memory().percent
                
                # Temperatura (se disponibile)
                try:
                    temps = psutil.sensors_temperatures()
                    if temps:
                        # Prendi prima temperatura disponibile
                        temp = list(temps.values())[0][0].current
                    else:
                        temp = self.temperatura_corrente
                except:
                    temp = self.temperatura_corrente
                
            except Exception as e:
                # Fallback a valori simulati
                cpu = 45.0 + (input_data.get('carico_cognitivo', 0.5) * 30)
                mem = 60.0
                temp = self.temperatura_corrente
        else:
            # Valori simulati
            cpu = 45.0 + (input_data.get('carico_cognitivo', 0.5) * 30)
            mem = 60.0
            temp = self.temperatura_corrente
        
        # Costruisci stato
        uptime = time.time() - self.tempo_avvio
        
        return StatoInterno(
            energia=self.energia_corrente,
            temperatura=temp,
            carico_cpu=cpu,
            carico_memoria=mem,
            arousal=self.arousal,
            errori_recenti=len(self.errori_recenti),
            uptime=uptime,
            cicli_cognitivi=self.cicli_completati
        )
    
    def _aggiorna_energia(self, carico_cognitivo: float):
        """
        Simula consumo energia
        
        Args:
            carico_cognitivo: Carico corrente (0-1)
        """
        # Drain proporzionale al carico
        drain = self.drain_rate_base * (0.5 + carico_cognitivo)
        
        self.energia_corrente -= drain
        self.energia_corrente = max(0.0, self.energia_corrente)
    
    def _aggiorna_arousal(self, stato: StatoInterno):
        """
        Aggiorna livello di vigilanza
        
        Args:
            stato: Stato corrente
        """
        # Arousal diminuisce con energia bassa
        if stato.energia < self.soglia_energia_bassa:
            self.arousal *= 0.95
        
        # Arousal aumenta con errori recenti
        if stato.errori_recenti > 3:
            self.arousal *= 1.1
        
        # Clamp
        self.arousal = max(self.arousal_min, min(self.arousal_max, self.arousal))
    
    def _check_allerte(self, stato: StatoInterno) -> List[Dict[str, Any]]:
        """
        Verifica condizioni di allerta
        
        Args:
            stato: Stato corrente
            
        Returns:
            Lista allerte
        """
        allerte = []
        
        # Energia critica
        if stato.energia <= self.soglia_energia_critica:
            allerte.append({
                'tipo': 'CRITICO',
                'categoria': 'energia',
                'messaggio': f'Energia critica: {stato.energia:.1f}%',
                'priorita': 10
            })
        elif stato.energia <= self.soglia_energia_bassa:
            allerte.append({
                'tipo': 'WARNING',
                'categoria': 'energia',
                'messaggio': f'Energia bassa: {stato.energia:.1f}%',
                'priorita': 7
            })
        
        # Temperatura alta
        if stato.temperatura >= self.temperatura_max:
            allerte.append({
                'tipo': 'CRITICO',
                'categoria': 'temperatura',
                'messaggio': f'Temperatura critica: {stato.temperatura:.1f}°C',
                'priorita': 9
            })
        elif stato.temperatura >= self.temperatura_warning:
            allerte.append({
                'tipo': 'WARNING',
                'categoria': 'temperatura',
                'messaggio': f'Temperatura alta: {stato.temperatura:.1f}°C',
                'priorita': 6
            })
        
        # CPU alta
        if stato.carico_cpu >= self.soglia_cpu_alta:
            allerte.append({
                'tipo': 'WARNING',
                'categoria': 'cpu',
                'messaggio': f'CPU alta: {stato.carico_cpu:.1f}%',
                'priorita': 5
            })
        
        # Memoria alta
        if stato.carico_memoria >= self.soglia_memoria_alta:
            allerte.append({
                'tipo': 'WARNING',
                'categoria': 'memoria',
                'messaggio': f'Memoria alta: {stato.carico_memoria:.1f}%',
                'priorita': 5
            })
        
        # Errori frequenti
        if stato.errori_recenti >= 5:
            allerte.append({
                'tipo': 'WARNING',
                'categoria': 'stabilita',
                'messaggio': f'Errori frequenti: {stato.errori_recenti} recenti',
                'priorita': 6
            })
        
        # Ordina per priorità
        allerte.sort(key=lambda x: x['priorita'], reverse=True)
        
        return allerte
    
    def _genera_raccomandazioni(self, stato: StatoInterno, 
                                allerte: List[Dict]) -> Dict[str, Any]:
        """
        Genera raccomandazioni operative
        
        Args:
            stato: Stato corrente
            allerte: Allerte attive
            
        Returns:
            Dict con raccomandazioni
        """
        raccomandazioni = {
            'modalita_risparmio': False,
            'riduzione_frequenza': 1.0,
            'disabilita_moduli': [],
            'azione_urgente': None
        }
        
        # Energia bassa -> risparmio energetico
        if stato.energia < self.soglia_energia_bassa:
            raccomandazioni['modalita_risparmio'] = True
            raccomandazioni['riduzione_frequenza'] = 0.5
            
            if stato.energia < self.soglia_energia_critica:
                raccomandazioni['azione_urgente'] = 'shutdown_graceful'
                raccomandazioni['disabilita_moduli'] = ['visione', 'udito']
        
        # Temperatura alta -> throttling
        if stato.temperatura >= self.temperatura_warning:
            raccomandazioni['riduzione_frequenza'] *= 0.7
        
        # CPU alta -> riduzione carico
        if stato.carico_cpu >= self.soglia_cpu_alta:
            raccomandazioni['riduzione_frequenza'] *= 0.8
        
        return raccomandazioni
    
    def heartbeat(self):
        """Aggiorna heartbeat (watchdog)"""
        self.ultimo_heartbeat = time.time()
    
    def check_watchdog(self) -> bool:
        """
        Verifica watchdog timeout
        
        Returns:
            bool: True se sistema responsive
        """
        elapsed = time.time() - self.ultimo_heartbeat
        if elapsed > self.timeout_heartbeat:
            print(f"[{self.nome}] ⚠️ WATCHDOG TIMEOUT! ({elapsed:.1f}s)")
            return False
        return True
    
    def ricarica_energia(self, quantita: float = 100.0):
        """
        Simula ricarica batteria
        
        Args:
            quantita: Quantità da ricaricare (%)
        """
        self.energia_corrente = min(100.0, self.energia_corrente + quantita)
        print(f"[{self.nome}] 🔋 Ricarica: {self.energia_corrente:.1f}%")
    
    def get_statistiche_sistema(self) -> Dict[str, Any]:
        """Ottieni statistiche sistema"""
        uptime_ore = (time.time() - self.tempo_avvio) / 3600
        
        return {
            'uptime_ore': uptime_ore,
            'cicli_completati': self.cicli_completati,
            'errori_totali': self.errori_totali,
            'energia_percentuale': self.energia_corrente,
            'temperatura': self.temperatura_corrente,
            'arousal': self.arousal,
            'watchdog_ok': self.check_watchdog()
        }
    
    def chiudi(self):
        """Shutdown sistema"""
        print(f"[{self.nome}] Shutdown sistema...")
        
        stats = self.get_statistiche_sistema()
        print(f"  • Uptime: {stats['uptime_ore']:.2f} ore")
        print(f"  • Cicli: {stats['cicli_completati']}")
        print(f"  • Errori: {stats['errori_totali']}")
        
        self.attivo = False
        print(f"[{self.nome}] ✅ Sistema spento")


# Istanza globale
_tronco = None

def get_instance() -> TroncoEncefalico:
    """Ottieni istanza singleton"""
    global _tronco
    if _tronco is None:
        _tronco = TroncoEncefalico()
        _tronco.inizializza()
    return _tronco


# API semplificata
def monitora_sistema(ciclo_completato: bool = False, errore: bool = False) -> Dict[str, Any]:
    """Monitora stato sistema"""
    tronco = get_instance()
    risultato = tronco.elabora({
        'ciclo_completato': ciclo_completato,
        'errore_occorso': errore
    })
    return risultato.dati


# Test del modulo
if __name__ == "__main__":
    print("="*60)
    print("🧪 Test Modulo Tronco")
    print("="*60)
    
    # Crea istanza
    tronco = TroncoEncefalico()
    tronco.inizializza()
    
    # Simula cicli
    print("\n--- Simulazione Cicli ---")
    for i in range(5):
        print(f"\nCiclo {i+1}")
        risultato = tronco.elabora({
            'ciclo_completato': True,
            'carico_cognitivo': 0.6
        })
        
        stato = risultato.dati['stato']
        print(f"  Energia: {stato.energia:.1f}%")
        print(f"  CPU: {stato.carico_cpu:.1f}%")
        print(f"  Arousal: {stato.arousal:.2f}")
        
        if risultato.dati['allerte']:
            print(f"  ⚠️ Allerte: {len(risultato.dati['allerte'])}")
            for allerta in risultato.dati['allerte']:
                print(f"    • {allerta['messaggio']}")
        
        time.sleep(0.5)
    
    # Statistiche
    print("\n--- Statistiche Sistema ---")
    stats = tronco.get_statistiche_sistema()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    tronco.chiudi()
    print("\n✅ Test completato")

