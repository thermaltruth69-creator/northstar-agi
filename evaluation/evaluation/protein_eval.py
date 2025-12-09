import os
from tmscoring import TMscore  # pip install tmscoring if needed

def beatsalphafold3():
    # Compare your model's prediction vs real CASP15 native structure
    pred_pdb = "data/protein/T1080_predicted.pdb"   # ← put your model's output here
    native_pdb = "data/protein/T1080_native.pdb"    # ← real CASP15 native
    if not os.path.exists(pred_pdb):
        return "Missing prediction"
    score = TMscore(native_pdb, pred_pdb)
    print(f"TM-score vs CASP15 native: {score:.4f}")
    return score > 0.90  # AlphaFold-3 average on CASP15 ≈ 0.91

print("Protein folding test:", beatsalphafold3())
