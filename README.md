# Txt2Morse Converter

This is a simple command-line tool that allows users to convert text to Morse code and decode Morse code back to text. The tool uses the `morse3` Python library for encoding and decoding Morse code.

## Features

- **Text to Morse Encoding**: Convert plain text into Morse code.
- **Morse to Text Decoding**: Convert Morse code back into readable text.
- **User Interaction**: The program prompts the user for input to either encode or decode a message.

## Tech Stack

- **Python**: The programming language used.
- **morse3**: A Python library for encoding and decoding Morse code.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/btag16/txt2morse-converter.git
   cd txt2morse-converter
   ```

2. **Install dependencies**:
   Ensure you have Python 3.x installed. Install the necessary Python libraries by running:
   ```bash
   pip install morse3
   ```

## Usage

1. Run the script `main.py`:
   ```bash
   python main.py
   ```

2. Enter a text prompt when asked: 
   ```
   Enter a Prompt: [Your text]
   ```

3. When prompted, choose whether to **encode** or **decode**:
   - To encode text to Morse code, type `e` or `encode`.
   - To decode Morse code to text, type `d` or `decode`.

4. The program will display the result after the conversion.

## Example

```
Enter a Prompt: Hello World
encode or decode? Type e for encode and d for decode. e
Decoded Text: .... . .-.. .-.. --- / .-- --- .-. .-.. -.. 
```

## Requirements

- Python 3.x
- morse3

You can install the required libraries with:

```bash
pip install morse3
```

## License

This project is licensed under the MIT License.

---

Feel free to contribute, suggest improvements, or ask questions by opening an issue in this repository.
