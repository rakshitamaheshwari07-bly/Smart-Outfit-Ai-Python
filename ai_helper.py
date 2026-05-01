import google.generativeai as genai

# 🔑 Add your API key here
genai.configure(api_key="AIzaSyCi6LMnLDqo_KkpKC6hnr0cziw1MBuzx_E")

# Load Gemini model
model = genai.GenerativeModel("gemini-pro")


def get_ai_outfits(gender, occasion, budget):

    # 🎯 Strict prompt to control output
    prompt = f"""
    You are a fashion expert.

    Suggest ONLY outfits for a {gender}.
    Do NOT include outfits for any other gender.

    Occasion: {occasion}
    Budget: {budget}

    Give exactly 3 outfits in this format:
    Outfit 1: Top, Bottom, Footwear
    Outfit 2: Top, Bottom, Footwear
    Outfit 3: Top, Bottom, Footwear
    """

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"