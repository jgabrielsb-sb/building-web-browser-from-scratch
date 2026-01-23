
from os import splice
from building_web_browser_from_scratch.core.ports import ConversorPort
from building_web_browser_from_scratch.core.models import URL, SchemesEnum

class ConvertStrToUrl(ConversorPort):
    def _run(self, input: str) -> URL:
        if not isinstance(input, str):
            raise TypeError('input must be a str')


        # getting scheme
        if not "://" in input:
            raise ValueError("Failed getting url scheme: the input does not have `://`.")
        
        character = "://"
        split_by_character = input.split(character)

        try:
            scheme_str = split_by_character[0].upper()
            scheme = SchemesEnum(scheme_str)
        except ValueError as e:
            raise ValueError(f"Failed getting url scheme: the value '{split_by_character[0]}' is not a valid SchemeEnum")

        # getting hostname and path
        character = '/'

        input_without_scheme = split_by_character[1]
        if not character in input_without_scheme:
            raise ValueError(f"Failed getting hostname: the {input_without_scheme} does not contain {character}. Then, it could not be spplited.")

        hostname, path  = input_without_scheme.split(character, 1)
        path = "/" + path
        return URL(
            scheme=scheme,
            hostname=hostname,
            path=path
        )

        



        



        
        
        

        

        return None

if __name__ == '__main__':
    convert_str_to_url = ConvertStrToUrl()
    url = convert_str_to_url.run('https://www.example.com/index.html')
    print(url)

    

        

