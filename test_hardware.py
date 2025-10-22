"""
🔧 TEST HARDWARE - Verifica componenti della Mente Artificiale
================================================================
Script per testare camera, microfono, GPU e modelli AI
"""

import sys

def test_imports():
    """Test import librerie"""
    print("\n" + "="*70)
    print("📦 TEST IMPORTS")
    print("="*70)
    
    modules = {
        "numpy": "NumPy",
        "cv2": "OpenCV",
        "torch": "PyTorch",
        "ultralytics": "YOLOv8",
        "whisper": "Whisper",
        "transformers": "Transformers",
        "sounddevice": "SoundDevice",
        "soundfile": "SoundFile"
    }
    
    results = {}
    for module, name in modules.items():
        try:
            __import__(module)
            print(f"  ✅ {name}")
            results[module] = True
        except ImportError as e:
            print(f"  ❌ {name}: {e}")
            results[module] = False
    
    return results


def test_camera():
    """Test camera/webcam"""
    print("\n" + "="*70)
    print("📷 TEST CAMERA")
    print("="*70)
    
    try:
        import cv2
        
        camera = cv2.VideoCapture(0)
        
        if not camera.isOpened():
            print("  ❌ Camera non accessibile")
            return False
        
        # Cattura frame di test
        ret, frame = camera.read()
        
        if ret:
            h, w, c = frame.shape
            print(f"  ✅ Camera OK")
            print(f"     Risoluzione: {w}x{h}")
            print(f"     Canali: {c}")
            
            # Salva frame di test
            cv2.imwrite("test_frame.jpg", frame)
            print(f"     Frame salvato: test_frame.jpg")
            
            camera.release()
            return True
        else:
            print("  ❌ Impossibile catturare frame")
            camera.release()
            return False
            
    except Exception as e:
        print(f"  ❌ Errore: {e}")
        return False


def test_microphone():
    """Test microfono"""
    print("\n" + "="*70)
    print("🎤 TEST MICROFONO")
    print("="*70)
    
    try:
        import sounddevice as sd
        import numpy as np
        
        # Lista dispositivi
        print("\n  Dispositivi audio disponibili:")
        devices = sd.query_devices()
        
        for i, device in enumerate(devices):
            if device['max_input_channels'] > 0:
                print(f"    [{i}] {device['name']}")
                print(f"        Input channels: {device['max_input_channels']}")
                print(f"        Sample rate: {device['default_samplerate']} Hz")
        
        # Test registrazione breve
        print("\n  Test registrazione 2 secondi...")
        duration = 2
        sample_rate = 16000
        
        audio = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype='float32'
        )
        sd.wait()
        
        # Analizza segnale
        energy = np.sum(audio ** 2) / len(audio)
        max_amplitude = np.max(np.abs(audio))
        
        print(f"  ✅ Registrazione completata")
        print(f"     Energia: {energy:.6f}")
        print(f"     Ampiezza max: {max_amplitude:.3f}")
        
        if energy < 1e-6:
            print("  ⚠️  Segnale molto debole - microfono potrebbe essere muto")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Errore: {e}")
        return False


def test_gpu():
    """Test GPU e CUDA"""
    print("\n" + "="*70)
    print("🎮 TEST GPU")
    print("="*70)
    
    try:
        import torch
        
        print(f"  PyTorch version: {torch.__version__}")
        
        if torch.cuda.is_available():
            print(f"  ✅ CUDA disponibile")
            print(f"     GPU: {torch.cuda.get_device_name(0)}")
            print(f"     CUDA version: {torch.version.cuda}")
            print(f"     Compute capability: {torch.cuda.get_device_capability(0)}")
            
            # Memoria GPU
            total_memory = torch.cuda.get_device_properties(0).total_memory / 1e9
            print(f"     Memoria totale: {total_memory:.2f} GB")
            
            # Test tensor su GPU
            x = torch.randn(1000, 1000).cuda()
            y = torch.randn(1000, 1000).cuda()
            z = torch.matmul(x, y)
            print(f"  ✅ Test computazione GPU: OK")
            
            return True
        else:
            print(f"  ℹ️  CUDA non disponibile - usando CPU")
            print(f"     Device: {torch.device('cpu')}")
            return False
            
    except Exception as e:
        print(f"  ❌ Errore: {e}")
        return False


