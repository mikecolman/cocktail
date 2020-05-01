"""
User interface for cocktails

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Michael Colman
Date:   May 1, 2020
"""

drink = str(input('Name a drink: '))

import ingredients

json = ingredients.service_response(drink)
instructions = ingredients.get_strInstructions(json)
official_drink = ingredients.get_strDrink(json)

#ingredients
ingredient1 = ingredients.get_strIngredient1(json)
ingredient2 = ingredients.get_strIngredient2(json)
ingredient3 = ingredients.get_strIngredient3(json)
ingredient4 = ingredients.get_strIngredient4(json)
ingredient5 = ingredients.get_strIngredient5(json)
ingredient6 = ingredients.get_strIngredient6(json)
ingredient7 = ingredients.get_strIngredient7(json)
ingredient8 = ingredients.get_strIngredient8(json)
ingredient9 = ingredients.get_strIngredient9(json)
ingredient10 = ingredients.get_strIngredient10(json)
ingredient11 = ingredients.get_strIngredient11(json)
ingredient12 = ingredients.get_strIngredient12(json)
ingredient13 = ingredients.get_strIngredient13(json)
ingredient14 = ingredients.get_strIngredient14(json)
ingredient15 = ingredients.get_strIngredient15(json)

#measurements

measurement1 = ingredients.get_strMeasure1(json)
measurement2 = ingredients.get_strMeasure2(json)
measurement3 = ingredients.get_strMeasure3(json)
measurement4 = ingredients.get_strMeasure4(json)
measurement5 = ingredients.get_strMeasure5(json)
measurement6 = ingredients.get_strMeasure6(json)
measurement7 = ingredients.get_strMeasure7(json)
measurement8 = ingredients.get_strMeasure8(json)
measurement9 = ingredients.get_strMeasure9(json)
measurement10 = ingredients.get_strMeasure10(json)
measurement11 = ingredients.get_strMeasure11(json)
measurement12 = ingredients.get_strMeasure12(json)
measurement13 = ingredients.get_strMeasure13(json)
measurement14 = ingredients.get_strMeasure14(json)
measurement15 = ingredients.get_strMeasure15(json)




#Print Statements

print('\nHere is how to make a '+str(official_drink)+'.\n')
print('Instructions:\n\n'+str(instructions)+'\n')
print('Ingredients:\n')
print(str(ingredient1)+' '+str(measurement1))
print(str(ingredient2)+' '+str(measurement2))
print(str(ingredient3)+' '+str(measurement3))
print(str(ingredient4)+' '+str(measurement4))
print(str(ingredient5)+' '+str(measurement5))
print(str(ingredient6)+' '+str(measurement6))
print(str(ingredient7)+' '+str(measurement7))
print(str(ingredient8)+' '+str(measurement8))
print(str(ingredient9)+' '+str(measurement9))
print(str(ingredient10)+' '+str(measurement10))
print(str(ingredient11)+' '+str(measurement11))
print(str(ingredient12)+' '+str(measurement12))
print(str(ingredient13)+' '+str(measurement13))
print(str(ingredient14)+' '+str(measurement14))
print(str(ingredient15)+' '+str(measurement15))
