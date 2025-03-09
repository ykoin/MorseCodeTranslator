import re

# Słownik tłumaczący kod Morse’a dla cyfr
morse_digit = {
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0"
}

def decode_morse(morse_text):
    """
    Funkcja dzieli tekst Morse’a na grupy (oddzielone przynajmniej dwoma spacjami),
    każda grupa to ciąg znaków reprezentujących cyfry w kodzie Morse’a.
    Po przetłumaczeniu na cyfry ciąg jest interpretowany jako kod ASCII (lub Unicode),
    który konwertujemy na znak.
    """
    # Dzielenie na grupy – założenie: grupa oddzielona jest co najmniej dwoma spacjami
    groups = re.split(r'\s{2,}', morse_text.strip())
    decoded_chars = []
    for group in groups:
        # Podział każdej grupy na poszczególne znaki Morse’a
        parts = group.split()
        # Tłumaczenie części na cyfry i łączenie w jeden ciąg znaków
        number_str = "".join(morse_digit.get(part, '') for part in parts)
        if number_str:
            try:
                num = int(number_str)
                decoded_chars.append(chr(num))
            except Exception as e:
                # W razie problemu dodajemy znak zastępczy
                decoded_chars.append('?')
    return "".join(decoded_chars)

if __name__ == "__main__":
    # Zakładamy, że plik "telegraf.txt" znajduje się w tym samym katalogu
    with open("telegraf.txt", "r", encoding="utf-8") as file:
        morse_text = file.read()
    flag = decode_morse(morse_text)
    print("Odszyfrowana wiadomość:", flag)
