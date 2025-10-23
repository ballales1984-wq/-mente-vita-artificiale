"""
🧠 MENTE ARTIFICIALE MODULARE
================================
Simulazione di un'architettura cognitiva ispirata al cervello umano.
Sistema modulare con flusso continuo di dati, decisioni, feedback ed energia.
"""

import time
import random
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum
import json


# ==================== STRUTTURE DATI ====================

class StatoEmotivo(Enum):
    """Stati emotivi base dell'agente"""
    NEUTRO = "neutro"
    POSITIVO = "positivo"
    NEGATIVO = "negativo"
    ALLERTA = "allerta"
    CALMO = "calmo"


@dataclass
class DatoSensoriale:
    """Dati grezzi dai sensori"""
    tipo: str  # visivo, uditivo, tattile, propriocettivo
    contenuto: Any
    timestamp: float
    priorita: int = 1


@dataclass
class PercezioneElaborata:
    """Percezione processata e interpretata"""
    tipo: str
    descrizione: str
    entita: List[str]
    rilevanza: float
    timestamp: float


@dataclass
class Memoria:
    """Singola memoria episodica"""
    contenuto: str
    contesto: Dict[str, Any]
    valenza_emotiva: float
    timestamp: float
    accessi: int = 0


@dataclass
class StatoInterno:
    """Stato interno del sistema"""
    energia: float = 100.0  # percentuale batteria
    temperatura: float = 45.0  # temperatura CPU
    carico_cognitivo: float = 0.3  # utilizzo risorse
    stato_emotivo: StatoEmotivo = StatoEmotivo.NEUTRO
    allerta: float = 0.5  # livello di vigilanza


# ==================== MODULI CEREBRALI ====================

class CortecciaVisiva:
    """Elaborazione delle informazioni visive"""
    
    def __init__(self):
        self.nome = "Corteccia Visiva"
        self.buffer_frames = []
        
    def processa(self, dato: DatoSensoriale) -> List[PercezioneElaborata]:
        """Simula CNN per riconoscimento oggetti"""
        print(f"  🔵 [{self.nome}] Elaborazione immagine...")
        
        percezioni = []
        if "persona" in dato.contenuto.lower():
            percezioni.append(PercezioneElaborata(
                tipo="visivo",
                descrizione="Persona rilevata",
                entita=["persona", "movimento"],
                rilevanza=0.8,
                timestamp=time.time()
            ))
        
        if "veicolo" in dato.contenuto.lower():
            percezioni.append(PercezioneElaborata(
                tipo="visivo",
                descrizione="Veicolo in movimento",
                entita=["veicolo", "pericolo_potenziale"],
                rilevanza=0.9,
                timestamp=time.time()
            ))
            
        return percezioni


class CortecciaUditiva:
    """Elaborazione delle informazioni uditive"""
    
    def __init__(self):
        self.nome = "Corteccia Uditiva"
        
    def processa(self, dato: DatoSensoriale) -> List[PercezioneElaborata]:
        """Simula modello Whisper + analisi semantica"""
        print(f"  🔵 [{self.nome}] Trascrizione audio...")
        
        audio = dato.contenuto
        
        # Analisi tono
        tono = "amichevole"
        if any(word in audio.lower() for word in ["aiuto", "urgente", "pericolo"]):
            tono = "urgente"
        
        percezione = PercezioneElaborata(
            tipo="uditivo",
            descrizione=f"Comando vocale: '{audio}' (tono: {tono})",
            entita=["voce_umana", "comando", tono],
            rilevanza=0.85,
            timestamp=time.time()
        )
        
        return [percezione]


class Talamo:
    """Router centrale - smista informazioni sensoriali"""
    
    def __init__(self):
        self.nome = "Talamo"
        self.corteccia_visiva = CortecciaVisiva()
        self.corteccia_uditiva = CortecciaUditiva()
        
    def smista(self, dati: List[DatoSensoriale]) -> List[PercezioneElaborata]:
        """Smista i dati sensoriali ai moduli appropriati"""
        print(f"\n⚡ [{self.nome}] Routing informazioni sensoriali...")
        
        percezioni = []
        
        for dato in dati:
            if dato.tipo == "visivo":
                percezioni.extend(self.corteccia_visiva.processa(dato))
            elif dato.tipo == "uditivo":
                percezioni.extend(self.corteccia_uditiva.processa(dato))
                
        return percezioni


