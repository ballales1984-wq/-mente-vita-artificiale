"""
👁️ MODULO VISIONE - Corteccia Visiva
======================================
Simula l'elaborazione visiva usando computer vision
Equivalente: Corteccia visiva primaria (V1) e aree associative
"""

import os
from typing import List, Dict, Any, Optional
import numpy as np

# Import condizionali
try:
    from ultralytics import YOLO
    YOLO_AVAILABLE = True
except ImportError:
    YOLO_AVAILABLE = False

try:
    import cv2
    CV2_AVAILABLE = True
except ImportError:
    CV2_AVAILABLE = False


class CortecciaVisiva:
    """
    Modulo di elaborazione visiva
    Funzioni:
    - Rilevamento oggetti (YOLOv8)
    - Riconoscimento forme
    - Analisi movimento
    - Depth estimation
    """
    
    def __init__(self, model_name: str = "yolov8n.pt"):
        self.nome = "Corteccia Visiva"
        self.model_name = model_name
        self.model = None
        self.ultima_elaborazione = None
        self.attivo = False
        
        if YOLO_AVAILABLE:
            try:
                print(f"[{self.nome}] Caricamento modello {model_name}...")
                self.model = YOLO(model_name)
                self.attivo = True
                print(f"[{self.nome}] ✅ Modello caricato")
            except Exception as e:
                print(f"[{self.nome}] ⚠️ Errore caricamento: {e}")
                self.attivo = True  # Attivo comunque in modalità simulata
    
    def elabora(self, source: Any, confidenza: float = 0.5) -> Dict[str, Any]:
        """
        Elabora input visivo (immagine, video, camera)
        
        Args:
            source: Path immagine, array numpy, o indice camera
            confidenza: Soglia di confidenza per detections
            
        Returns:
            Dict con risultati elaborazione
        """
        print(f"[{self.nome}] Elaborazione input visivo...")
        
        # Carica immagine se è un path
        if isinstance(source, str):
            if not os.path.exists(source):
                return self._elaborazione_simulata(f"File non trovato: {source}")
            
            if CV2_AVAILABLE:
                immagine = cv2.imread(source)
            else:
                return self._elaborazione_simulata(source)
        else:
            immagine = source
        
        # Elaborazione reale o simulata
        if self.model is not None and immagine is not None:
            risultati = self._elaborazione_reale(immagine, confidenza)
        else:
            risultati = self._elaborazione_simulata(source)
        
        self.ultima_elaborazione = risultati
        return risultati
    
    def _elaborazione_reale(self, immagine: np.ndarray, confidenza: float) -> Dict:
        """Elaborazione con YOLO"""
        try:
            results = self.model(immagine, conf=confidenza, verbose=False)
            
            oggetti_rilevati = []
            for result in results:
                boxes = result.boxes
                for box in boxes:
                    cls = int(box.cls[0])
                    conf = float(box.conf[0])
                    coords = box.xyxy[0].tolist()
                    
                    oggetti_rilevati.append({
                        'classe': result.names[cls],
                        'confidenza': conf,
                        'bbox': coords,
                        'centro': self._calcola_centro(coords)
                    })
            
            return {
                'tipo': 'reale',
                'num_oggetti': len(oggetti_rilevati),
                'oggetti': oggetti_rilevati,
                'descrizione': self._genera_descrizione(oggetti_rilevati),
                'attenzione': self._calcola_focus(oggetti_rilevati)
            }
        except Exception as e:
            print(f"[{self.nome}] ⚠️ Errore: {e}")
            return self._elaborazione_simulata(immagine)
    
    def _elaborazione_simulata(self, source: Any) -> Dict:
        """Fallback simulato"""
        return {
            'tipo': 'simulato',
            'num_oggetti': 2,
            'oggetti': [
                {
                    'classe': 'person',
                    'confidenza': 0.85,
                    'bbox': [100, 100, 300, 400],
                    'centro': [200, 250]
                },
                {
                    'classe': 'chair',
                    'confidenza': 0.72,
                    'bbox': [350, 200, 500, 450],
                    'centro': [425, 325]
                }
            ],
            'descrizione': 'Scena indoor: persona seduta vicino a una sedia',
            'attenzione': {'focus': 'person', 'rilevanza': 0.85}
        }
    
    def _calcola_centro(self, bbox: List[float]) -> List[float]:
        """Calcola centro del bounding box"""
        return [(bbox[0] + bbox[2]) / 2, (bbox[1] + bbox[3]) / 2]
    
    def _genera_descrizione(self, oggetti: List[Dict]) -> str:
        """Genera descrizione linguistica della scena"""
        if not oggetti:
            return "Nessun oggetto rilevato"
        
        classi = [obj['classe'] for obj in oggetti]
        conteggio = {}
        for classe in classi:
            conteggio[classe] = conteggio.get(classe, 0) + 1
        
        parti = []
        for classe, count in conteggio.items():
            if count == 1:
                parti.append(f"1 {classe}")
            else:
                parti.append(f"{count} {classe}")
        
        return "Rilevati: " + ", ".join(parti)
    
    def _calcola_focus(self, oggetti: List[Dict]) -> Dict[str, Any]:
        """Determina oggetto più rilevante (attention mechanism)"""
        if not oggetti:
            return {'focus': None, 'rilevanza': 0.0}
        
        # Priorità: person > animal > vehicle > altri
        priorita = {
            'person': 1.0,
            'cat': 0.8, 'dog': 0.8,
            'car': 0.7, 'truck': 0.7,
            'chair': 0.3, 'bottle': 0.2
        }
        
        max_score = 0
        focus_obj = None
        
        for obj in oggetti:
            classe = obj['classe']
            conf = obj['confidenza']
            peso = priorita.get(classe, 0.5)
            score = conf * peso
            
            if score > max_score:
                max_score = score
                focus_obj = classe
        
        return {'focus': focus_obj, 'rilevanza': max_score}
    
    def cattura_da_camera(self, camera_id: int = 0, n_frames: int = 1) -> Optional[np.ndarray]:
        """Cattura frame da camera"""
        if not CV2_AVAILABLE:
            print(f"[{self.nome}] ⚠️ OpenCV non disponibile")
            return None
        
        cap = cv2.VideoCapture(camera_id)
        
        if not cap.isOpened():
            print(f"[{self.nome}] ⚠️ Impossibile aprire camera {camera_id}")
            return None
        
        # Scarta primi frame per stabilizzazione
        for _ in range(n_frames - 1):
            cap.read()
        
        ret, frame = cap.read()
        cap.release()
        
        if ret:
            return frame
        else:
            return None
    
    def annotazioni_visual(self, immagine: np.ndarray, risultati: Dict) -> np.ndarray:
        """Disegna annotazioni sull'immagine"""
        if not CV2_AVAILABLE:
            return immagine
        
        img_annotata = immagine.copy()
        
        for obj in risultati.get('oggetti', []):
            bbox = obj['bbox']
            classe = obj['classe']
            conf = obj['confidenza']
            
            # Bounding box
            cv2.rectangle(
                img_annotata,
                (int(bbox[0]), int(bbox[1])),
                (int(bbox[2]), int(bbox[3])),
                (0, 255, 0), 2
            )
            
            # Label
            label = f"{classe} {conf:.2f}"
            cv2.putText(
                img_annotata, label,
                (int(bbox[0]), int(bbox[1]) - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2
            )
        
        return img_annotata


# Istanza globale (pattern singleton)
_corteccia_visiva = None

def get_instance() -> CortecciaVisiva:
    """Ottieni istanza singleton"""
    global _corteccia_visiva
    if _corteccia_visiva is None:
        _corteccia_visiva = CortecciaVisiva()
    return _corteccia_visiva


# API semplificata
def elabora(source: Any, confidenza: float = 0.5) -> Dict[str, Any]:
    """Elabora input visivo"""
    return get_instance().elabora(source, confidenza)


def cattura_camera(camera_id: int = 0) -> Optional[np.ndarray]:
    """Cattura da camera"""
    return get_instance().cattura_da_camera(camera_id)


def annota(immagine: np.ndarray, risultati: Dict) -> np.ndarray:
    """Aggiungi annotazioni visive"""
    return get_instance().annotazioni_visual(immagine, risultati)


# Test del modulo
if __name__ == "__main__":
    print("="*60)
    print("🧪 Test Modulo Visione")
    print("="*60)
    
    corteccia = CortecciaVisiva()
    
    # Test elaborazione simulata
    risultati = corteccia.elabora("immagine_test.jpg")
    
    print(f"\nRisultati:")
    print(f"  Tipo: {risultati['tipo']}")
    print(f"  Oggetti rilevati: {risultati['num_oggetti']}")
    print(f"  Descrizione: {risultati['descrizione']}")
    print(f"  Focus: {risultati['attenzione']}")
    
    print("\n✅ Test completato")

