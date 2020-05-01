"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Michael Colman
Date:   April 16, 2020
"""

import introcs
import ingredients


def test_before_space():
    """Test procedure for before_space"""

    #Test case 1
    result = ingredients.before_space('Hello World')
    introcs.assert_equals('Hello',result)

    #Test case 2
    result = ingredients.before_space('Hello World Bye')
    introcs.assert_equals('Hello',result)

    #Test case 3
    result = ingredients.before_space('Hello  World')
    introcs.assert_equals('Hello',result)

    #Test case 4
    result = ingredients.before_space(' HelloWorld')
    introcs.assert_equals('',result)

    print('Testing before_space')


def test_after_space():
    """Test procedure for after_space"""

    #Test case 1
    result = ingredients.after_space('Hello World')
    introcs.assert_equals('World',result)

    #Test case 2
    result = ingredients.after_space('Hello World Bye')
    introcs.assert_equals('World Bye',result)

    #Test case 3
    result = ingredients.after_space('Hello  World')
    introcs.assert_equals(' World',result)

    #Test case 4
    result = ingredients.after_space('HelloWorld ')
    introcs.assert_equals('',result)

    print('Testing after_space')


def test_first_inside_quotes():
    """Test procedure for first_inside_quotes"""

    #Test case 1
    result = ingredients.first_inside_quotes('A "B C" D')
    introcs.assert_equals('B C',result)

    #Test case 2
    result = ingredients.first_inside_quotes('A "B C" D "E F" G')
    introcs.assert_equals('B C',result)

    #Test case 3
    result = ingredients.first_inside_quotes('""A B C D E F G')
    introcs.assert_equals('',result)

    #Test case 4
    result = ingredients.first_inside_quotes('"A B C"')
    introcs.assert_equals('A B C',result)

    #Test case 5
    #result = currency.first_inside_quotes()
    #introcs.assert_equals(,True)

    #Test case 6
    #result = currency.first_inside_quotes()
    #introcs.assert_equals(,True)

    print('Testing first_inside_quotes')

def test_get_strDrink():
    """Test procedure for get_strDrink"""

    #Test case 1
    result = ingredients.get_strDrink('{"drinks":[{"idDrink":"11007","strDrink":"Margarita","strDrinkAlternate":null,"strDrinkES":null,"strDrinkDE":null,"strDrinkFR":null,"strDrinkZH-HANS":null,"strDrinkZH-HANT":null,"strTags":"IBA,ContemporaryClassic","strVideo":null,"strCategory":"Ordinary Drink","strIBA":"Contemporary Classics","strAlcoholic":"Alcoholic","strGlass":"Cocktail glass","strInstructions":"Rub the rim of the glass with the lime slice to make the salt stick to it. Take care to moisten only the outer rim and sprinkle the salt on it. The salt should present to the lips of the imbiber and never mix into the cocktail. Shake the other ingredients with ice, then carefully pour into the glass.","strInstructionsES":null,"strInstructionsDE":"Reiben Sie den Rand des Glases mit der Limettenscheibe, damit das Salz daran haftet. Achten Sie darauf, dass nur der \u00e4u\u00dfere Rand angefeuchtet wird und streuen Sie das Salz darauf. Das Salz sollte sich auf den Lippen des Genie\u00dfers befinden und niemals in den Cocktail einmischen. Die anderen Zutaten mit Eis sch\u00fctteln und vorsichtig in das Glas geben.","strInstructionsFR":null,"strInstructionsZH-HANS":null,"strInstructionsZH-HANT":null,"strDrinkThumb":"https:\/\/www.thecocktaildb.com\/images\/media\/drink\/wpxpvu1439905379.jpg","strIngredient1":"Tequila","strIngredient2":"Triple sec","strIngredient3":"Lime juice","strIngredient4":"Salt","strIngredient5":null,"strIngredient6":null,"strIngredient7":null,"strIngredient8":null,"strIngredient9":null,"strIngredient10":null,"strIngredient11":null,"strIngredient12":null,"strIngredient13":null,"strIngredient14":null,"strIngredient15":null,"strMeasure1":"1 1\/2 oz ","strMeasure2":"1\/2 oz ","strMeasure3":"1 oz ","strMeasure4":null,"strMeasure5":null,"strMeasure6":null,"strMeasure7":null,"strMeasure8":null,"strMeasure9":null,"strMeasure10":null,"strMeasure11":null,"strMeasure12":null,"strMeasure13":null,"strMeasure14":null,"strMeasure15":null,"strCreativeCommonsConfirmed":"No","dateModified":"2015-08-18 14:42:59"}')
    introcs.assert_equals('Margarita',result)

    print('Testing get_strDrink')


def test_is_drink():
    """Test procedure for is_drink"""

    #Test case 1
    result = ingredients.is_drink('{"drinks":[{"idDrink":"11007","strDrink":"Margarita","strDrinkAlternate":null,"strDrinkES":null,"strDrinkDE":null,"strDrinkFR":null,"strDrinkZH-HANS":null,"strDrinkZH-HANT":null,"strTags":"IBA,ContemporaryClassic","strVideo":null,"strCategory":"Ordinary Drink","strIBA":"Contemporary Classics","strAlcoholic":"Alcoholic","strGlass":"Cocktail glass","strInstructions":"Rub the rim of the glass with the lime slice to make the salt stick to it. Take care to moisten only the outer rim and sprinkle the salt on it. The salt should present to the lips of the imbiber and never mix into the cocktail. Shake the other ingredients with ice, then carefully pour into the glass.","strInstructionsES":null,"strInstructionsDE":"Reiben Sie den Rand des Glases mit der Limettenscheibe, damit das Salz daran haftet. Achten Sie darauf, dass nur der \u00e4u\u00dfere Rand angefeuchtet wird und streuen Sie das Salz darauf. Das Salz sollte sich auf den Lippen des Genie\u00dfers befinden und niemals in den Cocktail einmischen. Die anderen Zutaten mit Eis sch\u00fctteln und vorsichtig in das Glas geben.","strInstructionsFR":null,"strInstructionsZH-HANS":null,"strInstructionsZH-HANT":null,"strDrinkThumb":"https:\/\/www.thecocktaildb.com\/images\/media\/drink\/wpxpvu1439905379.jpg","strIngredient1":"Tequila","strIngredient2":"Triple sec","strIngredient3":"Lime juice","strIngredient4":"Salt","strIngredient5":null,"strIngredient6":null,"strIngredient7":null,"strIngredient8":null,"strIngredient9":null,"strIngredient10":null,"strIngredient11":null,"strIngredient12":null,"strIngredient13":null,"strIngredient14":null,"strIngredient15":null,"strMeasure1":"1 1\/2 oz ","strMeasure2":"1\/2 oz ","strMeasure3":"1 oz ","strMeasure4":null,"strMeasure5":null,"strMeasure6":null,"strMeasure7":null,"strMeasure8":null,"strMeasure9":null,"strMeasure10":null,"strMeasure11":null,"strMeasure12":null,"strMeasure13":null,"strMeasure14":null,"strMeasure15":null,"strCreativeCommonsConfirmed":"No","dateModified":"2015-08-18 14:42:59"}')
    introcs.assert_false(result)

    #Test case 2
    result = ingredients.is_drink('{"drinks":null}')
    introcs.assert_false(result)

    print('Testing is_drink')


def test_get_strInstructions():
    """Test procedure for get_strInstructions."""

    result = ingredients.get_strInstructions('{"drinks":[{"idDrink":"11007","strDrink":"Margarita","strDrinkAlternate":null,"strDrinkES":null,"strDrinkDE":null,"strDrinkFR":null,"strDrinkZH-HANS":null,"strDrinkZH-HANT":null,"strTags":"IBA,ContemporaryClassic","strVideo":null,"strCategory":"Ordinary Drink","strIBA":"Contemporary Classics","strAlcoholic":"Alcoholic","strGlass":"Cocktail glass","strInstructions":"Rub the rim of the glass with the lime slice to make the salt stick to it. Take care to moisten only the outer rim and sprinkle the salt on it. The salt should present to the lips of the imbiber and never mix into the cocktail. Shake the other ingredients with ice, then carefully pour into the glass.","strInstructionsES":null,"strInstructionsDE":"Reiben Sie den Rand des Glases mit der Limettenscheibe, damit das Salz daran haftet. Achten Sie darauf, dass nur der \u00e4u\u00dfere Rand angefeuchtet wird und streuen Sie das Salz darauf. Das Salz sollte sich auf den Lippen des Genie\u00dfers befinden und niemals in den Cocktail einmischen. Die anderen Zutaten mit Eis sch\u00fctteln und vorsichtig in das Glas geben.","strInstructionsFR":null,"strInstructionsZH-HANS":null,"strInstructionsZH-HANT":null,"strDrinkThumb":"https:\/\/www.thecocktaildb.com\/images\/media\/drink\/wpxpvu1439905379.jpg","strIngredient1":"Tequila","strIngredient2":"Triple sec","strIngredient3":"Lime juice","strIngredient4":"Salt","strIngredient5":null,"strIngredient6":null,"strIngredient7":null,"strIngredient8":null,"strIngredient9":null,"strIngredient10":null,"strIngredient11":null,"strIngredient12":null,"strIngredient13":null,"strIngredient14":null,"strIngredient15":null,"strMeasure1":"1 1\/2 oz ","strMeasure2":"1\/2 oz ","strMeasure3":"1 oz ","strMeasure4":null,"strMeasure5":null,"strMeasure6":null,"strMeasure7":null,"strMeasure8":null,"strMeasure9":null,"strMeasure10":null,"strMeasure11":null,"strMeasure12":null,"strMeasure13":null,"strMeasure14":null,"strMeasure15":null,"strCreativeCommonsConfirmed":"No","dateModified":"2015-08-18 14:42:59"}')
    introcs.assert_equals('Rub the rim of the glass with the lime slice to make the salt stick to it. Take care to moisten only the outer rim and sprinkle the salt on it. The salt should present to the lips of the imbiber and never mix into the cocktail. Shake the other ingredients with ice, then carefully pour into the glass.',result)

    print('Testing get_strInstructions')


# Call scripts
test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_strDrink()
test_is_drink()
test_get_strInstructions()
test_get_strIngredient1()
test_get_strIngredient2()
test_get_strIngredient3()
test_get_strIngredient4()
test_get_strIngredient5()
test_get_strIngredient6()
test_get_strIngredient7()
test_get_strIngredient8()
test_get_strIngredient9()
test_get_strIngredient10()
test_get_strIngredient11()
test_get_strIngredient12()
test_get_strIngredient13()
test_get_strIngredient14()
test_get_strIngredient15()
test_get_strMeasure1()
test_get_strMeasure2()
test_get_strMeasure3()
test_get_strMeasure4()
test_get_strMeasure5()
test_get_strMeasure6()
test_get_strMeasure7()
test_get_strMeasure8()
test_get_strMeasure9()
test_get_strMeasure10()
test_get_strMeasure11()
test_get_strMeasure12()
test_get_strMeasure13()
test_get_strMeasure14()
test_get_strMeasure15()