class Ippocampo:
    """Sistema di memoria episodica e semantica"""
    
    def __init__(self):
        self.nome = "Ippocampo"
        self.memoria_episodica: List[Memoria] = []
        self.memoria_semantica: Dict[str, Any] = {
            "voce_operatore": {
                "caratteristiche": "tono medio, cadenza regolare",
                "affidabilita": 0.95
            },
            "comandi_noti": ["vieni qui", "fermati", "seguimi", "aspetta"]
        }
        
    def memorizza(self, contenuto: str, contesto: Dict, valenza: float):
        """Memorizza un nuovo evento"""
        memoria = Memoria(
            contenuto=contenuto,
            contesto=contesto,
            valenza_emotiva=valenza,
            timestamp=time.time()
        )
        self.memoria_episodica.append(memoria)
        print(f"  💾 [{self.nome}] Memorizzato: {contenuto[:50]}...")
        
    def richiama(self, query: str) -> Optional[Memoria]:
        """Recupera memoria simile"""
        # Simulazione semplice di ricerca semantica
        for memoria in reversed(self.memoria_episodica):
            if query.lower() in memoria.contenuto.lower():
                memoria.accessi += 1
                return memoria
        return None
    
    def conosco_voce(self, descrizione: str) -> bool:
        """Verifica se una voce è nota"""
        return "operatore" in descrizione.lower()


class Amigdala:
    """Sistema di valutazione emotiva e reward"""
    
    def __init__(self):
        self.nome = "Amigdala"
        self.stato_corrente = StatoEmotivo.NEUTRO
        self.reward_history = []
        
    def valuta(self, percezioni: List[PercezioneElaborata], memoria: Ippocampo) -> StatoEmotivo:
        """Valuta valenza emotiva della situazione"""
        print(f"\n❤️  [{self.nome}] Valutazione emotiva...")
        
        punteggio_valenza = 0.0
        
        for p in percezioni:
            if "pericolo" in p.entita:
                punteggio_valenza -= 0.5
            if "amichevole" in p.entita or "urgente" in p.entita:
                punteggio_valenza += 0.3
            if "voce_umana" in p.entita and memoria.conosco_voce(p.descrizione):
                punteggio_valenza += 0.4
                
        if punteggio_valenza > 0.3:
            self.stato_corrente = StatoEmotivo.POSITIVO
        elif punteggio_valenza < -0.3:
            self.stato_corrente = StatoEmotivo.NEGATIVO
        else:
            self.stato_corrente = StatoEmotivo.NEUTRO
            
        print(f"  💚 Stato emotivo: {self.stato_corrente.value} (valenza: {punteggio_valenza:.2f})")
        return self.stato_corrente
    
    def reward(self, azione: str, successo: bool) -> float:
        """Sistema di rinforzo"""
        reward_value = 1.0 if successo else -0.5
        self.reward_history.append((azione, reward_value, time.time()))
        print(f"  🎁 Reward: {reward_value:+.2f} per azione '{azione}'")
        return reward_value


class CortecciaPrefrontale:
    """Centro decisionale e pianificazione"""
    
    def __init__(self, ippocampo: Ippocampo, amigdala: Amigdala):
        self.nome = "Corteccia Prefrontale"
        self.ippocampo = ippocampo
        self.amigdala = amigdala
        self.obiettivo_corrente = None
        
    def analizza_e_decidi(self, percezioni: List[PercezioneElaborata]) -> Dict[str, Any]:
        """Ragionamento di alto livello e decision making"""
        print(f"\n🧠 [{self.nome}] Analisi e pianificazione...")
        
        # Consulta memoria
        for p in percezioni:
            if p.tipo == "uditivo" and "comando" in p.entita:
                memoria_simile = self.ippocampo.richiama("comando vocale")
                if memoria_simile:
                    print(f"  📖 Memoria simile trovata (accessi: {memoria_simile.accessi})")
        
        # Decisione basata su percezioni e stato emotivo
        decisione = {
            "azione": "avvicinati_con_cautela",
            "parametri": {
                "direzione": "sinistra",
                "angolo": 40,
                "velocita": 0.5,
                "modalita": "cautela"
            },
            "ragionamento": "Voce conosciuta, nessun pericolo rilevato. Azione appropriata.",
            "priorita": 0.7
        }
        
        # Verifica stato emotivo
        if self.amigdala.stato_corrente == StatoEmotivo.NEGATIVO:
            decisione["parametri"]["velocita"] = 0.2
            decisione["parametri"]["modalita"] = "alta_cautela"
            
        print(f"  ✅ Decisione: {decisione['azione']}")
        print(f"  📊 Ragionamento: {decisione['ragionamento']}")
        
        return decisione


