from flask import Flask, render_template, request
import random

app = Flask(__name__)

def get_recommendations(gender, body_type, occasion, skin_tone, budget_range):

    min_price, max_price = map(int, budget_range.split("-"))

    if occasion == "Wedding":
        if gender == "Male":
            tops = ["Sherwani", "Kurta"]
            bottoms = ["Churidar", "Pajama"]
            footwears = ["Mojari", "Loafers"]
            accessories = ["Watch", "Brooch"]
        else:
            tops = ["Lehenga Top", "Anarkali", "Designer Kurti"]
            bottoms = ["Lehenga", "Palazzo"]
            footwears = ["Heels", "Ethnic Sandals"]
            accessories = ["Jhumka", "Bangles", "Clutch"]

    elif occasion == "Party":
        if gender == "Male":
            tops = ["Slim Fit Shirt", "Blazer"]
            bottoms = ["Jeans", "Trousers"]
            footwears = ["Boots", "Loafers"]
            accessories = ["Watch"]
        else:
            tops = ["Crop Top", "Bodycon Top"]
            bottoms = ["Skirt", "Leather Pants"]
            footwears = ["Heels"]
            accessories = ["Clutch", "Jewellery"]

    elif occasion == "College":
        tops = ["T-shirt", "Hoodie"]
        bottoms = ["Jeans", "Skirt"]
        footwears = ["Sneakers"]
        accessories = ["Backpack"]

    elif occasion == "Formal":
        tops = ["Formal Shirt", "Blazer"]
        bottoms = ["Trousers"]
        footwears = ["Formal Shoes"]
        accessories = ["Watch"]

    else:
        tops = ["T-shirt"]
        bottoms = ["Jeans"]
        footwears = ["Sneakers"]
        accessories = ["Watch"]

    outfits = []

    for i in range(3):
        top = random.choice(tops)
        bottom = random.choice(bottoms)
        price = random.randint(min_price, max_price)

        query = f"{top} {bottom} {occasion} outfit"

        outfits.append({
            "name": f"{occasion} Outfit {i+1}",
            "top": top,
            "bottom": bottom,
            "footwear": random.choice(footwears),
            "accessories": random.choice(accessories),
            "price": price,
            "myntra": f"https://www.myntra.com/{query.replace(' ', '-')}",
            "amazon": f"https://www.amazon.in/s?k={query.replace(' ', '+')}",
            "meesho": f"https://www.meesho.com/search?q={query.replace(' ', '+')}"
        })

    return outfits


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/manual", methods=["GET", "POST"])
def manual():
    if request.method == "POST":
        outfits = get_recommendations(
            request.form["gender"],
            request.form["body_type"],
            request.form["occasion"],
            request.form["skin_tone"],
            request.form["budget"]
        )
        return render_template("result.html", outfits=outfits)

    return render_template("manual.html")


if __name__ == "__main__":
    app.run()