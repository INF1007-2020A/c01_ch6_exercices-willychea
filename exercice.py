#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> bool:
    if values is None:
        values = [input("Entrez vos valeurs") for _ in range(10)]

    return values == sorted(values)
        


def anagrams(words: list = None) -> bool:
    if words is None:
        words = [sorted(input()), sorted(input())]

    return words[0] == words[1]


def contains_doubles(items: list) -> bool:
    uniques = set (items)

    return len(items) == len(uniques) 
        

def best_grades(student_grades: dict) -> dict:
    list_student, list_grades = [], []
    nom, note = None, None

    for student in student_grades:
        student_grades[student] = sum(student_grades[student]) / len(student_grades[student])
        list_student.append(student)
        list_grades.append(student_grades[student])
        print (list_student, list_grades)

    for student in range(len(list_student)):
        if list_grades[student] > list_grades[student-1]:
            nom = list_student[student]
            note = list_grades[student]
    
    return nom, note

def histogram(sentence: str) -> tuple:
    hist = {}

    for charac in sentence:
        if charac in hist:
            hist[charac] += 1
        
        else : 
            hist[charac] = 1 

    threshold = 5 
    most_frequent = []
    for k in hist: 
        if hist(k) > threshold and hist(k) != ' ': 
            most_frequent.append(k)

    #most_frequent = [k for k, v in hist.items() if v > threshold and k != ' ']

    return hist, most_frequent


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingrédients et enregistrer dans une structure de données 
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    print(order())

    print(f"On vérifie les anagrammes...")
    print(anagrams())

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste ne contient pas de doublons. {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    name, result = best_grades(grades)
    print(f"{name} a la meilleure moyenne: {result}")

    sentence = input('Donnez une phrase:')
    print(type(histogram(sentence)))
    print(histogram(sentence))

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