class CortecciaMotoria:
    """Esecuzione dei comandi motori"""
    
    def __init__(self):
        self.nome = "Corteccia Motoria"
        self.posizione_corrente = {"x": 0, "y": 0, "theta": 0}
        
    def esegui(self, decisione: Dict[str, Any]) -> bool:
        """Esegue azione motoria"""
        print(f"\n🦿 [{self.nome}] Esecuzione azione: {decisione['azione']}")
        
        params = decisione["parametri"]
        
        # Simulazione movimento
        print(f"  ⚙️  Ruota di {params['angolo']}° verso {params['direzione']}")
        time.sleep(0.3)
        
        print(f"  🏃 Avanzamento a {params['velocita']} m/s")
        time.sleep(0.5)
        
        # Feedback sensori
        print(f"  📡 Sensori prossimità: OK")
        print(f"  📡 Accelerometro: movimento fluido")
        
        return True


class Cervelletto:
    """Coordinazione fine e equilibrio"""
    
    def __init__(self):
        self.nome = "Cervelletto"
        
    def stabilizza(self, stato_movimento: Dict) -> Dict:
        """Regola equilibrio e movimenti fini"""
        print(f"  🌀 [{self.nome}] Correzione equilibrio...")
        
        # Simulazione PID controller
        correzioni = {
            "pitch": 0.02,
            "roll": -0.01,
            "yaw": 0.0
        }
        
        return correzioni


class SistemaReticolare:
    """Regolazione arousal e veglia"""
    
    def __init__(self):
        self.nome = "Sistema Reticolare"
        
    def monitora(self, stato: StatoInterno) -> StatoInterno:
        """Monitora e regola lo stato interno"""
        print(f"\n🌙 [{self.nome}] Monitoraggio stato interno...")
        
        # Degrado energia (simulato)
        stato.energia -= 0.5
        
        print(f"  🔋 Energia: {stato.energia:.1f}%")
        print(f"  🌡️  Temperatura: {stato.temperatura:.1f}°C")
        print(f"  🧮 Carico cognitivo: {stato.carico_cognitivo:.1%}")
        
        # Gestione allerta
        if stato.energia < 25:
            print(f"  ⚠️  ALERT: Energia bassa, considerare risparmio energetico")
            stato.allerta = 0.8
            
        return stato


# ==================== MENTE ARTIFICIALE ====================

class MenteArtificiale:
    """Architettura cognitiva completa"""
    
    def __init__(self):
        self.nome = "Mente Artificiale Modulare"
        
        # Inizializzazione moduli
        self.talamo = Talamo()
        self.ippocampo = Ippocampo()
        self.amigdala = Amigdala()
        self.prefrontale = CortecciaPrefrontale(self.ippocampo, self.amigdala)
        self.motoria = CortecciaMotoria()
        self.cervelletto = Cervelletto()
        self.sistema_reticolare = SistemaReticolare()
        
        # Stato interno
        self.stato = StatoInterno()
        
        print(f"\n{'='*60}")
        print(f"✨ {self.nome} - INIZIALIZZATA")
        print(f"{'='*60}")
        
    def ciclo_cognitivo(self, dati_sensoriali: List[DatoSensoriale]):
        """Esegue un ciclo completo di elaborazione cognitiva"""
        
        print(f"\n{'='*60}")
        print(f"🔄 NUOVO CICLO COGNITIVO")
        print(f"{'='*60}")
        
        # 1. PERCEZIONE: Elaborazione sensoriale
        percezioni = self.talamo.smista(dati_sensoriali)
        
        # 2. EMOZIONE: Valutazione affettiva
        stato_emotivo = self.amigdala.valuta(percezioni, self.ippocampo)
        self.stato.stato_emotivo = stato_emotivo
        
        # 3. COGNIZIONE: Analisi e decisione
        decisione = self.prefrontale.analizza_e_decidi(percezioni)
        
        # 4. AZIONE: Esecuzione motoria
        successo = self.motoria.esegui(decisione)
        
        # 5. COORDINAZIONE: Stabilizzazione
        self.cervelletto.stabilizza({"movimento": "avanzamento"})
        
        # 6. MEMORIA: Memorizzazione episodio
        self.ippocampo.memorizza(
            contenuto=f"Azione: {decisione['azione']} - Successo: {successo}",
            contesto={"percezioni": len(percezioni), "stato": stato_emotivo.value},
            valenza=0.8 if successo else -0.2
        )
        
        # 7. APPRENDIMENTO: Rinforzo
        reward = self.amigdala.reward(decisione['azione'], successo)
        
        # 8. AUTOREGOLAZIONE: Monitoraggio interno
        self.stato = self.sistema_reticolare.monitora(self.stato)
        
        print(f"\n{'='*60}")
        print(f"✅ CICLO COMPLETATO")
        print(f"{'='*60}\n")
        
        return decisione, successo


# ==================== SIMULAZIONE ====================