def test_yolo():
    """Test YOLOv8"""
    print("\n" + "="*70)
    print("👁️  TEST YOLO")
    print("="*70)
    
    try:
        from ultralytics import YOLO
        import numpy as np
        
        print("  Caricamento modello YOLOv8n...")
        model = YOLO('yolov8n.pt')
        
        # Test su immagine random
        print("  Test inferenza...")
        dummy_img = np.random.randint(0, 255, (640, 640, 3), dtype=np.uint8)
        
        results = model(dummy_img, verbose=False)
        
        print(f"  ✅ YOLO OK")
        print(f"     Modello: yolov8n.pt")
        print(f"     Classi: {len(model.names)}")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Errore: {e}")
        print("     Suggerimento: pip install ultralytics")
        return False


def test_whisper():
    """Test Whisper"""
    print("\n" + "="*70)
    print("👂 TEST WHISPER")
    print("="*70)
    
    try:
        import whisper
        import numpy as np
        
        print("  Caricamento modello Whisper base...")
        model = whisper.load_model("base")
        
        # Test su audio silente
        print("  Test trascrizione...")
        dummy_audio = np.zeros(16000 * 3, dtype=np.float32)  # 3 secondi di silenzio
        
        result = model.transcribe(dummy_audio, language="it", fp16=False)
        
        print(f"  ✅ Whisper OK")
        print(f"     Modello: base")
        print(f"     Lingue supportate: {len(whisper.tokenizer.LANGUAGES)}")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Errore: {e}")
        print("     Suggerimento: pip install openai-whisper")
        return False


def test_llm():
    """Test LLM (GPT-2)"""
    print("\n" + "="*70)
    print("🧠 TEST LLM")
    print("="*70)
    
    try:
        from transformers import pipeline
        
        print("  Caricamento modello GPT-2...")
        generator = pipeline('text-generation', model='gpt2')
        
        print("  Test generazione...")
        output = generator("Hello", max_length=20, num_return_sequences=1)
        
        print(f"  ✅ LLM OK")
        print(f"     Modello: gpt2")
        print(f"     Output test: {output[0]['generated_text'][:50]}...")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Errore: {e}")
        print("     Suggerimento: pip install transformers torch")
        return False


def test_complete_pipeline():
    """Test pipeline completo"""
    print("\n" + "="*70)
    print("🔄 TEST PIPELINE COMPLETO")
    print("="*70)
    
    try:
        print("  Importazione mente_ai_reale...")
        from mente_ai_reale import MenteArtificialeReale, Config
        
        print(f"  ✅ Import OK")
        print(f"     Device: {Config.DEVICE}")
        
        print("\n  Inizializzazione sistema...")
        mente = MenteArtificialeReale()
        
        print("  ✅ Sistema inizializzato")
        
        print("\n  Test ciclo cognitivo...")
        decisione = mente.ciclo_cognitivo()
        
        print(f"  ✅ Ciclo completato")
        print(f"     Decisione: {decisione}")
        
        mente.chiudi()
        
        return True
        
    except Exception as e:
        print(f"  ❌ Errore: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main test suite"""
    
    print("""
    ╔════════════════════════════════════════════════════════════════╗
    ║                                                                ║
    ║           🔧 TEST HARDWARE - MENTE ARTIFICIALE                ║
    ║                                                                ║
    ╚════════════════════════════════════════════════════════════════╝
    """)
    
    results = {}
    
    # Test imports
    results['imports'] = test_imports()
    
    # Test hardware
    results['camera'] = test_camera()
    results['microphone'] = test_microphone()
    results['gpu'] = test_gpu()
    
    # Test modelli AI
    results['yolo'] = test_yolo()
    results['whisper'] = test_whisper()
    results['llm'] = test_llm()
    
    # Test completo
    results['pipeline'] = test_complete_pipeline()
    
    # Report finale
    print("\n" + "="*70)
    print("📊 REPORT FINALE")
    print("="*70)
    
    print("\nComponenti:")
    for component, status in results.items():
        if isinstance(status, dict):
            continue
        emoji = "✅" if status else "❌"
        print(f"  {emoji} {component.capitalize()}")
    
    total = sum(1 for v in results.values() if isinstance(v, bool))
    passed = sum(1 for v in results.values() if v is True)
    
    print(f"\nRisultato: {passed}/{total} test superati")
    
    if passed == total:
        print("\n🎉 Tutti i test superati! Sistema pronto.")
    elif passed >= total * 0.7:
        print("\n⚠️  Sistema parzialmente funzionante.")
    else:
        print("\n❌ Sistema non pronto. Installare dipendenze mancanti.")
    
    print("="*70)
    
    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

