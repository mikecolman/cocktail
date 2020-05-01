"""
Get cocktails by name

Author: Michael Colman
Date: April 28, 2020

url: https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita
"""

import introcs
APIKEY = '1'

def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """

    assert type(s) == str, repr(s)+' is not a string.'
    assert introcs.count_str(s,' ') >= 1, repr(s)+' does not contain at least one space.'

    #find location of first space
    space = introcs.find_str(s,' ')

    #get string before first space
    result = s[:space]

    #return the result
    return result


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """

    assert type(s) == str, repr(s)+' is not a string.'
    assert introcs.count_str(s,' ') >= 1, repr(s)+' does not contain at least one space.'

    #find location of first string
    space = introcs.find_str(s,' ')

    #get string after first space
    result = s[space+1:]

    #return the result
    return result


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """

    assert type(s) == str, repr(s)+' is not a string.'
    assert introcs.count_str(s,'"') >= 2, repr(s)+' needs two "" characters.'

    #find first double quotation

    first = introcs.find_str(s,'"')
    #print(first)
    #find second double quotation

    second = introcs.find_str(s,'"',first+1)
    #print(second)
    #get string between first and second quotation

    result = s[first+1:second]
    #print(result)
    #print(type(result))
    #return the result
    return result


def first_inside_colon_comma(s):
    """
    Returns substring after colon and before comma
    """

    colon = introcs.find_str(s,':')
    #print(colon)
    comma = introcs.find_str(s,',',colon+1)
    #print(comma)
    result1 = s[colon+1:comma]
    result2 = introcs.replace_str(result1,'\\','')
    result = introcs.replace_str(result2,'"','')
    #print(result)
    #print(type(result))

    return result


def get_strDrink(json):
    """
    Returns the strDrink value in the response to a drink query.

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service
    """

    strDrink = introcs.find_str(json,'"strDrink"')


    string = json[strDrink+10:]


    result = first_inside_quotes(string)


    return result


def is_drink(json):
    """Returns True if query is a drink"""

    drinks = introcs.find_str(json,'"drinks"')

    string = json[drinks+9:]

    result = bool(string == 'null')


def get_strInstructions(json):
    """
    Returns the strInstructions value in the response to a drink query.

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service
    """

    strInstructions = introcs.find_str(json,'"strInstructions"')


    string = json[strInstructions+17:]


    result = first_inside_quotes(string)


    return result


def get_strIngredient1(json):

    strIngredient = introcs.find_str(json,'"strIngredient1"')
    #print(strIngredient)

    string = json[strIngredient+16:]
    #print(string)

    #result = first_inside_colon_comma(string)
    result = first_inside_quotes(string)
    #print(result)
    #print(type(result))

    return result

def get_strIngredient2(json):

    strIngredient = introcs.find_str(json,'"strIngredient2"')
    #print(strIngredient)


    string = json[strIngredient+16:]

    result = first_inside_colon_comma(string)

    return result

def get_strIngredient3(json):

    strIngredient = introcs.find_str(json,'"strIngredient3"')
    string = json[strIngredient+16:]
    result = first_inside_colon_comma(string)
    return result


def get_strIngredient4(json):

    strIngredient = introcs.find_str(json,'"strIngredient4"')
    string = json[strIngredient+16:]
    result = first_inside_colon_comma(string)
    return result


def get_strIngredient5(json):

    strIngredient = introcs.find_str(json,'"strIngredient5"')
    string = json[strIngredient+16:]
    result = first_inside_colon_comma(string)
    return result

def get_strIngredient6(json):

    strIngredient = introcs.find_str(json,'"strIngredient6"')
    string = json[strIngredient+16:]
    result = first_inside_colon_comma(string)
    return result


def get_strIngredient7(json):

    strIngredient = introcs.find_str(json,'"strIngredient7"')
    string = json[strIngredient+16:]
    result = first_inside_colon_comma(string)
    return result


def get_strIngredient8(json):

    strIngredient = introcs.find_str(json,'"strIngredient8"')
    string = json[strIngredient+16:]
    result = first_inside_colon_comma(string)
    return result


def get_strIngredient9(json):

    strIngredient = introcs.find_str(json,'"strIngredient9"')
    string = json[strIngredient+16:]
    result = first_inside_colon_comma(string)
    return result


def get_strIngredient10(json):

    strIngredient = introcs.find_str(json,'"strIngredient10"')
    string = json[strIngredient+16:]
    result = first_inside_colon_comma(string)
    return result

def get_strIngredient11(json):

    strIngredient = introcs.find_str(json,'"strIngredient11"')
    string = json[strIngredient+16:]
    result = first_inside_colon_comma(string)
    return result


def get_strIngredient12(json):

    strIngredient = introcs.find_str(json,'"strIngredient12"')
    string = json[strIngredient+16:]
    result = first_inside_colon_comma(string)
    return result


def get_strIngredient13(json):

    strIngredient = introcs.find_str(json,'"strIngredient13"')
    string = json[strIngredient+16:]
    result = first_inside_colon_comma(string)
    return result

def get_strIngredient14(json):

    strIngredient = introcs.find_str(json,'"strIngredient14"')
    string = json[strIngredient+16:]
    result = first_inside_colon_comma(string)
    return result


def get_strIngredient15(json):

    strIngredient = introcs.find_str(json,'"strIngredient15"')
    string = json[strIngredient+16:]
    result = first_inside_colon_comma(string)
    return result


def get_strMeasure1(json):

    strMeasurement = introcs.find_str(json,'"strMeasure1"')
    string = json[strMeasurement+12:]
    result = first_inside_colon_comma(string)
    return result


def get_strMeasure2(json):

    strMeasurement = introcs.find_str(json,'"strMeasure2"')
    string = json[strMeasurement+12:]
    result = first_inside_colon_comma(string)
    return result


def get_strMeasure3(json):

    strMeasurement = introcs.find_str(json,'"strMeasure3"')
    string = json[strMeasurement+12:]
    result = first_inside_colon_comma(string)
    return result


def get_strMeasure4(json):

    strMeasurement = introcs.find_str(json,'"strMeasure4"')
    string = json[strMeasurement+12:]
    result = first_inside_colon_comma(string)
    return result


def get_strMeasure5(json):

    strMeasurement = introcs.find_str(json,'"strMeasure5"')
    string = json[strMeasurement+12:]
    result = first_inside_colon_comma(string)
    return result


def get_strMeasure6(json):

    strMeasurement = introcs.find_str(json,'"strMeasure6"')
    string = json[strMeasurement+12:]
    result = first_inside_colon_comma(string)
    return result


def get_strMeasure7(json):

    strMeasurement = introcs.find_str(json,'"strMeasure7"')
    string = json[strMeasurement+12:]
    result = first_inside_colon_comma(string)
    return result


def get_strMeasure8(json):

    strMeasurement = introcs.find_str(json,'"strMeasure8"')
    string = json[strMeasurement+12:]
    result = first_inside_colon_comma(string)
    return result


def get_strMeasure9(json):

    strMeasurement = introcs.find_str(json,'"strMeasure9"')
    string = json[strMeasurement+12:]
    result = first_inside_colon_comma(string)
    return result


def get_strMeasure10(json):

    strMeasurement = introcs.find_str(json,'"strMeasure10"')
    string = json[strMeasurement+12:]
    result = first_inside_colon_comma(string)
    return result


def get_strMeasure11(json):

    strMeasurement = introcs.find_str(json,'"strMeasure11"')
    string = json[strMeasurement+12:]
    result = first_inside_colon_comma(string)
    return result


def get_strMeasure12(json):

    strMeasurement = introcs.find_str(json,'"strMeasure12"')
    string = json[strMeasurement+12:]
    result = first_inside_colon_comma(string)
    return result


def get_strMeasure13(json):

    strMeasurement = introcs.find_str(json,'"strMeasure13"')
    string = json[strMeasurement+12:]
    result = first_inside_colon_comma(string)
    return result


def get_strMeasure14(json):

    strMeasurement = introcs.find_str(json,'"strMeasure14"')
    string = json[strMeasurement+12:]
    result = first_inside_colon_comma(string)
    return result


def get_strMeasure15(json):

    strMeasurement = introcs.find_str(json,'"strMeasure15"')
    string = json[strMeasurement+12:]
    result = first_inside_colon_comma(string)
    return result



def service_response(drink):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the currency dst. The response
    should be a string of the form

        '{"success": true, "src": "<src-amount>", dst: "<dst-amount>", error: ""}'

    where the values src-amount and dst-amount contain the value and name for the src
    and dst currencies, respectively. If the query is invalid, both src-amount and
    dst-amount will be empty, and the error message will not be empty.

    There may or may not be spaces after the colon.  To test this function, you should
    chose specific examples from your web browser.

    Parameter src: the currency on hand
    Precondition src is a nonempty string with only letters

    Parameter dst: the currency to convert to
    Precondition dst is a nonempty string with only letters

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """

    #create url
    drink2 = introcs.replace_str(drink,' ','%20')
    url = str('https://www.thecocktaildb.com/api/json/v1/'+APIKEY+'/search.php?s='+str(drink2))

    #query url
    result = introcs.urlread(url)

    #return result
    return result
