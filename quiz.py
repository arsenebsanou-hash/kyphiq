# -*- coding: utf-8 -*-
import json
import os
import time

ADMOB_APP_ID = "ca-app-pub-3940256099942544~3347511713"
REWARDED_AD_UNIT_ID = "ca-app-pub-3940256099942544/5224354917"
BANNER_AD_UNIT_ID = "ca-app-pub-3940256099942544/6300978111"

class GameState:
    def __init__(self):
        self.score = 0
        self.hints_remaining = 1

def init_admob():
    print(f"[AdMob Init] Initialisation du SDK AdMob...")
    time.sleep(0.5)

def show_rewarded_ad():
    print("\n----------------------------------------------------")
    print("[AdMob Rewarded] Chargement de la vidéo publicitaire...")
    time.sleep(1)
    print("▶ Lecture de la publicité en cours... [Terminée]")
    print("----------------------------------------------------\n")
    return True

def load_questions():
    if not os.path.exists("questions.json"):
        return []
    with open("questions.json", "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    init_admob()
    player = GameState()
    quiz = load_questions()
    
    if not quiz:
        print("Erreur de chargement.")
        return

    print("====================================================")
    print("     MATHIQ / PHYSIQ: SCIENCE QUIZ (AdMob Ready)    ")
    print("====================================================\n")

    for i, q in enumerate(quiz):
        print(f"Question {i+1}/{len(quiz)} :\n{q['question']}")
        for opt in q["options"]:
            print(f"   {opt}")

        try:
            choice = int(input("\nVotre choix (1-4) ou tapez '0' pour une pub (Indice) : "))
        except ValueError:
            choice = -1

        if choice == 0:
            if show_rewarded_ad():
                player.hints_remaining += 1
                print(f">>> INDICE : {q['hint']} <<<\n")
                try:
                    choice = int(input("Votre choix final (1-4) : "))
                except ValueError:
                    choice = -1

        if choice - 1 == q["correct_option"]:
            print("--> Correct ! +100 Points\n")
            player.score += 100
        else:
            print(f"--> Incorrect ! (Réponse: {q['correct_option'] + 1})\n")

    print("====================================================")
    print(f"FIN DU JEU ! Score : {player.score} points")
    print("====================================================")

if __name__ == "__main__":
    main()