def scenario_urbano():
    """
    Scenario: Robot autonomo in ambiente urbano riceve comando vocale
    """
    
    print("\n" + "="*60)
    print("🤖 SCENARIO: ROBOT AUTONOMO IN AMBIENTE URBANO")
    print("="*60)
    
    # Inizializza la mente
    mente = MenteArtificiale()
    
    time.sleep(1)
    
    # Simula input sensoriali multipli
    input_scenario = [
        DatoSensoriale(
            tipo="visivo",
            contenuto="Persona in avvicinamento da sinistra, distanza 2.3m, movimento lento",
            timestamp=time.time(),
            priorita=2
        ),
        DatoSensoriale(
            tipo="uditivo",
            contenuto="Ehi, vieni qui!",
            timestamp=time.time(),
            priorita=3
        ),
        DatoSensoriale(
            tipo="visivo",
            contenuto="Veicolo in movimento sulla strada principale, distanza 15m",
            timestamp=time.time(),
            priorita=2
        )
    ]
    
    # Esegui ciclo cognitivo
    decisione, successo = mente.ciclo_cognitivo(input_scenario)
    
    # Report finale
    print("\n" + "="*60)
    print("📊 REPORT FINALE")
    print("="*60)
    print(f"Memorie episodiche: {len(mente.ippocampo.memoria_episodica)}")
    print(f"Stato emotivo finale: {mente.stato.stato_emotivo.value}")
    print(f"Energia residua: {mente.stato.energia:.1f}%")
    print(f"Reward totale: {sum(r[1] for r in mente.amigdala.reward_history):.2f}")
    print("="*60)
    
    return mente


def scenario_multiplo():
    """Simula più cicli cognitivi consecutivi"""
    
    print("\n" + "="*60)
    print("🔄 SCENARIO ESTESO: SEQUENZA DI EVENTI")
    print("="*60)
    
    mente = MenteArtificiale()
    
    scenari = [
        {
            "nome": "Evento 1: Comando vocale",
            "dati": [
                DatoSensoriale("uditivo", "Seguimi", time.time(), 3),
                DatoSensoriale("visivo", "Persona frontale, distanza 1.5m", time.time(), 2)
            ]
        },
        {
            "nome": "Evento 2: Ostacolo imprevisto",
            "dati": [
                DatoSensoriale("visivo", "Veicolo in rapido avvicinamento!", time.time(), 5),
                DatoSensoriale("uditivo", "Clacson veicolo", time.time(), 4)
            ]
        },
        {
            "nome": "Evento 3: Situazione calma",
            "dati": [
                DatoSensoriale("visivo", "Ambiente tranquillo, nessun movimento", time.time(), 1),
                DatoSensoriale("uditivo", "Silenzio ambientale", time.time(), 1)
            ]
        }
    ]
    
    for scenario in scenari:
        print(f"\n\n{'#'*60}")
        print(f"📍 {scenario['nome']}")
        print(f"{'#'*60}")
        time.sleep(1)
        mente.ciclo_cognitivo(scenario['dati'])
        time.sleep(0.5)
    
    # Report conclusivo
    print("\n\n" + "="*60)
    print("📈 ANALISI COMPORTAMENTO ESTESO")
    print("="*60)
    print(f"Cicli cognitivi eseguiti: {len(scenari)}")
    print(f"Memorie accumulate: {len(mente.ippocampo.memoria_episodica)}")
    print(f"Energia finale: {mente.stato.energia:.1f}%")
    print(f"\n📚 Storia emotiva:")
    for i, (azione, reward, _) in enumerate(mente.amigdala.reward_history, 1):
        print(f"  {i}. {azione}: reward {reward:+.2f}")
    print("="*60)


# ==================== MAIN ====================

if __name__ == "__main__":
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║                                                            ║
    ║           🧠 MENTE ARTIFICIALE MODULARE 🧠                ║
    ║                                                            ║
    ║     Simulazione di architettura cognitiva ispirata        ║
    ║              al cervello biologico umano                   ║
    ║                                                            ║
    ╚════════════════════════════════════════════════════════════╝
    """)
    
    print("\nScegli lo scenario da eseguire:")
    print("1. Scenario singolo (robot riceve comando vocale)")
    print("2. Scenario multiplo (sequenza di eventi)")
    print("3. Esegui entrambi")
    
    scelta = input("\nScelta (1/2/3): ").strip()
    
    if scelta == "1":
        scenario_urbano()
    elif scelta == "2":
        scenario_multiplo()
    elif scelta == "3":
        scenario_urbano()
        time.sleep(2)
        scenario_multiplo()
    else:
        print("Scelta non valida, eseguo scenario singolo...")
        scenario_urbano()
    
    print("\n✨ Simulazione completata!")

