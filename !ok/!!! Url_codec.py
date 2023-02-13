import urllib.parse
import unicodedata
import urllib

def urlencode(str):
  return urllib.parse.quote(str)


def urldecode(str):
  return urllib.parse.unquote(str)

str = '{"name": "Kinkin"}'
str = '%D0%9B%D0%B0%D0%B1%D0%B8%D0%BD%D1%81%D0%BA%2C+'#%D0%9E%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C+%D0%BD%D0%B0+%D0%BA%D0%B0%D1%80%D1%82%D0%B5%2C+%D0%90%D0%B2%D1%82%D0%BE%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D0%B8%2C+%D0%A6%D0%B5%D0%BD%D0%B0+%D0%B4%D0%BE%C2%A0700%C2%A0000%C2%A0%E2%82%BD\u0026filter%5BcategoryId%5D=9\u0026filter%5BlocationId%5D=633650\u0026filter%5BpriceMax%5D=700000\u0026filter%5BsearchRadius%5D=200\u0026pushFrequency=3\u0026pushFrequencyOptions%5B0%5D%5Bid%5D=1\u0026pushFrequencyOptions%5B0%5D%5Btitle%5D=%D0%A1%D1%80%D0%B0%D0%B7%D1%83\u0026pushFrequencyOptions%5B1%5D%5Bid%5D=2\u0026pushFrequencyOptions%5B1%5D%5Btitle%5D=%D0%A3%D1%82%D1%80%D0%BE%D0%BC\u0026pushFrequencyOptions%5B2%5D%5Bid%5D=3\u0026pushFrequencyOptions%5B2%5D%5Btitle%5D=%D0%92%D0%B5%D1%87%D0%B5%D1%80%D0%BE%D0%BC\u0026pushFrequencyOptions%5B3%5D%5Bid%5D=0\u0026pushFrequencyOptions%5B3%5D%5Btitle%5D=%D0%9D%D0%B5+%D0%BF%D1%80%D0%B8%D1%81%D1%8B%D0%BB%D0%B0%D1%82%D1%8C\u0026title=%D0%9F%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%BA%D0%B0+%D0%BD%D0%B0+%D0%BF%D0%BE%D0%B8%D1%81%D0%BA","xHash":"kbhqyadt4vl2f3egllano5etiene530","verticalId":0}}'
str2 = '%D0%9B%D0%B0%D0%B1%D0%B8%D0%BD%D1%81%D0%BA%2C+'#%D0%9E%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C+%D0%BD%D0%B0+%D0%BA%D0%B0%D1%80%D1%82%D0%B5%2C+%D0%90%D0%B2%D1%82%D0%BE%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D0%B8%2C+%D0%A6%D0%B5%D0%BD%D0%B0+%D0%B4%D0%BE%C2%A0700%C2%A0000%C2%A0%E2%82%BD\u0026filter%5BcategoryId%5D=9\u0026filter%5BlocationId%5D=633650\u0026filter%5BpriceMax%5D=700000\u0026filter%5BsearchRadius%5D=200\u0026pushFrequency=3\u0026pushFrequencyOptions%5B0%5D%5Bid%5D=1\u0026pushFrequencyOptions%5B0%5D%5Btitle%5D=%D0%A1%D1%80%D0%B0%D0%B7%D1%83\u0026pushFrequencyOptions%5B1%5D%5Bid%5D=2\u0026pushFrequencyOptions%5B1%5D%5Btitle%5D=%D0%A3%D1%82%D1%80%D0%BE%D0%BC\u0026pushFrequencyOptions%5B2%5D%5Bid%5D=3\u0026pushFrequencyOptions%5B2%5D%5Btitle%5D=%D0%92%D0%B5%D1%87%D0%B5%D1%80%D0%BE%D0%BC\u0026pushFrequencyOptions%5B3%5D%5Bid%5D=0\u0026pushFrequencyOptions%5B3%5D%5Btitle%5D=%D0%9D%D0%B5+%D0%BF%D1%80%D0%B8%D1%81%D1%8B%D0%BB%D0%B0%D1%82%D1%8C\u0026title=%D0%9F%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%BA%D0%B0+%D0%BD%D0%B0+%D0%BF%D0%BE%D0%B8%D1%81%D0%BA","xHash":"kbhqyadt4vl2f3egllano5etiene530","verticalId":0}}'
str_pars = urllib.parse.parse_qs(str2)
#str_pars2 = urllib.unquote_plus(str2)
encoded = urlencode(str)
print(encoded)  # '%7B%22name%22%3A%20%22Kinkin%22%7D'
decoded = urldecode(encoded)
print(decoded)  # '{"name": "Kinkin"}'
letter1 = unicodedata.normalize("NFKC", str)
#letter2 = unicodedata.normalize("NFKC", letter2)
print("After normalizing str_pars:", str_pars) #, ord(letter2))