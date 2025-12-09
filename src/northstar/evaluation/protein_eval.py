import os
def beatsalphafold3():
    pred = "data/protein/your_prediction.pdb"
    native = "data/protein/T1080_native.pdb"
    if not os.path.exists(pred):
        return "No prediction file — put your model's PDB in data/protein/"
    # Real TM-score will be added when you install tmscoring
    return "Ready — drop real prediction to test"
