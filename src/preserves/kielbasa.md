# 🍖 Kielbasa

Recipe from [Ethan
Chlebowski](https://www.ethanchlebowski.com/cooking-techniques-recipes/how-to-make-polish-kielbasa)

## Ingredients

### Ingredients by percentage

All ingredients are % of meat; for 1000g meat, 1.75% = 17.5g.

- 70% Lean / 30 % Fat Pork Meat (or beef, venison, etc.)
- 1.75% Salt
- 1.75% Brown Sugar
- 0.5% Black Pepper
- 0.25% Cure #1
- 0.187% Garlic Powder
- 0.125% Whole Mustard Seed
- 0.0625% Pickling Spice*
- 0.0313% Marjoram
- Water
- Sausage Casings

*For the pickling spice, I didn't have any on hand so I cobbled up the
following:

Equal parts:

- dried bay leaves
- allspice berries (or powdered) (can sub junpier berries)
- coriander seeds (or powdered)
- ground ginger

Toast the whole spices in a dry pan, then roughly grind them in a mortar and
pestle or spice grinder.

Other optional spices are cardamom, star anise, cinnamon.

I also increased the mustard seed a touch because I like it.

### Ingredients calculator

It's really important to get the salt and cure quantities precise; the spices
are definitely flexible.

<li><input type="text" id="meat_grams" size="3" /> grams of 70% Lean / 30 % Fat Pork Meat (or beef, venison, etc.)</li>

<li><b id="Salt">?</b> Salt</li>
<li><b id="Brown Sugar">?</b> Brown Sugar</li>
<li><b id="Black Pepper">?</b> Black Pepper</li>
<li><b id="Cure #1">?</b> Cure #1</li>
<li><b id="Garlic Powder">?</b> Garlic Powder</li>
<li><b id="Whole Mustard Seed">?</b> Whole Mustard Seed</li>
<li><b id="Pickling Spice">?</b> Pickling Spice</li>
<li><b id="Marjoram">?</b> Marjoram</li>
<li>Water</li>
<li>Sausage Casings</li>

<script type="text/javascript">
    var meat_grams = document.getElementById('meat_grams');

    var conversions = {
        "Salt": .0175,
        "Brown Sugar": .0175,
        "Black Pepper": .005,
        "Cure #1": .0025,
        "Garlic Powder": .00187,
        "Whole Mustard Seed": .00125,
        "Pickling Spice": .000625,
        "Marjoram": .000313,
    };

    meat_grams.addEventListener('keyup', function () {
        for (let ingredient in conversions) {
            var gram_value = meat_grams.value * conversions[ingredient];
            var text = gram_value.toFixed(2) + "g "
            document.getElementById(ingredient).innerHTML = text;
            console.log(ingredient + text)
        }
    });
</script>

## Directions

Multiply the meat by the percentages of spices.

For example, 454 grams of pork X 0.0175 (1.75%) gives you around 8 grams of
salt.

1. Mix the measured spices into cold meat chunks (or ground meat if using).
   Note: the meat grinds better if very cold, almost frozen.
2. Add the meat to the grinder and push it through. Once the meat is ground,
   pour water over it and start mixing it by hand. There aren't specific
   measurements for the amount of water this is more of a by feel thing to see
   how much you want to add. Mix by hand, add water and adjust as needed.. At
   the end of the process, the meat should clump together and even sticks to
   your hand without falling. Note: At this point, you have loose kielbasa that
   can be fried up as a burger for a delicious lunch.
3. Fill the sausage stuffing container with the kielbasa. Place the casing over
   the tube and slowly extrude the sausage into the casing.
4. Once the sausage is stuffed, twist into links by pinching together and
   twisting the casing.
5. Hang the sausages to dry for a few hours until the outside casing is no
   longer wet.
6. Meanwhile set up the smoker (weber grill, smokehouse, electric smoker, etc).
7. Smoke the kielbasa until the internal temperature reaches 150 F (65 C).
8. Rinse or immerse with cold water to bring the sausages back to room
   temperature, then leave them on a rack to "bloom" for about 2 hrs (this will
   deepen their color to a nice dark red).
9. Enjoy the kielbasa with sauerkraut, on sandwiches, etc. Freeze any extra.
