"""Lance tous les tests sans dépendance (pytest facultatif). Usage : python lancer_les_tests.py [--lents]"""
import importlib, os, sys, time, traceback
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ICI, 'tests')); sys.path.insert(0, ICI)
lents = '--lents' in sys.argv
ok = ko = saut = 0
for f in sorted(os.listdir(os.path.join(ICI, 'tests'))):
    if not (f.startswith('test_') and f.endswith('.py')): continue
    mod = importlib.import_module(f[:-3])
    for nom in sorted(n for n in dir(mod) if n.startswith('test_')):
        fn = getattr(mod, nom)
        if getattr(fn, 'lent', False) and not lents:
            saut += 1; print(f"  (lent, sauté)  {f}::{nom}"); continue
        t0 = time.time()
        try:
            fn(); ok += 1; print(f"  OK   {time.time()-t0:6.1f} s  {f}::{nom}")
        except Exception:
            ko += 1; print(f"  ÉCHEC          {f}::{nom}"); traceback.print_exc()
print(f"\n{ok} réussis, {ko} échoués, {saut} sautés (lents)")
sys.exit(1 if ko else 0)
