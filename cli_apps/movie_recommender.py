"""Web Series Recommendation Engine.

Refactors, fixes, and completes moviedata.txt and webseries.txt.
Loads dataset from data/webseries.json and uses Euclidean Distance similarity scores
to find similar users and recommend unwatched series.
"""

import json
import os
import math
from typing import Dict, List, Tuple


def load_dataset() -> Dict[str, Dict[str, float]]:
    """Load webseries ratings dataset from the data directory.
    
    Uses dynamic path resolution.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", "webseries.json")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset not found at: {file_path}")
        
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def euclidean_similarity(dataset: Dict[str, Dict[str, float]], person1: str, person2: str) -> float:
    """Calculate the Euclidean distance similarity score between person1 and person2.
    
    Returns a score between 0 (no similarity) and 1 (identical ratings).
    """
    if person1 not in dataset or person2 not in dataset:
        return 0.0
        
    # Get shared items
    shared_items = [item for item in dataset[person1] if item in dataset[person2]]
    
    if len(shared_items) == 0:
        return 0.0
        
    # Sum of squared differences
    sum_of_squares = sum(
        (dataset[person1][item] - dataset[person2][item]) ** 2 
        for item in shared_items
    )
    
    # Return Euclidean distance similarity score
    return 1.0 / (1.0 + math.sqrt(sum_of_squares))


def get_similar_users(dataset: Dict[str, Dict[str, float]], person: str) -> List[Tuple[str, float]]:
    """Find the most similar users to a given person."""
    if person not in dataset:
        return []
        
    scores = [
        (other, euclidean_similarity(dataset, person, other))
        for other in dataset if other != person
    ]
    
    # Sort by similarity score in descending order
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores


def get_recommendations(dataset: Dict[str, Dict[str, float]], person: str) -> List[Tuple[str, float]]:
    """Get recommendations for a person based on weighted ratings of similar users."""
    if person not in dataset:
        return []
        
    totals: Dict[str, float] = {}
    sim_sums: Dict[str, float] = {}
    
    for other in dataset:
        if other == person:
            continue
            
        sim = euclidean_similarity(dataset, person, other)
        if sim <= 0:
            continue
            
        for item in dataset[other]:
            # Recommend only items the person has not rated yet
            if item not in dataset[person] or dataset[person][item] == 0:
                totals.setdefault(item, 0.0)
                totals[item] += dataset[other][item] * sim
                sim_sums.setdefault(item, 0.0)
                sim_sums[item] += sim
                
    # Create normalized list
    rankings = [
        (item, round(total / sim_sums[item], 2))
        for item, total in totals.items()
    ]
    
    # Sort rankings in descending order of score
    rankings.sort(key=lambda x: x[1], reverse=True)
    return rankings


def run_app() -> None:
    """Main execution of the Movie Recommender App."""
    print("=" * 45)
    print("Movie/Webseries Recommender".center(45))
    print("=" * 45)
    
    try:
        dataset = load_dataset()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please check that data/webseries.json exists.")
        return

    users = list(dataset.keys())
    print("\nAvailable Users in Database:")
    print(", ".join(users))
    
    print("\nSelect an action:")
    print("1. Find Similar Users")
    print("2. Get Show Recommendations")
    
    action = input("Enter choice (1-2): ").strip()
    if action not in ['1', '2']:
        print("Invalid choice.")
        return
        
    user_name = input("Enter user's name from list above: ").strip()
    # Handle casing tolerance
    matched_user = next((u for u in users if u.lower() == user_name.lower()), None)
    
    if not matched_user:
        print("User not found in dataset.")
        return

    if action == '1':
        print(f"\nComputing user similarity scores for {matched_user}...")
        similar_users = get_similar_users(dataset, matched_user)
        print("\nSimilar Users (Euclidean Similarity):")
        for other, score in similar_users:
            percent = round(score * 100, 1)
            print(f" - {other}: {percent}% match similarity")
            
    elif action == '2':
        print(f"\nGenerating recommendations for {matched_user}...")
        recommendations = get_recommendations(dataset, matched_user)
        if recommendations:
            print("\nRecommended Shows:")
            for item, score in recommendations:
                print(f" - {item} (Predicted Rating: {score}/5)")
        else:
            print(f"\nNo recommendations available for {matched_user} (they might have already watched all shows).")


if __name__ == "__main__":
    run_app()
