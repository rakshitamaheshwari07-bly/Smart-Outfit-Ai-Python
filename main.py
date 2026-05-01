from recommender import get_recommendations

def take_input():

    print("👗 Smart Outfit Recommender\n")

    gender = input("Enter Gender (Male/Female/Neutral): ")
    body_type = input("Enter Body Type (Pear/Rectangle/Inverted Triangle/Hourglass/Apple): ")
    occasion = input("Enter Occasion (College/Party/Wedding/Formal/Casual): ")
    skin_tone = input("Enter Skin Tone (Fair/Medium/Dark): ")

    print("\nSelect Budget:")
    print("1. 0-399")
    print("2. 400-999")
    print("3. 1000-3000")
    print("4. 3000-7000")

    choice = input("Enter choice (1-4): ")

    budget_map = {
        "1": "0-399",
        "2": "400-999",
        "3": "1000-3000",
        "4": "3000-7000"
    }

    budget = budget_map.get(choice, "0-999")

    return gender, body_type, occasion, skin_tone, budget


def display_outfits(outfits):

    print("\n🛍️ Recommended Outfits:\n")

    for item in outfits:
        print(f"--- {item['name']} ---")
        print(f"Top: {item['top']}")
        print(f"Bottom: {item['bottom']}")
        print(f"Footwear: {item['footwear']}")
        print(f"Accessories: {item['accessories']}")
        print(f"Price: ₹{item['price']}")
        print("Links:")
        print(f"Myntra: {item['myntra']}")
        print(f"Amazon: {item['amazon']}")
        print(f"Meesho: {item['meesho']}")
        print("\n")


if __name__ == "__main__":
    user_input = take_input()
    outfits = get_recommendations(*user_input)
    display_outfits(outfits)